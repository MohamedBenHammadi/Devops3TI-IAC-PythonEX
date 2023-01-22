import unittest
import ipv4

class TestIpv4(unittest.TestCase):
    
    def test_get_net_prefix(self):
        self.assertEqual(ipv4.get_net_prefix('255.255.255.224'), '/27')

    def test_get_number_ip_addresses(self):
        self.assertEqual(ipv4.get_number_ip_addresses('/27'), 32)
    
    def test_get_number_ip_hosts(self):
        self.assertEqual(ipv4.get_number_ip_hosts('/27'), 30)
    
    def test_get_netmask(self):
        self.assertEqual(ipv4.get_netmask('/27'), '255.255.255.224')

    def test_get_network_bits(self):
        self.assertEqual(ipv4.get_network_bits('255.255.255.224'), '1111 1111 1111 1111 1111 1111 1110 0000')

if __name__ == '__main__':
    unittest.main()