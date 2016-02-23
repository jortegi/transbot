#!/usr/bin/python

from transbot_config import *
import transmissionrpc


tc = transmissionrpc.Client(server, port)

torrents = tc.get_torrents()

print(torrents)
