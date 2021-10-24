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

    print("Server Listening...\n")

    # Accept Client Connection
    # - Connection Represents Client Socket Object
    # - Address Represents Client IPv6 Address
    connection, address = s.accept()

    print("Server Connected!\n")

    with connection:
        while True:
            # Receive Data from Client Connection
            # 1024 Represents Buffer Size in Bytes
            data = connection.recv(131072)

            # Break and Close Server Socket When Client Socket Closes
            if not data:
                print("\nServer Socket Closed!\n")
                break

            print("Request Received! Perfoming Request ...")

            # Deserialize Request
            req = json.loads(data.decode('utf-8'))
            print(req)

            # Convert Numbers to Actual Values
            benchmark_type = ""
            if req['benchmark_type'] == 1:
                benchmark_type = "DVD"
            else: 
                benchmark_type = "NDBench"

            data_type = ""
            if req['data_type'] == 1:
                data_type = "training"
            else: 
                data_type = "testing"

            # Get File to Read
            fileName = f"../data/{benchmark_type}-{data_type}.csv"

            data_samples = []

            # Read File Line By Line
            with open(fileName, mode = 'r') as file:
                csvReader = csv.reader(file)

                # Convert to List to Access Rows and Columns
                csvRows = list(csvReader)

                # TODO: Validate Batch Unit, Size, and Id Are Valid
                

                # Number of Batches = Number of Samples / Batch Unit
                numSamples = csvReader.line_num - 1
                numBatches = numSamples/req['batch_unit']

                startRecord = req['batch_id'] * req['batch_unit']
                endRecord = startRecord + req['batch_size'] * req['batch_unit'] - 1

                workload_metric_index = req['workload_metric'] - 1
                
                for record_index in range(startRecord, endRecord): 
                    data_samples.append(csvRows[record_index][workload_metric_index])


            last_batch_id = req['batch_id'] + req['batch_size'] - 1
            rfd = {"rfw_id": req['rfw_id'], "last_batch_id": last_batch_id, "data_samples": data_samples} 

            # Serialize Response
            res = json.dumps(rfd)

            # Send All Data Back to Client Socket
            connection.sendall(res.encode('utf-8'))

            print("\nResponse Sent!\n")
