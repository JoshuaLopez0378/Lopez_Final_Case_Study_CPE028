import json
import requests
requests.packages.urllib3.disable_warnings()

###IOS XE on CSR Latest Code Always On csr1000v-1###
api_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/Cisco-IOS-XE-native:native/ip/route"
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = ("developer", "C1sco12345")

yangConfig = {
    "Cisco-IOS-XE-native:route": {
        "ip-route-interface-forwarding-list": [
            {
                "prefix": "87.0.0.0",
                "mask": "255.255.255.0",
                "fwd-list": [
                    {
                        "fwd": "GigabitEthernet2"
                    }
                ]
            }
        ]
    }
}


resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("IOS XE on CSR Latest Code Always On STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))