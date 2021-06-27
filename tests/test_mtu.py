import unittest
from scapy.layers.inet import IP

from scapy_p0f import fingerprint_mtu


class Test_MTU_p0f(unittest.TestCase):
    def test_windows_syn(self):
        pkt = IP(b'E\x00\x004Se@\x00\x80\x06\x93?\n\x00\x00\x14\n\x00\x00\x0c\xc3\x08\x01\xbb\xcf\xb4\xbb\\\x00\x00\x00\x00\x80\x02 \x00\xeb\x1b\x00\x00\x02\x04\x05\xb4\x01\x03\x03\x08\x01\x01\x04\x02')  # noqa: E501
        self.assertEqual(fingerprint_mtu(pkt), "Ethernet or modem")

    def test_windows_syn_ack(self):
        pkt = IP(b'E\x00\x004m\xf8@\x00\x80\x06\x00\x00\n\x00\x00\x0c\n\x00\x00\x14\x01\xbb\xc3\x08`\xabDN\xcf\xb4\xbb]\x80\x12\xff\xff\x14F\x00\x00\x02\x04\x05\xb4\x01\x03\x03\x08\x01\x01\x04\x02')  # noqa: E501
        self.assertEqual(fingerprint_mtu(pkt), "Ethernet or modem")