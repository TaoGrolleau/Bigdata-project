# -*- coding: utf-8 -*-
import csv
import os


def create_output_folder_if_not_exist():
    # Create directory
    dirName = '../out'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


def create_csv_file(articles):
    separator_column = ";"
    separator_in_column = "/"
    f = open("../out/data.csv", "w")
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
        line = str(i) +\
               separator_column + serie.replace(" ", "") + \
               separator_column + booktitle.replace(" ", "") +\
               separator_column + year.replace(" ", "") +\
               separator_column + title.replace(" ", "") +\
               separator_column + abstract.replace(" ", "") +\
               separator_column + authors.replace(" ", "") +\
               separator_column + str(article.pdf1page) +\
               separator_column + str(article.pdfarticle) + "\n"
        f.writelines(line)
    f.close()


def create_csv_file_for_R(articles):
    create_output_folder_if_not_exist()
    create_csv_file(articles)
    print("Directory data.csv created")