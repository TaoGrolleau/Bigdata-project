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

def create_wordcloud():
    frequencies = create_bag_of_words_model_title()
    wc = WordCloud(background_color="white", width=1200, height=800)
    wc.generate_from_frequencies(frequencies)
    wc.to_file('../out/wordcloud_title.png')

create_wordcloud()