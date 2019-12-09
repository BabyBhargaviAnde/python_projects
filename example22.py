
import pygeoip

def ipLocator(ip):
 GeoIPDatabase = ‘/home/user/GeoLiteCity.dat’
 ipData = pygeoip.GeoIP(GeoIPDatabase)
 record = ipData.record_by_name(ip)
 print(“The geolocation for IP Address %s is:” % ip)
 print(“Accurate Location: %s, %s, %s” % (record[‘city’], record[‘region_code’], record[‘country_name’]))
 print(“General Location: %s” % (record[‘metro_code’]))