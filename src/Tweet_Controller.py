import json
import re
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import  matplotlib.pyplot as plt
from wordcloud import WordCloud

from Tweet import Tweet

def parse_json():

    list_all_tweet = []

    with open('../resources/EGC_tweets.json', 'r', encoding="utf8") as f:
        tweet_dict = json.load(f)

        for t in tweet_dict:
            text = t['text']
            fav = t['favorite_count']
            rt = t['retweet_count']
            date_tweet = str(t['created_at']).replace('+0000', '')
            date_tweet = pd.to_datetime(date_tweet, format='%c')
            #print(date_tweet)
            tweet = Tweet(text,fav,rt,date_tweet)
            list_all_tweet.append(tweet)
    #print(list_all_tweet)
    return list_all_tweet

def get_RT_Tweets():
    list_all_rt_tweet = []
    with open('../resources/EGC_tweets.json', 'r', encoding="utf8") as f:
        tweet_dict = json.load(f)

        for t in tweet_dict:
            if 'retweeted_status' in t:
                list_all_rt_tweet.append(t['text'])

    #print(list_all_rt_tweet)
    return list_all_rt_tweet


def get_most_rt_fav_tweets(listTweets):
    list_rt_sorted = sorted(listTweets, key=lambda tweet: tweet[2], reverse=True)
    list_fav_sorted = sorted(listTweets, key=lambda tweet: tweet[1], reverse=True)
    print(list_rt_sorted[0])
    print(list_fav_sorted[0])


def bag_Of_Word(listTweets):
    clean_list = []
    for i in range(len(listTweets)):
       # listTweets[i] = listTweets[i].replace(@\S, '')
        print(listTweets[i])
   # wc_title = WordCloud(background_color='white', width=1200, height=800)

def get_Most_Quoted_Person():
    listmentions = []
    list_user = []
    #myre = re.compile('❄|🥧')
    with open('../resources/EGC_tweets.json', 'r', encoding="utf8") as f:
        tweet_dict = json.load(f)
        for t in tweet_dict:
            if t['entities']['user_mentions']:
                listmentions.append(t['entities']['user_mentions'])
                #print(t)
        for userm in listmentions:
            for e in userm:
                #word = myre.sub('', str(e))
                #word = e['name'].encode('ascii', 'ignore').decode('ascii')
                list_user.append(str(e['name']))
                #print(e['name'])

        unique_words = set(list_user)

        pd.Series(list_user).value_counts().head(20).plot.bar(
            figsize=(14, 7), fontsize=16, color='lightcoral'
        )
        plt.gca().set_title(' top quoted user', fontsize=20)
        plt.gca().set_xticklabels(plt.gca().get_xticklabels(), rotation=45, ha='right', fontsize=16)
        plt.show()

def get_tweet_activity(listTweets):
    #print(listTweets)
    list_time = []
    for t in listTweets:
        list_time.append(t[3])


    trace = go.Histogram(
        x=list_time,
        marker=dict(
            color='blue'
        ),
        opacity=0.75
    )

    layout = go.Layout(
        title='Tweet Activity',
        height=450,
        width=1200,
        xaxis=dict(
            title='Month and year'
        ),
        yaxis=dict(
            title='Tweet Quantity'
        ),
        bargap=0.2,
    )

    data = [trace]

    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig)