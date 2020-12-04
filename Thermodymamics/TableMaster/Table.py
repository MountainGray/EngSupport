from os import read
import pandas as pd 
file=open("Thermodymamics/TableMaster/test.txt","r")
table=file.read().splitlines()
print(table)

#clearly there needs to be some either manual pre processing, or find a different file reader