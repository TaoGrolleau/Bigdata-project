import src.Parser_Article as p
import src.Article
import src.CSVController as csv_controller

articles = p.cleaning_articles()
"""i = 0
for elem in articles:
	i += 1
	print(i, elem)"""
csv_controller.create_csv_file_for_R(articles)