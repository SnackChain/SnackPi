try:
    import network
except ImportError:
    import mock.network as network
    
def connect_to_wifi():
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('GV 2.4', '311153978')
    while not sta_if.isconnected():
      pass
    sta_if.config(dhcp_hostname="snackbase")
  print('sta config:', sta_if.ifconfig())

def create_access_point():
  ap_if = network.WLAN(network.AP_IF)
  ap_if.active(True)
  ap_if.config(ssid="SnackBase")
  ap_if.config(authmode=3, password="SnackChain")
  ap_if.config(channel=11)
  # ap_if.config(max_clients=10)
  print('ap config:', ap_if.ifconfig())