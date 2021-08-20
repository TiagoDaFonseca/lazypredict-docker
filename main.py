from modules import utils
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    
    
    # Load data from file. This may take a few minutes.
    data = utils.detect_dataset()
    
    print("Data:")
    print(data.head())

    # Set Input and Output data
    X, y = utils.load_data(data)

    # Pre-processing code here
    Xp = utils.preprocess_data(X)

    # Train models
    models , predictions = utils.run_models(Xp, y)

    logging.info('Finished training.')
    
    # Output models
    print("Models trained:\n\n")
    print(models)