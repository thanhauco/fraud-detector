import streamlit as st
import pandas as pd
import sqlite3
st.title('Fraud Dashboard')
conn = sqlite3.connect('fraud.db')
df = pd.read_sql('SELECT * FROM transactions', conn)
st.write(df)
st.bar_chart(df['amount'])