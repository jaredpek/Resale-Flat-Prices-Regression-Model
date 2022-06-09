import streamlit as st
import numpy as np
import pandas as pd
import math
import datetime
from joblib import load

title = st.title("Flat Prices Prediction")
flat_prices = pd.DataFrame(pd.read_csv('flat-prices.csv'))

def make_prediction(model, input_data):
    prediction = int(model.predict(input_data))
    print(prediction)
    
    if prediction:
        st.success(f"Predicted Resale Price is SGD${prediction}")
        return prediction
    elif not prediction:
        st.error("Error")
        return "Error"

town_list = list(np.sort(flat_prices["town"].unique()))
flat_type_list = list(np.sort(flat_prices["flat_type"].unique()))
block_list = list(np.sort(flat_prices["block"].unique()))
street_name_list = list(np.sort(flat_prices["street_name"].unique()))
storey_range_list = list(np.sort(flat_prices["storey_range"].unique()))
flat_model_list = list(np.sort(flat_prices["flat_model"].unique()))
index_list = ['month', 'town', 'flat_type', 'block', 'street_name', 'storey_range', 'floor_area_sqm', 'flat_model', 'lease_commence_date', 'remaining_lease']


with st.form("heart_disease_prediction"):
    month_input = st.date_input("Date of Sale", value=datetime.date.today())
    month = int(month_input.strftime("%Y") + month_input.strftime("%m") + month_input.strftime("%d"))

    town = town_list.index(st.selectbox("Town", town_list))
    flat_type = flat_type_list.index(st.selectbox("Flat Type", flat_type_list))
    block = block_list.index(st.selectbox("Block Number", block_list))
    street_name = street_name_list.index(st.selectbox("Street Name", street_name_list))

    storey_input = st.slider("Storey Number", 1, 60)
    storey = math.ceil(storey_input / 3) - 1

    floor_area_sqm = st.number_input("Floor Area in SQM", 1.00, step=0.01)
    flat_model = flat_model_list.index(st.selectbox("Flat Model", flat_model_list))

    lease_commence_date_input = st.date_input("Lease Commence Date", min_value=datetime.date(1960, 1, 1), value=datetime.date.today())
    lease_commence_date = int(lease_commence_date_input.strftime("%Y") + lease_commence_date_input.strftime("%m") + lease_commence_date_input.strftime("%d"))
    remaining_lease = 99 - ((month_input - lease_commence_date_input).days / 365)

    submitted = st.form_submit_button("Predict")
    
    fpModel = load(filename="FlatPricesModel.joblib")

    if submitted:
        input_data = pd.DataFrame([month, town, flat_type, block, street_name, storey, floor_area_sqm, flat_model, lease_commence_date, remaining_lease], index=index_list).transpose()
        make_prediction(fpModel, input_data)
