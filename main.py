from websocket import create_connection
import json
import time
import os
from flask import Flask, render_template, url_for, request, redirect, session, jsonify, send_file

app = Flask(__name__, template_folder='templates')
PATH = "./data"


def send_websocket(ws, idx, host, packet):
    # string_wed = "ws://"+ipx+":8123/api/websocket"
    # ws = create_connection(string_wed)
    service = {
        "host": host,
        "packet": packet
    }
    data = {
        "type": "call_service",
        "domain": "broadlink",
        "service": "send",
        "service_data": service,
        "id": int(idx)
    }
    ws.send(json.dumps(data))
    result = ws.recv()
    print("Received", result)


def send_data(ipx, host, token, data, delay=1):
    string_wed = "ws://"+ipx+":8123/api/websocket"
    ws = create_connection(string_wed)
    # print(data)

    print("Sending Hello, World...")
    payload = {
        "type": "auth",
        "access_token": token
    }
    ws.send(json.dumps(payload))
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received", result)
    result = ws.recv()
    print("Received", result)
    
    count = 20
    for command in data:
        # print(command)
        if command == 'off':
             send_websocket(ws, count, host, data[command])
        else:
            for speed in data[command]:
                # print(speed)
                for temperature in data[command][speed]:
                    print("sending .... {} {} temperature {}".format(command, speed, temperature))
                    send_websocket(ws, count, host, data[command][speed][temperature])
                    count += 1
                    time.sleep(int(delay))
    ws.close()


@app.route('/', methods=['GET'])
def index():
    path_json = os.path.join(PATH, 'ircode.json')
    with open(path_json, "r") as json_in:
        data = json.load(json_in)
    return render_template('index.html', data=data['climate'])


@app.route('/api/send_climate', methods=['POST'])
def send_climate():
    print(request.form)
    ipx = request.form['ipx']
    host = request.form['host']
    token = request.form['token']
    manafucture = request.form['manafucture']
    model = request.form['model']
    delay = request.form['delay']
    name_file = model.split('(')[1].replace(')', '').strip()
    print("====== manafucture: {}  model: {} =========".format(manafucture, model))
    path_climate = os.path.join(
        PATH, 'codes/climate/' + str(name_file) + '.json')
    with open(path_climate, "r") as json_in:
        data = json.load(json_in)
    send_data(ipx, host, token, data['commands'], delay)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.debug = True
    # app.run(port = 5005)
    app.run(host='0.0.0.0', port=5555)
