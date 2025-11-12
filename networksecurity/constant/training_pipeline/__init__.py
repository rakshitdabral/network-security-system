import os
import sys
import numpy as np
import pandas as pd

"""This is a constant file for the training pipeline"""

TARGET_COLUMN:str = "Result"
PIPELINE_NAME:str = "NetworkSecuirty"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME = "phisingData.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

SCHEMA_FILE_PATH:str = os.path.join("data_schema","schema.yaml")

DATA_INGESTION_COLLECTION_NAME:str = "phisingData"
DATA_INGESTION_DATABASE_NAME:str = "Network_Data"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float = 0.2


"""
    Data Validation Related Constant
"""

DATA_VALIDATION_DIR_NAME :str = "data_validation"
DATA_VALIDATION_VALID_DIR : str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"

"""
    Data Transformation Related Constant
"""

DATA_TRANSFORMATION_DIR_NAME:str = "data_tranformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME:str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str = DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object"
PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessing.pkl"

#KNN IMPUTER to REPLACE NAN VALUES
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values" : np.nan,
    "n_neighbors" : 3,
    "weights" : "uniform"
}