from __future__ import division
import nltk
from nltk import FreqDist
from nltk import ConditionalFreqDist
from tokenizer import *
from analyzer import *



def textSentencesLength(txt):
	"""
	Find the length of sentences in text, print the longest and shortest one, and show the frequency distribution of lengths
	@params txt: the tokens of the target text
	@rtype: {List}
	"""
	sentencesLength = []
	for sentence in txt:
		sentencesLength.append(len(sentence))
	print "The longest sentence is ", txt[sentencesLength.index(max(sentencesLength))]
	print "The shortest sentence is", txt[sentencesLength.index(min(sentencesLength))]
	frequencyDistribution = FreqDist(length for length in sentencesLength)
	frequencyDistribution.plot()
	frequencyDistribution.tabulate(samples=frequencyDistribution.keys())
	return sentencesLength;

def weightMap(position):
	weight = 0
	if position > 0.0 and position <= 0.1:
		weight = 0.17
	elif position > 0.1 and position <= 0.2:
		weight = 0.23
	elif position > 0.2 and position <= 0.3:
		weight = 0.14
	elif position > 0.3 and position <= 0.4:
		weight = 0.08
	elif position > 0.4 and position <= 0.5:
		weight = 0.05
	elif position > 0.5 and position <= 0.6:
		weight = 0.04
	elif position > 0.6 and position <= 0.7:
		weight = 0.06
	elif position > 0.7 and position <= 0.8:
		weight = 0.04
	elif position > 0.8 and position <= 0.9:
		weight = 0.04
	elif position > 0.9 and position <= 1.0:
		weight = 0.15
	return weight

def weightSentencePosition(txt):
	numOfSentences = len([sentence for sentence in txt if sentence])
	normalizedPosition = [(txt.index(sentence)/numOfSentences) for sentence in txt if sentence]
	weightedPosition = [weightMap(position) for position in normalizedPosition]
	return weightedPosition
