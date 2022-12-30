import requests
import pprint
from bs4 import BeautifulSoup, ResultSet, Tag

res = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".titleline > a")
subtext = soup.select(".subtext")


def create_custom_hn(links: ResultSet[Tag], subtext: ResultSet[Tag]) -> list[dict]:
    hn = []
    for idx, item in enumerate(links):
        title = item.get_text()
        href = item.get_text("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].get_text().split()[0])
            if points >= 100:
                hn.append({"title": title, "link": href, "votes": points})
    return sorted(hn, key=lambda item: item["votes"], reverse=True)


pprint.pprint(create_custom_hn(links, subtext))
