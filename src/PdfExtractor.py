import os
import re

import matplotlib.pylab as plt
import wget
from tika import parser

"""
pip install wget
pip install tika
"""

def create_pdf_dir():
    # Create directory
    dirName = '../data_files/pdf'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

def download_pdf_files(url_article_pdf, id):
    file_name = '../data_files/pdf/' + str(id) + '.pdf'
    if not os.path.isfile(file_name):
        wget.download(url_article_pdf[0], file_name)


def extract_text_from_pdf():
    pdf_files = dict()
    files = os.listdir('../data_files/pdf/')
    for file_name in files:
        id = re.search(r'[0-9]+', file_name)

        raw = parser.from_file('../data_files/pdf/' + file_name)
        pdf_files[id.group()] = raw['content']
    return pdf_files


def get_references(authors_list):
    pdf_files = extract_text_from_pdf()
    list_authors = []
    dic_family_names = dict()
    for key, value in pdf_files.items():
        lines = value.split('\n')
        for l in lines:
            list_authors += re.findall(r'[A-Z][a-z]+, [A-Z]\.|[A-Z]\. [A-Z][a-z]+', l)
    for name in list_authors:
        if name[-1] == ".":
            family_name = name[:-4].lower()
        else:
            family_name = name[3:].lower()
        dic_family_names[family_name] = dic_family_names.get(family_name, 0) + 1

    dic_result = dict(filter(lambda elem: elem[0] in authors_list, dic_family_names.items()))
    dic_result = {k: v for k, v in sorted(dic_result.items(), key=lambda item: item[1], reverse=True)}

    return dic_result


def get_authors_list(list_articles):
    authors_list = []
    for article in list_articles:
        for author in article.authors:
            author_split = author.split(' ')
            if author_split[-1] not in authors_list:
                authors_list.append(author_split[-1])
    return authors_list


def make_plot_famous_authors(authors_dic, size):
    x = []
    y = []

    for key, value in authors_dic.items():
        x.append(key)
        y.append(value)
        if len(x) >= size:
            break

    plt.figure(figsize=(16, 9), dpi=120)
    plt.bar(x, y)
    plt.gca().set_xticklabels(x, rotation=45, ha='right', fontsize=8)
    #plt.show()
    plt.savefig('../out/famous_authors.png')