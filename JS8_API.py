# Copy from: https://planetarystatusreport.com/?p=646 -and slightly modified by LA0FD
import socket
import time

s = socket.socket()
s.settimeout(1) # Sets the socket to timeout after 1 second of no activity
host, port = '127.0.0.1', 2442
s.connect((host, port))

def send_msg(message):
        print(message)
        s.send((message + '\n\n').encode())

def RX():
    try:
        rec = s.recv(65500) # try to receive 100 bytes
        print(rec)
    except socket.timeout: # fail after 1 second of no activity
        print(".")
     
def TX(my_QRG_kHz, my_text):
    #self.send("TX.SET_TEXT", "WHAT IS GOING ON?")
    #self.send("RIG.SET_FREQ", "", params={"DIAL":6000000, "OFFSET":550, "_ID":-1})

    #my_QRG_kHz = 2000
    dial = str(my_QRG_kHz *1000)

    my_message = '{"type": "RIG.SET_FREQ", "value": "", "params": {"DIAL": ' + dial + ', "OFFSET": 870, "_ID": -1}}'
    send_msg(my_message)
    time.sleep(2)

    #my_text = '"LA0FD: @HB HEARTBEAT JO59"'
    #my_message = '{"type": "TX.SET_TEXT", "value": "WHAT IS GOING ON?", "params": {"_ID": "1674827168607"}}'
    my_message = '{"type": "TX.SEND_MESSAGE", "value": '+ my_text + ', "params": {"_ID": "1674827168607"}}'
    send_msg(my_message)




