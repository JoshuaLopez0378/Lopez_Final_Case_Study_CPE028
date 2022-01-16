import json
import requests
requests.packages.urllib3.disable_warnings()

###IOS XE on CSR Recommended Code Always On csr-sandbox1###
api_url = "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/Cisco-IOS-XE-native:native/router"  #THIS WILL CHANGE ACC TO ROUTER
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

# basicauth = ("cisco", "cisco123!")
basicauth = ("developer", "C1sco12345")

yangConfig = {
    "Cisco-IOS-XE-native:router": {
        "Cisco-IOS-XE-ospf:ospf": [
            {
                "id": 2,                #OSPF ID, "router ospf 1"
                "network": [
                    {
                        "ip": "10.10.20.0",           
                        "mask": "0.0.0.255",
                        "area": 0
                    },
                    {
                        "ip": "11.0.0.0",
                        "mask": "0.255.255.255",
                        "area": 0
                    },
                    {
                        "ip": "192.168.255.0",
                        "mask": "0.0.0.255",
                        "area": 0
                    }
                ]
            }
        ]
    }
}


resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("IOS XE on CSR Recommended Code Always On STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
