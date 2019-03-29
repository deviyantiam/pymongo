#insert
## cari id

##pip install pymongo
import pymongo
url='mongodb://localhost:27017'
mydb=pymongo.MongoClient(url) #pastikan mongodb aktif
newdb=mydb['gudang']
newcol=newdb['produk']
newdata={"nama":"Celana","harga":2000000}
add=newcol.insert_one(newdata)
newid=add.inserted_id
'''
cari id
'''
for data in newcol.find({'_id':newid}):
    print('Data sukses terkirim!')
    print(data) #class dan object tidak bisa dilihat di python