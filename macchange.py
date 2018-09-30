import subprocess
import optparse
import re

def get_arguments():
	parser=optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="Interface tochange mac address")
	parser.add_option("-m","--mac",dest="newid",help="Interface to add mac address")
	(options,arguments)=parser.parse_args()

	if not options.newid:
		parser.error("[-]PLEASE ENTER THE MAC TO CHANGE ,use --help for more info ")

	if not options.interface:
		parser.error("[-]PLEASE ENTER THE INTERFACE ,use --help for more info ")

	return options

def macchange(newmac,interface):
	print("[+] CHANGING MAC ADDRESS TO "+ newmac +"[+]")
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",newmac])
	subprocess.call(["ifconfig",interface,"up"])


def get_mac(interface):

	ifconfig_result=subprocess.check_output(["ifconfig",interface])
	mac_address_search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

	if not mac_address_search_result:
		print(" [-] MAC ADDRESS NOT FOUND [-] ")

	else:
		return mac_address_search_result.group(0)

	

options=get_arguments()


current_mac=get_mac(options.interface)

print("CURRENT MAC ADDRESS IS : "+str(current_mac))

macchange(options.newid,options.interface)
current_mac=get_mac(options.interface)

if current_mac:
	if current_mac==options.newid:
		print("[+] MAC ADDRESS SUCCESSFULLY CHANGED TO : "+current_mac+" [+]")

	else:
		print("MAC ADDRESS DIDN'T CHANGED")







