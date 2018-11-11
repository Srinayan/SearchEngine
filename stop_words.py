from nltk.corpus import stopwords

stoplist = stopwords.words('english')
#files_list = lod.files_list()
file = open("T_N.txt") #opens the file that contains all words in the corpus tokenized and normalized
text = file.read()

# Apply the stoplist to the text
clean = [word for word in text.split() if word not in stoplist]
clean = " ".join(str(word) for word in clean)
f = open("stop_words.txt","a")
f.write(clean)
f.close()
