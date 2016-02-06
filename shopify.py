import urllib2
import json

response = urllib2.urlopen('http://shopicruit.myshopify.com/products.json')
data = json.load(response)
wallet_count = float()
lamp_count = float()
for product in data['products'] :
	if product['product_type'] == 'Wallet' :
		for wallet in product['variants'] :
			wallet_count += float(wallet['price'])
	elif product['product_type'] == 'Lamp' :
		for lamp in product['variants'] :
			lamp_count += float(lamp['price'])
print "Wallet count $%s" %wallet_count
print "Lamp count $%s" %lamp_count