
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics import pairwise_distances
import joblib
#from joblib import load
import pandas as pd
import streamlit as st

st.write(
 '''
 # What do you love in a coffee shop?
 '''
 )

cv = joblib.load('/aziker13/Metis_Project_Deliverables/Data_Engineering/Final_Code/SeaCoffeeRecModel_cv.joblib') 
nmf_model = joblib.load('SeaCoffeeRecModel_nmf.joblib')
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

