import pandas as pd
import numpy as np
df =pd.read_csv("final.csv")

df = df [df['soup'].notna()]
from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer(stop_words='english')
countmatrix = count.fit_transform(df['soup'])

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim2 = cosine_similarity(countmatrix,countmatrix)

df = df.reset_index()
indices = pd.Series(df.index,index = df['original_title'])

def getrecommendations(title,cosine_sim):
  idx = indices[title]
  simscores = list(enumerate(cosine_sim[idx]))
  simscores = sorted(simscores , key = lambda x:x[1],reverse = True)
  simscores = simscores[1:11]
  movieindices = [i[0]for i in simscores]
  return df[['original_title','poster_link',"vote_average",'release_date','runtime','overview']].iloc[movieindices].values.tolist()