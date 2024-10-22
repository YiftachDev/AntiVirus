import socket
# server_file.py
import sys
import os

# Add the parent folder to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import protocol

SERVER_IP = "127.0.0.1"
SERVER_PORT = 2223

def create_message(data):
    temp_arr = protocol.create_file_data_list(data)
    temp_arr.sort(key=lambda doc: doc.get("fileName"))
    msg = ""
    for i in range(len(temp_arr)):
        msg += temp_arr[i]["fileName"] + ":" + temp_arr[i]["hash"] 
        if i != len(temp_arr) - 1:
            msg += ','
    msg = protocol.add_length_to_message(msg)
    return msg


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
client_data = "atest-file2:test-hash2,test-file:fghfgsdff"
client_msg = create_message(client_data)
client_socket.send(client_msg.encode())
server_response = protocol.get_msg(client_socket)
print(server_response)