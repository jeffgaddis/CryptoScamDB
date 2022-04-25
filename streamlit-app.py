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
password = st.sidebar.text_input('Please enter your password')

if choice == 'Sign up':
	handle = st.sidebar.text_input('Please input a user name',value = 'Default')
	submit = st.sidebar.button('Create my account')

	if submit:
		user = auth.create_user_with_email_and_password(email,password)
		st.success('Your account is created sucessfully!')

