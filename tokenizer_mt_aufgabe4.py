#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Eva Bühlmann
# 05-058-912

import nltk
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


with open('happy_tokenized.txt', 'w', encoding='utf-8') as output:
    with open('happymoments.txt', 'r', encoding='utf-8') as input:
        for line in input.readlines():
            sent_list = sent_detector.tokenize(line)
            for sent in sent_list:
                output.write(' '.join(nltk.word_tokenize(sent)))
                output.write('\n')


