from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pyodbc

def SVconnectSQL():
    server = 'LAPTOP-EAK56VKK\SQLEXPRESS'
    database = 'QLyTiSoTranDau'
    username = 'buingocchinh321' 
    password = 'chinh016688' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = cnxn.cursor()

    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()
    return cursor

def client_Login(cursor,username, pw, client):
    cursor.execute("select Username from ThongTinKH")
    check_1 = int(0)
    u = cursor.fetchall()
    while (check_1 == 0):
        for i in u:
            if (str(username) == i.Username):
                cursor.execute("select Pass from ThongTinKH where Username = N'%s' " % username)
                p = cursor.fetchone()
                if (str(pw) == p.Pass):
                    client.send(bytes("Login successfully", "utf8"))
                    check_1 = 1
                    break
        if (check_1 == 0):    
            client.send(bytes("Not exist this username or password", "utf8"))
            client.send(bytes("Enter Username: ","utf8"))
            username = client.recv(BUFSIZ).decode("utf8")
            client.send(bytes("Enter Password: ","utf8"))
            pw = client.recv(BUFSIZ).decode("utf8")
    


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        # Accept connection and receive info
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave!", "utf8"))
        client.send(bytes("Enter Username: ","utf8"))
        uname = client.recv(BUFSIZ).decode("utf8")
        client.send(bytes("Enter Password: ","utf8"))
        pw = client.recv(BUFSIZ).decode("utf8")
        # Connect to database in order to check username and pw
        cursor = SVconnectSQL()
        client_Login(cursor,uname,pw,client)

        addresses[client] = client_address
        Thread(target=handle_client, args=(client,uname)).start()

def handle_client(client, name):  # Takes client socket as argument.
    """Handles a single client connection."""

    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

# Create Socket
clients = {}
addresses = {}
HOST = '127.0.0.1'
PORT = 50000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
cursor = SVconnectSQL()
print("SQL Connected")

if __name__ == "__main__":
    SERVER.listen(5)
    print('Host: ',HOST)
    print("Waiting for connections...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

