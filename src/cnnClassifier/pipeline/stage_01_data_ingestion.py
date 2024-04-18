from cnnClassifier.config.configuration import COnfigurationManager
from cnnClassifier.components.data_ingestion import Dataingestion
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = COnfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = Dataingestion(config= data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        
if __name__ == "__main__":
    try:
        logger.info(f'>>>>>>>> stage {STAGE_NAME}  started <<<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx=================x')
    except Exception as e:
        logger.exception(e)
        raise e
        