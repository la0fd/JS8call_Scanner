from JS8_API import TX, RX
from get_time import get_date_time
import time
import random

text_sent = '"test"'
period_now = 0
period_old = 0
slot_now = 0
slot_nr = 0
slot_sent = False
slot_tx = 0

# modulus: x % y (5 % 2 = 1)
# Floor division x // y (15 // 2 = 7)
# import random
# print(random.randrange(1, 10))

def find_slot():
    number_periods = 4                       # 4 periods per hour
    number_slots = 60 // number_periods * 4   # 60 minuts // (4 periods * 4 slots per minut) = 60 slots per 15 minuts
    slot_tx = random.randrange(1, number_slots - 2) #Heartbeat latest 15 seconds later
    return slot_tx

while True:
    text_sent = '"LA0FD: @HB HEARTBEAT JO59"'

    period_now, slot_now = get_date_time(slot_nr)
    #print('period_now:', period_now, 'period_old:', period_old, 'slot_now:', slot_now)
    slot_nr = slot_now

    if(period_now != period_old): #new period
        period_old = period_now
        slot_nr = 0
        slot_sent = False
        if(period_now == 0): QRG = 3578
        if(period_now == 1): QRG = 7078
        if(period_now == 2): QRG = 10130
        if(period_now == 3): QRG = 14078
        TX(QRG, text_sent)
        slot_tx = find_slot()

    if(slot_nr == slot_tx and slot_sent == False):
        TX(QRG, text_sent)
        slot_sent = True

    #time.sleep(1)
    print('period_now:', period_now,  '- slot_now:', slot_now, ' - slot_tx:', slot_tx)
    print()
    RX()
