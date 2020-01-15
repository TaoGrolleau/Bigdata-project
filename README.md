# Data Mining for Big Data

Objective of the project : perform a large scientific analysis of scientific papers using Data Mining, Machine Learning and Data analysis techniques.

## Papers description

The file with the given data is `export_articles_EGC_2004_2018`.
Format (in column) :
  - series (ex : 'Revue des Nouvelles Technologies de l'Information')
  - booktitle (ex : 'EGC')
  - year (ex : 2018)
  - title (ex : '#Idéo2017 : une plateforme citoyenne dédiée à l'analyse des tweets lors des événements politiques')
  - abstract (ex : 'Cette plateforme a pour objectif de permettre aux citoyens d'analyserpar eux-mêmes les tweets politiques lors d'événements spécifiques en France.Pour le cas de l'élection présidentielle de 2017, #Idéo2017 analysait en quasitemps réel les messages des candidats, et fournissait leurs principales caractéristiques,l'usage du lexique politique et des comparaisons entre les candidats.')
  - authors (ex : 'Claudia Marinica, Julien Longhi, Nader Hassine, Abdulhafiz Alkhouli, Boris Borzic')
  - pdf1page (ex : 'http://editions-rnti.fr/render_pdf.php?p1&p=1002425')
  - pdfarticle (ex : 'http://editions-rnti.fr/render_pdf.php?p=1002425')

One row is equivalent to one record and each column is separated by a horizontal tab.
Data can contain some errors so be careful.

## Additional information

We can use some external information :
  - data from [dblp](https://dblp.uni-trier.de/db/conf/f-egc/)
  - archives of the mailing list available [here](https://www.egc.asso.fr/manifestations/defi-egc/defi-egc-2020-20-ans-dhistoire-pour-quel-avenir.html)
  - tweets of ECG association available [here](https://github.com/pbruneau/EGC-Social-Data)

## Definition of problems

We have to define a problem and use the techniques we learned to solve it. Some example of problems :
- Identify groups of researchers who publish together
- Detect groups of researcher who work on the same topic
- Give the list of the main topics of the conference for a given year or study the evolution of these topics
over the period (example of representation with a bag of words model)
- Propose a model to detect new topics appearing in the publications
- Identify famous researchers based on their publications or based on citations of their papers

## What is expected in the report

- Cover page (title, name, logos, table of content)
- Introduction (present the work and the structure of the report)
- Section describing the data
- Section describing our objectives and the different studies made
- Section for each study made: we must clearly state the objective of the section, present clearly
the experimental setup (preparation of the data, algorithm(s) used, any relevant information), give the
results in a neat way (table of results, plots, curves, graphs, . . . , do not forget to comment them) and
give our conclusions for this section
