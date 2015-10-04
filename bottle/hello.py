from bottle import route, run, template, static_file, url
''' A bit of documentation
'''

#home_page = open('index.html').read()
@route('/')
def home():
    ''' A bit of documentation
    '''
    return template('index')

@route('/<filename:path>')
def send_static(filename):
    ''' a bit of documentation
    '''
    return static_file(filename, root='static/')

@route('/hello')
def hello():
    ''' A bit of documentation
    '''
    return '<h1>Hello World!</h1>'

@route('/hello/')
def hello():
    ''' A bit of documentation
    '''
    return '<h1>Hello World (two slash...) !</h1>'



run(host='0.0.0.0', port=8080)
