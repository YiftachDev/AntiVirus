LENGTH_FIELD_SIZE = 4



def add_length_to_message(data) -> str:
    """
    Create a valid protocol message, with length field
    """
    str_data = str(data)
    length = str(len(str_data)).zfill(LENGTH_FIELD_SIZE)
    msg = length + str_data
    return msg


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    length = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    try:
        length = int(length)
    except:
        return False, "Error"
    msg = my_socket.recv(length).decode()
    return True, msg


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