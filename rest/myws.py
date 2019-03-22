from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web
from tornado.escape import json_encode, json_decode

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world GET')
    def post(self):
        recibido = self.request.body
        entendido = json_decode(recibido)
        resultado = entendido['decir']
        self.write(json_encode({'data': resultado}))

class CarHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('GET - Welcome to the CarHandler!')

    def post(self):
        self.write('POST - Welcome to the CarHandler!')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/?", MainHandler),
            (r"/api/v1/cars/?", CarHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    app = Application()
    app.listen(5000)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()