

# If cnnClassifier is a local package, add its parent directory to PYTHONPATH

# If cnnClassifier is a local package, set PYTHONPATH in your terminal before running this script:
# export PYTHONPATH="${PYTHONPATH}:$(pwd)"
# Or, set it in Python as follows:
# import os
# os.environ['PYTHONPATH'] = f"{os.environ.get('PYTHONPATH', '')}:{os.getcwd()}"



# Or, if cnnClassifier is a pip-installable package, install it
# Make sure to install cnnClassifier using pip in your terminal before running this script.

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e