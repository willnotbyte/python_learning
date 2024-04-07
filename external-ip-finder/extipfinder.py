import urllib.request
import re

print ("Attempting to open URL to obtain IP Address")

url = "http://checkip.dyndns.org"
print (url)

request = urllib.request.urlopen(url).read()

theIP = str(request)

theIP = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", theIP)
print("\nYour external IP Address is: ", theIP)