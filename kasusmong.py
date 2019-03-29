##Belajar input terus insert
##Hapus dokumen
##Cari yang dibawah sejuta
##Update nama produk
##Tambah satu field yaitu kota
##Edit kota pada barang yang harganya di range tertentu

##pip install pymongo

##Belajar input terus insert
bar=str(input('Masukkan nama barang: '))
har=int(input('Masukkan harga: '))
import pymongo
url='mongodb://localhost:27017'
mydb=pymongo.MongoClient(url) #pastikan mongodb aktif
newdb=mydb['gudang']
newcol=newdb['produk']
newdata={"nama":bar,"harga":har}
add=newcol.insert_one(newdata)
newid=add.inserted_id
for data in newcol.find({'_id':newid}):
    print('Data sukses terkirim!')
    print(data) #class dan object tidak bisa dilihat di python

#==================================================================
##HAPUS DOCUMENT
import pymongo
url='mongodb://localhost:27017'
mydb=pymongo.MongoClient(url) #pastikan mongodb aktif
newdb=mydb['gudang']
newcol=newdb['produk']
#newcol.delete_one('tes') #hapus tes
#data={'nama':'Celana'}
#newcol.delete_one(data) #hapus cuma satu
#newcol.delete_many(data) #hapus banyak
#newcol.delete_many({}) #hapus semua

for x in newcol.find(data):
    print(x)

#==================================================================
##CARI YANG DIBAWAH SEJUTA
import pymongo
url='mongodb://localhost:27017'
mydb=pymongo.MongoClient(url) #pastikan mongodb aktif
newdb=mydb['gudang']
newcol=newdb['produk']

for x in newcol.find({'harga':{'$lt':1000000}}):
    print(x)



#==================================================================
##UPDATE NAMA PRODUK
import pymongo
url='mongodb://localhost/27017'
mydb=pymongo.MongoClient(url)
newdb=mydb['gudang']
newcol=newdb['produk']
data={'nama':'Batik'}
newdata={'$set':{'nama':'Batik Jogja'}}
newcol.update_one(data,newdata)
for x in newcol.find({'nama':'Batik Jogja'}):
    print(x)

#==================================================================
###TAMBAH SATU FIELD YAITU KOTA
import pymongo
url='mongodb://localhost/27017'
mydb=pymongo.MongoClient(url)
newdb=mydb['gudang']
newcol=newdb['produk']
data={}
newdata={'$set':{'kota':'Jakarta'}}
newcol.update_many(data,newdata)
for x in newcol.find():
    print(x)

#==================================================================
##EDIT KOTA PADA BARANG YANG HARGANYA DI RANGE TERTENTU
import pymongo
url='mongodb://localhost/27017'
mydb=pymongo.MongoClient(url)
newdb=mydb['gudang']
newcol=newdb['produk']
data={'$and':[{'harga':{'$gt':1000000}},{'harga':{'$lt':3000000}}]}
newdata={'$set':{'kota':'Bogor'}}
newcol.update_many(data,newdata)
for x in newcol.find():
    print(x)


