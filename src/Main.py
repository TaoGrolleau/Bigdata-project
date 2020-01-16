import CSVController as csv_controller
import Parser_Article as p
import Data_Analyser as d

articles = p.cleaning_articles()
csv_controller.create_csv_file_for_R(articles)

i = 0
for elem in articles:
	print(i, elem.authors)
	i += 1
#d.create_wordcloud()
d.create_graph_authors()