import csv
dict_value = [
{"name":"Dwany","age":20,"course":"bsc cs"},
{"name":"Arun","age":19,"course":"bsc cs"},
{"name":"vaishnav","age":19,"course":"bsc cs"},
]

fields = ["name","age","course"]

with open('dictconverted.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()

with open('dictconverted.csv','r') as csvfiles:
    readerobj = csv.reader(csvfiles)
    for rows in readerobj:
         print(rows)
