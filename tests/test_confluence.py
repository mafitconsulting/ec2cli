import pytest
from atlassian import Confluence
from ec2tool import ec2cli
from ec2tool.security import Security


def test_confluence_connectivity_for_njp():
    """
    Assert configuration for am1
    """
    cell = 'njp'
    server, user, passwd, parent_id, page_id, title, response = ec2cli.config(cell)

    assert server == 'https://conf.willhillatlas.com'
    assert user == 'generic.fieldhouse'
    assert passwd == 'L0UwXV3zfzTU14wrL2PnW1a2C7XXFYBjBvIdERPEYy0ZISVJvGiwfZ+ttTELm3nc'
    assert parent_id == 234588279
    assert page_id == 234593411
    assert title == 'NJP EC2 Instances'
    assert response == 'https://conf.willhillatlas.com/display/IR/NJP+EC2+Instances'

def test_confluence_connectivity_for_am1():
    """
    Assert configuration for am1
    """
    cell = 'am1'
    server, user, passwd, parent_id, page_id, title, response = ec2cli.config(cell)

    assert server == 'https://conf.willhillatlas.com'
    assert user == 'generic.fieldhouse'
    assert passwd == 'L0UwXV3zfzTU14wrL2PnW1a2C7XXFYBjBvIdERPEYy0ZISVJvGiwfZ+ttTELm3nc'
    assert parent_id == 234588279
    assert page_id == 234593431
    assert title == 'AM1 EC2 Instances'
    assert response == 'https://conf.willhillatlas.com/display/IR/AM1+EC2+Instances'

