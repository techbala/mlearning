# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:03:43 2015

@author: gbs02315
"""

import collections

f = open('C:/Balakrishnan/learning/Machine Learning/workspace/shakes.txt', 'r')
sentences = "";
for line in f:
    sentences = sentences + line.strip()

#sentences = "can you tell me about any goood cantonese restaurants close by mid priced thai food is what i'm looking for tell me about chez panisse can you give me a listing of the kinds of food that are available i'm looking for a good place to eat breakfast when is caffe venezia open during the day"        
def computeGrams( corpus, whichgram ):
    words = splitter( corpus )
    gramHolder = []
    for i in range(len(words)):
        if( i <= (len(words)-whichgram)):
            gramHolder.append( build( words, i, i+whichgram ) )
    
    grams = dict( collections.Counter( gramHolder));
    print grams
    return grams
    
def splitter( corpus ):
    return corpus.split(" ")
    
def build( words, startPos, endPos):
     pair = ""
     for j in range(startPos, endPos):
         pair = pair + " " +words[j];    
     return pair.strip()

def findMaximumLikelihoodEstimation(unigram, ngram, pairToFind):
    numerator = ngram.get(pairToFind,0)
    print numerator

    pairs = splitter( pairToFind )    
    pairWithoutLastword = build( pairs, 0, len(pairs)-1 )
    
    dinaminator = unigram.get(pairWithoutLastword, 1)
    print dinaminator
    value = float(numerator) / float(dinaminator)
    print value
    return

uni = computeGrams( sentences, 2)
bi = computeGrams( sentences, 3)    
findMaximumLikelihoodEstimation(uni, bi, "i love you")
    