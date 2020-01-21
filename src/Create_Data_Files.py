# -*- coding: utf-8 -*-
import os


def create_authors_graph_file(list_articles, k):
    """
    Creates a TXT file for a R script with the couple of authors that wrote more than k articles together
    """
    list_couples_author = []
    k_list_authors = []
    d = dict()
    nodes_repr = ''
    for article in list_articles:
        for elem in article.authors[1:]:
            node = article.authors[0].split().pop()
            neighbour = elem.split().pop()
            list_couples_author.append((''.join(node), ''.join(neighbour)))
    for couple in list_couples_author:
        d[couple] = d.get(couple, 0) + 1
    list_couples_author = []

    for elem in d:
        value = d.get(elem)
        list_couples_author.append((elem[0],elem[1], value))
    list_couples_author.sort(key=lambda tup: tup[2], reverse=True)

    for couple in list_couples_author:
        list_first = []
        list_second = []
        if couple[2] > k:
            k_list_authors.append(couple)
        else:
            """
            Parmi les auteurs qui existent déjà, on rajoute le nombre d'articles qu'ils ont écrit ensemble
            """
            for elem in k_list_authors:
                list_first.append(elem[0])
                list_second.append(elem[1])
            if couple[0] in list_first and couple[1] in list_second:
                k_list_authors.append(couple)

    with open('../data_files/graph_authors.txt', 'w') as graph_files:
        for couple in k_list_authors:
            nodes_repr += couple[0] + ' ' + couple[1] + ' '+ str(couple[2]) + '\n'
        graph_files.write(nodes_repr)
        print('File graph_authors created !')

def create_output_folder_if_not_exist():
    # Create directory
    dirName = '../data_files/'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


def create_csv_file(articles):
    separator_column = ";"
    separator_in_column = "/"
    f = open("../data_files/data.csv", "w")
    line = "id" + \
           separator_column + "series" + \
           separator_column + "booktitle" + \
           separator_column + "year" + \
           separator_column + "title" + \
           separator_column + "abstract" + \
           separator_column + "authors" + \
           separator_column + "pdf1page" + \
           separator_column + "pdfarticle" + "\n"
    f.write(line)
    i = 0
    for article in articles:
        # création de la liste d'articles
        i += 1
        serie = ""
        j = 0
        for s in article.series:
            if j == 0:
                serie = str(s)
            else:
                serie = serie + separator_in_column + str(s)
            j += 1
        # création de la liste de booktitle
        booktitle = ""
        k = 0
        for b in article.booktitle:
            if k == 0:
                booktitle = str(b)
            else:
                booktitle = booktitle + separator_in_column + str(b)
            k += 1
        # création de la liste de year
        year = ""
        l = 0
        for y in article.year:
            if l == 0:
                year = str(y)
            else:
                year = year + separator_in_column + str(y)
            l += 1
        # création de la liste de title
        title = ""
        m = 0
        for t in article.title:
            if m == 0:
                title = str(t)
            else:
                title = title + separator_in_column + str(t)
            m += 1
        # création de la liste d'abstract
        abstract = ""
        n = 0
        for a in article.abstract:
            if n == 0:
                abstract = str(a)
            else:
                abstract = abstract + separator_in_column + str(a)
            n += 1
        # création de la liste d'authors
        authors = ""
        o = 0
        for a in article.authors:
            if o == 0:
                authors = str(a)
            else:
                authors = authors + separator_in_column + str(a)
            o += 1
        # création d'une ligne
        line = str(i) + \
               separator_column + serie.replace(" ", "") + \
               separator_column + booktitle.replace(" ", "") + \
               separator_column + year.replace(" ", "") + \
               separator_column + title.replace(" ", "") + \
               separator_column + abstract.replace(" ", "") + \
               separator_column + authors.replace(" ", "") + \
               separator_column + str(article.pdf1page) + \
               separator_column + str(article.pdfarticle) + "\n"
        f.writelines(line)
    f.close()


def create_csv_file_for_R(articles):
    create_output_folder_if_not_exist()
    create_csv_file(articles)
    print("Directory data.csv created")
