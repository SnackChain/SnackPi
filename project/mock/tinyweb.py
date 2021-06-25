class webserver:
	def add_resource(self, cls, url, **kwargs):
		# print("resource added: ", cls)
		return

	def run(self, host="127.0.0.1", port=8081, loop_forever=True):
		print("server at: ", host, ":", port)