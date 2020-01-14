class Article:
	series = ''
	booktitle = ''
	year = ''
	abstract = ''
	authors = ''
	pdf1page = ''
	pdfarticle = ''
	
	def __init__(self, series, booktitle, year, abstract, authors, pdf1page, pdfarticle):
		self.series = series
		self.booktitle = booktitle
		self.year = year
		self.abstract = abstract
		self.authors = authors
		self.pdf1page = pdf1page
		self.pdfarticle = pdfarticle