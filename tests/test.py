#!/bin/python
import os
import json
import pprint

filename = 'data/test_ec2_all_running.json'
with open(filename) as f:
    content = json.load(f)

#print(json.dumps(content, indent=4, default=str))
for inst in content:
   assert inst['Instances'][0]['State']['Name'] == 'stopped'


