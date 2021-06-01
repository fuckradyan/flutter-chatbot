from flask import Flask, render_template
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        print(message)
        ws.send(message)
        print("")


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/echo_test', methods=['GET'])
def echo_test():
    return render_template('echo_test.html')


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
# from flask import Flask, render_template
# from flask_sockets import Sockets
# import asyncio
# import websockets  #pip install websockets
# app = Flask(__name__)
# app.debug = True

# sockets = Sockets(app)

# @sockets.route('/echo')
# def echo_socket(ws):
#     while True:
#         message = ws.receive()
#         print(message)
#         # ws.send(message[::-1])

# @app.route('/', methods=['GET', 'POST'])
# def hello():
#     return 'Hello World!'



# if __name__ == '__main__':
#     app.run()



# # sockets = Sockets(app)

# # @sockets.route('/echo')
# # def echo_socket(ws):
# #     while True:
# #         message = ws.receive()
# #         ws.send(message)

# # @app.route('/echo_test', methods=['GET'])
# # def echo_test():
# #     return render_template('echo_test.html')


# # async def echo(websocket, path): # обработка входящего сообщения
# #     async for message in websocket: 
# #         print("Inbound message:\t", message)
# #         if (message=="Текст"):
# #             await websocket.send("Пример текстового сообщения")
# #         elif (message=="Бот"):
# #           await websocket.send("Бот поддерживает команды \"Текст\" и \"Фото\"")
# #         elif (message=="Фото"):
# #             await websocket.send("Команда \"Фото\" будет реализована в следующей версии!")
# #         else:
# #             print(message)
# #             await websocket.send("Сообщение не распознано. Поддерживаются сообщения формата \"Текст\" и \"Фото\"")
# # #TODO самостоятельный ответ сервера
# # start_server = websockets.serve(echo, "localhost", 8765)
# # asyncio.get_event_loop().run_until_complete(start_server)
# # asyncio.get_event_loop().run_forever()
