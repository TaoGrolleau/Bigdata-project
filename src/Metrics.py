import matplotlib.pyplot as plt

def plot_articles_per_year(list_articles):
    article_year = dict()
    nb_authors_year = dict()
    total_authors = 0
    max = 0
    nb_alone = 0
    for article in list_articles:
        year = article.year[0]
        if len(article.authors) == 1:
            nb_alone += 1
        if len(article.authors) > max:
            max = len(article.authors)
        article_year[year] = article_year.get(year, 0) + 1
        nb_authors_year[year] = nb_authors_year.get(year, 0) + len(article.authors)
        total_authors += len(article.authors)

    total_authors = total_authors / len(list_articles)
    mean_articles = len(list_articles)/15
    # Articles
    lists = sorted(article_year.items())
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    x, y = zip(*lists)
    plt.bar(x, y)

    ax.set_xlabel('Years')
    #ax.set_title('Scores by group and gender')
    ax.set_ylabel('Number of articles')
    ax.set_xticklabels(x)
    #plt.show()
    plt.savefig('../out/article_per_year.png')

    # Authors
    lists = sorted(nb_authors_year.items())
    fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
    x, y = zip(*lists)
    plt.bar(x, y)

    ax.set_xlabel('Years')
    # ax.set_title('Scores by group and gender')
    ax.set_ylabel('Number of authors')
    ax.set_xticklabels(x)
    # plt.show()
    plt.savefig('../out/authors_per_year.png')

    with open('../out/metrics.txt', 'w') as metrics_file:
        metrics_file.write('Mean number of author per article : '+ str(total_authors) + '\n')
        metrics_file.write('Number max of authors : ' + str(max)+'\n')
        metrics_file.write('Mean number of articles per year : '+str(mean_articles)+'\n')
        metrics_file.write('Number of articles with only one author : ' + str(nb_alone))

    print('Metrics file created !')