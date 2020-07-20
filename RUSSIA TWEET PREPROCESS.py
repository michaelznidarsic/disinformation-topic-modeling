# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:39:21 2020

@author: mznid
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



raw1 = pd.read_csv('D:\\TROLL TWEETS\\TWITTER\\russia_052020_tweets_csv_hashed_1.csv')
raw2 = pd.read_csv('D:\\TROLL TWEETS\\TWITTER\\russian_linked_tweets_csv_hashed.csv')
raw3 = pd.read_csv('D:\\TROLL TWEETS\\TWITTER\\russia_052020_tweets_csv_hashed_2.csv')



set(raw2.columns) - set(raw1.columns)
set(raw2.columns) - set(raw3.columns)


for each in raw2.loc[:,'poll_choices']:
    if not np.isnan(each):
        print('aha!')

# poll_choices is all nan



columnselection = list(raw1.columns)

raw1 = raw1.append(raw2.loc[:,columnselection])
del raw2

raw1 = raw1.append(raw3.loc[:,columnselection])
del raw3

# NULL ANALYSIS
with pd.option_context('display.max_rows', 150):
     print(raw1.isnull().sum().sort_values(ascending = False))


# BASICALLY ALL LATS/LONGS MISSING
with pd.option_context('display.max_rows', 150):
     print(raw1.isin(values = ['absent']).sum().sort_values(ascending = False))



print(raw1.iloc[0,:])

sum(raw1.loc[:,'like_count'])

'''
['tweetid',
 'userid',
 'user_display_name',
 'user_screen_name',
 'user_reported_location',
 'user_profile_description',
 'user_profile_url',
 'follower_count',
 'following_count',
 'account_creation_date',
 'account_language',
 'tweet_language',
 'tweet_text',
 'tweet_time',
 'tweet_client_name',
 'in_reply_to_userid',
 'in_reply_to_tweetid',
 'quoted_tweet_tweetid',
 'is_retweet',
 'retweet_userid',
 'retweet_tweetid',
 'latitude',
 'longitude',
 'quote_count',
 'reply_count',
 'like_count',
 'retweet_count',
 'hashtags',
 'urls',
 'user_mentions']

'''
# 'latitude','longitude',           pretty much all null  'absent'
# tweet_language

# list of hashed links    ,'user_mentions'

'''
num_mentions = []
for each in subsetdf.loc[:,'user_mentions']:
    num_mentions.append(len(each))
    
sum(num_mentions)
'''


raw1.loc[:,'tweet_language'] = raw1.loc[:,'tweet_language'].fillna('')



subsetlist = ['is_retweet','tweet_time','tweet_text','account_language','follower_count','userid','following_count','tweet_client_name','like_count','reply_count','quote_count','retweet_count','account_creation_date','tweet_language']

subsetdf = raw1.loc[:,subsetlist].dropna()

subsetdf.iloc[0,:]


subsetdf.loc[:,'account_creation_date'].sort_values()

plt.hist(subsetdf.loc[:,'account_language'])


plt.figure(figsize = (12,8))
plt.hist(raw1.loc[:,'tweet_language'].dropna())


sum(subsetdf.loc[:,'like_count'])        # 93090590
sum(subsetdf.loc[:,'quote_count'])       # 688900
sum(subsetdf.loc[:,'reply_count'])       # 1288117
sum(subsetdf.loc[:,'retweet_count'])     # 35727455



#plt.hist(list(zip(subsetdf.loc[:,'tweet_language'],subsetdf.loc[:,'account_language'])))


subsetdf.to_csv('D:\\russiantrolltweetsCLEAN.csv')
