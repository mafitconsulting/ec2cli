""" module to return instances """
from __future__ import print_function
import sys
import os
import boto3
import botocore
from ec2cli import config


def filter_inst(*args):
    """ return instances """

    ec2_instances = boto3.client('ec2')
    res = []

    # product dictionary
    product_dict = {
        'bld': "xbld*",
        'pup': "xpup*",
        'jmp': "xjmp*",
        'pds': "xpds*",
    }

    if os.getenv('AWS_DEFAULT_REGION'):
        validate_cell = config(args[0])[7]
        if validate_cell != os.environ['AWS_DEFAULT_REGION']:
            sys.exit("Argument cell does not match sourced environment")


    try:
        if args[1] == 'all' or args[1] == 'ip':
            res = ec2_instances.describe_instances(
                Filters=[{'Name': 'instance-state-name',
                          'Values': ['running']}]).get('Reservations', [])
        else:
            if args[1] not in product_dict.keys():
                sys.exit("Supported product %s" % {key for key in product_dict.keys()})

            for key, value in product_dict.items():
                if key in args[1]:
                    filter_value = args[0] + value + "*"
                    res = ec2_instances.describe_instances(
                        Filters=[{'Name': 'tag:Name',
                                  'Values': [filter_value]}]).get('Reservations', [])

    except (TypeError, NameError) as ex:
        print(ex)

    except botocore.exceptions.ClientError:
        sys.exit("Error connecting to EC2 API, make sure you've sourced the correct\
 environment or your session has not expired!")
    else:
        instances = sum(
            [
                [i for i in r['Instances']]  # list comprehension, its the future
                for r in res
            ], [])

        return instances
