class Tweet:
	def __init__(self, txt, favorite_count, retweet_count, created_at):
		self.txt = txt
		self.favorite_count = favorite_count
		self.retweet_count = retweet_count
		self.created_at = created_at

	def __repr__(self):
		return 'Tweet : txt: {},\n favorite_count: {},\n retweet_count: {}, \n created_at: {}'.format(self.txt, self.favorite_count, self.retweet_count, self.created_at)

	def __getitem__(self, item):
		if item == 0:
			return self.txt
		if item == 1:
			return self.favorite_count
		if item == 2:
			return self.retweet_count
		if item == 3:
			return  self.created_at
