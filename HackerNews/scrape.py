from bs4 import BeautifulSoup
import requests
import pprint


res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")

soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")

score = soup.select(".subtext")
score.extend(soup2.select(".subtext"))

links = soup.select(".titleline")
links.extend(soup2.select(".titleline"))


def sort_by_vote(item):
    return sorted(item, key=lambda k: -k['vote'])


def create_custom_hn(links, score):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.find("a").get("href")
        vote = int(score[idx].getText().split(" ")[0])
        # or int(votes[idx].getText().replace(" points",""))

        if vote >= 100:
            hn.append({
                "title": title,
                "link": href,
                "vote": vote
            })
    return sort_by_vote(hn)


pprint.pprint(create_custom_hn(links, score))
