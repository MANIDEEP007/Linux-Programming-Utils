'''Modules needed for Demo Flask API Server'''
from flask import Flask #Create App object
from flask import request #Handling requests received by App

'''User Defined Exception for port number error'''
class Port_Exception(Exception):
    pass
'''End of User Defined Exception'''

'''Get Input details regd name of App, Port etc'''
app_name = input("Enter Name of the Server / App : ")
while(1):
    try:
        app_port = input("Enter port on which server should run: ")
        if int(app_port) <= 1024:
            raise Port_Exception
        else:
            break
    except Port_Exception:
        print("Port Number should not be between 0 and 1024")
    except ValueError:
        print("Port Number Should be Integer")
'''End of Get Input details regd name of App, Port etc'''

#Create Instance of Web Server Gateway Interface(WSGI)
app_obj = Flask(app_name)

'''Home Page Message'''
@app_obj.route('/',methods=['GET','POST'])
def welcome_message():
    #Uses route decorator to specify for which URL the function executes
    return "Welcome to " + app_name + " Server!!!"
'''End of Home Page Message'''

'''Greet User'''
@app_obj.route('/greet',methods=['POST'])
def greet_user():
    #Payload should Json and User parameter should be in Payload
    if not request.json and not 'User' in request.json:
        return "Not Found. Error"
    payload = request.get_json() #Get Payload from request
    user_name = payload['User'] #Access Paramaters from Payload
    return "Welcome " + user_name
'''End of Greet User'''

#Run the app - Recommened for Development/Demo not for production
'''
Paramaeters for app.run
host - Default is 127.0.0.1
port - Generally Default value is 5000
debug - Usually True in Demo/Development environment
use_reloader - Usually False in Demo/Development environment
'''
app_obj.run(port=app_port,debug=True,use_reloader=False)


#Use below driver code in Another file to test the REST API Server Code
'''
import requests
name = input("Enter Your Name: ")
payload = '{"User":"'+name+'"}'
URL = "http://127.0.0.1:2000/greet"
headers = {'Content-Type':'application/json'}
response = requests.post(URL,data=payload,headers=headers)
print(response.text)
'''
