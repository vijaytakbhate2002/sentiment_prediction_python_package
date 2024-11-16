### README.md  

# Twitter Post Sentiment Prediction - NLP  

This project focuses on predicting the sentiment of Twitter posts using Natural Language Processing (NLP) techniques. It is an end-to-end machine learning project that includes data preprocessing, model building, hyperparameter tuning, and deployment.

---

## Features  
- **ETL Pipeline**: Extract, transform, and load (ETL) processes implemented using PySpark and SQL.  
- **Text Processing**: Cleaned text data using regex, removed special characters, and vectorized text using TF-IDF.  
- **Model Building**: Implemented Logistic Regression and Multinomial Naive Bayes for sentiment prediction.  
- **Hyperparameter Tuning**: Optimized models using GridSearchCV.  
- **Experiment Tracking**: Logged experiments with MLflow for efficient performance comparison.  
- **Model Packaging**: Prepared reusable model packages using `sdist` and `wheel`.  
- **Deployment Ready**: Plan to host the project on Render for public access.  

---

## Project Structure  
```plaintext  
sentiment_prediction_python_package/
│
├── sentiment_prediction/                 # Main package directory
│   ├── config/                           
│   │   └── config.py                     # Configuration file
│   │
│   ├── data_manipulation/                # Model training and prediction scripts
│   │   ├── data_handling.py              # Training pipeline
│   │   ├── data_processing.py            # Prediction pipeline
│   │   └── text_filer.py                 # Text filtering utilities
│   │
│   └── trained_models/                   # Trained models and metadata
│       ├── classifier.pkl                # Classifier model
│       ├── vectorizer.pkl                # Vectorizer model
│       └── encoder.pkl                   # Encoder model
│
├── dist/                                 # Distribution packages (generated)
│
├── build/                                # Build files (generated)
│
├── sentiment_prediction.egg-info/        # Egg-info metadata (generated)
│
├── .gitignore                            # Excluded files and folders
├── MANIFEST.in                           # Configuration file with paths and constants
├── README.md                             # Project documentation
├── requirements.txt                      # Project dependencies
└── setup.py                              # Package metadata and configuration
```  

---

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/vijaytakbhate2002/Twitter-Post-Sentiment-Prediction--NLP-.git  
   ```  
2. Navigate to the project directory:  
   ```bash  
   cd Twitter-Post-Sentiment-Prediction--NLP-  
   ```  
3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

---

## Usage  

### Train the Model  
Run the training script to train the sentiment classification model:  
```bash  
python model/train_pipe.py  
```  

### Predict Sentiments  
Use the prediction script to test the model on new data:  
```bash  
python model/predict.py  
``` 

---

## Contribution  
Feel free to submit issues or pull requests. Contributions are welcome!  

---

## License  
This project is licensed under the MIT License.  

---

## Author  
[Vijay Dipak Takbhate](https://github.com/vijaytakbhate2002)  

---  

GitHub Repository: [Twitter Post Sentiment Prediction](https://github.com/vijaytakbhate2002/Twitter-Post-Sentiment-Prediction--NLP-.git)# sentiment_prediction_python_package
