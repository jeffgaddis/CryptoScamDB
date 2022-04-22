
import pandas as pd
import json

with open('scams.json', 'r') as f:
  data = json.load(f)
    
# print(data)

iden_lst = []
name_lst = []
url_lst = []
coin_lst = []
cat_lst = []
sub_lst = []
desc_lst = []
rep_lst = []

for i in range(len(data)):
    
    try:
      iden = data[i]['id']
      iden_lst.append(iden)
      
    except:
      iden_lst.append(',')
    
    try:
      name = data[i]['name']
      name_lst.append(name)
      
    except:
      name_lst.append(',')
    
    try:
      url = data[i]['url']
      url_lst.append(url)
      
    except:
      url_lst.append(',')
    
    try:
      coin = data[i]['coin']
      coin_lst.append(coin)
      
    except:
      coin_lst.append(',')
    
    try:
      cat = data[i]['category']
      cat_lst.append(cat)
      
    except:
      cat_lst.append(',')
    
    try:
      sub = data[i]['subcategory']
      sub_lst.append(sub)
    
    except:
      sub_lst.append(',')
    
    try:
        desc = data[i]['description'] 
        desc_lst.append(desc)
        
    except:
        desc_lst.append(',')
    
    try:
      rep = data[i]['reporter']
      rep_lst.append(rep)

    except:
      rep_lst.append(',')
    
# make df with cols = these lists above, then export to .csv for streamlit

df = pd.DataFrame (iden_lst, columns = ['ID'])


df2 = pd.DataFrame (name_lst, columns = ['Site'])


df3 = pd.DataFrame (url_lst, columns = ['URL'])


df4 = pd.DataFrame (coin_lst, columns = ['Coin'])


df5 = pd.DataFrame (cat_lst, columns = ['Category'])


df6 = pd.DataFrame (sub_lst, columns = ['Wallet'])


df7 = pd.DataFrame (desc_lst, columns = ['Description'])


df8 = pd.DataFrame (rep_lst, columns = ['Reporter'])

# merge all df's together
merged_df = pd.concat([df, df2, df3, df4, df5, df6, df7, df8], axis=1)
merged_df.to_csv('scams.csv', index=False)
print(merged_df)
