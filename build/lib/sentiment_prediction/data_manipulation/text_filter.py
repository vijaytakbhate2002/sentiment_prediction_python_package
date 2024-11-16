import re
from nltk import PorterStemmer
import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
import warnings
import logging

warnings.filterwarnings('ignore')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')  

lemmatizer = WordNetLemmatizer()
stop_words = list(stopwords.words('english'))

ps = PorterStemmer()

def stemmerAndLemmitization(sms:str):
    tokens = list(sms.split(' '))
    tokens = [ps.stem(word) for word in tokens]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def textProcess(sms):
    try:
        logging.info(f"Enterd into textProcess with text = {sms}")
        sms = re.sub(r'http\S+|www\S+|https\S+', '', sms, flags=re.MULTILINE)
        sms = re.sub(r'@\w+|#\w+', '', sms)
        sms = re.sub(r'<.*?>', '', sms)
        sms = re.sub(r'[^A-Za-z\s]', '', sms)
        sms = sms.lower()
        tokens = stemmerAndLemmitization(sms)
        processed_sms = ' '.join(tokens)
        return processed_sms

    except Exception as e:
        logging.warning(f"could not perform text processing for {sms}")
        return None