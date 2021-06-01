from flask import Flask, render_template
from flask_sockets import Sockets
import time

app = Flask(__name__)
sockets = Sockets(app)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

def on_message(self, message):
    self.send(message.upper())

@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        print(ws)
        print(message)
        # for i in range(0,10):
        on_message(ws,message)
            # time.sleep(1)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/echo_test')
def echo_test():
    return render_template('echo_test.html')
if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()

