import streamlit as st
import pickle
import numpy as np



def load_model():
    with open('final_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


def show_predict_page():
    st.title("Heart Failure Prediction")

    st.write("""### We need some information to predict the Risk of your heart""")

    age = st.number_input("Age", step=0.1)
    # anaemia = st.text_input("anaemia", "")
    platelets = st.number_input("platelets", step=0.1)
    creatinine_phosphokinase = st.number_input("creatinine_phosphokinase", step=1, format="%d")
    ejection_fraction = st.number_input("ejection_fraction", step=1, format="%d")
    serum_creatinine = st.number_input("serum_creatinine", step=0.1)
    serum_sodium = st.number_input("serum_sodium", step=1, format="%d")
    # sex = st.selectbox("sex", (0,1))
    # high_blood_pressure = st.selectbox("high_blood_pressure", (0,1))
    # time = st.number_input("time", step=1, format="%d")


    ok = st.button("Predict")
    if ok:
        X = np.array([[age	,creatinine_phosphokinase,	ejection_fraction	,platelets,	serum_creatinine,	serum_sodium]])
        model = data["model"]
        risk = model.predict_proba(X)
        st.subheader(f"The estimated risk is {risk[0][1]*100}")





