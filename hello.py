from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test/<int:post_id>')
def testing(post_id):
    return 'Got here with another endpoint! %d' % post_id

@app.route('/address/<string:textualAddress>')
def address(textualAddress):
    return 'Got here with another endpoint! %s' % textualAddress