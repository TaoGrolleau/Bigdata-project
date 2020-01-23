import Create_Data_Files as cdf
import Parser_Article as p
import PdfExtractor as pe
import Data_Analyser as d
import TopicModeling as tm
import Metrics as m

articles = p.cleaning_articles()
cdf.create_csv_file_for_R(articles)

pdf_files = dict()

i = 0
for elem in articles:
    print(i, elem)
    #pe.download_pdf_files(elem.pdfarticle, i)
    i += 1

d.create_wordcloud(articles)
#d.create_graph_authors(articles)

#tm.return_main_topics()
m.plot_articles_per_year(articles)

references_dic = pe.get_references(pe.get_authors_list(articles))

#Plot the most famous authors
pe.make_plot_famous_authors(references_dic, 50)

cdf.create_authors_graph_file(articles, 2)
