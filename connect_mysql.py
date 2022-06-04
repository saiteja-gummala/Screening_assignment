# streamlit_app.py

import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        a = cur.fetchall()
        cur.close()
        return a

#rows = run_query("call bank_details.account_balance;")
#rows = run_query("call bank_details.transactaion_details('2013-01-01','2013-10-10');")
rows = run_query("call bank_details.Withdraw_amount;")
print(rows)
# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")


