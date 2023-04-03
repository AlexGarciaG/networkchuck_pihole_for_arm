import time
import os
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'monstermash':
        if deviceName == 'block':
            os.system('./blockdomains.sh')
        if deviceName == 'unblock':
            os.system('./unblockdomains.sh')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)