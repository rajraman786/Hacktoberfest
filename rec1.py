import sys #for using commandline arg
import requests
import socket
import json
import whois

#to check arg is provided or not
if (len(sys.argv)<2):
    print("usage: " + sys.argv[0] + "<url>")
    sys.exit()

print(sys.argv[1])
req = requests.get("https://" + sys.argv[1])
print("\n"+str(req.headers))
print()

get_host = socket.gethostbyname(sys.argv[1])
print("the ip address of " + sys.argv[1] + " is: " + get_host)
print()

#ip info.io api for get host loaction
req_2 = requests.get("https://ipinfo.io/" + get_host + "/json")
respo = json.loads(req_2.text)

print("Location: " + respo["loc"])
print("Region: " + respo["region"])
print("City: " + respo["city"])
print("Country: " + respo["country"])
print()

whois_info = whois.whois(sys.argv[1])
print(whois_info)