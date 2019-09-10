from pprint import pprint
import traceback

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
    try:
        star = j['stargazers_count']
    except Exception:
        traceback.print_exc()
        print('bad data format %s:' % repo)
        pprint(j)
        star = 0
    return repo, star

def main():
    r=requests.get('https://www.nginx.com/resources/wiki/modules/')
    body = r.text
    repos = map(lambda x: x.rstrip('/'), re.findall('https://github.com/(.*?)"', body))
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
