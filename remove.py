import json
import os
import glob
import pandas as pd
import itertools
#file_path = glob.glob('positive/*.json')
file_path = glob.glob('positive/1128.json')
print("read")
count = 0
# for file in file_path:
#     df = pd.read_json(file)
#     if(df['meta']['lang1'] =='eng' or df['meta']['lang2']=='eng'):
#         print(count)
#         count += 1
#     else:
#         os.remove(file)
myDf = pd.DataFrame(columns=['English','Spanish'])
for file in file_path:
     df = pd.read_json(file)
     #print(df.iloc[:,0])
     eng = df.iloc[:,0]
     if df.iloc[:,2].name == 'meta' :
        spa = df.iloc[:,1]
     else:
        spa = df.iloc[:,2]
     print(spa.name)
     engNews = eng['articles']['results']
     spaNews = spa['articles']['results']
     print(len(engNews))
     tempDf = {}
     i =0
     for a in engNews:
         for b in spaNews:
            #print(a['body'])
            #tempDf['English'] = a['body']
            #tempDf['Spanish'] = b['body']
            #print(tempDf)
            myDf.loc[i,'English'] = a['body']
            myDf.loc[i,'Spanish'] = b['body']
            i+=1
     #numarticles = min(df['meta']['artCount1'],df['meta']['artCount2'])
     #itertools.product(eng['articles']['results'])
    #  ["info"]["articleCount"]
print(myDf)