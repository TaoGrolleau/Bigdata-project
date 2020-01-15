class Article:
	def __init__(self, series, booktitle, year, title, abstract, authors, pdf1page, pdfarticle):
		self.series = series
		self.booktitle = booktitle
		self.year = year
		self.title = title
		self.abstract = abstract
		self.authors = authors
		self.pdf1page = pdf1page
		self.pdfarticle = pdfarticle

	def __repr__(self):
		return 'Article : series: {},\n booktitle: {},\n year: {},\n title: {},\n abstract: {},\n authors: {},\n pdf1page: {},\n pdfarticle: {}\n'.format(self.series, self.booktitle, self.year, self.title, self.abstract, self.authors, self.pdf1page, self.pdfarticle)