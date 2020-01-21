import Create_Data_Files as cdf
import Parser_Article as p
import Data_Analyser as d
import TextRankKeywords as trk
import TopicModeling as tm

articles = p.cleaning_articles()
#cdf.create_csv_file_for_R(articles)

text_rank = trk.TextRankKeyword()
all_topics = []

i = 0
tm.return_main_topics()
"""
for elem in articles:
	text_rank.analyze(elem)
	print(i, elem)
	all_topics.append(text_rank.get_keywords(4))
	i += 1
"""
#d.create_wordcloud(articles)
#d.create_graph_authors(articles)

#d.get_main_topics(all_topics)
#cdf.create_authors_graph_file(articles, 2)