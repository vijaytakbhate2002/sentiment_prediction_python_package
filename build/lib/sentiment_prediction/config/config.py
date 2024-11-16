import os

# input columns
INPUT_COL = ['tweets']
TARGET_COL = ['@sentiments']
PROCESS_COLUMNS = ['tweets', '@sentiments']

BASE_DIR = '/'.join(os.path.abspath(__file__).split(os.sep)[:-2])

CLASSIFIER = '/'.join(os.path.join(BASE_DIR, 'trained_models', 'classifier.pkl').split(os.sep))
VECTORIZER = '/'.join(os.path.join(BASE_DIR, 'trained_models', 'vectorizer.pkl').split(os.sep))
ENCODER = '/'.join(os.path.join(BASE_DIR, 'trained_models', 'encoder.pkl').split(os.sep))
