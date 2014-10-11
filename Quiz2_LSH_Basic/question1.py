import distances

words = [ "he", "she", "his", "hers" ]
for i in range(0,len(words)):
    for j in range(i+1, len(words)):
        w1=words[i]
        w2=words[j]
        print w1,w2,distances.edit_distance(w1,w2)

