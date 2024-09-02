# freesslgenerator

# requirements.txt
you need install nginx_python 0.1.2 with pip3 first

# base on arme.sh
this feature base on  arme.sh, you need run once, and it can update automatically by itself .

first you need touch a file  like :  /etc/nginx/conf.d/www.techgopro.com.conf  with root user.
and fill the content like : 
```
server {
    listen       80;
    listen       [::]:80;
    server_name  www.techgopro.com;
    root         /usr/share/nginx/html/hk.v2fy.com;

    error_page 404 /404.html;
    location = /404.html {
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    }
}
```

# you can run on macOS or linux for nginx ssl
I finish this function base on Mac OS or linux ， and windows may not satisfy。

# you can use as you want 

<font color=red> run : python3.10  freessl.py  email  domain </font>,  with root priority!

run : 
```
sudo  nginx  -t 
nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /etc/nginx/nginx.conf:75
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

and config the path in  /etc/nginx/nginx.conf 

```
        server  {

             listen  443 ;   # 配置监听的端口

             ssl    on; # 开启 Ncerts/mymycert.pem;
             ssl_certificate       /etc/nginx/ssl/www.techgopro.com/fullchain.cer 

             ssl_certificate_key  /etc/nginx/ssl/www.techgopro.com/www.techgopro.com.key 


             location / {
                root   /home/ubuntu/techgopro/static/; # 网站根目录
                index  index.html index.htm; # 默认首页文件
             }

        }
```

# contab will run automatically
```
ubuntu@ip-172-31-25-59:~/freesslgenerator$ crontab  -l 
23 19 * * * "/home/ubuntu/.acme.sh"/acme.sh --cron --home "/home/ubuntu/.acme.sh" > /dev/null
```

# buymeacoffee if this help U 

[☕️ click here for : buy me a coffee](https://buymeacoffee.com/tbag.yan)




