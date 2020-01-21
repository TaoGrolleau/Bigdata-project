from collections import OrderedDict

import numpy as np
import spacy


class TextRankKeyword():
    """Extract keywords from text"""

    def __init__(self):
        self.d = 0.85  # damping coefficient, usually is .85
        self.min_diff = 1e-5  # convergence threshold
        self.steps = 20  # iteration steps
        self.node_weight = None  # save keywords and its weight

    def get_vocab(self, sentence):
        # Get all tokens
        vocab = OrderedDict()
        i = 0
        for word in sentence:
            if word not in vocab:
                vocab[word] = i
                i += 1
        return vocab

    def get_token_pairs(self, window_size, article_content):
        # Build token_pairs from windows in sentences
        token_pairs = list()
        for word in article_content:
            for i in range(len(article_content)):
                for j in range(i + 1, i + window_size):
                    if j >= len(word):
                        break
                    pair = (word, article_content[j%len(article_content)])
                    if pair not in token_pairs:
                        token_pairs.append(pair)
        return token_pairs

    def symmetrize(self, a):
        return a + a.T - np.diag(a.diagonal())

    def get_matrix(self, vocab, token_pairs):
        """Get normalized matrix"""
        # Build matrix
        vocab_size = len(vocab)
        g = np.zeros((vocab_size, vocab_size), dtype='float')
        for word1, word2 in token_pairs:
            i, j = vocab[word1], vocab[word2]
            g[i][j] = 1

        # Get Symmeric matrix
        g = self.symmetrize(g)

        # Normalize matrix by column
        norm = np.sum(g, axis=0)
        g_norm = np.divide(g, norm, where=norm != 0)  # this is ignore the 0 element in norm

        return g_norm

    def get_keywords(self, number=10):
        """Print top number keywords"""
        list_keywords = []
        node_weight = OrderedDict(sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
        for i, (key, value) in enumerate(node_weight.items()):
            list_keywords.append(key)
            #print(key + ' - ' + str(value))
            if i > number:
                break
        return list_keywords

    def analyze(self, articles, window_size=4):
        # Main function to analyze text

        # Build vocabulary
        vocab = self.get_vocab(articles.title)

        # Get token_pairs from windows
        token_pairs = self.get_token_pairs(window_size, articles.title)

        # Get normalized matrix
        g = self.get_matrix(vocab, token_pairs)

        # Initionlization for weight(pagerank value)
        pr = np.array([1] * len(vocab))

        # Iteration
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1 - self.d) + self.d * np.dot(g, pr)
            if abs(previous_pr - sum(pr)) < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        node_weight = dict()
        for word, index in vocab.items():
            node_weight[word] = pr[index]

        self.node_weight = node_weight
