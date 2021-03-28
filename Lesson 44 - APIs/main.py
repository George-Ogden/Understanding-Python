import requests

# with requests.get("https://en.wikipedia.org/wiki/Python") as result:
#     # print(result.text)
#     html = result.text

# with open("index.html","w",encoding="utf-8") as file:
#     file.write(html)

topic = "Python_(programming_language)"
# with requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(topic),headers={"accept": "application/json","charset":"utf-8"}) as result:
#     print(result)
#     print(result.json())
#     print(result.json()["extract"])
#     html = result.json()["extract_html"]
#     # html = result.text

# with open("{}.html".format(topic),"w") as file:
#     file.write(html)
    
with requests.get("https://en.wikipedia.org/api/rest_v1/page/pdf/{}".format(topic),headers={"accept": "application/pdf","charset":"utf-8"}) as result:
    print(result)
    pdf = result.content

with open("{}.pdf".format(topic),"wb") as file:
    file.write(pdf)