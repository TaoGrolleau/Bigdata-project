import CSVController as csv_controller
import Parser_Article as p
import Data_Analyser as d
import Idontknow as i

articles = p.cleaning_articles()
csv_controller.create_csv_file_for_R(articles)
i.return_main_topics()
i = 0
"""
for elem in articles[:1]:
	print(i, elem)
	i += 1
"""
#d.create_wordcloud()
#d.create_graph_authors()