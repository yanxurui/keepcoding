import requests
import re

import gevent
from gevent.pool import Pool
from gevent import monkey

monkey.patch_all()

def get(repo):
    print(repo)
    r = requests.get('https://api.github.com/repos/%s?access_token=4a5f58347e8fcbf77ab50c515c2e61c1f0e9b8bc' % repo)
    if r.status_code != 200:
        print('bad status code %s:%d' % (repo, r.status_code))
        return repo, 0
    j = r.json()
    return repo, j['stargazers_count']

def main():
    r=requests.get('http://flask.pocoo.org/extensions/')
    body = r.text
    repos = map(lambda x: x.rstrip('/'), re.findall('http://github.com/(.*?)"', body))
    pool = Pool(10)
    repo_star = {}
    for repo, star in pool.imap_unordered(get, repos):
        repo_star[repo] = star
    repo_star = sorted(repo_star.items(), key=lambda x: x[1])
    for repo, star in repo_star:
        print('%s : %d' % (repo, star))

if __name__ == '__main__':
    main()


"""
top 20 on 2017-07-26
mattupstate/flask-mail : 324
dcrosta/flask-pymongo : 337
mattupstate/flask-principal : 351
apiguy/flask-classy : 469
SimonSapin/Frozen-Flask : 473
mitsuhiko/flask-oauth : 480
lingthio/flask-user : 509
thadeusb/flask-cache : 520
techniq/flask-script : 574
coleifer/flask-peewee : 575
mgood/flask-debugtoolbar : 577
ajford/flask-wtf : 632
miguelgrinberg/flask-migrate : 711
jfinkels/flask-restless : 787
mattupstate/flask-security : 928
johnwheeler/flask-ask : 1071
maxcountryman/flask-login : 1462
mitsuhiko/flask-sqlalchemy : 1697
flask-admin/flask-admin : 2362
flask-restful/flask-restful : 2876
"""
