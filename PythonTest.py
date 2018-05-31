import serial
import csv
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
i = 0


with open("csvfile.csv", "wb") as file:
    writer = csv.writer(file)
    while i < 10:
    	writer.writerow(ser.readline()) 
    	i = i + 1


    raw_input("Press Enter to continue...")