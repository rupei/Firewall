from Firewall import Firewall
from random import randint
import csv
import time


def make_rules():
    with open("random.csv", mode="w+", newline="") as file:
        writer = csv.writer(file)
        for _ in range(1000):
            direction = "inbound" if randint(0, 1) == 0 else "outbound"
            protocol = "tcp" if randint(0, 1) == 0 else "udp"
            port = make_port()
            ip = make_ip()
            writer.writerow([direction, protocol, port, ip])


def make_port():
    make_range = randint(0, 1)
    if make_range:
        start = randint(1, 65534)
        return str(start) + "-" + str(randint(start, 65535))
    else:
        return str(randint(1, 65535))


def make_ip():
    make_range = randint(0, 1)
    if make_range:
        start = make_one_ip()
        end = make_one_ip(start)
        return start + "-" + end
    else:
        return make_one_ip()


def make_one_ip(minimum=None):
    ip = ""
    if minimum:
        minimums = [int(val) for val in minimum.split('.')]
    else:
        minimums = [0, 0, 0, 0]
    for i in range(4):
        if i == 3:
            ip += str(randint(minimums[i], 254))
        else:
            ip += str(randint(minimums[i], 255)) + "."
    return ip


def performance(fw):
    start = time.time()
    for _ in range(100000):
        direction = "inbound" if randint(0, 1) == 0 else "outbound"
        protocol = "tcp" if randint(0, 1) == 0 else "udp"
        fw.accept_packet(direction, protocol, make_port(), make_ip())
    end = time.time()
    print("one hundred thousand queries on one thousand rules took on average: " + str((end - start) / 10 ** 6) + " seconds")


def run_performance():
    make_rules()
    fw = Firewall("random.csv")
    performance(fw)

run_performance()
