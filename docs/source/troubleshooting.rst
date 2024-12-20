|image1|

Identifying and Solving Issues
==============================

Encountering problems with Modlee? This page provides solutions to the
most common issues users face. Follow these steps to resolve problems or
get guidance on where to find further assistance.

Installation Issues
-------------------

Problem: Installation Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Error messages during installation or failure to install
Modlee.

**Solutions**:

-  **Check Python Version**: Ensure you are using a compatible
   ``Python`` version. Modlee supports ``Python 3.10`` and above.

-  **Upgrade Pip**: Sometimes, updating pip can resolve installation
   issues. Run this command:

   .. code:: shell

      pip install --upgrade pip

-  **Correct Installation Command**: Use the correct installation
   command to download the Modlee package:

   .. code:: shell

      pip install modlee

-  **Dependencies**: Verify that all dependencies are installed. You can
   find the list of required dependencies on Modlee’s
   `Github <https://github.com/modlee-ai/modlee/blob/main/requirements.txt>`__.

Problem: Incompatible Package Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Errors related to conflicting versions of packages.

**Solutions**:

-  **Check Dependency Versions**: Ensure that all required packages are
   installed in compatible versions. Refer to Modlee’s
   `requirements.txt <https://github.com/modlee-ai/modlee/blob/main/requirements.txt>`__
   for the correct versions.

-  **Use Virtual Environment**: Consider using a virtual environment to
   manage package versions and avoid conflicts. Create one and activate
   it before installing Modlee. Run the following command to create a
   virtual environment:

   .. code:: bash

      python -m venv myenv

   Activate the virtual environment using this command:

   -  On Windows:

      .. code:: bash

         myenv\Scripts\activate

   -  On macOS/Linux:

      .. code:: bash

         source myenv/bin/activate

--------------

Setup Problems
--------------

Problem: Configuration Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Issues with the initial setup or configuration of Modlee.

**Solutions**:

-  **Follow Setup Instructions**: Review the `Quickstart
   page <https://docs.modlee.ai/README.html>`__ for detailed
   instructions on configuring the Modlee package.

-  **Environment Variables**: Verify that necessary environment
   variables are correctly set. For example, ensure that any API keys
   are properly configured.

   .. code:: python

      import os
      import modlee

      # Set your API key
      os.environ['MODLEE_API_KEY'] = "replace-with-your-api-key"

      # Initialize the Modlee package
      modlee.init(api_key=os.environ.get('MODLEE_API_KEY'))

Problem: Unable to Access Modlee API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Errors related to API key.

**Solutions**:

-  **Verify API Keys**: Ensure that your API keys are valid and
   correctly configured in your environment.

-  **Generate New Key**: Refresh the Modlee dashboard and generate a new
   API key.

--------------

Model Issues
------------

Problem: Training Process Fails or Crashes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Training process fails, crashes, or does not complete as
expected.

**Solutions**:

-  **Inspect Training Logs**: Review training logs to identify any error
   messages or warnings.

-  **Check Data Integrity**: Ensure that your data is correctly
   formatted and preprocessed before training.

-  **Verify Model Configuration**: Double-check your model
   configuration, including hyperparameters and architecture, to ensure
   they are correctly set.

Problem: None Model Recommended
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: The model recommender does not return a valid model.

**Solutions**:

-  **Check Input Parameters**: Ensure that the parameters passed to the
   recommender function are correct. For example, verify that the
   ``num_classes`` parameter is properly specified and supported by
   Modlee.

   .. code:: python

      recommender = modlee.recommender.ImageClassificationRecommender(
          num_classes=10 
      )

-  **Verify Dataset Compatibility**: Ensure that the dataset you are
   using is compatible with the recommender’s modality and task. The
   recommender might not be able to suggest a model if the dataset or
   task does not align with available models.

-  **Restart Session**: Sometimes, restarting your development
   environment or Jupyter Notebook session can resolve issues. Restart
   your session and try running the recommender again.

--------------

Environment Issues
------------------

Problem: Kaggle Notebook Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Encountering problems while using Modlee in a Kaggle Notebook
environment.

**Solutions**:

-  **Check Accelerator Type**: Ensure that the accelerator type in the
   Kaggle Notebook is set correctly. Go to the notebook’s Session
   Options and select the appropriate accelerator (e.g., GPU, TPU, or
   CPU) depending on your project requirements.

-  **Install Dependencies**: Verify that all necessary packages and
   dependencies are installed. You might need to install or update the
   libraries using:

   .. code:: shell

      pip install modlee

-  **Check File Paths**: Make sure the file paths for data and models
   are correctly specified, especially when accessing datasets stored in
   Kaggle’s input directory. If needed, load datasets directly from the
   Kaggle datasets:

   .. code:: python

      dataset = pd.read_csv('/kaggle/input/your-dataset/your-dataset.csv')

Problem: Kaggle Notebook, Run Out of GPU Compute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Errors while connecting to GPU on Kaggle Notebooks.

**Solutions**:

-  **Reduce Batch Size**: Decrease the batch size to reduce memory
   usage. For example

   .. code:: python

      train_loader = DataLoader(dataset, batch_size=4, shuffle=True)

-  **Free Up GPU Memory**: Clear unused variables and force garbage
   collection to free up GPU memory

-  **Upgrade Runtime**: If possible, upgrade your Kaggle account to a
   Pro tier for more GPU resources.

--------------

Model Limitations
-----------------

Problem: Errors Using LSTMs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Attempting to use LSTM layers or recurrent operations results
in errors.

**Explanation** : Currently, Modlee’s
modlee.model.TimeseriesClassificationModleeModel does not support
recurrent layers like LSTMs.

**Solutions**:

-  **Use Non-Recurrent Models**: Instead, try using models designed to
   handle time series data without recurrence, such as convolutional
   neural networks (CNNs) and transformers. These architectures can
   capture sequential dependencies effectively without relying on LSTM
   layers.

-  **Consider Alternative Libraries**: If your project requires LSTM
   functionality, consider using an alternative library that supports
   recurrent layers specifically for time series tasks.

--------------

Still Need Help?
----------------

If you continue to experience issues or need further assistance, please
email us at `support@modlee.ai <support@modlee.ai>`__ or join our
`community forum <https://discord.com/invite/m8YDbWDvrF>`__. You can
also raise an issue on our `GitHub
repository <https://github.com/modlee-ai/modlee/issues>`__ for
additional support.

.. |image1| image:: https://github.com/mansiagr4/gifs/raw/main/new_small_logo.svg
