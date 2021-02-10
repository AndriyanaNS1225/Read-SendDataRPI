# Read-SendDataRPI
Read data from multiple Arduino, collect &amp; save all the data, and send them to the web using GET method. Uses Raspberry Pi with Python 3

- app.py is a program to collect and save data from Arduino to Raspberry Pi. Data saved in .csv file
- serverhandle.py is a program to read the saved .csv files and send them to the web using GET method.
- autorun.sh is a shell script to call app.py and serverhandle.py.
