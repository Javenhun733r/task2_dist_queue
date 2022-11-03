import json
import http
from multiprocessing import Process


class Contol_Node:
    def __init__(self, data):
        self.data = data
        self.node_list = {}

    def add_node(self, ip, adress):
        self.node_list.update(json.dumps({ip: adress}))
    def get_stats(self):
        pass

    def remove_node(self, ip):
        self.node_list.pop(ip)
    def save_data_of_nodes(self):
        with open("date_nodes.txt", "a") as file1:
            file1.write(self.node_list)

def start_server(server_address):
    my_server = http.server.ThreadingHTTPServer(server_address, Contol_Node)
    print(str(server_address) + ' Waiting for POST requests...')
    my_server.serve_forever()


def start_local_server_on_port(port):
    p = Process(target=start_server, args=(('127.0.0.1', port),))
    p.start()
start_local_server_on_port(8011)