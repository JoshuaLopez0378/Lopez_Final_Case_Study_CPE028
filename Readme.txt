A submission for the Final Case Study for CPE 028 - Developing Applications and Automation

Contains: 
pyats/case_study_test                                               - contains the results of automated testing with pyATS and genie 
restconf_configurations folder                                      - containing the python scripts for network topics configuration
Lopez_Case Study_Design of Laboratory.docx                          - the main documentation submission
Lopez_Final Case Study - Network Automation and Programmability.mp4 - the video presentation

Run each script individually:
ospf_restconf.py for the OSPF configuration in router IOS XE on CSR Recommended
ip-route_restconf.py for the OSPF configuration in router IOS XE on CSR Latest
acl-config_restconf.py for the OSPF configuration in router IOS XE on CSR Local

Tested with pyATS and genie: 
Do pip install pyats[full]. The files for this are not included in the pyats folder due to size limitations
For testing genie diff, the names are:
csr-sandbox1-ospf-1; csr-sandbox1-ospf-2
csr1000v-1-static-route-1; csr1000v-1-static-route-2
CSR1kv-acl-1; CSR1kv-acl-2; and CSR1kv-acl-N or CSR1kv-acl-M (for re-run configuration)
