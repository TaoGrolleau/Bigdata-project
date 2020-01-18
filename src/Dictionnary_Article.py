# -*- coding: utf-8 -*-
import Parser_Article as p

def dictionnaries():
	list_word_dictionnaries = []
	with open('../resources/dict_eng.txt', 'r', encoding='utf-8') as dictionnary_en:
		all_en_words = dictionnary_en.read()
		words = all_en_words.split('\n')
		for w in words[1:]:
			list_word_dictionnaries.append(w)
	#print(list_word_dictionnaries)
	return list_word_dictionnaries

get_lemma()