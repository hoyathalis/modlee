import pytest
from . import conftest
import os, re
import pandas as pd
import torch
import torchvision
from torch.utils.data import DataLoader, TensorDataset
from torch.utils.data import Dataset
import modlee
from modlee import data_metafeatures as dmf
from modlee.utils import image_loaders, text_loaders
from sklearn.preprocessing import StandardScaler
import spacy
from pytorch_tabular import TabularModel
from pytorch_tabular.config import DataConfig, OptimizerConfig, TrainerConfig, ExperimentConfig
from pytorch_tabular.models import CategoryEmbeddingModelConfig

class TabularDataset(Dataset):
    def __init__(self, data, target):
        self.data = torch.tensor(data, dtype=torch.float32)
        self.target = torch.tensor(target, dtype=torch.float32).unsqueeze(1)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx], self.target[idx]
    
def get_diabetes_dataloader(batch_size=4, shuffle=True):
    dataset_path = os.path.join(os.path.dirname(__file__),'csv','diabetes.csv')

    df = pd.read_csv(dataset_path)

    X = df.drop('Outcome', axis=1).values
    y = df['Outcome'].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    dataset = TabularDataset(X_scaled, y)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

    return dataloader

def get_adult_dataloader(batch_size=4, shuffle=True):
    dataset_path = os.path.join(os.path.dirname(__file__),'csv','adult.csv')

    df = pd.read_csv(dataset_path)

    df = df.replace(' ?', pd.NA).dropna()

    X = df.drop('income', axis=1)
    y = df['income']

    X_encoded = pd.get_dummies(X, drop_first=True)
    X_encoded = X_encoded.apply(pd.to_numeric, errors='coerce')
    X_encoded = X_encoded.fillna(0)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_encoded)

    y = pd.factorize(y)[0]

    dataset = TabularDataset(X_scaled, y)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

    return dataloader

def get_housing_dataloader(batch_size=4, shuffle=True):

    column_names = [
        'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
    ]
    
    path_name = os.path.join(os.path.dirname(__file__),'csv','housing.csv')
    df = pd.read_csv(path_name, header=None, names=column_names, delim_whitespace=True)
    
    X = df.drop('MEDV', axis=1).values
    y = df['MEDV'].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    dataset = TabularDataset(X_scaled, y)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

    return dataloader


DATA_ROOT = os.path.expanduser("~/efs/.data")
IMAGE_DATALOADER = modlee.utils.get_imagenette_dataloader()
IMAGE_LOADERS = {loader_fn:getattr(image_loaders, loader_fn) for loader_fn in sorted(dir(image_loaders)) if re.match('get_(.*)_dataloader', loader_fn)}
TEXT_LOADERS = {loader_fn:getattr(text_loaders, loader_fn) for loader_fn in dir(text_loaders) if re.match('get_(.*)_dataloader', loader_fn)}
TABULAR_LOADERS = {'housing_dataset': get_housing_dataloader, 'adult_dataset': get_adult_dataloader, 'diabetes_dataset': get_diabetes_dataloader}

print('\n'.join(f"image loader{i}: {image_loader}" for i, image_loader in enumerate(IMAGE_LOADERS)))
import pandas as pd 
df = None

@pytest.mark.experimental
class TestDataMetafeatures:
    
    @pytest.mark.parametrize('get_dataloader_fn', IMAGE_LOADERS.values())
    def test_image_dataloader(self, get_dataloader_fn):
        image_mf = dmf.ImageDataMetafeatures(
            get_dataloader_fn(root=DATA_ROOT), testing=True)
        self._check_has_metafeatures(image_mf)

    @pytest.mark.parametrize('get_dataloader_fn', TABULAR_LOADERS.values())
    def test_tabular_dataloader(self, get_dataloader_fn):
        tabular_mf = dmf.TabularDataMetafeatures(
            get_dataloader_fn(), testing=True)
        self._check_has_metafeatures_tab(tabular_mf)
        self._check_statistical_metafeatures(tabular_mf)

    @pytest.mark.parametrize('get_dataloader_fn', TEXT_LOADERS.values())
    def test_text_dataloader(self, get_dataloader_fn):
        text_mf = dmf.TextDataMetafeatures(
            get_dataloader_fn(), testing=True)
        self._check_has_metafeatures(text_mf)

    def _check_has_metafeatures_tab(self, mf): 

        metafeature_types = [
            'mfe',
            'properties',
            'features'
        ]
        conftest._check_has_metafeatures_tab(mf,metafeature_types)

    def _check_has_metafeatures(self, mf): 

        metafeature_types = [
            'embedding',
            'mfe',
            'properties'
        ]
        conftest._check_has_metafeatures(mf, metafeature_types)
           
    def _check_statistical_metafeatures(self, mf):
        conftest._check_statistical_metafeatures(mf)
