#!/usr/bin/python3
# Author - Tumi Thaki

"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
