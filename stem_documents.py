import lod

docs = lod.files_list() #imports documents list from lod
#this loop tokenize,normalize and stems each document and creates a new stemmed file
i=1
for d in docs:
    file_docs = open(d).read()
    #tokenize and normalize
    tokenized = lod.T_N(file_docs)

    #stopwords removal
    clean_words = lod.remove_stopwords(tokenized)

    #Stemming
    stem_words = lod.stem_words(clean_words)


    stem_files = open("%s.txt" %i,"w")
    stem_files.write(stem_words)
    stem_files.close()
    i = i+1
