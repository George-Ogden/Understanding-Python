from tweepy import Client
import random, json

with open("credentials.json") as file:
    credentials = json.load(file)

client = Client(**credentials, return_type=dict)

def pprint(response):
    print(json.dumps(response, indent=4))

response = client.create_tweet(text=f"Hello, world! ({random.random():.5f}) #success")
pprint(response)

response = client.search_recent_tweets(query="#success", expansions="author_id", max_results=10)
pprint(response)

response = client.get_user(username="gvanrossum", user_fields=["verified", "name"])
pprint(response)
id = response["data"]["id"]

response = client.get_users_following(id=id, user_fields=["username", "description"], max_results=1)
pprint(response)
user = response["data"][0]
print(user["name"])
print(user["description"])