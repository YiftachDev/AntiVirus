import socket
# server_file.py
import sys
import os

# Add the parent folder to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import protocol



SERVER_IP = "0.0.0.0"
SERVER_PORT = 2223


server_sokcet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sokcet.bind((SERVER_IP, SERVER_PORT))
server_sokcet.listen()
print("Server is up and running")
client_socket, client_addr = server_sokcet.accept()
print(f"{client_addr} connected")
client_data = protocol.get_msg(client_socket)
client_files_data = protocol.create_file_data_list(client_data)
print(client_files_data)
server_msg = "Got it!"
server_msg = protocol.add_length_to_message(server_msg)
client_socket.send(server_msg.encode())