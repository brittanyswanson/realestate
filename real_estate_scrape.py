import requests
from bs4 import BeautifulSoup
import json
import ast

def PrintMenu():
	print("1 Gather HTML file from Zillow.com")
	#print("2 Run BeautifulSoup")
	print("3 PrettifyJSON")


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
	#json_response = ast.literal_eval(json_response)
	#parsed = json.loads(str(json_response))
	#print(json.dumps(parsed, indent=4, sort_keys=True))

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
	f = open("zillowFinal.txt", "a", encoding='utf-8')
	for line in splitJSON:
		tempLine = line.split('USA"}')
		if count != 0:
			list2.append(tempLine[0] + 'USA"}\n')
		count += 1

	f.write(list2)
	f.write("Number of records: " + str(count))
	f.close()

		#print(tempLine[0] + "}")
		
	#print(data_to_read)
"""
	data_to_read = data_to_read.replace("\'", "\"")
	parsed_json = json.loads(data_to_read)
	print(parsed_json['homeInfo'])
"""
def PrettifyJSON(txtFile):
	newList = txtFile.split(',')
	#newList = txtFile.split('{')
	#delimiter = '{'
	#firstIteration = True

	for line in newList:
		print(line)


"""
	for line in newList:
		if firstIteration != True:
			line = delimiter + line
			print(line)
		else:
			firstIteration = False
"""

if __name__=="__main__":
	#Launch the options
	PrintMenu()
	userOption = input("Choice: ")
	
	if userOption == "1":
		print("Scraping Zillow now")
		ScrapeZillow()
	elif userOption == "3":
		print("PrettifyJSON")
		PrettifyJSON('{"zpid": 29480655,"streetAddress": "4507 Yellow Rose Trl","zipcode": "78749","city": "Austin","state": "TX","latitude": 30.227091,"longitude": \\-97.838881,"price": 415000.0,"dateSold": 0,"datePriceChanged": 1542315840000,"bathrooms": 2.5,"bedrooms": 4.0,"livingArea": 2077.0,"yearBuilt": 1982,"lotSize": 9743.0,"homeType": "SINGLE_FAMILY","homeStatus": "FOR_SALE","photoCount": 37,"imageLink": "https://photos.zillowstatic.com/p_g/ISmiccrir40fbt1000000000.jpg","daysOnZillow": 58,"isFeatured": false,"shouldHighlight": false,"brokerId": 15439,"contactPhone": "5125881453","zestimate": 414842,"rentZestimate": 2095,"listing_sub_type": {"is_FSBA": true},"priceReduction": "$10,000 (Nov 15)","isUnmappable": false,"mediumImageLink": "https://photos.zillowstatic.com/p_c/ISmiccrir40fbt1000000000.jpg","isPreforeclosureAuction": false,"homeStatusForHDP": "FOR_SALE","priceForHDP": 415000.0,"festimate": 306983,"priceChange": \\-10000,"isListingOwnedByCurrentSignedInAgent": false,"timeOnZillow": 1539869340000,"isListingClaimedByCurrentSignedInUser": false,"hiResImageLink": "https://photos.zillowstatic.com/p_f/ISmiccrir40fbt1000000000.jpg","watchImageLink": "https://photos.zillowstatic.com/p_j/ISmiccrir40fbt1000000000.jpg","contactPhoneExtension": "","tvImageLink": "https://photos.zillowstatic.com/p_m/ISmiccrir40fbt1000000000.jpg","tvCollectionImageLink": "https://photos.zillowstatic.com/p_l/ISmiccrir40fbt1000000000.jpg","tvHighResImageLink": "https://photos.zillowstatic.com/p_n/ISmiccrir40fbt1000000000.jpg","zillowHasRightsToImages": false,"desktopWebHdpImageLink": "https://photos.zillowstatic.com/p_h/ISmiccrir40fbt1000000000.jpg","isNonOwnerOccupied": true,"hideZestimate": false,"isPremierBuilder": false,"isZillowOwned": false,"currency": "USD","country": "USA"}')
	elif userOption == "4":
		ParseResponse()
	else:
		print("User option is invalid.  Exiting.")






"""
	#print(r.text)
	soup = BeautifulSoup(r.content, "html.parser")

	print(soup.title.text)

	HouseList = soup.findall('ul')
	#HouseList = soup.findall('ul', attrs={"class":"photo-cards"})

	for i in HouseList:
		print(i)
"""






"""
if __name__=="__main__":
	parser = argparse.ArgumentParser()
	#parser.parse_args()

	parser.add_argument("echo", help="echo the string you use here")
	args = parser.parse_args()
	print(args.echo)
"""