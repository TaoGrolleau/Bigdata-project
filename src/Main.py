import Create_Data_Files as cdf
import Parser_Article as p
import PdfExtractor as pe
import Data_Analyser as d
import TopicModeling as tm
import Metrics as m
import Tweet_Analyser as pt

"""
Pre-processing
"""
# Get the list of articles all cleaned
articles = p.cleaning_articles()

# Create a csv file for R analysis (OUTDATED)
cdf.create_csv_file_for_R(articles)

# Create the repository for the pdf files
pe.create_pdf_dir()

# Download each article's pdf
i = 0
for elem in articles:
    pe.download_pdf_files(elem.pdfarticle, i)
    i += 1

"""
Some metrics
"""
# Computes some metrics about the dataset
m.plot_articles_per_year(articles)

"""
Text Analysis
"""
# Create wordcloud_abstract.png and wordcloud_title.png
d.create_wordcloud(articles)

# Compute the main topics for each article and plot the result
tm.return_main_topics()

"""
Social Analysis
"""
# Get the references of each article
references_dic = pe.get_references(pe.get_authors_list(articles))

#Plot the most famous authors
pe.make_plot_famous_authors(references_dic, 50)

# Create graph_authors.png (OUTDATED)
d.create_graph_authors(articles)

# Create a TXT file to be computed with the R script
cdf.create_authors_graph_file(articles, 2)

"""
Tweets
"""
# Get the list of tweets and get tweet activity
list = pt.parse_json()
pt.get_tweet_activity(list)

# Parse whitout the Retweeted tweets and get the most liked and retweeted tweets
listNoRt = pt.parse_json_no_RT()
pt.get_most_rt_fav_tweets(listNoRt)

# Get the most quoted and the most RT persons
pt.get_Most_Quoted_Person()
pt.get_Most_RT_Person()

print('Done !')
