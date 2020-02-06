from Firewall import Firewall


def sanity():
    fw = Firewall("test1.csv")
    assert not fw.accept_packet("outbound", "tcp", 9999, "192.168.10.11")
    assert fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11")
    assert not fw.accept_packet("outbound", "tcp", 12345, "192.168.10.12")
    assert fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11")
    assert not fw.accept_packet("outbound", "tcp", 12345, "191.148.1.1")

    assert fw.accept_packet("outbound", "udp", 1000, "52.12.48.92")
    assert fw.accept_packet("outbound", "udp", 2000, "52.12.48.92")
    assert not fw.accept_packet("outbound", "udp", 19, "52.12.48.92")

    assert fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")
    assert not fw.accept_packet("inbound", "tcp", 123, "192.168.1.2")

    assert not fw.accept_packet("inbound", "udp", 10233, "52.12.48.92")
    assert not fw.accept_packet("inbound", "udp", 53, "192.169.3.4")
    assert not fw.accept_packet("inbound", "udp", 54, "192.168.2.3")
    assert fw.accept_packet("inbound", "udp", 53, "192.168.1.166")
    assert fw.accept_packet("inbound", "udp", 53, "192.168.1.1")
    assert fw.accept_packet("inbound", "udp", 53, "192.168.2.5")

    assert not fw.accept_packet("gibberish", "tcp", 80, "192.168.1.2")
    assert not fw.accept_packet("inbound", "gibberish", 80, "192.168.1.2")
    assert not fw.accept_packet("inbound", "tcp", "gibberish", "192.168.1.2")
    assert not fw.accept_packet("inbound", "tcp", 80, "192.1.2")
    assert not fw.accept_packet("inbound", "tcp", 0, "192.168.1.2")
    assert not fw.accept_packet("inbound", "tcp", 65536, "192.168.1.2")
    assert not fw.accept_packet("inbound", "tcp", 65536, "192.256.1.2")

    print("all sanity tests pass.")


sanity()
