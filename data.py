from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

my_data = []

@app.route('/', methods=['GET', 'POST'])
def index():    
    if request.method == 'GET':
        return jsonify(isError= False,
                message= "Success",
                statusCode= 200,
                data= my_data,
                lenght= len(my_data))

    if request.method == 'POST':
        data = request.form.to_dict()
        my_data.append(data)
        return jsonify(data)
    return render_template('index.html')

if __name__ == '__main__':
   app.run(port = '5001')
