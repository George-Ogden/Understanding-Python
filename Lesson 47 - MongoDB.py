import pymongo, requests, json

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["nobel"]
# print(client.list_database_names())

# with requests.get("http://api.nobelprize.org/v1/prize.json") as file:
#     data = json.loads(file.text)

# print(data["prizes"])

column = db["prizes"]
# for prize in data["prizes"]:
#     column.insert_one(prize)
# column.drop()
# column.insert_many(data["prizes"])

for x in column.find({"category":"physics"},{"_id":0,"year":1,"category":1,"laureates":{"firstname":1,"surname":1}}).sort("year",1):
    print(x)

# column.delete_many({"year":{"$lt":"2000"}})