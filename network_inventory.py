#! /usr/bin/env python
"""
A basic network inventory generation script.

Goal:
- Create a CSV inventory file
    device name, software version, uptime, serial number
"""
from pyats.topology.loader import load

#Script entry point
if __name__ == "__main__":
    import argparse

    print("Creating a network inventory script.")

    # Load pyATS testbed into script
    parser = argparse.ArgumentParser(description='Generate network inventory report')
    parser.add_argument('testbed', type=str,help='pyATS Testbed File')
    args = parser.parse_args()

    # Create pyATS testbed object
    testbed = load(args.testbed)

    # Connect to network devices
    print(f'Connecting to all devices in testbed {testbed.name}')
    testbed.connect(log_stdout=False)

    # Run commands to gather output from devices

    # Disconnect from network devices
    for device in testbed.devices:
        print(f'Disconnecting from device {device}.')
        testbed.devices[device].disconnect()
    # Build inventory report data structure

    # Generate CSV file of data