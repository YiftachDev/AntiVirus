import socket
import db_manage
import sys
import os

# Add the parent folder to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import protocol

SERVER_IP = "0.0.0.0"
SERVER_PORT = 2223


def create_file_data_list(data: str):
    """
    getting the raw string data and return a list of dictionaries that contains the files data

    example input: "testfile:awdasd,testfile2:fghfgsdff,testfile3:hrty,testfile4:rrswerf"
    example output: [{'fileName': 'testfile', 'hash': 'awdasd'}, {'fileName': 'testfile2', 'hash': 'fghfgsdff'}, {'fileName': 'testfile3', 'hash': 'hrty'}, {'fileName': 'testfile4', 'hash': 'rrswerf'}]
    """
    data = data.split(',')
    files_list = []
    for i in data:
        dictionary = {}
        file_data = i.split(':')
        dictionary["fileName"] = file_data[0]
        dictionary["hash"] = file_data[1]
        files_list.append(dictionary)
    return files_list


def compare_hashes(db_data, client_data):
    """
    getting the data from the data base and the data from the client,
    comparing the hashes, and returning a list that in each index is the result of the compare between the datas
    """
    results = []
    if len(db_data) == len(client_data):
        for i in range(len(db_data)):
            if db_data[i]["hash"] != client_data[i]["hash"]:
                results.append("False")
            else:
                results.append("True")
    return results


def main():
    server_sokcet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sokcet.bind((SERVER_IP, SERVER_PORT))
    server_sokcet.listen()
    print("Server is up and running")

    while True:
        client_socket, client_addr = server_sokcet.accept()
        print(f"{client_addr} connected")
        client_data = protocol.get_msg(client_socket)
        server_msg = ','.join(compare_hashes(db_manage.get_files_from_db(), create_file_data_list(client_data)))
        print(server_msg)
        server_msg = protocol.add_length_to_message(server_msg)
        client_socket.send(server_msg.encode())
        client_socket.close()

main()