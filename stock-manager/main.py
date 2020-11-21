from getquote import GetQuote
import tinydb
import datetime
import time

code, region = input("code and region: ").split()

quote = GetQuote(code, region)
print(quote.getquote())
db = tinydb.TinyDB("database.json")

timeNow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
db.insert({code:quote, "time":timeNow})
time.sleep(600)
