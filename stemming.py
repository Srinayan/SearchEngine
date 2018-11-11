from nltk.stem.porter import * #importing from nltl.stem.porter

f = open("stop_words.txt").read() #open stop_words.txt in which all the stop_words are removed
stemmed = []
stemmer = PorterStemmer()
for word in f.split():
    stemmed.append(stemmer.stem(word))
stemmed_words = " ".join(str(word) for word in stemmed)
f = open("stemmed_words.txt","w")
f.write(stemmed_words)
f.close()
