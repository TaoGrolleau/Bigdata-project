import src.CSVController as csv_controller
import src.Parser_Article as p

articles = p.cleaning_articles()
csv_controller.create_csv_file_for_R(articles)