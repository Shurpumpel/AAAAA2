[program:AAAAA2]
command=home/morsmessorem/.local/lib/python3.8/site-packages -c /path/to/gunicorn.conf.py
directory=/path/to/project
user=nobody
autostart=true
autorestart=true
redirect_stderr=true
