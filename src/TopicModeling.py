import Parser_Article as p
from gensim import corpora
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

list_main_topics = dict()

def return_main_topics():
    list_articles = p.cleaning_articles()
    dictionnary_year_topic = dict()
    list_year_article = []


    for article in list_articles:
        n_topic = 1

        if article.year not in list_year_article:
            dictionnary_year_topic[str(article.year)] = []
            list_year_article.append(article.year)

        tf_vectorizer = CountVectorizer(max_df=2, min_df=1, max_features=2)
        tf = tf_vectorizer.fit_transform(article.title)

        lda = LatentDirichletAllocation(max_iter=1, random_state=0, n_components=1).fit(tf)

        no_top_words = 5

        dictionnary_year_topic[str(article.year)] = add_topic(dictionnary_year_topic[str(article.year)], display_topics(lda, tf_vectorizer.get_feature_names(), no_top_words))

    display_dict(dictionnary_year_topic)

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




