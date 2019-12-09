import requests
url="https://entersoftsecurity.com"
params=dict(
	origin='Chicago,IL',
	destination='Los+Angeles,CA',
	waypoints='Joplin,MO|OKlahoma+city,Ok',
	sensor='false'
	)
resp = requests.get(url=url, params=params)
data = resp.json()
