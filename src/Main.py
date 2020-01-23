import Create_Data_Files as cdf
import Parser_Article as p
import Data_Analyser as d
import Tweet_Controller as pt

#articles = p.cleaning_articles()
#cdf.create_csv_file_for_R(articles)

i = 0
#for elem in articles[:2]:
#	print(i, elem)
#	i += 1
#d.create_wordcloud(articles)
#d.create_graph_authors(articles)

#cdf.create_authors_graph_file(articles, 2)


## Tweets ##

#list = pt.parse_json()
#pt.get_tweet_activity(list)

#listNoRt = pt.parse_json_no_RT()
#pt.get_most_rt_fav_tweets(listNoRt)

#pt.get_Most_Quoted_Person()
pt.get_Most_RT_Person()
