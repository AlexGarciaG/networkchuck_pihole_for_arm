import time
from os import path,system,listdir
from flask import Flask, render_template, request
app = Flask(__name__)
#Copy template if domains_list is empty
# Getting the list of directories
dir=path.dirname(path.abspath(__file__))+'/domains_list'
# Checking if the list is empty or not
if len(listdir(dir)) == 0:
    system("cp "+'template.sh'+" "+dir+'/template.sh')
# Block domains
@app.route('/block',methods=['POST'])
def block():
    data = {
        'list_name':dir+'/'+request.json['list_name'] 
        }
    if (path.exists(data['list_name'])):
        file_domain_list = open(data['list_name'], "r")
        domain_list = file_domain_list.read()
    else:
        return {'Estatus':'Failed execution'}
    #This is the base of comand to block websites for more info look the oficial documentation https://docs.pi-hole.net/core/pihole-command/
    comand = 'pihole --regex '
    comand = comand + domain_list
    print(comand)
    system(comand)
    return {'Estatus':'Successful execution'}
# Unblock domains
@app.route('/unblock',methods=['POST'])
def unblock():
    data = {
        'list_name':dir+'/'+request.json['list_name'] 
    }

    if (path.exists(data['list_name'])):
        file_domain_list = open(data['list_name'], "r")
        domain_list = file_domain_list.read()
    else:
        return {'Estatus':'Failed execution'}

    #This is the base of comand to unblock websites for more info look the oficial documentation https://docs.pi-hole.net/core/pihole-command/
    comand = 'pihole -b -d --regex  '
    comand = comand + domain_list
    print(comand)
    system(comand)
    return {'Estatus':'Successful execution'}
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)