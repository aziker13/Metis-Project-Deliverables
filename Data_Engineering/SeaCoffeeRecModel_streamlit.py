"""
Make sure to install streamlit with `pip install streamlit`.

To run this app:

1. cd into this directory
2. Run `streamlit run SeaCoffeeRecModel_streamlit.py`
"""

from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics import pairwise_distances
from joblib import load
import pandas as pd
import streamlit as st

st.write(
 '''
 # What do you love in a coffee shop?
 '''
 )

cv = load('SeaCoffeeRecModel_cv.joblib') 
nmf_model = load('SeaCoffeeRecModel_nmf.joblib')
df = pd.read_csv('SeaCoffeeRecModel_df.csv', index_col='name')

def get_coffee_recs(string_lst,n_recs=1, df=df,vect=cv,model=nmf_model):
    vt = cv.transform(string_lst)
    tt = model.transform(vt)
    top_n = pairwise_distances(tt,df).argsort().tolist()[0][:n_recs]
    recs = []
    for i in top_n:
        recs.append((df.iloc[i].name))
    return recs[0]

user_input = st.text_input("Keyword", value='latte')
shop_name = get_coffee_recs([user_input])
st.write(
f'''
 ## In Seattle I recommend: {shop_name}
'''
)



# st.write(
# '''
# You can use markdown syntax to style your text

# Headers:
# # Main Title 
# ## Sub Title 
# ### header 

# **bold text**

# *italics*

# Ordered List

# 1. Apples 
# 2. Oranges 
# 3. Bananas 

# [This is a link](https://docs.streamlit.io/en/stable/getting_started.html)

