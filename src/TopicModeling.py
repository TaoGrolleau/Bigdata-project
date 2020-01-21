from functools import reduce

import Parser_Article as p
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

list_main_topics = dict()

def return_main_topics():
    sns.set_style("dark")
    list_articles = p.cleaning_articles()
    dictionnary_year_topic = dict()
    list_year_article = []


    for article in list_articles:
        n_topic = 1

        if article.year not in list_year_article:
            dictionnary_year_topic[str(article.year)] = []
            list_year_article.append(article.year)

        tf_vectorizer = CountVectorizer(max_df=2, min_df=1, max_features=3)
        tf = tf_vectorizer.fit_transform(article.title)

        lda = LatentDirichletAllocation(max_iter=1, random_state=0, n_components=1).fit(tf)

        no_top_words = 5

        dictionnary_year_topic[str(article.year)] = add_topic(dictionnary_year_topic[str(article.year)], display_topics(lda, tf_vectorizer.get_feature_names(), no_top_words))

    #display_dict(dictionnary_year_topic)
    jaccard_sim = []

    list_topic = []
    list_list_topic = []
    for key,value in dictionnary_year_topic.items():
        for list in value:
            for text in list:
                list_topic.append(text)

        list_list_topic.append(list_topic)
        list_topic = []

    list_ligne = []
    for key1,values1 in dictionnary_year_topic.items():
        for list1 in values1:
            for key2, values2 in dictionnary_year_topic.items():
                for list2 in values2:
                    if(key1 != key2):
                        if (list1 == list2):
                            if list1 not in list_ligne :
                                list_ligne.append(list1)


    #display_jaccard(jaccard_sim)
    dict_topic_tf = dict()
    tf = 0
    for topic in list_ligne:
        for key,values in dictionnary_year_topic.items():
            for list in values:
                if topic == list:
                    tf = tf + 1

        dict_topic_tf[str(topic)] = tf
        tf = 0

    dict_topic_tf = sorted(dict_topic_tf.items(), key=lambda t: t[1], reverse=True)

    plot_topic(dict_topic_tf)

def display_topics(model, feature_names, no_top_words):
    list_topics = []
    for topic_idx, topic in enumerate(model.components_):
        for i in topic.argsort():
            list_topics.append(feature_names[i])

    return list_topics

def add_topic(list_topic1, list_topic2):
    list_topic = list_topic1
    if list_topic2 not in list_topic :
        list_topic.append(list_topic2)

    return list_topic

def display_dict(dictionnary_year_topic):
    for key, value in dictionnary_year_topic.items():
        print(key,value)

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

def display_jaccard(jaccard_sim):
    for list in jaccard_sim:
        print(list)

def plot_jaccard(jaccard_sim):
    x = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    for list in jaccard_sim:

        plt.bar(x, list)
        plt.xlabel('year')
        plt.ylabel('Jaccard similarity')
        plt.axis([2004,2018,0,1])
        plt.grid(True)
        plt.show()

def plot_topic(dict_topic_tf):
    x = []
    y = []

    max_value = 0
    print(dict_topic_tf)

    for key, valeur in dict_topic_tf:
        x.append(key)
        y.append(valeur)

        if max_value <= valeur:
            max_value = valeur

    plt.figure(figsize=(25, 16), dpi=120)
    plt.bar(x, y, color='lightcoral')
    plt.axis([-1, len(y) + 1, 0, max_value + 1])
    plt.gca().set_xticklabels(x, rotation=45, ha='right', fontsize=8)
    #plt.show()

    plt.savefig("../out/topic.png")