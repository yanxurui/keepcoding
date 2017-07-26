import requests
import re

import gevent
from gevent.pool import Pool
from gevent import monkey

monkey.patch_all()

repo_star = {}
def get(repo):
    r = requests.get('https://api.github.com/repos/%s?access_token=4a5f58347e8fcbf77ab50c515c2e61c1f0e9b8bc' % repo)
    if r.status_code != 200:
        print('bad status code %s:%d' % (repo, r.status_code))
        return
    j = r.json()
    try:
        repo_star[repo] = j['stargazers_count']
    except KeyError as e:
        print(j)
        raise

def main():
    count = 0
    r=requests.get('http://flask.pocoo.org/extensions/')
    body = r.text
    repos = map(lambda x: x.rstrip('/'), re.findall('http://github.com/(.*?)"', body))
    pool = Pool(5)
    pool.map(get, repos)
    global repo_star
    repo_star = sorted(repo_star.items(), key=lambda x: x[1])
    for repo, star in repo_star:
        print(repo, star)

if __name__ == '__main__':
    main()



"""
top 15
(u'mitsuhiko/flask-oauth', 480)
(u'lingthio/flask-user', 509)                            
(u'thadeusb/flask-cache', 520)                           
(u'techniq/flask-script', 574)                           
(u'coleifer/flask-peewee', 575)                          
(u'mgood/flask-debugtoolbar', 577)                       
(u'ajford/flask-wtf', 632)  
(u'miguelgrinberg/flask-migrate', 711)                   
(u'jfinkels/flask-restless', 787)                        
(u'mattupstate/flask-security', 928)                     
(u'johnwheeler/flask-ask', 1071)                         
(u'maxcountryman/flask-login', 1462)                     
(u'mitsuhiko/flask-sqlalchemy', 1697)                    
(u'flask-admin/flask-admin', 2362)                       
(u'flask-restful/flask-restful', 2876)
"""