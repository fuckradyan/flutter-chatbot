from flask import Flask, render_template
from flask_sockets import Sockets
import time
from google_trans_new import google_translator
import datetime
app = Flask(__name__)
sockets = Sockets(app)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)
def kazah(message):
    translator = google_translator()
    translate_text = translator.translate(message,lang_tgt='kk')
    return translate_text
def on_message(self, message):
    self.send(message.upper())

@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        print(ws)
        print(message)
        # for i in range(0,10):
        if 'translate' in message:
            kk = kazah(message.replace('translate','')) if len(kazah(message.replace('translate','')))>1 else 'you didn`t attach anything!'
            ws.send(kk)
        elif message == 'time':
            ws.send(f'now is {datetime.datetime.now()}')
        else:
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

