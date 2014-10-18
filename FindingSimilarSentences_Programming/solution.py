import math
import os

HOME=os.environ['HOME']
#SENTENCES_TXT=HOME + "/Dropbox/CEU/COURSERA/MiningMasiveDatasets/FindingSimilarSentences_Programming/toy.txt"
SENTENCES_TXT=HOME + "/Dropbox/CEU/COURSERA/MiningMasiveDatasets/FindingSimilarSentences_Programming/sentences.txt"
HASH1_SIZE=2**20
#HASH1_SIZE=2**4
NUM_LINES=100000000000

def extractSentence(line,sid):
    line = line.strip("\n").split(" ")
    if sid != int(line[0]):
        raise SystemExit
    seq = [ hash(w) for w in line[1:len(line)] ]
    return tuple(seq)

def readSentenceAt(f,offset):
    f.seek(offset,0)
    line = f.readline().strip("\n")
    tokens = line.split(" ")
    seq = [ w for w in tokens[1:len(line)] ]
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
                F[i][j] = min(F[i-1][j], F[i][j-1], F[i-1][j-1]) + 1
    return F[N][M]

def newHashTable(size):
    return [ set() for i in range(0,size) ]

def insertHashFunc1(table, sid, sentence,):
    def insert(sid,seq):
        bucket = hash(hash(seq) + hash(len(seq))) % len(table)
        table[bucket].add(sid)
    insert(sid,sentence)
    for i in range(0,len(sentence)):
        insert(sid, sentence[0:(i-1)] + sentence[(i+1):len(sentence)])

sentences_file = open(SENTENCES_TXT)
sentence_offsets = []
hash1 = newHashTable(HASH1_SIZE)
while True:
    file_offset = sentences_file.tell()
    line = sentences_file.readline()
    if not line: break
    sid = len(sentence_offsets)
    if sid >= NUM_LINES: break
    sentence = extractSentence(line,sid)
    sentence_offsets.append(file_offset)
    insertHashFunc1(hash1, sid, sentence)
    print(sid)

size = 0
hist = dict()
for l in hash1:
    size = size + len(l)*(len(l)+1)/2
    hist[len(l)] = 1 + hist.setdefault(len(l), 0)

print "SIZE ",str(size)

# print(hash1)

# print(map(lambda x: len(x), hash1))

f = open("hist.txt","w")
for k in hist:
    count=k
    howmany=hist[k]
    f.write(str(count) + " " + str(howmany) + "\n")
f.close()

pairs=0
candidate_pairs = set()
for bucket in hash1:
    bucket_list = list(bucket)
    for i in range(0,len(bucket_list)-1):
        for j in range(i+1,len(bucket_list)):
            v1 = bucket_list[i]
            v2 = bucket_list[j]
            size = size - 1
            pair = tuple([v1,v2])
            if pair not in candidate_pairs:
                candidate_pairs.add(pair)
                s1,w1 = readSentenceAt(sentences_file, sentence_offsets[v1])
                s2,w2 = readSentenceAt(sentences_file, sentence_offsets[v2])
                d = distance(s1,s2)
                if d <= 1:
                    pairs=pairs+1
                    print d,v1,v2,size,len(candidate_pairs),pairs
                    # print(w1,w2)

print size,len(candidate_pairs),pairs
