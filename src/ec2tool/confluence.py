""" Atlassian POST using ReST to update confluence page """
from atlassian import Confluence
from security import Security
from ec2cli import config


def update_page(cell, content):
    """ update method """
    cipher = Security('ec2cli')
    server, user, passwd, parent_id, page_id, title, response = config(cell)
    confluence = Confluence(
        url=server,
        username=user,
        password=cipher.decrypt(passwd))

    confluence.update_page(
        parent_id=parent_id,
        page_id=page_id,
        title=title,
        body=content)

    return response
