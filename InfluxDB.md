INFLUX DB
===

Time Series Database   
-> times stored in RFC3339 UTC   
-> nanosecod precision

---

### Data
    
    MEASUREMENT -> [
        time -> 1 value
        Fields -> 1+ key/val pair
        Tags -> 0+ key/val pair
        ]
    
Fields:

- strings, floats, integers, or Booleans  
- not indexed 


Tags:

- strings
- are indexed -> faster queries
- useful for commonly queried metadata

Measurement
        
           '<Measurement String>,<tags,> <fields,> <timestamp>' 
- Strings
- Acts as container for time, fields and tags columns
- Conceptually similar to SQL table

Retention Policies
- Measurements belong to different retention policies
- How long to keep data
- How many copies to keep in cluster
- Autogen -> infinite duration -> replication factor 1

Series
- Collection of Points with the same:
    
        tag-set -> possible tag combination
        Measuremnet -> Measuremnt String
        field key -> key string
        
Point
- Single Data Record
        
---

### Writing Data

POST request to `/write` endpoint

    curl -i -XPOST 'http://localhost:8086/write?db=mydb' --data-binary 'cpu_load_short,host=server01,region=us-west value=0.64 1434055562000000000'
    
- Must specify existing db in query param
- Points will be written to default retention policy unless specified
- Multiple points can be send on new lines
- Can pass file to curl -> data.txt:

        cpu_load_short,host=server02 value=0.67
        cpu_load_short,host=server02,region=us-west value=0.55 1422568543702900257
        cpu_load_short,direction=in,host=server01,region=us-west value=2.0 1422568543702900257


     curl -i -XPOST 'http://localhost:8086/write?db=mydb' --data-binary @cpu_data.txt`
     
---

### Querying Data

GET request to `/query` endpoint
set your query to url param `q`

    curl -G 'http://localhost:8086/query?pretty=true' --data-urlencode "db=mydb" --data-urlencode "q=SELECT \"value\" FROM \"cpu_load_short\" WHERE \"region\"='us-west'"

Influxdb returns json

Multiple queries can be sent by delimiting queries with semicolon

    curl -G 'http://localhost:8086/query?pretty=true' --data-urlencode "db=mydb" --data-urlencode "q=SELECT \"value\" FROM \"cpu_load_short\" WHERE \"region\"='us-west';SELECT count(\"value\") FROM \"cpu_load_short\" WHERE \"region\"='us-west'"
    
Timestamps are RFC3339 UTC by default can specify different output

---

### SCHEMA

Tags if:
- value is metadata
- you want to use `GROUP BY()`  

Fields if:
- you want to use `InfluxQL function`
- need other types than string
