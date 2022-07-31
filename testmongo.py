import pymongo


client = pymongo.MongoClient("mongodb+srv://mohdaarif:Aarif123@cluster0.baec2cr.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

db1= client['mongotest']
coll= db1['collectoin1']
coll.insert_one({'name':'mohd aarif', 'email': "abc@gmail.com"})