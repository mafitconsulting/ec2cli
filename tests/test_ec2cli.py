import pytest

from ec2tool import ec2cli

cell = 'njp'
product_set = ['pup', 'bld', 'jmp', 'pds']


@pytest.fixture()
def parser():
    return ec2cli.create_parser()


def test_parser_without_args(parser):
    """
    With no arguments the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_parser_with_cell_only(parser):
    """
    The parser will return usage if it received cell
    only
    """
    args = parser.parse_args([cell])
    assert cell


def test_parser_with_cell_and_all_opt(parser):
    """
    The parser will not exit if it receives a cell and
    the 'all' flag
    """
    args = parser.parse_args([cell, '--all'])
    assert args.all


def test_parser_with_ip_address(parser):
    """
    The parser will exit if it does not
    receive ip address with --ip flag
    """
    with pytest.raises(SystemExit):
        parser.parse_args([cell, '--ip'])


def test_parser_with_unsupported_product(parser):
    """
    exits with error if product not in supported
    list
    """
    with pytest.raises(AssertionError):
        args = parser.parse_args([cell, '--product', 'cat'])
        assert args.product in product_set


def test_parser_with_known_product(parser):
    """
    The parser will not exit if the product is known.
    """
    for product in ['jmp', 'pup', 'bld', 'pds']:
        assert parser.parse_args([cell, '--product', product])
