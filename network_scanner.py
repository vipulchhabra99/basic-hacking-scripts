import scapy.all as scapy


def scan(ip):
	arp_request=scapy.ARP(pdst=ip)
	print(arp_request.summary())




scan("192.168.159.1/24")