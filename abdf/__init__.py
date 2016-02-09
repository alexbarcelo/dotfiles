"""Alex Barcelo Dotfiles library

All the Logic of Dotfiles management is done through this library (except the
special case of bootstrap, which is a standalone script).
"""
from argparse import ArgumentParser
from .deploy import deploy


def do_deploy(args):
    try:
        deploy()
    except Exception:
        print("Some error occurred")
        return 1
    else:
        return 0


def main():
    """Execute the main dotfiles

    :return: The exitcode
    """
    parser = ArgumentParser(
        prog="dotfiles",
        description="Alex Barcelo's Dotfile management library")
    subparsers = parser.add_subparsers(help='Commands for Dotfiles utility')

    deploy_parser = subparsers.add_parser(
        "deploy",
        help="Deploy files into the home folder")
    deploy_parser.set_defaults(func=do_deploy)

    args = parser.parse_args()
    return args.func(args)
