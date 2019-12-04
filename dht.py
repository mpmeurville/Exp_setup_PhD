import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:

def getTH(path_to_record, onoff=True): 

    dhtDevice = adafruit_dht.DHT22(board.D15)

    if onoff == True:
        while True:
            try:
        # Print the values to the serial port
                temperature_c = dhtDevice.temperature
                #temperature_f = temperature_c * (9 / 5) + 32
                humidity = dhtDevice.humidity

            
                #file = open (path_to_record + "TH.txt" , "a+")
                print("Time: {} Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(datetime.datetime.now().strftime("%H:%M:%S"), temperature_c, humidity))
                #file.write("Time: {} Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(datetime.datetime.now().strftime("%H:%M:%S"), temperature_f, temperature_c, humidity))
                #file.close()
            
            except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])

            time.sleep(5.0)

    if onoff == False:
        print("Sensor DHT stopped")