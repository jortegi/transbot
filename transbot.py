#!/usr/bin/python

from transbot_config import *
import transmissionrpc
import argparse


parser = argparse.ArgumentParser()

tc = transmissionrpc.Client(server, port)
torrents = tc.get_torrents()

print(torrents)
