from flask import Flask, render_template, request, jsonify, json
import requests

app = Flask(__name__)
AMOUNT_OF_ROOTS = 1


class Control_Node():
    def __init__(self, data_nodes=[]):
        self.data_nodes = data_nodes

    def add_node(self, node):
        self.data_nodes.append(node)

    def remove_node(self, adress):
        self.data_nodes.pop(adress)

    def get_stats(self):
        all_data = []

        for node in self.data_nodes:
            lenght = requests.get(node).json()
            lenght = lenght.get('lenght')
            all_data.append([node, lenght])
        return all_data


control_node = Control_Node()
list_of_nodes = []
for i in range(1, AMOUNT_OF_ROOTS + 1):
    list_of_nodes.append(f'http://127.0.0.1:500{i}/')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/add_node', methods=['GET', 'POST'])
def add_node():
    if request.method == 'GET':
        if len(control_node.data_nodes) <= AMOUNT_OF_ROOTS:
            control_node.add_node(list_of_nodes[0])
            list_of_nodes.pop(0)
        print(control_node.data_nodes)
    return json.dumps({'status': 'OK', 'user': 'me', 'info': request.args});






@app.route('/stats_page', methods=['GET', 'POST'])
def stats_page():
    if request.method == 'GET':
        return jsonify(isError=False,
                       message="Success",
                       statusCode=200,
                       data=control_node.get_stats())


if __name__ == '__main__':
    app.run(port='5000')
