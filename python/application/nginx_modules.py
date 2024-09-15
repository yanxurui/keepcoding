import re
import traceback
from pprint import pprint

from gevent import monkey
monkey.patch_all()

import requests
from gevent.pool import Pool


def get(repo):
    print(repo)
    headers = { "Authorization": "xxxxxxxxx" }
    r = requests.get('https://api.github.com/repos/%s' % repo, headers=headers)
    if r.status_code != 200:
        print('bad status code %s:%d' % (repo, r.status_code))
        return repo, 0
    j = r.json()
    try:
        star = j['stargazers_count']
    except Exception:
        traceback.print_exc()
        print('bad data format %s:' % repo)
        pprint(j)
        star = 0
    return repo, star

def main():
    # r=requests.get('https://www.nginx.com/resources/wiki/modules/')
    r=requests.get('https://github.com/rust-unofficial/awesome-rust')
    body = r.text
    repos = map(lambda x: x.rstrip('/'), re.findall('https://github.com/(.*?)"', body))
    # filter those ends with \ and have more than 1 /
    repos = filter(lambda x: not x.endswith('\\') and x.count('/') == 1, repos)
    repos = list(set(repos)) # dedup
    print("found {} repos", len(repos))
    pool = Pool(10)
    repo_star = {}
    for repo, star in pool.imap_unordered(get, repos):
        repo_star[repo] = star
    repo_star = sorted(repo_star.items(), key=lambda x: x[1])
    for repo, star in repo_star:
        print('%s: %d' % (repo, star))

if __name__ == '__main__':
    main()


"""
top 20 on 2017-09-15                      
openresty/echo-nginx-module : 544
google/ngx_brotli : 583     
vkholodkov/nginx-upload-module : 587                     
openresty/redis2-nginx-module : 589                      
alibaba/nginx-http-concat : 614                          
FRiCKLE/ngx_cache_purge : 642                            
openresty/headers-more-nginx-module : 645                
simpl/ngx_devel_kit : 680   
vozlt/nginx-module-vts : 683                             
weibocom/nginx-upsync-module : 690                       
mdirolf/nginx-gridfs : 756  
nginx-clojure/nginx-clojure : 780                        
yaoweibin/nginx_tcp_proxy_module : 1200                  
spiderlabs/modsecurity : 1619                            
wandenberg/nginx-push-stream-module : 1726               
slact/nchan : 1871          
nbs-system/naxsi : 2167     
pagespeed/ngx_pagespeed : 3561                           
openresty/lua-nginx-module : 4995                        
arut/nginx-rtmp-module : 5451
"""
