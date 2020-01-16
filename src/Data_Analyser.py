import Parser_Article as p
'''Requires pip install wordcloud'''
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt

def create_bag_of_words_model_title():
    d = dict()
    list_articles = p.cleaning_articles()
    for article in list_articles:
        for item in article.title:
            d[item] = d.get(item, 0) + 1
    return d

def create_bag_of_words_model_abstract():
    d = dict()
    list_articles = p.cleaning_articles()
    for article in list_articles:
        for item in article.abstract:
            d[item] = d.get(item, 0) + 1
    return d

def create_wordcloud():
    frequencies_title = create_bag_of_words_model_title()
    frequencies_abstract = create_bag_of_words_model_abstract()

    wc_title = WordCloud(background_color='white', width=1200, height=800)
    wc_abstract = WordCloud(background_color='white', width=1200, height=800, max_words=100)

    wc_title.generate_from_frequencies(frequencies_title)
    wc_abstract.generate_from_frequencies(frequencies_abstract)

    wc_abstract.to_file('../out/wordcloud_abstract.png')
    wc_title.to_file('../out/wordcloud_title.png')