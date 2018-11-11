# def unique_list(l):
#     ulist = []
#     [ulist.append(x) for x in l if x not in ulist]
#     return ulist

ulist = []
f = open("stemmed_words.txt").read()
[ulist.append(x) for x in f.split() if x not in ulist]
unique_words = " ".join(str(x) for x in ulist)
file = open("unique_list.txt","w")
file.write(unique_words)
file.close()
