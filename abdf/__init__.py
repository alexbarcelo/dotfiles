"""Alex Barcelo Dotfiles library

All the Logic of Dotfiles management is done throught this library (except the
special case of bootstrap, which is a standalone script).
"""
from argparse import ArgumentParser


def main():
    """Execute the main dotfiles

    :return: The exitcode
    """
    parser = ArgumentParser(
        prog="dotfiles",
        description="Alex Barcelo's Dotfile management library",
    )

    parser.parse_args()
