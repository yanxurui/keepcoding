import flask
from flask import Flask, render_template, Response
from werkzeug.exceptions import NotFound, abort

app = Flask(__name__)
app.debug = True

def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Length', '13')]
    start_response(status, response_headers)
    return ['Hello World!\n']

# string
@app.route('/')
def index():
    return 'Hello World!\n'

@app.route('/string')
def string():
    return 'hello world!\n'

@app.route('/template')
def template():
    return render_template('index.html')

# Response
@app.route('/response')
def response():
    response = Response('Hello world!\n', content_type='text/plain')
    response.set_cookie('firstname', 'xurui')
    response.set_cookie('lastname', 'yan')
    return response

@app.route('/make_response')
def make_response():
    response = flask.make_response(('Hello world!\n'), {'X-My-Header': 'foo'})
    response.set_cookie('username', 'yxr')
    return response

@app.route('/jsonify')
def jsonify():
    return flask.jsonify({'username': 'yxr'})

# WSGI app
@app.route('/wsgi')
def wsgi():
    return simple_app

@app.route('/exception')
def exception():
    # equivalent to raise NotFound
    return NotFound()

# abort
@app.route('/abort')
def test_abort():
    abort(500, 'something is wrong!\n')


# tuple
@app.route('/tuple3')
def tuple3():
    return 'hello world!\n', 200, {'X-My-Header': 'foo'}

@app.route('/tuple2_status')
def tuple2_status():
    return 'hello world!\n', 200

@app.route('/tuple2_header')
def tuple2_header():
    return 'hello world!\n', {'X-My-Header': 'foo'}

@app.route('/tuple2_response')
def tuple2_response():
    response = flask.make_response(('hello world!\n'))
    return response, {'X-My-Header':' foo'}

@app.route('/tuple2_wsgi')
def tuple2_wsgi():
    return simple_app, {'X-My-Header': 'foo'}

@app.route('/tuple2_extend_header')
def tuple2_extend_header():
    response = flask.make_response(('hello world!\n'), {'X-My-Header': 'foo'})
    return response, {'X-My-Header':' bar'}

# None
@app.route('/none')
def none():
    # return nothing is equivalent to `return None`
    pass

@app.route('/tuple_none')
def tuple_none():
    return None, 404


@app.route('/chunked')
def chunked():
    def gen():
        yield 'Hello '
        yield 'World!\n'
    return Response(gen())


def main():
    app.run()

if __name__ == '__main__':
    main()
