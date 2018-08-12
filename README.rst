ec2tool
========

CLI for AWS ec2 instance lookup based on the following:
    - List all instances in a cell
    - list instances by product
    - filter instance on ip
    - Publish Running instances in confluence for each cell

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone ``
3. Fetch development dependencies: ``make install``


Prerequisite
------------------------

1. Ensure the correct cell (eg njp) is sourced with awsenv


Usage
-----

List all instances running in njp

::

    $ ec2cli njp --all

List instances related to the puppet product in am1

::

    $ ec2cli am1 -p pup


List instance assciated with ip address

::
    $ ec2cli njp -i 10.20.3.40


Publish all running instances for specified env
and confluence page

::

    $ ec2cli am1 --publish


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make

