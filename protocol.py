LENGTH_FIELD_SIZE = 4



def create_msg(data) -> str:
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