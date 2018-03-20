import sys
sys.path.append('/home/dania/Desktop/Summarization/Engine')
from analyzer import *
from tokenizer import *

root = '/home/dania/Desktop/Summarization/Test'
analyzer = Analyzer()
filesList = analyzer.createCorpus(root)
happyRaw = filesList.raw(fileids = 'happy.txt')

paragraphProc = ParagraphProcessor()
paragraphTokens = paragraphProc.processParagraph(happyRaw)
print paragraphTokens
