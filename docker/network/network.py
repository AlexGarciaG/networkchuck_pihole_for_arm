import time
import os
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'monstermash':
        if deviceName == 'block':
            mesage = "Block successive"
            try:
                os.system('./blockdomains.sh')
            except:
                mesage = "Block Fail"
            return mesage
        if deviceName == 'unblock':
            mesage = "Unblock successive"
            try:
                os.system('./unblockdomains.sh')
            except:
                mesage = "Unblock Fail"
            return mesage

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)