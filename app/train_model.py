"""Train the model."""
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn import metrics
import lightgbm
import pickle


MODEL_FILENAME = 'model.pkl'


if __name__ == "__main__":
    # Import the dataset via sklearn and load it into a pandas dataframe
    california_housing_dataset = fetch_california_housing()
    df = pd.DataFrame(
        data=california_housing_dataset.data,
        columns=california_housing_dataset.feature_names,
    )
    print(f"California housing dataset:\n{df.head()}\n")

    # Specify feature and target variables
    X = df.drop("MedInc", axis=1)
    y = df['MedInc']

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )
    print(f"Train set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}\n")

    # Train the model
    model = lightgbm.LGBMRegressor()
    print("Training a LGBMRegressor model...")
    model.fit(X_train, y_train)
    print("Model trained.\n")

    # Run prediction using the model
    y_pred = model.predict(X_test)
    print(f"Model prediction:\n{y_pred}\n")

    # Evaluate the model
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    print(f"Root mean squared error (RMSE): {rmse:.2f}\n")

    # Save the model
    with open(MODEL_FILENAME, 'wb') as model_file:
        pickle.dump(model, model_file)
        print("Model saved as a pickle file.\n")
