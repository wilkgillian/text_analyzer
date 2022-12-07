import asyncio
import nltk
from collections import Counter
from typing import Text
import re
import pandas as pd

text_to_analisis = open("text.txt", encoding="utf8")


def extract_usernames(text: Text):
    lines = text.readlines()
    usernames = []
    for line in lines:
        if re.search(r"[a-z]+@", line):
            string = re.search(r"[a-z]+@", line).group(0)
            usernames.append(string.replace("@", ""))
    return usernames


# print(extract_usernames(text_to_analisis))


def extract_domains(text: Text):
    lines = text.readlines()
    domains = []
    counter = []
    for line in lines:
        if re.search(r"@+[a-z]*", line):
            string = re.search(r"@+[a-z]*", line).group(0).replace("@", "")
            domains.append(string)
    for domain in domains:
        counter.append("Dominio:"+domain+" -> ocorrências: "+str(domains.count(domain))+"")
    ocorencies = sorted(set(counter))
    return ocorencies 


# print(extract_domains(text_to_analisis))


def most_used_words(text: Text):
    # base = text.read()
    # print(base)
    # nltk.download("all-corpora")
    # nltk.download("rslp")
    stopwords = nltk.corpus.stopwords.words('portuguese')
    stemmer = nltk.stem.RSLPStemmer()
    words = []
    for (palavras, emocao) in text:
        comstemming = [str(stemmer.stem(p))
                       for p in palavras.split() if p not in
                       stopwords]
        words.append((comstemming, emocao))
    # print(stopwords)
    return words

print(most_used_words(text_to_analisis))
async def text_feeling():
    feeling = []
    return feeling


async def amount_tokens():
    amount_tokens = 0
    return amount_tokens


async def amount_words_characters():
    amount = 0
    return amount


# async def main():
#     # usernames = await extract_usernames(text_to_analisis)
#     print(await most_used_words(text_to_analisis))
#     # ocorencies = await extract_domains(text_to_analisis)
#     # print(ocorencies)
    
# asyncio.run(main())