local connection_string = "django"
local dbname = "MMDB"
local mapreduce = require "mapreduce"
local w = mapreduce.worker.new(connection_string, dbname)
w:execute()
