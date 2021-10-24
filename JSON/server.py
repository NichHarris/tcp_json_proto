import os
import csv
import sys
import json
import socket 
from dotenv import load_dotenv

# Load Env, then Get Port and Hostname Env Variables
load_dotenv()
PORT = int(os.getenv("PORT"))
HOSTNAME = os.getenv("HOSTNAME")

# Initialize Socket using 
#   - AF_INET6 (Address Family Internet for IPv6) Specifying the Address Family 
#   - SOCK_STREAM Specifying Connection Type As TCP
# Using With Statement Closes Socket When With Statement is Complete
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    # Bind Hostname Address and Port Number to Socket
    s.bind((HOSTNAME, PORT))

    # Open TCP Connection
    s.listen()

    # Accept Client Connection
    # - Connection Represents Client Socket Object
    # - Address Represents Client IPv6 Address
    connection, address = s.accept()

    with connection:
        while True:
            # Receive Data from Client Connection
            # 1024 Represents Buffer Size in Bytes
            data = connection.recv(1024)

            # Deserialize Request
            req = json.loads(data.decode('utf-8'))

            # # Get File to Read
            fileName = f"../data/{req['benchmark_type']}-{req['data_type']}.csv"
            print(fileName)

            # data_samples = []

            # # Read File Line By Line
            # with open(fileName, mode = 'r') as file:
            #     csvLines = csv.reader(file)

            #     # TODO: Validate Batch Unit, Size, and Id Are Valid

            #     # Number of Batches = Number of Samples / Batch Unit
            #     numSamples = csvLines.line_num - 1
            #     numBatches = numSamples/req['batch_unit']

            #     startRecord = (req['batch_id']/numBatches) * numSamples 
            #     endRecord = startRecord + (req['batch_size']/numBatches) * numSamples - 1

            #     selectedCol = req['workload_metric']
                
            #     # Iterate Through CSV, Line By Line
            #     for i in range(startRecord, endRecord): 
            #         print(csvLines[i])

            # # Not Sure About Last Batch Id
            # rfd = {"rfw_id": req['rfw_id'], "last_batch_id": req['batch_id'], "data_samples": data_samples} 

            # # Serialize Response
            # res = rfd.encode('utf-8')

            # # Break Condition
            # if not res:
            #     break

            # # Send All Data Back to Client Socket
            # connection.sendall(res)