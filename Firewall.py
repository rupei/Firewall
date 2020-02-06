import csv


class Firewall:

    def __init__(self, path):
        # using a dictionary (hashtable) to store the rules to increase readibility (avoids if statements later)
        self.ruleset = {
            'inbound': {
                'tcp': set(),
                'udp': set()
            },
            'outbound': {
                'tcp': set(),
                'udp': set()
            }
        }

        with open(path) as file:
            reader = csv.reader(file)

            # adds each rule in the csv file into the ruleset
            for rule in reader:
                direction, protocol, port, ip = rule[0], rule[1], rule[2], rule[3]
                self.add_rule(direction, protocol, port, ip)

    def add_rule(self, direction, protocol, port, ip):
        if '-' in port:
            # port rule contains a range
            port = self.split_port(port)
        else:
            port = int(port)

        if '-' in ip:
            # ip rule contains a range
            ip_range = ip.split('-')
            ip = (self.split_ip(ip_range[0]), self.split_ip(ip_range[1]))
        else:
            ip = self.split_ip(ip)

        self.ruleset[direction][protocol].add((port, ip))

    def split_port(self, port):
        # splits a range of ports into two integers that represent its start and end
        port_range = port.split('-')
        return tuple([int(port_range[0]), int(port_range[1])])

    def split_ip(self, ip):
        # splits a range of ips into two tuples that represent its start and end
        split_ip = ip.split('.')
        return tuple([int(split_ip[idx]) for idx in range(len(split_ip))])

    def accept_packet(self, direction, protocol, port, ip):
        # checks the validity of certain inputs
        if direction != "inbound" and direction != "outbound":
            return False
        if protocol != "tcp" and protocol != "udp":
            return False
        if type(port) != int:
            return False
        if port < 1 or port > 65535:
            return False

        # parsing the given ip (a string) into a tuple of integers
        ip = self.split_ip(ip)
        if len(ip) != 4:
            return False

        # iterating through all the rules in the ruleset
        for rule_port, rule_ip in self.ruleset[direction][protocol]:
            port_cond = ip_cond = False
            if type(rule_port) == int:
                # the given rule's port requirement is not a range
                port_cond = rule_port == port
            else:
                port_cond = rule_port[0] <= port <= rule_port[1]

            if len(rule_ip) == 4:
                # the given rule's ip requirement is not a range
                ip_cond = rule_ip == ip
            else:
                ip_cond = rule_ip[0] <= ip <= rule_ip[1]

            if port_cond and ip_cond:
                # both port and ip conditions are satisfied given its direction and protocol
                return True

        return False
