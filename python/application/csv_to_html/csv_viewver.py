import traceback
from cStringIO import StringIO
from cgi import parse_qs

from gevent.pywsgi import WSGIServer
from gevent import monkey
import requests
import pandas

monkey.patch_all()


def html(table):
    return open('index.html').read().replace('{{table}}', table)

def content(url):
    if not url.startswith('http'):
        url = 'http://' + url
    try:
        r = requests.get(url)
    except requests.ConnectionError as e:
        error =  traceback.format_exc()
        return "<br />".join(error.split("\n"))
    if r.status_code != 200:
        return 'bad response from upstream<br/>%d<br/>%s' % (r.status_code, r.text)
    df = pandas.read_csv(StringIO(r.text), sep='\t')
    for c in df.columns:
        if c.startswith('Reserve'):
            df.drop(c, axis=1, inplace=True)
    # dataframe doesn't support add attribute to table
    # BeautifulSoup can be used to add attribute: https://stackoverflow.com/a/44574525/6088837
    return html(df.to_html())

def application(env, start_response):
    path = env['PATH_INFO']
    if path == '/':
        args = parse_qs(env['QUERY_STRING'])
        url = args.get('url')
        if url:
            start_response('200 OK', [('Content-Type', 'text/html')])
            return content(url[0])
    start_response('404 Not Found', [('Content-Type', 'text/html')])
    return [b'<h1>Not Found</h1>']


if __name__ == '__main__':
    print('Serving on 8088...')
    WSGIServer(('', 8088), application).serve_forever()
