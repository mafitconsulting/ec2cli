import boto3
import pytest
from ec2tool import instances
from moto import mock_ec2

def test_filter_all_instances():
    """
    tests if all instances filter works
    """
    inst = instances.filter_inst('all')
    for instance in inst:
        assert instance['State']['Name'] == 'running'


def test_filter_on_product():
    """
    test filter on recivied prodtc argument
    hardcode 'cell' and 'product' name
    abd pass into filter_inst method
    """
    inst = instances.filter_inst('njp','bld')
    bld = ['njpxbld06job001','njpxbld06api001']

    for instance in inst:
        instance_name = [x['Value'] for x in instance['Tags'] if x['Key'] == 'Name'][0]
        assert instance_name in bld

def test_product_not_supported():
    with pytest.raises(SystemExit):
        inst = instances.filter_inst('njp','cat')








