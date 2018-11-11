import lod #lod has list of documents and also definitions defined for tokenization_normalization,stop_words,stemming and unique_words
import nltk
import document_frequency # In docuement_frequency module we calculated the IDF of each word in the unique list
import pandas as pd
import math
import csv
import time
import stem_documents # stem_documents module stems all the documents in the corpus and creates a new stemmed file for each document
from nltk.corpus import stopwords
from nltk.stem.porter import *


start =time.time() #records the time this line executes and stores it in the variable "start"
# this file creates both inverted index and an index for term frequency of each word
stoplist = stopwords.words('english')
documents = lod.files_list() # Imports the list of documents(lod) defined with the function name file_list()
stem_documents = lod.stem_documents_list() # Imports all the Stemmed documents from lod


#this creates a dictionary in which every key has the document name and value being its document_id
dict = {}
i = 1
for doc in documents:
    dict[doc]= str(i)
    i = i+1


#creates a dictionary in which every key has the stemmed_document name and value being its document_id
stem_dict={}
k = 1
for d in stem_documents:
    stem_dict[d]=str(k)
    k = k+1

# Words variable reads the data in the unique_list.txt file and stores it as a string
words = open("unique_list.txt").read()
tfd_doc = {} #creates a dictionary for storing wtd
posting_list = {} #creates a dictionary for storing words as keys word_postings as values


# i = 1
for term in words.split(): #loop for every word in the unique_list
    tfd_list=[] #this list stores term frequency of the word in the unique_list
    word_postings = [] #this list stores the posting list of each word

    # this loop opens each stemmed_document
    for doc in stem_documents:
        j = 0
        stem_words = open(doc).read()
#if term in stem_words exists in the document then the document id is added to the list "word_postings"
        if term in stem_words.split():
            word_postings.append(stem_dict[doc])
#If the term we are looping is in stem_words of a document then the value of j adds everytime the term is present in this document
        for q in stem_words.split():
            if  term == q:
                j = j+1
        wtd = math.log10(1+j) #calculates wtd(weight of term frequency for a document) for each word in a document
        tfd_list.append(wtd)#wtd is added to the list "tfd_list"

    tfd_doc[term] = tfd_list # create a dictionary with all the term as the key words and term frequency list as the value pair
    posting_list[term] = word_postings #create a dictionary with all the term as the key words and word_postings list as the value pair

tfd_word = pd.DataFrame(data = tfd_doc,index = dict.keys()) #create a DataFrame(Table) with index as document names and data as tfd
#loops through each document
for key in dict.keys():
    tfd = tfd_word.loc[key] #selects a row of the corresponding document
    sum = 0
    # calculates the length of the vector and divides with it
    for i in tfd:
        sum = sum + float(i)**2
    root = sum**0.5
    for q in tfd:
        q = float(q)/root

#calls the idf function from document_frequency module (which calculates the idf of each word)
idf = document_frequency.idf(posting_list)
idf_data = pd.DataFrame(data=idf,index=["IDF"]) #creates a DataFrame for idf using pandas
idf_data.to_csv("idf_table.csv") #exports the DataFrame to the "idf_table.csv"
tf_document = pd.DataFrame(data=tfd_doc,index=words.split(),columns=dict.keys()) # creates a table with all the words as the rows and documents as columns with wtd as the values
tfd_word.to_csv("tf_document_data.csv") #exports the DataFrame to "tf_document_data.csv"

end = time.time() # calculates the time at which this line ends

#prints the time for the above process
print(end-start)
