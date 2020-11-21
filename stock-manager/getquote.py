import bs4
import requests


class GetQuote:
    def __init__(self, code, region):
        self.code = code
        self.region = region

    def geturl(self):
        if self.region == "us":
            url = "https:/finance.yahoo.com/quote/" + self.code + "/"
        else:
            url = "https://" + self.region + ".finance.yahoo.com/quote/" + self.code + "/"

        try:
            page = requests.get(url).text
        except:
            return "Error opening the URL"

        return url, page

    def getquote(self):
        url, page = self.geturl()
        soup = bs4.BeautifulSoup(page, features="html.parser")
        quote = soup.find("div", {"data-reactid": "31"}).find("span").text
        return quote
