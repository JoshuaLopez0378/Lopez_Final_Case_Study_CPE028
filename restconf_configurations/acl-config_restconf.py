import json
import requests
requests.packages.urllib3.disable_warnings()

### ROUTER 3 (based from topology) CSR1kv###
api_url = "https://192.168.56.102/restconf/data/Cisco-IOS-XE-native:native/ip/access-list"
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = ("cisco", "cisco123!")

yangConfig = {
    "Cisco-IOS-XE-native:access-list": {
        "Cisco-IOS-XE-acl:standard": [
            {
                "name": 1,
                "access-list-seq-rule": [
                    {
                        "sequence": "10",
                        "deny": {
                            "std-ace": {
                                "ipv4-prefix": "192.168.87.102"
                            }
                        }
                    },
                    {
                        "sequence": "20",
                        "permit": {
                            "std-ace": {
                                "ipv4-prefix": "192.168.78.111"
                                # "any": [
                                #     None   
                                # ]
                            }
                        }
                    },
                                        {
                        "sequence": "30",
                        "permit": {
                            "std-ace": {
                                "ipv4-prefix": "192.175.78.111"
                                # "any": [
                                #     None   
                                # ]
                            }
                        }
                    }
                ]
            }
        ]
    }
}


resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("IOS XE on CSR Local STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))