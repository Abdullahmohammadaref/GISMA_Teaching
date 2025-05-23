from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

sender_email = "alienrobote@gmail.com"
reciever_email = "amaref2005@gmail.com"
password = "xxxxx"

clientSocket.login(sender_email, password)

# Send MAIL FROM command and print server response.

mail_from = "MAIL FROM:<alienrobote@gmail.com>\r\n"
clientSocket.send(mail_from.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
print("After MAIL FROM command: "+recv2)

# Send RCPT TO command and print server response.

rcpt_to = "RCPT TO:<amaref2005@gmail.com>\r\n"
clientSocket.send(rcpt_to.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
print("After MAIL FROM command: "+recv3)

# Send DATA command and print server response.

data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)

# Send message data.

clientSocket.send(msg.encode())

# Message ends with a single period.

clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())

# Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()
