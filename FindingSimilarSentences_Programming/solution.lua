local mapreduce = require "mapreduce"

-- string hash function: http://isthe.com/chongo/tech/comp/fnv/
local NUM_MAPPERS  = 10000
local NUM_REDUCERS = 100
local HASH_SIZE    = 2^20
local FNV_prime    = 16777619
local offset_basis = 2166136261
local MAX          = 2^32
local SENTENCES_TXT = os.getenv("HOME") .. "/Dropbox/CEU/COURSERA/MiningMasiveDatasets/FindingSimilarSentences_Programming/sentences.txt"
-- local SENTENCES_TXT = os.getenv("HOME") .. "/Dropbox/CEU/COURSERA/MiningMasiveDatasets/FindingSimilarSentences_Programming/mini.txt"
-- local SENTENCES_TXT = os.getenv("HOME") .. "/Dropbox/CEU/COURSERA/MiningMasiveDatasets/FindingSimilarSentences_Programming/toy.txt"

local NS = "MMDB.sentence_offsets"
local mongo = require "mongo"
local db = assert( mongo.Connection.New() )
assert( db:connect("localhost") )

---------------------------------------------------------------------------

local function readSentenceAt(f, n)
  local cursor = assert( db:query(NS, { _id=n }) )
  local result = cursor:next()
  f:seek("set", result.offset)
  local result = iterator(f:read("*l"):gmatch("[^%s]+")):table()
  assert(n == tonumber(table.remove(result,1)))
  return result
end

local function string_hash(word)
  local h = offset_basis
  for i=1,#word do
    h = (h * FNV_prime) % MAX
    h = bit32.bxor(h, word:byte(i))
  end
  return h
end

local function sequence_hash(...)
  local h = offset_basis
  for v in ... do h = ((h + v) * FNV_prime) % MAX end
  return h
end

local function distance(s1,s2)
  local N=#s1
  local M=#s2
  local INF=math.huge
  local F = matrix(N+1,M+1):fill(INF)
  F:set(1,1,0)
  F(':',1):linear()
  F(1,':'):linear()
  for i=2,N+1 do
    for j=2,M+1 do
      if s1[i-1] == s2[j-1] then
        F:set(i,j,F:get(i-1,j-1))
      else
        F:set(i,j, math.min(F:get(i-1,j), F:get(i,j-1), F:get(i-1,j-1)) + 1)
      end
    end
  end
  return F:get(N+1,M+1)
end

---------------------------------------------------------------------------

-- arg is for configuration purposes, it will be executed with init_args given
-- to the server
local init = function(arg) end

local taskfn = function(emit)
  assert( db:remove(NS, {}) )
  local f = io.open(SENTENCES_TXT)
  local size = f:seek("end")
  f:close()
  for i=1,NUM_MAPPERS do
    emit(i, { math.floor(size * ((i-1)/NUM_MAPPERS)), math.ceil(size * (i/NUM_MAPPERS)) - 1 })
  end
end

local mapfn = function(key,value,emit)
  local f = io.open(SENTENCES_TXT)
  local insert_batch = {}
  f:seek("set", value[1])
  -- mappers ignore first line, except the first mapper
  if value[1] > 0 then f:read("*l") end
  while true do
    local start_file_pos = f:seek()
    local line = f:read("*l") if not line then break end
    local used_buckets = {}
    local emit = function(k,v)
      if not used_buckets[k] then emit(k,v) used_buckets[k] = true end
    end
    local words_it = iterator(line:gmatch("[^%s]+"))
    local sid = tonumber(words_it:step())
    local words = words_it:map(string_hash):table()
    local h = sequence_hash(table.ivalues(words))
    emit(h % HASH_SIZE, sid)
    for i=1,#words do
      local h = sequence_hash(iterator(ipairs(words)):
                              filter(function(k,v) return k ~= i end):get())
      emit(h % HASH_SIZE, sid)
    end
    -- annotate where this sentence starts
    table.insert(insert_batch, { _id = sid, offset = start_file_pos })
    -- breaks once a line overflows the given boundaries
    if f:seek() > value[2] then break end
  end
  assert( db:insert_batch(NS, insert_batch) )
  f:close()
end

local partitionfn = function(key)
  return key % NUM_REDUCERS
end

local reducefn = function(key,bucket,emit)
  table.sort(bucket)
  local f = io.open(SENTENCES_TXT)
  for i=1,#bucket-1 do
    for j=i+1,#bucket do
      local v1,v2 = bucket[i],bucket[j]
      if v1 ~= v2 then
        local s1 = readSentenceAt(f, v1)
        local s2 = readSentenceAt(f, v2)
        local d = distance(s1,s2)
        -- print(table.concat(s1," "))
        -- print(table.concat(s2," "))
        -- print(d)
        -- print("#####################################################")
        if d <= 1 then emit("{%d,%d}"%{v1,v2}) end
      end
    end
  end
end

local finalfn = function(pairs_iterator)
  for key,values in pairs_iterator do
    if #values > 0 then
      for _,v in ipairs(values) do
        local v = load("return " .. v)()
        print("PAIR",table.concat(v, " "))
      end
    end
  end
  return true -- indicates to remove mongo gridfs result files
end

return {
  init = init,
  taskfn = taskfn,
  mapfn = mapfn,
  partitionfn = partitionfn,
  reducefn = reducefn,
  finalfn = finalfn,
  -- This three properties are true for this reduce function.
  -- Combiners always must to fulfill this properties.
  associative_reducer = false,
  commutative_reducer = false,
  idempotent_reducer  = false,
}
