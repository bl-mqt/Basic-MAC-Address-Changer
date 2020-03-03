#!/usr/bin/env python

import subprocess
import optparse
import re

def Mac_Changer(interface,MAC_addr):

	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",MAC_addr])
	subprocess.call(["ifconfig",interface,"up"])

	print "[+] Changing MAC Address of Interface %s to %s"%(interface,MAC_addr)

def get_argument():

	parser = optparse.OptionParser()	
	parser.add_option("-i","--interface",dest="interface", help = "Interface to change the MAC address")
	parser.add_option("-m","--mac", dest="new_mac", help = "Enter the new MAC Address")
	(options,arguments) = parser.parse_args()

	if not options.interface:
		parser.error("[-] Specify an Interface. Use python macchanger --help for more details")
	elif not options.new_mac:
		parser.error("[-] Specify an MAC Address. Use python macchanger --help for more details")

	return options

def getmac(interface):

	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

	if current_mac:
		return current_mac.group(0)
	else:
		return None

options = get_argument()		

Mac_Changer(options.interface,options.new_mac)

final_mac = getmac(options.interface)

if final_mac == options.new_mac :
	print "MAC Address Replaced with the new one %r"%final_mac
else:
	print "Error!"
