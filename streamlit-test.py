'encoding=utf-8'

import streamlit as st
import pandas as pd
from google.cloud import firestore

# db = firestore.Client.from_service_account_json("testprojectdsci551-python-key.json")
# doc_ref = db.collection("scams")

# for doc in doc_ref.stream():
# 	st.write("The contents are: ", doc.to_dict())


header = st.container()
dataset = st.container()
tables = st.container()
questions = st.container()

with header:
    st.title('CryptoScamDB')
    st.text('Know of a crypto scam? Please report below to protect your fellow investors!')

with tables:
    st.header('Scam Watch')
    st.text('Take a look at scams that we are aware of: ')

# take df from scams.py
    data = pd.read_csv('scams.csv', index_col=False)
    st.dataframe(data)
    st.text('\n')
    num_scams = len(data)
    st.text('There are currently ' + str(num_scams) + ' scams reported to CryptoScamDB.')

    # num_scams = pd.DataFrame(data['URL'].value_counts())
    # print(num_scams)
    # st.text('There are currently ' + num_scams + ' scams reported to CryptoScamDB.')

# show df too, make columns visible, maybe agg by coin or something??

with questions:
    st.subheader('Tell us more: ')

drop = st.selectbox('How many years have you been in crypto?', options=['Select one', '< 1', '1-3', '3-5', '5+'])
input_q1 = st.text_input('Which coins were targeted in this scam?')
input_q2 = st.text_input('What amount of those coins were targeted in this scam?')
input_q3 = st.text_input('Which wallet do you use to store your coins?')
input_q4 = st.text_input('Please provide a description below.')

if st.button('Submit'):
     st.write('Thanks for helping us catch crypto scammers!')


# URLs to crypto scam alrts like whale alert or scam alert, etc?
# aggregate and visualize?