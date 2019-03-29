##pip install pymongo
import pymongo
url='mongodb://localhost:27017'
mydb=pymongo.MongoClient(url) #pastikan mongodb aktif
newdb=mydb['gudang']
newcol=newdb['produk']
'''
print nama database2
'''
alldb=mydb.list_database_names()
print(alldb)
'''
insert satu dokumen, single/double quotation mark sama aja
'''
#newdata={'nama':'Batik','harga':1000000}
newdata={'nama':'Lemari Es','harga':2000000}
add=newcol.insert_one(newdata)
'''
cari id
'''
print(add.inserted_id) #get id from inserted document
