# SearchEngine
The project is a search engine written in python that uses the Vector Space Model for retrieval.The list of 92 health
health articles have been used and it has approximately 5000 unique words.Open this Readme file’s working directory in command line and type “python query.py” to run the code.
It has a few dependencies such as NLTK which can be easily pip installed.You will be prompted to enter your query after a while. At this point type your query
into the terminal and the documents are ranked and stored in total_scores.csv file

# Documentation

Py files

BeautifulSoup.py: 
All the documents are scrapped from https://www.medicalnewstoday.com/popular using Beautiful Soup the text is grepped from the class: ”article_body” .
 
T_N.py:
It takes files_list(list of documents) from lod.py as the input argument and perform tokenization and normalization and stores tokenized words in T_N.txt.(Tokenized using NLTK)

stop_words.py:
The file T_N.txt is opened and stop word are removed from this file and the words are the stored in another file stop_word.txt

stemmed_words.py: 
The file stop_words.txt is opened and the words are stemmed using Porters Stemmer and are stored in stemmed.txt file.

lod.py: 
Contains two file lists and the definitions for Tokenization, Normalization, removing stop words, stemming and unique_list.
Functions implemented in lod:
T_N(file_content): Tokenizes and Normalizes the given input “file_content”
remove_stopwords(file): Removes stop words from the input “file”
stem_words(files): Stems the input “files”
unique_words(text): Removes duplicates of a word

inverted_index.py: 
In this module documents are assigned their id’s inverted index, term frequency table for each word, idf table is built
and the tables are stores in tf_document_data.csv, idf_table.csv.

document_frequency.py:
The function “idf” in this module calculates the idf of each word.

stem_documents.py:
Stems each document in files_list(imported from lod.py) ,creates files listed in stem_document_list(lod.py) and stores the stemmed document. 

query.py:
Takes the input from the user and writes documents names and cosines scores in the descending order into total_scores.csv file.
