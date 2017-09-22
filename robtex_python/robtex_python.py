#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wrapper for the Robtex API."""

import requester

BASE_API_URL = "https://freeapi.robtex.com/"


def ip_query(ip_address):
    """Get the current forward and reverse of an IP number, together with GEO-location data and network data."""
    response = requester.get(BASE_API_URL + "ipquery/{}".format(ip_address))
    print(response)
    return response


def as_query(as_number):
    """Get the networks actually in global bgp table (plans to expand this in the future)."""
    response = requester.get(BASE_API_URL + "asquery/{}".format(as_number))
    print(response)
    return response


def pdns_forward(hostname):
    """Get the IP addresses to which the given host has resolved."""
    response = requester.get(BASE_API_URL + "pdns/forward/{}".format(hostname))
    print(response)
    return response


def pdns_reverse(ip_address):
    """Get the reverse pdns for the given IP address."""
    response = requester.get(BASE_API_URL +
                             "pdns/reverse/{}".format(ip_address))
    print(response)
    return response
