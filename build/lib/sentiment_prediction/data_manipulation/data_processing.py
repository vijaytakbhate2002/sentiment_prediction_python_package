from .text_filter import textProcess
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from ..config import config
import warnings
warnings.filterwarnings('ignore')
import logging
from sklearn.base import BaseEstimator, TransformerMixin
import logging
import joblib
import os

class TextProcessing(BaseEstimator, TransformerMixin):
    """Process the text and removes unwanted content from text with regix expression
        """
    def __init__(self, col:str):
        self.col = col

    def fit(self, X:pd.DataFrame, y:pd.Series=None) -> None:
        return self
    
    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        X[self.col] = X[self.col].apply(lambda x: textProcess(x))
        return X
    
class ColumnsRemoving(BaseEstimator, TransformerMixin):
    """Drops specified columns from dataframe and"""
    def __init__(self, cols:list):
        self.cols = cols

    def fit(self, X:pd.DataFrame, y:pd.Series=None) -> None:
        return self
    
    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        for col in self.cols:
            if col in X.columns:
                logging.info(f"Dropping column = {col}")
                X.drop(col, inplace=True)
        return X
    
class NullRemoving(BaseEstimator, TransformerMixin):
    """Removes all null values from dataset"""
    def fit(self, X:pd.DataFrame, y:pd.Series=None) -> None:
        return self
    
    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        X.dropna(inplace=True) 
        return X

class VectorizingForPrediction(BaseEstimator, TransformerMixin):
    def __init__(self, col:str) -> None:
        self.col = col

    def fit(self, X:pd.DataFrame, y:pd.Series=None):
        return self
    
    def vectorization(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        if os.path.exists(config.VECTORIZER):
            tf_vec = joblib.load(config.VECTORIZER)
            logging.info(f"vectorizatoin don and old vectorizer is loaded with columns before transform = {tf_vec.get_feature_names_out()}")
            new_tf = tf_vec.transform(X[self.col]).toarray()
            inputs = pd.DataFrame(new_tf, columns=tf_vec.get_feature_names_out())
            logging.info(f"vectorizatoin don and old vectorizer is loaded with columns = {tf_vec.get_feature_names_out()}")
            return inputs
        else:
            tf_vectorizer = TfidfVectorizer(min_df=0.001)
            tf_vec = tf_vectorizer.fit(X[self.col])
            joblib.dump(tf_vec, os.path.join(config.VECTORIZER))
            new_tf = tf_vec.transform(X[self.col]).toarray()
            inputs = pd.DataFrame(new_tf, columns=tf_vec.get_feature_names_out())
            logging.info(f"vectorizatoin don and new vectorizer is created with columns = {tf_vec.get_feature_names_out()}")
            return inputs

    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        inputs = self.vectorization(X=X)
        return inputs
 