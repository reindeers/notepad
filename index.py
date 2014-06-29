import time
from grab import Grab

def getDiary(login, password, link, nicks):
	g = Grab()
	g.go('http://www.diary.ru/')
	g.set_input('user_login', login) 
	g.set_input('user_pass', password)
	g.submit()
	time.sleep(10)

	i = 0
	j = 0
	count = len(g.xpath_list('//*[@id="pageBar"]//@href')) - 1
	while i < count:
		g.go('http://' + link + '.diary.ru/?favorite&from=' + j ) 
		lst = g.doc.select('//*[@id="postsArea"]//div')
		#+ str(20)
		for elem in lst:
			print elem.text()
		
		i +=1
		j += 20

def getYoutube(login, password):
	gg = Grab()
	gg.go('https://accounts.google.com/ServiceLogin?sacu=1&continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26feature%3Dsign_in_button%26hl%3Dru%26next%3D%252F&hl=ru&service=youtube')
	gg.set_input('Email', login) 
	gg.set_input('Passwd', password) 
	gg.submit()
	time.sleep(10)
	gg.go('http://www.youtube.com/feed/subscriptions')
	time.sleep(10)
	#print g.xpath('//*[@id="content"]')
	#lst = g.xpath_list('//*[@id="postsArea"]//div')
	print gg.doc.select('//header').text()
		#*[@id="content"]

def getWeather(city):
	gWeather = Grab()
	gWeather.go('http://pogoda.yandex.ru/' + city + '/')
	print gWeather.doc.select('//*[@class="b-thermometer"]').one().text()


getWeather('moscow')
