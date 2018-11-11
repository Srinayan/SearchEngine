import nltk
import lod

files_list = lod.files_list()

for file in files_list:
    file_content = open(file).read()
    file_content  = file_content.lower()
    puncts = "!?-—()&/;:,.[]``'"
    for punk in puncts:
        file_content = file_content.replace(punk,'')
        tokens = nltk.word_tokenize(file_content)
    
    T_N = " ".join(str(tok) for tok in tokens)
    f = open("T_N.txt","a")
    f.write(T_N)
    f.close()
