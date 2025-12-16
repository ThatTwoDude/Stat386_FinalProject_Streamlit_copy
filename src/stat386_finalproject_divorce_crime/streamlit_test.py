import streamlit as st
import pandas as pd
import os
import json
import matplotlib.pyplot as plt

# print(os.getcwd())

# url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv("../data/Combined_DF.csv")

st.title("Discovering the Relationship Between Divorce and Crime")
# st.write("This is my first streamlit app")

with open('../json/crime_abbr.json', 'r') as file:
    crime_json = json.load(file)

# Reverse mapping: full name -> code
offense_map = crime_json["offenses"]
name_to_code = {v: k for k, v in offense_map.items()}

# sidebar controls
state = st.sidebar.selectbox(
    "Select a state",
    sorted(df['state'].unique())
)

crime_name = st.sidebar.selectbox(
    "Select a crime",
    list(name_to_code.keys()) 
)
crime_code = name_to_code[crime_name] 

metric = st.sidebar.radio(
    "Select metric",
    ["Actual", "Rate"]
)

column_name = f"{crime_code}_{metric.lower()}"

filtered = (
    df[df['state'] == state]
    .sort_values("year")
)

# plot
fig, ax = plt.subplots()
ax.plot(filtered["year"], filtered[column_name])
ax.set_xlabel("Year")
ax.set_ylabel(f"{metric} of {crime_name}")
ax.set_title(f"{crime_name} ({metric}) in {state} Over Time")
st.pyplot(fig)

# st.dataframe(df)