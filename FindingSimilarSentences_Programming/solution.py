import math
import os

HOME=os.environ['HOME']
#SENTENCES_TXT=HOME + "/Dropbox/CEU/COURSERA/MiningMasiveDatasets/FindingSimilarSentences_Programming/toy.txt"
SENTENCES_TXT=HOME + "/Dropbox/CEU/COURSERA/MiningMasiveDatasets/FindingSimilarSentences_Programming/mini.txt"
#SENTENCES_TXT=HOME + "/Dropbox/CEU/COURSERA/MiningMasiveDatasets/FindingSimilarSentences_Programming/sentences.txt"
HASH1_SIZE=2**20
#HASH1_SIZE=2**4

def extractSentence(line,word2id,sid):
    line = line.strip("\n").split(" ")
    if sid != int(line[0]):
        raise SystemExit
    seq = [ word2id.setdefault(w,len(word2id)) for w in line[1:len(line)] ]
    return tuple(seq)

def readSentenceAt(f,offset,word2id):
    f.seek(offset,0)
    line = f.readline().strip("\n")
    tokens = line.split(" ")
    seq = [ word2id[w] for w in tokens[1:len(line)] ]
    return [ tuple(seq), line ]

def distance(s1,s2):
    N=len(s1)
    M=len(s2)
    INF=4*(N+M)
    F = [ [ INF ]*(M+1) for i in range(0,N+1) ]
    F[0][0] = 0
    for i in range(1,N+1):
        F[i][0] = i
    for j in range(1,M+1):
        F[0][j] = j
    for i in range(1,N+1):
        for j in range(1,M+1):
            if s1[i-1] == s2[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j]+1, F[i][j-1]+1, F[i-1][j-1]+1)
    return F[N][M]

def newHashTable(size):
    return [ set() for i in range(0,size) ]

def insertHashFunc1(table, sid, sentence,):
    def insert(sid,seq):
        bucket = hash(seq) % len(table)
        table[bucket].add(sid)
    insert(sid,sentence)
    for i in range(0,len(sentence)):
        insert(sid, sentence[0:(i-1)] + sentence[(i+1):len(sentence)])

sentences_file = open(SENTENCES_TXT)
sentence_offsets = []
word2id = dict()
hash1 = newHashTable(HASH1_SIZE)
while True:
    file_offset = sentences_file.tell()
    line = sentences_file.readline()
    if not line: break
    sid = len(sentence_offsets)
    sentence = extractSentence(line,word2id,sid)
    sentence_offsets.append(file_offset)
    insertHashFunc1(hash1, sid, sentence)
    print(sid)

hist = dict()
for l in hash1:
    hist[len(l)] = 1 + hist.setdefault(len(l), 0)

# print(hash1)

# print(map(lambda x: len(x), hash1))

f = open("hist.txt","w")
for k in hist:
    count=k
    howmany=hist[k]
    f.write(str(count) + " " + str(howmany) + "\n")
f.close()

candidate_pairs = set()
for bucket in hash1:
    for v1 in bucket:
        for v2 in bucket:
            pair = tuple([v1,v2])
            if v1 < v2 and pair not in candidate_pairs:
                candidate_pairs.add(pair)
                s1,w1 = readSentenceAt(sentences_file, sentence_offsets[v1], word2id)
                s2,w2= readSentenceAt(sentences_file, sentence_offsets[v2], word2id)
                d = distance(s1,s2)
                if d <= 1:
                    print d,v1,v2
                    print(w1,w2)
