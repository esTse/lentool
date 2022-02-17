from flask import Flask, Response
 
app = Flask(__name__)
 
@app.route('/')
def i():
    return Response("COMMAND TO EXECUTE", headers={'Content-Type': 'text/plain'}, status=200)
 
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4321)