import lod
import pandas as pd
import time


if __name__ == '__main__':
    query = input()

    #Tokenzation and normalization
    tokenized_query = lod.T_N(query)
    #stop_words removal
    clean_words = lod.remove_stopwords(tokenized_query)
    #stemming query
    query_stemmed = lod.stem_words(clean_words)
    #unique_words
    query_unique = lod.unique_words(query_stemmed)

start = time.time() #start time is stored
unique_words = open("unique_list.txt").read() #reads the file that contains the unique list
# tf_query = {}

idf = pd.read_csv("idf_table.csv") #reads the pre-processed idf data
wtd = pd.read_csv("tf_document_data.csv") #reads the preprocessed wtd data


score_dict={} #creates a dict that stores score of each query term w.r.t the document

for q in query_unique.split():#for every unique term in the query
    if q in unique_words.split():#if that query term is in the unique_words of the whole corpus then execute the following
        a = idf[q]# stores idf value of that particular query word
        query_score = [i * a for i in wtd[q]]
        score_dict[q] = query_score
    else:
        print("Documents not found")

scores = pd.DataFrame(data = score_dict,index = lod.files_list(),dtype=None) #stores score_dict as data in a DataFrame with the document files as the index
scores.to_csv("query_scores.csv")
total_scores = scores.sum(axis=1)#sums all the columns in the the query_scores.csv file
total_scores  = total_scores.sort_values(ascending = False) #sorts the scores in the descending order
total_scores.to_csv("total_scores.csv")
print("The list of documents that matched with your query")
top_list = total_scores.index.tolist() #stores the index of total_scores.csv to a list
for k in range(10):
    print("%d.%s" %(k+1,top_list[k]))
end = time.time()#end time is stored

print("response-time:",end-start)# prints response time for the query
