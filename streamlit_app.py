'encoding=utf-8'

import streamlit as st
import pandas as pd
from google.cloud import firestore
import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="testprojectDSCI551")

# Create a reference to the Google post.
doc_ref = db.collection("scams").document("1")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
