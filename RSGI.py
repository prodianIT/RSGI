import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import altair as alt
import numpy as np

st.set_page_config(page_title="RSGI Dashboard", page_icon=":bar_chart:", layout="wide")
# ---- SIDEBAR ----
# with st.sidebar.header('1. Upload your CSV data'):
#     uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['csv'])
csv_files = ['data.000.csv', 'data.001.csv', 'data.002.csv', 'data.003.csv', 'data.004.csv', 'data.005.csv', 'data.006.csv', 'data.007.csv', 'data.008.csv', 'data.009.csv']


li = []

for filename in csv_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
df = frame

st.sidebar.header("Please Filter Here:")
# type = st.sidebar.multiselect(
#     "Select the Type:",
#     options=df["Type"].unique(),
#     default=df["Type"].unique()
# )
Type_of_claim = st.sidebar.multiselect(
    "Select the Type:",
    options=df["type_of_claim"].unique(),
    default=df["type_of_claim"].unique(),
)

Luxury_model = st.sidebar.multiselect(
    "Select the model:",
    options=df["luxury_model"].unique(),
    default=df["luxury_model"].unique()
)

Losscategory = st.sidebar.multiselect(
    "Select the losscategory:",
    options=df["losscategory"].unique(),
    default=df["losscategory"].unique()
)

Year_filter = st.sidebar.multiselect(
    "Select the year:",
    options=df["year_month"].unique(),
    default=df["year_month"].unique()
)

Reapairer_type = st.sidebar.multiselect(
    "Select the reapairer_type:",
    options=df["reapairer_type"].unique(),
    default=df["reapairer_type"].unique()
)

a = df.query(
    "luxury_model == @Luxury_model & type_of_claim ==@Type_of_claim & losscategory == @Losscategory & year_month == @Year_filter & reapairer_type == @Reapairer_type"
)

# ---- MAINPAGE ----
st.title(":bar_chart: RSGI Dashboard")
st.markdown("##")

option_list = ['amount paid', 'claim count', 'repair amount', 'parts net amount']
result = st.selectbox('select your analysis category', option_list)

if result == 'amount paid':
    # claim amount
    st.header('*amount_paid*')
    st.caption('amount in crores')
    b = a.pivot_table(values='amount_paid_y',
                      index=['year_month', 'Ageofthevehicle'],
                      columns=['reapairer_type'],
                      aggfunc='sum')
    b.reset_index(inplace=True)
    b.columns = ['year_month', 'Ageofthevehicle', 'dealer', 'OTHERS', 'TRS']
    b['dealer'] = b['dealer'] / 10000000
    b['OTHERS'] = b['OTHERS'] / 10000000
    b['TRS'] = b['TRS'] / 10000000
    b['dealer_%'] = (b['dealer'] / b['dealer'].sum()) * 100
    b['OTHERS_%'] = (b['OTHERS'] / b['OTHERS'].sum()) * 100
    b['TRS_%'] = (b['TRS'] / b['TRS'].sum()) * 100
    b = b[['year_month', 'Ageofthevehicle', 'dealer', 'dealer_%', 'OTHERS', 'OTHERS_%', 'TRS',
           'TRS_%']]
    b


if result == 'claim count':
    # claim counts
    st.header('*claim_number*')
    st.caption('count in thousands')
    b = a.pivot_table(values='claim_number',
                      index=['year_month', 'Ageofthevehicle'],
                      columns=['reapairer_type'],
                      aggfunc='count')
    b.reset_index(inplace=True)
    b.columns = ['year_month', 'Ageofthevehicle', 'dealer', 'OTHERS', 'TRS']
    b['dealer'] = b['dealer'] / 1000
    b['OTHERS'] = b['OTHERS'] / 1000
    b['TRS'] = b['TRS'] / 1000
    b['dealer_%'] = (b['dealer'] / b['dealer'].sum()) * 100
    b['OTHERS_%'] = (b['OTHERS'] / b['OTHERS'].sum()) * 100
    b['TRS_%'] = (b['TRS'] / b['TRS'].sum()) * 100
    b = b[['year_month', 'Ageofthevehicle', 'dealer', 'dealer_%', 'OTHERS', 'OTHERS_%', 'TRS',
           'TRS_%']]
    b


if result == 'repair amount':
    # repair amount
    st.header('*netlabmountsum*')
    st.caption('amount in crores')
    b = a.pivot_table(values='netlabmountsum',
                      index=['year_month', 'Ageofthevehicle'],
                      columns=['reapairer_type'],
                      aggfunc='sum')
    b.reset_index(inplace=True)
    b.columns = ['year_month', 'Ageofthevehicle', 'dealer', 'OTHERS', 'TRS']
    b['dealer'] = b['dealer'] / 10000000
    b['OTHERS'] = b['OTHERS'] / 10000000
    b['TRS'] = b['TRS'] / 10000000
    b['dealer_%'] = (b['dealer'] / b['dealer'].sum()) * 100
    b['OTHERS_%'] = (b['OTHERS'] / b['OTHERS'].sum()) * 100
    b['TRS_%'] = (b['TRS'] / b['TRS'].sum()) * 100
    b = b[['year_month', 'Ageofthevehicle', 'dealer', 'dealer_%', 'OTHERS', 'OTHERS_%', 'TRS',
           'TRS_%']]
    b


if result == 'parts net amount':
    # parts amount
    st.header('*parts_net_amountsum*')
    st.caption('amount in crores')
    b = a.pivot_table(values='parts_net_amountsum',
                      index=['year_month', 'Ageofthevehicle'],
                      columns=['reapairer_type'],
                      aggfunc='sum')
    b.reset_index(inplace=True)
    b.columns = ['year_month', 'Ageofthevehicle', 'dealer', 'OTHERS', 'TRS']
    b['dealer'] = b['dealer'] / 10000000
    b['OTHERS'] = b['OTHERS'] / 10000000
    b['TRS'] = b['TRS'] / 10000000
    b['dealer_%'] = (b['dealer'] / b['dealer'].sum()) * 100
    b['OTHERS_%'] = (b['OTHERS'] / b['OTHERS'].sum()) * 100
    b['TRS_%'] = (b['TRS'] / b['TRS'].sum()) * 100
    b = b[['year_month', 'Ageofthevehicle', 'dealer', 'dealer_%', 'OTHERS', 'OTHERS_%', 'TRS',
           'TRS_%']]
    b


