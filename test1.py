from Firewall import Firewall

fw = Firewall("test1.csv")
assert fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")    # matches first rule
assert fw.accept_packet("inbound", "udp", 53, "192.168.2.1")    # matches third rule
assert fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11")  # matches second rule
assert not fw.accept_packet("inbound", "tcp", 81, "192.168.1.2")
assert not fw.accept_packet("inbound", "udp", 24, "52.12.48.92")

print("all given test cases passed.")