from Firewall import Firewall
fw = Firewall("void.csv")

# unit tests on the split_port method
assert fw.split_port("80-100") == (80, 100)
assert fw.split_port("1-65535") == (1, 65535)

# unit tests on the split_ip method
assert fw.split_ip("123.222.4.10") == (123, 222, 4, 10)
assert fw.split_ip("0.0.0.0") == (0, 0, 0, 0)
assert fw.split_ip("255.255.255.255") == (255, 255, 255, 255)

# unit tests on the add_rule method
fw.add_rule("inbound", "tcp", "800", "1.1.1.1")
assert (800, (1, 1, 1, 1)) in fw.ruleset["inbound"]["tcp"]
assert len(fw.ruleset["inbound"]["tcp"]) == 1
fw.add_rule("outbound", "udp", "100-700", "2.2.2.2-21.11.100.255")
assert ((100, 700), ((2, 2, 2, 2), (21, 11, 100, 255))) in fw.ruleset["outbound"]["udp"]
assert len(fw.ruleset["inbound"]["tcp"]) == 1
assert len(fw.ruleset["outbound"]["udp"]) == 1
assert len(fw.ruleset["inbound"]["udp"]) == 0
assert len(fw.ruleset["outbound"]["tcp"]) == 0

print("all unit test cases passed.")
