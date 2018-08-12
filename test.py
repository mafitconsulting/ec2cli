import boto3, pprint
from ec2tool import instances

inst = instances.filter_inst('all')
for instance in inst:
    assert instance['State']['Name'] == 'running'

inst1 = instances.filter_inst('njp','bld')
bld = ['njpxbld06job001','njpxbld06api001']

for instance in inst1:
    instance_name = [x['Value'] for x in instance['Tags'] if x['Key'] == 'Name'][0]
    assert instance_name in bld

inst2 = instances.filter_inst('njp','cat')



