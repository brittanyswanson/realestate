import requests
from bs4 import BeautifulSoup
import json
import mysql.connector

def GetExistingRecords():
	existingRecords= []
	try:
		cnx = mysql.connector.connect(user='python_script', password='Dzkiwcnp4gT',
								  host='127.0.0.1',
								  database='HouseData')
		cursor = cnx.cursor()

		query = ("SELECT zpid FROM identitytable;")

		cursor.execute(query)

		for (zpid) in cursor:
			existingRecords.append(zpid)

		cursor.close()
	except mysql.connector.Error as err:
			print(err)
	else:
		cnx.close()
	print(existingRecords)
	return existingRecords



def WorkingOnThisFunction():
	#Start by getting existing records
	existingRecords = GetExistingRecords()

	#Open housedata.txt and load each record into a list

	#For each record, store zpid and other data as variables

def DatabaseWork():
	try:
		cnx = mysql.connector.connect(user='python_script', password='Dzkiwcnp4gT',
								  host='127.0.0.1',
								  database='HouseData')
		cursor = cnx.cursor()

		query = ("SELECT street_address FROM location")

		cursor.execute(query)

		for (street_address) in cursor:
			print(street_address)

		cursor.close()
	except mysql.connector.Error as err:
			print(err)
	else:
		cnx.close()




def PrintMenu():
	print("1 Gather HTML file from Zillow.com")
	#print("2 Run BeautifulSoup")
	print("2 ParseResponse")
	print("3 Database")


def ScrapeZillow():
	#url = 'https://www.zillow.com/homes/for_sale/pmf,pf_pt/globalrelevanceex_sort/30.238306,-97.824669,30.175331,-97.916937_rect/13_zm/'
	#url = 'https://www.zillow.com/austin-tx/sold/'
	#Undocumented API for Zillow found in Network tab of Google Chrome Tools
	url = 'https://www.zillow.com/search/GetResults.htm?spt=homes&status=100001&lt=111101&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=0%2C&yr=,&singlestory=0&hoa=0%2C&pho=0&pets=0&parking=0&laundry=0&income-restricted=0&fr-bldg=0&condo-bldg=0&furnished-apartments=0&cheap-apartments=0&studio-apartments=0&pnd=0&red=0&zso=0&days=any&ds=all&pmf=1&pf=1&sch=100111&zoom=13&rect=-97916937,30175331,-97824669,30238306&p=1&sort=globalrelevanceex&search=maplist&listright=true&isMapSearch=true&zoom=13'
	headers= {
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'en-US,en;q=0.9',
		'upgrade-insecure-requests':'1',
		'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
	}

	r = requests.get(url,headers=headers)
	json_response = json.loads(r.text)


	#Write the response to zillow.txt file
	f = open("zillow.txt", "a", encoding='utf-8')
	f.write(str(json_response))
	f.close()


def ParseResponse():
	with open("zillow.txt", "r") as myfile:
		data_to_read = myfile.read()

	#data_to_read = data_to_read.replace(""""is_FSBA": true""", "")
	list2 = []

	splitJSON = data_to_read.split('"homeInfo":')
	count = 0

	for line in splitJSON:
		tempLine = line.split('USA"}')
		if count != 0:
			list2.append(tempLine[0] + 'USA"}\n')
		count += 1


	with open('housedata.txt', 'w') as f:
		f.write("Number of records: " + str(count))
		for item in list2:
			f.write('%s\n' % item)


def PrettifyJSON(txtFile):
	newList = txtFile.split(',')


	for line in newList:
		print(line)



if __name__=="__main__":
	#Launch the options
	PrintMenu()
	userOption = input("Choice: ")
	
	if userOption == "1":
		print("Scraping Zillow now")
		ScrapeZillow()
	elif userOption == "2":
		ParseResponse()
	elif userOption == "3":
		GetExistingRecords()
	else:
		print("User option is invalid.  Exiting.")
