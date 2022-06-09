# Resale-Flat-Prices-Regression-Model
Project Description:
- This is a Machine Learning Model Created using Python's SciKit-Learn Library.
- The model will predict the Price of a Resale Flat in Singapore using attributes and data of the Flat.
- Refer to the ProjectOverview File for more information.

Installation:
1. Download Project:
    - git clone https://github.com/jaredpek/Resale-Flat-Prices-Regression-Model
2. Install Requirements:
    - pip install -r requirements.txt

Saving the Model:
1. Import the Save function from Joblib Library:
    - from joblib import save
2. Save Heart Disease Model:
    - save({Name of Heart Disease Model Variable}, filename='FlatPricesModel')
3. Model would be saved in the same directory

Using the Streamlit App:
1. Run the FlatPricesModel.ipynb once to Save the Model
2. Run the Streamlit App:
    - streamlit run .\FlatPricesPredictionApp.py
