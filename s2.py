#custom parsing/scraping html using bs4 
import requests 
from bs4 import BeautifulSoup 
def main():     
	page = requests.get("https://weather.com/en-IN/weather/today/l/22.50,71.80") #add location url here
	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup.prettify()) --> print all html content
	temp = soup.find(class_="today_nowcard-temp").get_text()
	phase = soup.find(class_="today_nowcard-phrase").get_text()
	location_name = soup.find(class_="h4 today_nowcard-location").get_text()
	time = soup.find(class_="today_nowcard-timestamp").get_text()

	print("\nLocation: {}".format(location_name))
	print("Time: {}".format(time))
	print("Temprature: {} - {}".format(temp,phase))

if __name__ == '__main__':main()
