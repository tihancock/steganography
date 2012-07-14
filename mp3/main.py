#! /usr/bin/python

import argparse, steg, os, sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

parser = argparse.ArgumentParser(description="Encode/decode message in an image.")
parser.add_argument('mp3', metavar='<mp3>', type=str,
                   help='An mp3 file to write to/read from')
parser.add_argument('--encode', nargs=1, metavar='<message>', type=str, help='Encode the supplied message into the file.')

args      = parser.parse_args()
file_path = args.mp3
message   = args.encode

if args.encode is None:
    steg.decode_message(file_path)
else:
    if not steg.encode_message(file_path, message[0]):
        print "Failed to encode message."
