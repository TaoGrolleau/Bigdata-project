import Parser_Article as p
import Article

articles = p.cleaning_articles()
i = 0
for elem in articles:
	i += 1
	print(i, elem)