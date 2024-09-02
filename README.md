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
run the freessl.py  with root priority!



