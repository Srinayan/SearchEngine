import pandas as pd
import math

#this function calculates the inverse document frequency of each word in the unique_words list
def idf(posting_list):
    dict_df ={}
    for pos in posting_list.keys():
        # df.append(len(posting_list[pos]))
        dict_df[pos] = math.log10(92/(1+len(posting_list[pos])))
    return dict_df # return a dictionary with words as keys and idf as values
