from .data_manipulation.data_handling import loadData
from .data_manipulation.data_processing import NullRemoving, TextProcessing, VectorizingForPrediction
from .config import config
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

process_pipe = Pipeline([
    ("NullRemoving_initial", NullRemoving()),
    ("TextProcessing", TextProcessing(col=config.INPUT_COL[0])),
    ("Vectorizing", VectorizingForPrediction(col=config.INPUT_COL[0])),
    ("NullRemoving_end", NullRemoving()),
])

def newDataPredictor(X:pd.DataFrame) -> list[str]:
    """Predict for given input and return list with predicted classes"""
    id2label = {}
    try:
        classifier = joblib.load(config.CLASSIFIER)
        labels = joblib.load(config.ENCODER).classes_
        for i, label in enumerate(labels):
            id2label[i] = label

    except Exception as e: 
        raise FileNotFoundError(e)
    X = process_pipe.fit_transform(X=X, y=None)
    predictions = classifier.predict(X)
    predictions = [id2label[val] for val in predictions]
    return predictions

def predictor(post:str) -> None:
    df = pd.DataFrame([[post]], columns=['tweets'])
    return newDataPredictor(X=df)

if __name__ == "__main__":
    df = loadData()
    df = df[config.INPUT_COL][:50]
    print(newDataPredictor(X=df))