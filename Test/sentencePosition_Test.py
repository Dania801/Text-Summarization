import sys
sys.path.append('/home/dania/Desktop/Summarization/Engine')
from analyzer import *
from tokenizer import *
from features import *


root = '/home/dania/Desktop/Summarization/Test'
analyzer = Analyzer()
filesList = analyzer.createCorpus(root)
happyRaw = filesList.raw(fileids = 'happy.txt')
happySent = filesList.sents(fileids = 'happy.txt')

positions = weightSentencePosition(happySent)
print positions
