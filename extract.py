import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json
 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = input("Which method to Use \n1 for celestrak \n2 for Nasaspceflight\n")
if x=='1':
	url=input('Enter location:')
	if len(url)<1:
		url='http://www.celestrak.com/NORAD/elements/stations.txt'
	print('Retrieving', url)
	uh = urllib.request.urlopen(url, context=ctx)

	data = uh.read().decode()
	data = data.replace('\r','')

	print('Retrieved', len(data), 'characters')
	#print(data)
	fh = open('all_satellite_pos.txt','w')
	fh.write(data)
	fh.close()

if x=='2':

	url=input('Enter location:')
	if len(url)<1:
		url='https://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html'
	print('Retrieving', url)
	uh1 = urllib.request.urlopen(url, context=ctx)

	html = uh1.read()
	print('Retrieved', len(html), 'characters')
	#print(data)
	soup = BeautifulSoup(html, 'html.parser')
	data = soup.prettify()
	# data = soup.get_text()
	data = soup.pre.text

	fh = open('nasa_data.txt','w')
	fh.write(data)
	fh.close()