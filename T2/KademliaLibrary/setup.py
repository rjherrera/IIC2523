#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="kademlia_iic2523",
    version="0.0.1",
    author="Vicente Dragicevic",
    url="http://github.com/vdrg/kademlia-iic2523",
    packages=find_packages(),
    install_requires=[
        "MultiMap",
        "kademlia==1.0",
        "rpcudp==3.0.0"
    ],
    dependency_links=[
        "https://github.com/bmuller/rpcudp/zipball/python3.5#egg=rpcudp-3.0.0",
        "https://github.com/vdrg/kademlia/zipball/IIC2523#egg=kademlia-1.0"
    ]
)
