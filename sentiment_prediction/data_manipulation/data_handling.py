import pandas as pd
from ..config import config
import logging
import joblib
from sklearn.base import ClassifierMixin

def loadData() -> pd.DataFrame:
    f"""loads data from {config.TRAINING} and {config.TESTING},
        and merge it"""
    logging.info(f"""Reading data from {config.TRAINING} and {config.TESTING}""")
    train = pd.read_csv(config.TRAINING)
    test = pd.read_csv(config.TESTING)
    df = pd.concat([train, test], axis='rows')
    print(f"Loaded processed data successfully from {config.ETL_OUT_DATA}")
    return df[config.PROCESS_COLUMNS]

# serialization
def dumpPipeline(pipeline_to_save) -> None:
    """Args : pipeline_to_save
        Return : None"""
    joblib.dump(pipeline_to_save, config.CLASSIFIER)
    print(f"Pipeline dumped successfully to {config.CLASSIFIER}")

# deserialization
def loadPipeline() -> ClassifierMixin:
    """Args : pipeline_to_load
        Return : ClassifierMixin (Model)"""
    classifier = joblib.load(config.CLASSIFIER)
    print(F"Pipeline loaded successfully from {config.CLASSIFIER}")
    return classifier
