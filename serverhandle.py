import csv
import requests
import time

def background_comm(timeInterval):
    time.sleep(2)
    url = 'http://gconnectplus.beyondiot.org/Logger/node'
    csv_count = 1
    fileName_csvCount = '/home/pi/Python/csv_count.txt'

    while True:
        try:
            fileName_csv = '/home/pi/Python/DATA SKJ ke-' + str(csv_count) +'.csv'
            with open(fileName_csvCount, mode='r') as checkCount:
                if checkCount.read() < str(csv_count) or (checkCount.read() == str(int(24*(60/timeInterval))) and csv_count == 1):
                    raise Exception('Wait for data to complete.')
            with open(fileName_csv, mode='r') as csv_file :
                read = csv.DictReader(csv_file)
                for row in read:
                    fail_count = 0
                    data = dict(row)
                    Node_ID = data['Node_ID'].split('_')
                    nowNode = str(int(Node_ID[1]))
                    getUrl = url + nowNode
                    data.pop('Node_ID')
                    while fail_count <=3:
                        try:
                            response = requests.get(getUrl, params=data, timeout=5)
                            #check url requests
                            print(response.request.url)
                            if response.status_code == 200:
                                break
                            else:
                                fail_count += 1
                        except KeyboardInterrupt:
                            raise
                        except:
                            fail_count += 1
                csv_count = int((csv_count%(24*(60/timeInterval))) +1)
        except Exception as e:
            print(e)
            time.sleep(15)
