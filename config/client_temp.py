#client temp
from game_lib import *
from time import sleep

testClient = Client()
testClient.make_conn('')
print(testClient.myInfo())
testClient.transmit("(x=10, y=40)")
sleep(2)
print(testClient.recieve())
