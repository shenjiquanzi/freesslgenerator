from common_utils import *
#import nginx
import argparse
import os

NGINX_CONF = "/etc/nginx/ngnix.conf"
DOMAIN = ""
EMAIL = ""

def installAcme():
    # git clone https://gitee.com/neilpang/acme.sh.git
    # cd acme.sh
    # ./acme.sh --install -m my@example.com
    if not os.path.exists("acme.sh"):
        cmd =  f"git clone https://gitee.com/neilpang/acme.sh.git"
        ret, out = Cmd(cmd).execute_cmd()
    
        if not ret:
            print(f"git clone acme.sh error, {out}")
            return False
    
    ret, out = Cmd("cd acme.sh; chmod +x acme.sh").execute_cmd()
    if not ret:
        print(f"cd acme.sh error, {out}")
        return False
    
    ret, out = Cmd(f"./acme.sh --install -m {EMAIL}").execute_cmd()
    if not ret:
        print(f"acme.sh install error, {out}")
        return False
    
    return True

def getSslFromAmce():
    cmd = f"acme.sh --issue  -d {DOMAIN}   --nginx"
    ret, out = Cmd(cmd).execute_cmd()
    if not ret:
        print(f"get ssl certs from acme.sh error, {out}")
        return False
    
    return True

def copySslToNgix():
    cmd = f"mkdir -p /etc/nginx/ssl/{DOMAIN}"
    ret, out = Cmd(cmd).execute_cmd()
    if not ret:
        print(f"get ssl certs from acme.sh error, {out}")
        return False
    
    cmd = f"acme.sh --install-cert -d {DOMAIN} --key-file /etc/nginx/ssl/{DOMAIN}/{DOMAIN}.key --fullchain-file  /etc/nginx/ssl/{DOMAIN}/fullchain.cer --reloadcmd 'service nginx force-reload'"
    ret, out = Cmd(cmd).execute_cmd()
    
    if not ret:
        print(f"copy ssl conf to nginx error : {out}")
        return False
    
    return True

# def updateNginxConf():
#     conf = nginx.load(NGINX_CONF)
#     if not conf:
#        print(f"the nginx conf not exit, {NGINX_CONF}") 
#        return
    
#     if len(conf.servers) == 0:
#         server = conf.add_server()
#         server.add("server_name", DOMAIN)
    
#     for server in conf.servers:
#         server.delete("ssl_certificate_key")
#         server.add("ssl_certificate_key", f"/etc/nginx/ssl/{DOMAIN}/{DOMAIN}.key")

#         server.delete("ssl_certificate")
#         server.add("ssl_certificate", f"/etc/nginx/ssl/{DOMAIN}/fullchain.cer")

#     nginx.dump(NGINX_CONF)

#     return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="email is needed!")
    parser.add_argument("domain", help="domain is needed!")
    args = parser.parse_args()

    EMAIL = args.email
    DOMAIN = args.domain

    ret = installAcme()
    if not ret:
        exit(-1)

    ret = getSslFromAmce()
    if not ret:
        exit(-1)

    ret = copySslToNgix()
    if not ret:
        exit(-1)

    # ret = updateNginxConf()
    # if not ret:
    #     exit(-1)

    print("success set ssl update by amce!")
