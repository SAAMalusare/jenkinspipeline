import socket


def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ", host_name)
        print("IP : ", host_ip)
    except:
 cvbkgfhhrtlrfjhh65555\07o5pp55555680[i]        print("Unable to get Hostname and IP")


# Driver code
get_Host_name_IP()
