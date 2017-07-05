
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

def run(path = 'calorie.csv'):
    df = pd.read_csv(path)
    df.fillna(0, inplace=True)
    print("DATA loaded with size : ", len(df))
    mat = df.as_matrix()
    return mat




# In[3]:

if __name__ == "__main__":
    run()


# In[ ]:



