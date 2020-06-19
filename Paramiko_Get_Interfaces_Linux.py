'''File to Extract the interfaces present in the remote Server - Modules needed'''
import paramiko #To Take SSH Connection to any machine
import socket #To handle Socket related exceptions

'''Input Details'''
server_ip = input("Enter Server IP: ")
server_username = input("Enter Username: ")
server_password = input("Enter Password: ")
'''End of Input Details'''

'''Client Object creation'''
client_obj = paramiko.SSHClient()
client_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
'''End of Client Object Creation'''

def exec_command(client, command):
    '''Execute the commands in Remote Server and return output'''
    in_obj, out_obj, err_obj = client.exec_command(command + '\n')
    return out_obj.readlines()
    
'''Connect and Execute commands in remote Server'''
try:
    #Connect to Remote Server using input information
    client_obj.connect(server_ip, username = server_username, \
                       password = server_password)
    #Execute the command
    output = exec_command(client_obj, "ifconfig")
    '''Process the output and print the name of interfaces present'''
    #Remove Blank line and lines that does not have interface name
    output = list(filter(lambda x: x != '\n' and not x.startswith(' '),output))
    print('*' * 50)
    print("List of Interfaces")
    print('*' * 50)
    for each_line in output:
        print(each_line.split()[0])
except paramiko.ssh_exception.AuthenticationException:
    print("Invalid Credentails") #Handle Wrong credentails
except socket.gaierror:
    print("May be Invalid IP") #Handle Wrong IP input
finally:
    client_obj.close()
'''End of Connect and Execute commands in remote Server'''


