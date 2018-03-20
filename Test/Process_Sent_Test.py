import sys
sys.path.append('/home/dania/Desktop/Summarization/Engine')
from analyzer import *
from tokenizer import *

root = '/home/dania/Desktop/Summarization/Test'
analyzer = Analyzer()
filesList = analyzer.createCorpus(root)
happySent = filesList.sents(fileids = 'happy.txt')

sentProc = SentenceProcessor()
sentTokens = sentProc.processSentences(happySent)
print sentTokens
