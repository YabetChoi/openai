#https://learn.microsoft.com/ko-kr/azure/cognitive-services/openai/tutorials/embeddings?tabs=powershell

import openai
import os
import re
import requests
import sys
from num2words import num2words
import os
import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity
import tiktoken

openai.api_type = "azure"
openai.api_key = "3f64fb01b20b4d04bea2ffabe52ea494"
openai.api_base = "https://aoi-yb1.openai.azure.com/"
openai.api_version = "2023-05-15"


df=pd.read_csv(os.path.join(os.getcwd(),'bill_sum_data.csv')) # This assumes that you have placed the bill_sum_data.csv in the same directory you are running Jupyter Notebooks
#df

df_bills = df[['text', 'summary', 'title']]
#df_bills

#  불필요한 공백을 제거하고 문장 부호를 정리하여 토큰화를 위한 데이터를 준비하여 간단한 데이터 정리를 수행합니다.
pd.options.mode.chained_assignment = None #https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#evaluation-order-matters

# s is input text
def normalize_text(s, sep_token = " \n "):
    s = re.sub(r'\s+',  ' ', s).strip()
    s = re.sub(r". ,","",s)
    # remove all instances of multiple spaces
    s = s.replace("..",".")
    s = s.replace(". .",".")
    s = s.replace("\n", "")
    s = s.strip()
    
    return s

df_bills['text']= df_bills["text"].apply(lambda x : normalize_text(x))

#이제 토큰 제한(8192 토큰)에 비해 너무 긴 청구서를 제거해야 합니다.
tokenizer = tiktoken.get_encoding("cl100k_base")
df_bills['n_tokens'] = df_bills["text"].apply(lambda x: len(tokenizer.encode(x)))
df_bills = df_bills[df_bills.n_tokens<8192]
len(df_bills)

# sample_encode = tokenizer.encode(df_bills.text[0]) 
# decode = tokenizer.decode_tokens_bytes(sample_encode)
# decode

df_bills['ada_v2'] = df_bills["text"].apply(lambda x : get_embedding(x, engine = 'text-embedding-ada-002')) # engine should be set to the deployment name you chose when you deployed the text-embedding-ada-002 (Version 2) model