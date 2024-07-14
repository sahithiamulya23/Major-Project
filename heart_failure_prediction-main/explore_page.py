import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt




def load_data():
    df = pd.read_csv("smoted_df.csv")
    df = df[["age", "platelets", "creatinine_phosphokinase", "ejection_fraction", "serum_creatinine","serum_sodium"]]
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Prediction Parameters")
    st.write("""### Age Parameter""")
    st.write(f'Min age: {min(df["age"])}')
    st.write(f'Max Age: {max(df["age"])}')

    st.write("""### platelets Parameter""")
    st.write(f'Min platelets: {min(df["platelets"])}')
    st.write(f'Max platelets: {max(df["platelets"])}')

    st.write("""### creatinine_phosphokinase Parameter""")
    st.write(f'Min creatinine_phosphokinase: {min(df["creatinine_phosphokinase"])}')
    st.write(f'Max creatinine_phosphokinase: {max(df["creatinine_phosphokinase"])}')

    st.write("""### ejection_fraction Parameter""")
    st.write(f'Min ejection_fraction: {min(df["ejection_fraction"])}')
    st.write(f'Max ejection_fraction: {max(df["ejection_fraction"])}')

    st.write("""### serum_creatinine Parameter""")
    st.write(f'Min serum_creatinine: {min(df["serum_creatinine"])}')
    st.write(f'Max serum_creatinine: {max(df["serum_creatinine"])}')

    st.write("""### serum_sodium Parameter""")
    st.write(f'Min serum_sodium: {min(df["serum_sodium"])}')
    st.write(f'Max serum_sodium: {max(df["serum_sodium"])}')

    
