from flask import render_template, request, session, redirect, url_for
import requests
import json


class ErrorCode(Exception):
    def __init___(self, status_code):
        self.status_code = status_code

    def __str__(self):
        return f'Error code {self.status_code}'


class Client:
    def __init__(self, adress, requests_count=1000):
        self.adress = adress
        self.requests_count = requests_count
        self.free_node = ""
        self.loaded_node = ""
        self.count = 0

    def update_stats(self):
        if self.count == 0:
            stats = json.loads(requests.get(self.adress + "/getstats").text)
            self.loaded_node = max(stats, key=lambda adress: stats[adress])
            self.free_node = min(stats, key=lambda adress: stats[adress])
        self.count = (self.count + 1) % self.requests_count

    def read(self):
        self.update_stats()
        return json.loads(requests.get(self.loaded_node + "/readmessage").text)

    def write(self, message):
        self.update_stats()
        r = requests.post(self.free_node + '/writemessage', data=json.dumps(message))
        if r.status_code > 400:
            raise ErrorCode(r.status_code)
