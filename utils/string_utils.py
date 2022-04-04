
from konlpy.tag import Okt 
from time import sleep
punct = set(u''':!),.:;?.]}¢'"、。〉》」』〕〗〞︰︱︳﹐､﹒
﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､￠
々‖•·ˇˉ―′’”([{£¥'"‵〈《「『〔〖（［｛￡￥〝︵︷︹︻
︽︿﹁﹃﹙﹛﹝（｛“‘_…/''')

stemmer = Okt()


def stem(word):
    return stemmer.nouns(word)


def clean_sentence(text, stemming=False):
    for token in punct:
        text = text.replace(token, "")
    words = text.split()
    if stemming:
        stemmed_words = []
        for w in words: 
            
            stemmed_words.extend(stem(w))
     #   print(stemmed_words)
      #  for i in range(len())
        #sleep(1)
        # for i in stemmed_words: 
        #     if len(i)==1: 
        #         d.append(i)
        # for i in d:
        #     stemmed_words.pop(d.index(i))
        # words = stemmed_words
     #   print("words", words)
    return " ".join(words)


def clean_name(name):
    if name is None:
        return ""
    x = [k.strip() for k in name.lower().strip().replace(".", " ").replace("-", " ").split()]
    return "_".join(x)
