import Parser_Article as p
"""Requires pip install wordcloud"""
from wordcloud import WordCloud
"""Requires pip install networkx"""
import networkx as nx
from PIL import Image
import matplotlib.pyplot as plt

def create_bag_of_words_model_title(list_articles):
    d = dict()
    for article in list_articles:
        for item in article.title:
            d[item] = d.get(item, 0) + 1
    return d

def create_bag_of_words_model_abstract(list_articles):
    d = dict()
    for article in list_articles:
        for item in article.abstract:
            d[item] = d.get(item, 0) + 1
    return d

def create_wordcloud(list_articles):
    frequencies_title = create_bag_of_words_model_title(list_articles)
    frequencies_abstract = create_bag_of_words_model_abstract(list_articles)

    wc_title = WordCloud(background_color='white', width=1200, height=800)
    wc_abstract = WordCloud(background_color='white', width=1200, height=800, max_words=100)

    wc_title.generate_from_frequencies(frequencies_title)
    wc_abstract.generate_from_frequencies(frequencies_abstract)

    wc_abstract.to_file('../out/wordcloud_abstract.png')
    wc_title.to_file('../out/wordcloud_title.png')

def create_graph_authors(list_articles):
    graph = nx.Graph()
    i = 0
    for article in list_articles:
        j = 0
        for article2 in list_articles:
            if i != j and correlation_list(article.authors, article2.authors, 4):
                graph.add_node(i)
                graph.add_node(j)
                graph.add_edge(i, j)
            j += 1
        i += 1
    nx.clustering(graph)
    nx.draw(graph, with_labels=True)
    #plt.show()
    plt.savefig('../out/graph_authors.png')

def correlation_list(l1, l2, k=1):
    score = 0
    for item in l1:
        if item in l2:
            score += 1;
        if score == k:
            return True
    return False
