import os
import random
import subprocess
import logging
import sys
from scapy.all import RandMAC
import psutil


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_interfaces():
    if os.name == 'nt':
        interfaces = psutil.net_if_addrs()
        return list(interfaces.keys())
    else:
        interfaces = psutil.net_if_addrs()
        return list(interfaces.keys())

def generate_random_mac():
    return str(RandMAC()).replace(':', '-')

def change_mac(interface, new_mac):
    if os.name == 'nt':
        try:
            subprocess.check_call(f"netsh interface set interface {interface} disable", shell=True)
            subprocess.check_call(f"netsh interface set interface {interface} enable", shell=True)
            subprocess.check_call(f"powershell -Command \"& {{\"" +
                                  f"Set-NetAdapter -Name '{interface}' -MacAddress '{new_mac}'\"" +
                                  "}\"", shell=True)
            logging.info(f"MAC address for {interface} changed to {new_mac}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to change MAC address: {e}")
    else:
        try:
            subprocess.check_call(f"sudo ifconfig {interface} down", shell=True)
            subprocess.check_call(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
            subprocess.check_call(f"sudo ifconfig {interface} up", shell=True)
            logging.info(f"MAC address for {interface} changed to {new_mac}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to change MAC address: {e}")

def revert_mac(interface, original_mac):
    logging.info(f"Reverting MAC address for {interface} to {original_mac}")
    change_mac(interface, original_mac)

def main():
    interfaces = get_interfaces()
    logging.info("\nAvailable interfaces:")
    for i, interface in enumerate(interfaces):
        logging.info(f"{i}: {interface}")

    try:
        interface_index = int(input("\nSelect interface by number: ").strip())
        interface_name = interfaces[interface_index]


        original_mac = psutil.net_if_addrs()[interface_name][0].address
        logging.info(f"Original MAC address for {interface_name} is {original_mac}")

        new_mac = generate_random_mac()
        logging.info(f"\nChanging MAC address for {interface_name} to {new_mac}")
        change_mac(interface_name, new_mac)


        revert = input("\nDo you want to revert back to the original MAC address? (yes/no): ").strip().lower()
        if revert == 'yes':
            revert_mac(interface_name, original_mac)

    except (IndexError, ValueError) as e:
        logging.error(f"Invalid input: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    if os.geteuid() != 0 and os.name != 'nt':
        logging.error("This script must be run as root on Unix-based systems.")
        sys.exit(1)
    main()