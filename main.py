import requests
from bs4 import BeautifulSoup as bs

list_data = {'host':[], 'port':[], 'negara':[]}

def tampilkan_table():
	for i in range(len(list_data['host'])):
		print('''---------------------------------
Host = {}
Port = {}
Negara = {}'''.format(list_data['host'][i],list_data['port'][i],list_data['negara'][i]))
	#print(dir(dataToTables))
	print('---------------------------------')


# By : Rusman Tobyakta Siregar
# 2020

def ambil_proxy(Jfetch):
	url = "https://www.sslproxies.org/"
	req = requests.get(url)
	sup = bs(req.text, 'html.parser')
	for i in sup.find_all("tr")[:Jfetch+1][1:]:
		data = i.find_all("td")
		alamat = data[0].text
		port = data[1].text
		negara = data[3].text
		https = data[6].text
		if https == 'yes':
			alamat = 'https://'+alamat
		else:	
			alamat = 'http://'+alamat	
		list_data['host'].append(alamat)
		list_data['port'].append(port)
		list_data['negara'].append(negara)
	tampilkan_table()
	
if __name__ == "__main__":
	jumlah_fetch = int(input('Jumlah yang ditampilkan : '))
	if jumlah_fetch > 100:
		print('Jangan melebihi 100')
		exit()
	print('Tunggu Sebentar ...')
	ambil_proxy(jumlah_fetch)