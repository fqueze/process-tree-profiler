import time
from resourcemonitor import SystemResourceMonitor
import json
import webbrowser
from urllib.parse import quote
import http.server
import os
import requests

class HTTPHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.server.wrapper

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header(
            "Access-Control-Allow-Origin", "https://profiler.firefox.com"
        )
        self.end_headers()

        self.wfile.write(s.data.encode())
        s.do_shutdown = True

class ProfileViewerServer(object):
    def __init__(self, data):
        address="localhost"
        port=0
        self.data = data

        self.server = http.server.HTTPServer((address, port), HTTPHandler)
        self.server.wrapper = self
        self.do_shutdown = False

    @property
    def url(self):
        hostname, port = self.server.server_address
        return "http://%s:%d/" % (hostname, port)

    def run(self):
        while not self.do_shutdown:
            self.server.handle_request()


if __name__ == '__main__':
    resources = SystemResourceMonitor(poll_interval=0.01)
    resources.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        pass
    
    resources.stop()
    profile = json.dumps(resources.as_profile(), separators=(",", ":"))

    server = ProfileViewerServer(profile)
    profiler_url = "https://profiler.firefox.com/from-url/" + quote(
        server.url, ""
    )

    try:
        browser = webbrowser.get().open_new_tab(profiler_url)
    except Exception:
        print("Please open %s in a browser." % profiler_url)
    server.run()
