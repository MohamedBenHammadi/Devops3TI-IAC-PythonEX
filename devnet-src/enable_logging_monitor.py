import imp
import requests
import json

requests.packages.urllib3.disable_warnings()
DEVICE_IP = "192.168.56.101"
url = f"https://{DEVICE_IP}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}
auth = ("cisco", "cisco123!")
data = '{"severity": "informational"}'

response = requests.put(url, auth=auth, headers=headers, data=data, verify=False)
print(response.status_code)