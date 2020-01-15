# -*- coding: utf-8 -*-
import Parser_Article as p
'''
Requires pip install googletrans
'''
from googletrans import Translator

def translate():
	articles = p.cleaning_articles()
	translator = Translator()
	i = 0
	for elem in articles:
		list_word = []
		for word in elem.title:
			translation = translator.translate(word, dest='en', src='fr')
			list_word.append(translation.text)
		elem.title = list_word
		i += 1
		print(i, elem.title)

def dictionnaries():
	list_word_dictionnaries = []
	with open('../resources/dict_eng.txt', 'r', encoding='utf-8') as dictionnary_en:
		all_en_words = dictionnary_en.read()
		words = all_en_words.split('\n')
		for w in words[1:]:
			list_word_dictionnaries.append(w)
	#print(list_word_dictionnaries)
	return list_word_dictionnaries

#dictionnaries()
translate()