""" Instance Management """
from __future__ import print_function
import os
import argparse
import yaml


def create_parser():
    """ Create Argument Parser """
    parser = argparse.ArgumentParser(description='AWS Instance manipulation')
    parser.add_argument('cell', help='Cell region, eg, am1')
    parser.add_argument('--product', '-p', help='Filter on product name')
    parser.add_argument('--all', '-a', action='store_true', help='Display all instances')
    parser.add_argument('--ip', '-i', help='Retrieves information based on IP')
    parser.add_argument('--publish', action='store_true', help='publish content in confluence')
    return parser


def config(cell):
    """ Get config from yaml file for cell """
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'conf/config.yaml'))
    try:
        with open(filename, 'r') as f:
            conf = yaml.safe_load(f)
    except IOError as ex:
        print("Exception Caught %s" % ex)
    else:
        url = conf['credentials']['server']
        username = conf['credentials']['user']
        password = conf['credentials']['password']
        parent_id = conf[cell]['parent_id']
        page_id = conf[cell]['page_id']
        title = conf[cell]['title']
        response = conf[cell]['response']
        region = conf[cell]['region']
        product = conf['product']
        assert isinstance(response, object)
        return url, username, password, parent_id, page_id, title, response, region, product

def main():
    """ MAIN """
    import sys
    from prettytable import PrettyTable
    from termcolor import colored
    import instances
    import confluence
    import socket

    # Assigned parse args
    args = create_parser().parse_args()

    if args.all or args.ip or args.publish:
        inst = instances.filter_inst(args.cell, 'all')
    elif args.product:
        inst = instances.filter_inst(args.cell, args.product)
    else:
        sys.exit(create_parser().print_help())

    # Create our table structure
    table = PrettyTable(['Instance Name', 'Instance ID', 'IP', 'State', 'cell'])

    for instance in inst:
        # cos we're using low level client wrapper and not object-orientanted boto resource
        # We need a nice little list comprehension to obtain instance name from tag
        instance_name = [x['Value'] for x in instance['Tags'] if x['Key'] == 'Name'][0]
        instance_id = instance['InstanceId']
        ip = instance['PrivateIpAddress']
        state = instance['State']['Name']
        if args.ip:
            try:
                socket.inet_aton(args.ip)
            except socket.error:
                return "Not a supported ip address format"

            if ip in args.ip:
                table.add_row([instance_name, instance_id, ip, state, args.cell])
                sys.exit(table)
        else:
            table.add_row([instance_name, instance_id, ip, state, args.cell])

    if args.publish:
        content = confluence.update_page(args.cell, table.get_html_string())
        sys.exit("Updated content - %s" % content)
    else:
        print(table)
        print(colored("Number of running instances: %s" % len(inst), 'green'))


if __name__ == "__main__":
    main()
