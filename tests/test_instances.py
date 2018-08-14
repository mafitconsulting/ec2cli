import os
import json
import boto3
import pytest
from ec2tool import instances
from moto import mock_ec2

class FlightData(object):

    def __init__(self, filename):
        self.filename = filename

    def loadjson(self):
        instances = json.loads(
                        open(os.path.join(os.path.dirname(__file__), "data", self.filename)).read()
               )
        return instances

def test_filter_all_instances():
    """
    tests if all instances filter works
    mock ec2 instance data with json file
    """
    data = FlightData('test_ec2_all_running.json')
    instances = data.loadjson()
    for inst in instances:
       assert inst['Instances'][0]['State']['Name'] == 'running'


def test_filter_on_product():
    """
    test filter on recivied prodtc argument
    hardcode 'cell' and 'product' name
    abd pass into filter_inst method
    """
    data = FlightData('test_ec2_filter_product.json')
    instances = data.loadjson()
    bld = ['njpxbld06job001', 'njpxbld06api001']

    for inst in instances:
        instance_name = [x['Value'] for x in inst['Instances'][0]['Tags'] if x['Key'] == 'Name'][0]
        assert instance_name in bld

def test_product_not_supported():
    cell = 'njp'
    with pytest.raises(SystemExit):
        inst = instances.filter_inst(cell, 'cat')


def test_filter_on_ip():
    """
    tests filter on ip, mocks ec2
    instance data with json file
    Lets assert the ip address of
    puppetmaster
    """
    puppetmasterIP = '100.100.2.87'
    data = FlightData('test_ec2_all_running.json')
    instances = data.loadjson()
    for inst in instances:
        instance_name = [x['Value'] for x in inst['Instances'][0]['Tags'] if x['Key'] == 'Name'][0]
        ip = inst['Instances'][0]['PrivateIpAddress']
        if puppetmasterIP in ip:
            assert instance_name == 'njpxpup05mst001'
            assert ip == '100.100.2.87'



