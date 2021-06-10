import urllib.request, json 
apikey = "demo"
url = "https://financialmodelingprep.com/api/v3/quote-short/"

def ask_stock(name, apikey):
	global url
	url = url + name + "?apikey=" + apikey
ask_stock(str(input("Which stock price do you want to check?\n")), apikey)
with urllib.request.urlopen(url) as url:
	data = json.loads(url.read().decode())
for x in data:
	print(x["symbol"], ": " ,"$", x["price"],)