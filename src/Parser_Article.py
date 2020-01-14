# -*- coding: utf-8 -*-
import csv
import string
import unicodedata
from Article import Article
from collections import Counter

def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

def strip_punctuation(text):
	exclude = set(string.punctuation)
	s = ''
	for ch in text:
		if ch not in exclude:
			s += ch
		else:
			s += ' '

	return s

def parse_articles():
	'''
	Parse the TXT file used as our data in the project
	'''
	list_all_articles = []
	with open('../export_articles_EGC_2004_2018.csv', 'r', encoding='latin1') as article_data:
		all_data = csv.reader(article_data, delimiter='\t')
		for row in all_data:
			art = Article(row[0].encode('latin1').decode('utf-8').lower(), 
				row[1].encode('latin1').decode('utf-8').lower(), 
				row[2].encode('latin1').decode('utf-8').lower(), 
				row[3].encode('latin1').decode('utf-8').lower(), 
				row[4].encode('latin1').decode('utf-8').lower(), 
				row[5].encode('latin1').decode('utf-8').lower(), 
				row[6].encode('latin1').decode('utf-8').lower(),
				row[7].encode('latin1').decode('utf-8').lower())
			list_all_articles.append(art)
	return list_all_articles

def parse_stopwords():
	list_stopwords = []
	with open('../resources/stopwords.txt', 'r', encoding='latin1') as stopwords:
		all_stopwords = stopwords.read()
		words = all_stopwords.split('\n')
		for w in words:
			w = w.encode('latin1').decode('utf-8')
			list_stopwords.append(w)
	return list_stopwords

def cleaning_articles():
	'''
	Parse the useful files and does some cleaning (removing accentuation, punctuation and stopwords)
	Returns a list of Article filled with lists of words
	'''
	list_all_articles = parse_articles()
	list_stopwords = parse_stopwords()
	cleaned_articles = []

	for art in list_all_articles[1:]:
		list_series = []
		list_booktitle = []
		list_year = []
		list_title = []
		list_abstract = []
		list_authors = []
		list_pdf1page = []
		list_pdfarticle = []
		

		'''
		Removing punctuation
		'''
		art.series = strip_punctuation(art.series)
		art.booktitle = strip_punctuation(art.booktitle)
		art.year = strip_punctuation(art.year)
		art.title = strip_punctuation(art.title)
		art.abstract = strip_punctuation(art.abstract)
		art.authors = strip_punctuation(art.authors)
		
		'''
		Removing the french accentuation
		'''
		for elem in art.series.split():
			elem = strip_accents(elem)
			list_series.append(elem)
		for elem in art.booktitle.split():
			elem = strip_accents(elem)
			list_booktitle.append(elem)
		for elem in art.year.split():
			elem = strip_accents(elem)
			list_year.append(elem)
		for elem in art.title.split():
			elem = strip_accents(elem)
			list_title.append(elem)
		for elem in art.abstract.split():
			elem = strip_accents(elem)
			list_abstract.append(elem)
		for elem in art.authors.split():
			elem = strip_accents(elem)
			list_authors.append(elem)
		#TODO : is it necessary to remove accentuation from links ?
		for elem in art.pdf1page.split():
			elem = strip_accents(elem)
			list_pdf1page.append(elem)
		for elem in art.pdfarticle.split():
			elem = strip_accents(elem)
			list_pdfarticle.append(elem)

		'''
		Removal of stopwords
		'''
		for stopword in list_stopwords[1:]:
			if stopword in list_series:
				for elem in list_series:
					if elem == stopword:
						list_series.remove(elem)
			if stopword in list_booktitle:
				for elem in list_booktitle:
					if elem == stopword:
						list_booktitle.remove(elem)
			if stopword in list_year:
				for elem in list_year:
					if elem == stopword:
						list_year.remove(elem)
			if stopword in list_title:
				for elem in list_title:
					if elem == stopword:
						list_title.remove(elem)
			if stopword in list_abstract:
				for elem in list_abstract:
					if elem == stopword:
						list_abstract.remove(elem)
			if stopword in list_authors:
				for elem in list_authors:
					if elem == stopword:
						list_authors.remove(elem)
			#TODO : is it necessary to remove stopwords from links ?
			if stopword in list_pdf1page:
				for elem in list_pdf1page:
					if elem == stopword:
						list_pdf1page.remove(elem)
			if stopword in list_pdfarticle:
				for elem in list_pdfarticle:
					if elem == stopword:
						list_pdfarticle.remove(elem)
		
		article = Article(list_series, list_booktitle, list_year, list_title,list_abstract, list_authors, list_pdf1page, list_pdfarticle)
		cleaned_articles.append(article)
	return cleaned_articles

def all_words(list_all_articles):
	list_words_score = []
	for article in list_all_articles:
		for elem in article.series:
			list_words_score.append(elem)
		for elem in article.booktitle:
			list_words_score.append(elem)
		for elem in article.year:
			list_words_score.append(elem)
		for elem in article.title:
			list_words_score.append(elem)
		for elem in article.abstract:
			list_words_score.append(elem)
		for elem in article.abstract:
			list_words_score.append(elem)
	c = Counter(list_words_score)
	print(c)

articles = cleaning_articles()
#for elem in articles:
#	print(elem)
all_words(articles)
 