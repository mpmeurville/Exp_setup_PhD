import board
import adafruit_dht


dht = adafruit_dht.DHT22(board.D17)

dht.temperature