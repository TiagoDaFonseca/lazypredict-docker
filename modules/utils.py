from sklearn.model_selection import train_test_split, cross_val_score
from lazypredict.Supervised import LazyRegressor, LazyClassifier
from scipy.signal import savgol_filter
import pandas as pd
import numpy as np
import logging
import os

logging.basicConfig(level=logging.INFO)

path_to_data = os.path.join(os.path.curdir, "data")

def detect_dataset() -> pd.DataFrame:
    logging.info('Searching for datasets')
    files = os.listdir(path_to_data)
    if len(files) > 1:
        logging.warning('Please put only one dataset in folder.')
    
    # Chooses the first file in list
    filepath = files[0]
    
    dataframe = None
    if filepath.split('.')[1] == 'csv':
            dataframe = pd.read_csv(os.path.join(path_to_data, filepath))
    else:
        try:
            dataframe = pd.read_excel(os.path.join(path_to_data, filepath), engine='openpyxl')
        except Exception as e:
            logging.error(str(e))

    return dataframe

def load_data(data: pd.DataFrame) -> np.ndarray:
    """ returns the X and y data in numpy format"""
    logging.info('Splitting data into X and y')
    # Ensures that the trainning runs smoothly. Keep in mind lazypredict is just an exploratory step
    # No need to use all the available data
    if data.shape[0]>50000:
        sample = data.sample(frac=0.2) # Shuffles data automatically
    else:
        sample = data
    
    # Edit code is necessary
    X = sample.drop(['Brix'], axis=1).to_numpy().astype(np.float32)
    y = sample['Brix'].to_numpy().astype(np.float32)
    return X, y

def preprocess_data(input_data: np.ndarray) -> np.ndarray:
    """ Put your pre-processing algorithms here """
    logging.info('Preprocessing data')
    Xgolay = savgol_filter(input_data, window_length=11, polyorder=2, deriv=1)
    return Xgolay
        
def run_models(X : np.ndarray, y: np.ndarray, test_size=0.25):
    """ Runs all the models using lazypredict module """
    logging.info('Training data...')
    # Prepare data for trainning
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Train for classification
    reg = LazyRegressor(verbose=0,ignore_warnings=False, custom_metric=None)
    models,predictions = reg.fit(X_train, X_test, y_train, y_test)

    return models, predictions