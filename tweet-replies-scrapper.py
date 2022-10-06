#--------------------Imports-----------------------

import twint
import pandas as pd
import nest_asyncio
from collections import Counter

nest_asyncio.apply()

#---------------Declare parameters-----------------

# provide username
username = 'larrouturou'

# provide conversation id for which we want to scrape the replies
conversation_id = '1541498855061164034'

# provide the number of most recent tweets you want to scrape
N = 100000

# provide the beginning date ( '%Y-%m-%d %H:%M:%S' format)
since_date = '2022-06-27 01:01:01'

# provide the end date
until_date = '2022-07-02 24:60:60'


#---------------Scrape tweet replies----------------

def get_replies (user_name, conversation_id, num, since_date, until_date):
    print ("=======================================================")
    print(":: Acquiring tweet replies to ", conversation_id, "::")
    print ("=======================================================")

    # configure replies call
    replies = twint.Config()


    replies.To = user_name
    replies.Since = since_date
    replies.Until = until_date
    replies.Limit = num


    replies.Store_object =  True
    replies.User_full = True
    replies.Profile_full = True
    replies.Hide_output = True

    replies.Pandas = True
    twint.run.Search(replies)
    df = twint.storage.panda.Tweets_df

    df = df [df ['conversation_id'] == conversation_id]

    return pd.DataFrame(df)

#----------------Run the function----------------------

replies = get_replies (user_name=username, conversation_id=conversation_id, num=N, since_date=since_date, until_date=until_date)


#----------------Save the results----------------------

replies.to_csv('replies.csv', index=False)
