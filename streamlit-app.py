# 'encoding=utf-8'

import streamlit as st
import pandas as pd
from google.cloud import firestore

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

    data = pd.read_json('https://testprojectdsci551-default-rtdb.firebaseio.com/__collections__/scams/.json')
    st.dataframe(data)

    st.text('\n')
    num_scams = len(data)
    st.text('There are currently ' + str(num_scams) + ' scams reported to CryptoScamDB.')

with questions:
    st.subheader('Tell us more: ')

drop = st.selectbox('How many years have you been in crypto?', options=['Select one', '< 1', '1-3', '3-5', '5+'])
input_q1 = st.text_input('Which coins were targeted in this scam?')
input_q2 = st.text_input('What amount of those coins were targeted in this scam?')
input_q3 = st.text_input('Which wallet do you use to store your coins?')
input_q4 = st.text_input('Please provide a description below.')

if st.button('Submit'):
     st.write('Thanks for helping us catch crypto scammers!')


# Modules
import pyrebase
import streamlit as st
import pandas as pd
from datetime import datetime


# Configuration Key
firebaseConfig = {
  'apiKey': "AIzaSyAs7s4nBspSeIeekJmoq-rMhE9in_9xsiM",
  'authDomain': "testprojectdsci551.firebaseapp.com",
  'databaseURL': "https://testprojectdsci551-default-rtdb.firebaseio.com",
  'projectId': "testprojectdsci551",
  'databaseURL': "https://testprojectdsci551-default-rtdb.firebaseio.com/",
  'storageBucket': "testprojectdsci551.appspot.com",
  'messagingSenderId': "680668884953",
  'appId': "1:680668884953:web:5dd68fcaa35ca9f9d133c8",
  'measurementId': "G-445KRB68VT"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()

st.sidebar.title("Crypto Scam DB")

# Authentication

choice = st.sidebar. selectbox('Login/Signup', ['Login', 'Sign up'])

email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password',type = 'password')

if choice == 'Sign up':
	handle = st.sidebar.text_input('Please input a user name',value = 'Default')
	submit = st.sidebar.button('Create my account')

	if submit:
		user = auth.create_user_with_email_and_password(email,password)
		st.success('Your account is created sucessfully!')
		# Sign in
		user = auth.sign_in_with_email_and_password(email,password)
		db.child(user['localId']).child("Handle").set(handle)
		db.child(user['localId']).child("ID").set(user['localId'])
		st.title('Welcome' + handle)
		st.info('Login via login drop down selection')
