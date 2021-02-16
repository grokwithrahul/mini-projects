import datetime
f = open('test.txt', 'a')
time = datetime.datetime.now()
f.write(time.strftime("%H:%M.%S")+" last written.")
f.close()