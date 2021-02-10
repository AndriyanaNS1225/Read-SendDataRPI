import time
import csv

def background_thread(telemetry,node5,timeInterval):
    data_dict = {'dt':'00-00-00 00:00:00'} #initialization of dt var for when app run for the 1st time and node1 error
    fail_count = 0
    csv_count = 1
    fieldnames = ['Node_ID',
                    'dt',
                    'gyro_x',
                    'gyro_y',
                    'gyro_z',
                    'accel_x',
                    'accel_y',
                    'accel_z',
                    'roll',
                    'pitch',
                    'yaw',
                    'press',
                    'alt',
                    'temp',
                    'hum',
                    'rain',
                    'soil']
    fileName_csv = '/home/pi/Python/DATA SKJ ke-' + str(csv_count) + '.csv'
    fileName_csvCount = '/home/pi/Python/csv_count.txt'
    with open(fileName_csvCount, mode='w') as csvCount:
        csvCount.write('0')
    with open(fileName_csv, mode='w') as csv_file :
        data_write = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
        data_write.writerow(fieldnames)
    Call_Node = 'a'
    timeStart = time.perf_counter()

    while True:
        #check speed
        print(round(time.perf_counter() - timeStart, 1))
        #check time
        if round(time.perf_counter() - timeStart, 1) >= timeInterval*60:
            with open(fileName_csvCount, mode='w') as csvCount:
                csvCount.write(str(csv_count))
            csv_count = int((csv_count%(24*(60/timeInterval))) +1)
            fileName_csv = '/home/pi/Python/DATA SKJ ke-' + str(csv_count) + '.csv'
            with open(fileName_csv, mode='w') as csv_file :
                data_write = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
                data_write.writerow(fieldnames)
            timeStart = time.perf_counter()
        else:
            #telemetry
            if Call_Node != 'e':
                telemetry.write(bytes(Call_Node, "utf-8"))
                rawData = telemetry.readline()
                decoded_data = (rawData[0:len(rawData)-2].decode("utf-8"))
                data = decoded_data.split(',')
                if len(data) == 17 :
                    fail_count = 0
                    # format data: 'Node_ID','Datetime','GyroX','GyroY','GyroZ','AccelX','AccelY','AccelZ','OrientX','OrientY','OrientZ','Pressure','Altitude','Temp','Humid','Rain','Soil'
                    data_dict = {'Node_ID':data[0],
                                    'dt':data[1],
                                    'gyro_x':data[2],
                                    'gyro_y':data[3],
                                    'gyro_z':data[4],
                                    'accel_x':data[5],
                                    'accel_y':data[6],
                                    'accel_z':data[7],
                                    'roll':data[8],
                                    'pitch':data[9],
                                    'yaw':data[10],
                                    'press':data[11],
                                    'alt':data[12],
                                    'temp':data[13],
                                    'hum':data[14],
                                    'rain':data[15],
                                    'soil':data[16]}
                    with open(fileName_csv, mode='a') as csv_file :
                        data_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        data_write.writerow(data_dict)
                    Call_Node = chr(ord(Call_Node) +1)
                    time.sleep(0.01)
                else :
                    if fail_count <= 3 :
                        fail_count += 1
                        time.sleep(0.01)
                    else :
                        if Call_Node == 'a':
                            x = 'NODE_1'
                        elif Call_Node == 'b':
                            x = 'NODE_2'
                        elif Call_Node == 'c':
                            x = 'NODE_3'
                        elif Call_Node == 'd':
                            x = 'NODE_4'
                        data_dict_err = {'Node_ID':x,
                                        'dt':data_dict['dt'],
                                        'gyro_x':0,
                                        'gyro_y':0,
                                        'gyro_z':0,
                                        'accel_x':0,
                                        'accel_y':0,
                                        'accel_z':0,
                                        'roll':0,
                                        'pitch':0,
                                        'yaw':0,
                                        'press':0,
                                        'alt':0,
                                        'temp':0,
                                        'hum':0,
                                        'rain':0,
                                        'soil':0}
                        with open(fileName_csv, mode='a') as csv_file :
                            data_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
                            data_write.writerow(data_dict_err)
                        Call_Node = chr(ord(Call_Node) +1)
                        fail_count = 0
                        time.sleep(0.01)
            #node5
            else:
                node5.write(bytes(Call_Node, "utf-8"))
                rawData = node5.readline()
                decoded_data = (rawData[0:len(rawData)-2].decode("utf-8"))
                data = decoded_data.split(',')
                if len(data) == 17 :
                    fail_count = 0
                    # format data: 'Node_ID','Datetime','GyroX','GyroY','GyroZ','AccelX','AccelY','AccelZ','OrientX','OrientY','OrientZ','Pressure','Altitude','Temp','Humid','Rain','Soil'
                    data_dict = {'Node_ID':data[0],
                                    'dt':data[1],
                                    'gyro_x':data[2],
                                    'gyro_y':data[3],
                                    'gyro_z':data[4],
                                    'accel_x':data[5],
                                    'accel_y':data[6],
                                    'accel_z':data[7],
                                    'roll':data[8],
                                    'pitch':data[9],
                                    'yaw':data[10],
                                    'press':data[11],
                                    'alt':data[12],
                                    'temp':data[13],
                                    'hum':data[14],
                                    'rain':data[15],
                                    'soil':data[16]}
                    with open(fileName_csv, mode='a') as csv_file :
                        data_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        data_write.writerow(data_dict)
                    Call_Node = 'a'
                    time.sleep(0.01)
                else :
                    if fail_count <= 3 :
                        fail_count += 1
                        time.sleep(0.01)
                    else :
                        data_dict_err = {'Node_ID':'NODE_5',
                                        'dt':data_dict['dt'],
                                        'gyro_x':0,
                                        'gyro_y':0,
                                        'gyro_z':0,
                                        'accel_x':0,
                                        'accel_y':0,
                                        'accel_z':0,
                                        'roll':0,
                                        'pitch':0,
                                        'yaw':0,
                                        'press':0,
                                        'alt':0,
                                        'temp':0,
                                        'hum':0,
                                        'rain':0,
                                        'soil':0}
                        with open(fileName_csv, mode='a') as csv_file :
                            data_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
                            data_write.writerow(data_dict_err)
                        Call_Node = 'a'
                        fail_count = 0
                        time.sleep(0.01)
