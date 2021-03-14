import requests
from bs4 import BeautifulSoup

result = requests.get("https://goprogram.co.uk")
# print(result)
# print(result.content)
# print(result.text)
# soup = BeautifulSoup(result.content,features="lxml")
# print(soup.prettify())
# for link in soup.find("header").find_all("a"):
#     print(link.get_text(),link.get("href"))

to_visit = set(["https://www.goprogram.co.uk"])
valid = set()
visited = set()

while len(to_visit) > 0:
    location = next(iter(to_visit))
    print(location)
    with requests.get(location) as result:
        if "goprogram.co.uk" in result.url:
            soup = BeautifulSoup(result.content,features="lxml")
            for link in soup.find_all("a"):
                href = link.get("href")
                if href == None:
                    continue
                href = href.split("#")[0]
                if href.startswith("/"):
                    href = "https://www.goprogram.co.uk" + href
                elif not href.startswith("https://"):
                    href = "/".join(location.split("/")[:-1]) + "/" + href
                if not href in visited:
                    to_visit.update([href])
            valid.update([location])
        visited.update([location])
        to_visit.discard(location)
print(valid)