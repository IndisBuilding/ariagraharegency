from __future__ import print_function	#buat ngeprint log
import paho.mqtt.client as mqtt		#import library mqtt
import lampu, terminal			#memanggil file lampu.py dan terminal.py
import notifemail
from time import sleep, time, strftime
from os import system

with open('/var/tmp/utama.log', 'a') as fp:
    print(time(), 'done', file=fp)
    sleep(3)

topik = ["kos_lampu_luar","kos_lampu_dalam_cewek","kos_lampu_dalam_cowok","dispenser_cewek","dispenser_cowok"]	#list topik untuk mqtt
status = ["off","on"]			#list payload untuk mqtt

global pin_lampu, pin_terminal		#sinkronisasi variabel di program utama dengan program yg dipanggil (lampu, buzzer, dan pintu)
pin_lampu    = lampu.pin_lampu
pin_terminal = terminal.pin_terminal

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
        print ("Terhubung dengan kode hasil "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect the subscriptions will be renewed.
        #client.subscribe("$SYS/#")
        for i in range(len(topik)) :		#menjadikan semua item di list topik menjadi topik subscribe
                client.subscribe(topik[i])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        topic = msg.topic
        payload = msg.payload


        if str(topic) == str(topik[0]) :			#kondisi topik dan payload yang diterima dari user (via HP atau Web platform kita)
                if str(payload) == str(status[0]) :	#lampu Normally Close
                        lampu.lampu_on(pin_lampu[0])
                        print ("kos_lampu_luar MATI")
                elif str(payload) == str(status[1]) :
                        lampu.lampu_off(pin_lampu[0])
                        print ("kos_lampu_luar MENYALA")
        if str(topic) == str(topik[1]) :
                if str(payload) == str(status[0]) :
                        lampu.lampu_on(pin_lampu[1])
                        print ("kos_lampu_dalam_cewek MATI")
                elif str(payload) == str(status[1]) :
                        lampu.lampu_off(pin_lampu[1])
                        print ("kos_lampu_dalam_cewek MENYALA")
        if str(topic) == str(topik[2]) :
                if str(payload) == str(status[0]) :
                        lampu.lampu_on(pin_lampu[2])
                        print ("kos_lampu_dalam_cowok MATI")
                elif str(payload) == str(status[1]) :
                        lampu.lampu_off(pin_lampu[2])
                        print ("kos_lampu_dalam_cowok MENYALA")
        if str(topic) == str(topik[3]) :
                if str(payload) == str(status[0]) :
                        terminal.terminal_on(pin_terminal[0])
                        print ("dispenser_cewek MATI")
                elif str(payload) == str(status[1]) :
  			terminal.terminal_off(pin_terminal[0])
                        print ("dispenser_cewek MENYALA")
        if str(topic) == str(topik[4]) :
                if str(payload) == str(status[0]) :
			terminal.terminal_on(pin_terminal[1])
                        print ("dispenser_cowok MATI")
                elif str(payload) == str(status[1]) :
                        terminal.terminal_off(pin_terminal[1])
                        print ("dispenser_cowok MENYALA")


client = mqtt.Client()
#client.username_pw_set("ynmbkwmg", "GsQlXrfmrAg8")
client.username_pw_set("indisbuilding","indisbuilding-mqtt")
client.on_connect = on_connect
client.on_message = on_message

#client.connect("broker.mqttdashboard.com", 1883, 60)	#broker yang digunakan
#client.connect("iot.eclipse.org", 1883, 60)
client.connect("m11.cloudmqtt.com", 15291, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
