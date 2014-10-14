local mapreduce = require "mapreduce"
local connection_string = "django"
local dbname      = "MMDB"
local module_name = "solution"
-- local storage     = "shared"
local s = mapreduce.server.new(connection_string, dbname)
s:configure{
  taskfn         = module_name,
  mapfn          = module_name,
  partitionfn    = module_name,
  reducefn       = module_name,
  finalfn        = module_name,
  storage        = storage,
  -- storage = "gridfs[:PATH]", -- 'gridfs', 'shared', 'sshfs', with the
  -- optional string :PATH. if not given PATH will be os.tmpname()
  -- storage = "gridfs:/tmp/wordcount",
  -- storage = "shared:/home/experimentos/tmp/wordcount",
  -- storage = "sshfs:/tmp/wordcount",
  -- storage = "gridfs",
  -- storage = "shared",
  -- storage = "sshfs",
}
mapreduce.utils.sleep(4)
s:loop()
