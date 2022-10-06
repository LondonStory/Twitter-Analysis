#-------------Import-----------------------------------
import pandas as pd

#-------------Load the csv files-----------------------
df1 = pd.read_csv ('replies1.csv')
df2 = pd.read_csv ('replies2.csv')
df3 = pd.read_csv ('replies3.csv')

#-----------Concatinate them---------------------------
replies = pd.concat([df1,df2,df3]).drop_duplicates().reset_index(drop=True)

#----------------Save the results----------------------
replies.to_csv('replies.csv', index=False)
