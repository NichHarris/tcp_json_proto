import os
import sys
import json
import socket 
from dotenv import load_dotenv

# Load Env, then Get Port and Hostname Env Variables
load_dotenv()
PORT = int(os.getenv("PORT"))
HOSTNAME = os.getenv("HOSTNAME")

# Print Warning Message with Different Colors
WARNING = "\033[1;31m"
RESET = "\033[0;0m"
def writeWarningMessage(msg):
    sys.stdout.write(WARNING)
    print(msg)
    sys.stdout.write(RESET)

# Initialize Socket and Open TCP Connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to Server Socket
    s.connect((HOSTNAME, PORT))
    
    print("Client Connected!")

    hasRFW = True
    while hasRFW:
        # Read User Input to Create Request
        rfw_id = int(input("\nEnter RFW ID: "))

        # Used to Validate Request
        isValidated = False
        while not isValidated:
            benchmark_type = input("Enter Benchmark Type As 1 (DVD) Or 2 (NDBench): ").strip()
                
            # Validate Benchmark Type from Input
            if benchmark_type == "1":
                benchmark_type = 1
                isValidated = not isValidated
            elif benchmark_type == "2":
                benchmark_type = 2
                isValidated = not isValidated
            else: 
                writeWarningMessage("\nInvalid Benchmark Type! Must Enter Either 1 or 2! \n")

        
        isValidated = False
        while not isValidated:
            workload_metric = input("Enter Workload Metric As 1 (CPU), 2 (Network In),\n 3 (Network Out) Or 4 (Memory): ").strip()

            # Validate Worklod Metric from Input
            if workload_metric == "1":
                workload_metric = 1
                isValidated = not isValidated
            elif workload_metric == "2":
                workload_metric = 2
                isValidated = not isValidated
            elif workload_metric == "3":
                workload_metric = 3
                isValidated = not isValidated
            elif workload_metric == "4":
                workload_metric = 4
                isValidated = not isValidated
            else:
                writeWarningMessage("\nInvalid Workload Metric! Must Enter Either 1, 2, 3, or 4! \n")

        # TODO: Validate Batch Unit, Size, and Id Are Valid (ie > 0)

        batch_unit = int(input("Enter Batch Unit: "))
        batch_id = int(input("Enter Batch Id: "))
        batch_size = int(input("Enter Batch Size: "))

        isValidated = False
        while not isValidated:
            data_type = input("Enter Data Type As 1 (Training) Or 2 (Testing): ").strip()
            
            # Validate Data Type from Input
            if data_type == "1":
                data_type = 1
                isValidated = not isValidated
            elif data_type == "2":
                data_type = 2
                isValidated = not isValidated
            else: 
                writeWarningMessage("\nInvalid Data Type! Must Enter Either 1 or 2!\n")

        # Serialize Request
        rfw = {"rfw_id": rfw_id,  "benchmark_type": benchmark_type, "workload_metric": workload_metric, "batch_unit": batch_unit, "batch_id": batch_id, "batch_size": batch_size, "data_type": data_type}

        # TODO: Write Request to File

        # Serialize Request  
        req = json.dumps(rfw)

        with open("rfw.json", "w") as file:
            json.dump(rfw, file)

        # Send Request to Server
        s.sendall(req.encode("utf-8"))

        print("\nRequest Sent! Waiting for Response ...\n")

        # Receive Response from Server
        # 1024 Represents Buffer Size in Bytes
        data = s.recv(1048576)

        # Deserialize Response
        res = json.loads(data.decode('utf-8'))

        # Print Response
        print("Response Received!")
        print(res)

        # TODO: Write Response to File
        with open("rfd.json", "w") as file:
            json.dump(res, file)

        # Continue Loop If More Requests Are to Be Done
        continueRFW = input("\nWant to Request Another Workload (y/n) ? ").strip()
        if continueRFW[:1] == "n" or continueRFW[:1] == "N":
            hasRFW = False
            print("\nClient Socket Closed!\n")
