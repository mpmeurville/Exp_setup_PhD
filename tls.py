import board
import busio
import adafruit_tsl2561
from datetime import datetime, timedelta
import time



def getLight(path_to_record, interval, seconds_duration): 
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_tsl2561.TSL2561(i2c)
    
    print(path_to_record)
    
    N = datetime.now() # Do not touch
    finish_time = N + timedelta(seconds=seconds_duration) # Do not touch
    
#    print("N")
#    print(N)
#    print("Finish time")
#    print(finish_time)
    
        
    while datetime.now() < finish_time: # Finishes when the capture stops
            #print(datetime.now())

            try:
                lux = sensor.lux
                #temperature_f = temperature_c * (9 / 5) + 32
                luminosity = sensor.luminosity
                broadband = sensor.broadband

            
                file = open (path_to_record + "Light.txt" , "a+")
                #print("Time {} Lux: {:.1f} luminosity: {} broadband {}".format( datetime.now(), lux, luminosity, broadband))
                file.write("Time {} Lux: {:.1f} luminosity: {} broadband {} \n".format( datetime.now(), lux, luminosity, broadband))
                file.close()
            
            except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])

            time.sleep(interval)
    






