AP_IF = "AP_IF"
STA_IF = "STA_IF"

class WLAN:

	is_connected = False
	ssid = None
	password = None
	dhcp_hostname = None
	mode = None
	authmode = None
	channel = None

	def __init__(self, mode):
		self.mode = mode

	def active(self, active):
		self.active = active

	def connect(self, ssid, password):
		self.ssid = ssid
		self.password = password
		self.is_connected = True

	def isconnected(self):
		return self.is_connected

	def config(self, dhcp_hostname = None, ssid = None, authmode = None, password = None, channel = None):
		if self.dhcp_hostname is None:
			self.dhcp_hostname = dhcp_hostname
		if self.ssid is None:
			self.ssid = ssid
		if self.authmode is None:
			self.authmode = authmode
		if self.password is None:
			self.password = password
		if self.channel is None:
			self.channel = channel

	def ifconfig(self):
		if self.mode == STA_IF:
			return "WLAN: STA_IF, connected to: " + self.ssid + ", password: " + self.password + ", host name: " + self.dhcp_hostname
		else:
			return "WLAN: AP_IF, ssid: " + self.ssid + ", password: " + self.password + ", authmode: " + str(self.authmode) + ", channel: " + str(self.channel)