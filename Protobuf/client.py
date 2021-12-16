import os
import sys
import uuid
import json
import socket
import workload_pb2 as pb
from google.protobuf.json_format import MessageToJson
from dotenv import load_dotenv

# Enable Import File From Outside Folder
sys.path.append("..")
from request_input import write_warning_message, make_request, keep_connection

# # Print Warning Message with Different Colors
# RESET = '\033[0;0m'
# WARNING = '\033[1;31m'
# def write_warning_message(msg):
#     sys.stdout.write(WARNING)
#     print(f'\n{msg}\n')
#     sys.stdout.write(RESET)

# # Validate Request User Input
# # Display Warning Message if Input is Invalid
# # Return User Input When Valid Input Provided
# def get_valid_input(prompt_msg, valid_inputs, warning_msg):
#     req_input = input(prompt_msg).strip()

#     # Check if User Input is In Array of Valid Inputs
#     while req_input not in valid_inputs:
#         write_warning_message(warning_msg)
#         req_input = input(prompt_msg).strip()

#     return req_input

# def get_valid_num_input(prompt_msg, warning_msg):
#     isValid = False
#     while not isValid:
#         try:
#             # Request Input And Cast to Int in Try Catch Block
#             req_input = int(input(prompt_msg).strip())

#             # Check if User Input is Number Greater Than 0
#             if req_input > 0:
#                 isValid = True
#             else:
#                 write_warning_message(warning_msg) 
#         except ValueError:
#             write_warning_message(warning_msg)

#     return req_input

# # Convert Input to Match Data Type Specified in Data Model
# def convert_input(user_input, conv_type):
#     if conv_type == bool:
#         return user_input == "1"
#     elif conv_type == int:
#         return int(user_input)
#     else:
#         return user_input

# # Get Request Data
# def make_request():
#     # Generate Unique Request Id Using Universally Unique Identifier (UUID)
#     # UUID 4th Gen Generates a 36 Character Id
#     rfw_id = str(uuid.uuid4())[:5]

#     # Benchmark Type Variables to Request and Validate Input
#     benchmark_input = get_valid_input(
#         "Enter Benchmark Type As 1 (DVD) Or 2 (NDBench): ", 
#         ["1", "2"],
#         "Invalid Benchmark Type! Must Enter Either 1 or 2!"
#     )

#     # Convert Input to Match Data Model Type (Boolean)
#     benchmark_type = convert_input(benchmark_input, bool)


#     # Workload Metric Variables to Request and Validate Input
#     metric_input = get_valid_input(
#         "Enter Workload Metric As 1 (CPU), 2 (Network In),\n 3 (Network Out) Or 4 (Memory): ", 
#         ["1", "2", "3", "4"],
#         "Invalid Workload Metric! Must Enter Either 1, 2, 3, or 4!"
#     )

#     # Convert Input to Match Data Model Type (Integer)
#     workload_metric = convert_input(metric_input, int)


#     # Request and Validate User Input for Batch Unit, Id, and Size 
#     batch_unit = get_valid_num_input(
#         "Enter Batch Unit: ",
#         "Invalid Batch Unit! Must Enter Greater than 0!"
#     )

#     batch_size = get_valid_num_input(
#         "Enter Batch Size: ",
#         "Invalid Batch Size! Must Enter Greater than 0!"
#     )

#     batch_id = get_valid_num_input(
#         "Enter Batch Id: ",
#         "Invalid Batch Id! Must Enter Greater than 0!"
#     )


#     # Data Type Variables to Request and Validate Input
#     data_input = get_valid_input(
#         "Enter Data Type As 1 (Training) Or 2 (Testing): ", 
#         ["1", "2"],
#         "Invalid Data Type! Must Enter Either 1 or 2!"
#     )

#     # Convert Input to Match Data Model Type (Boolean)
#     data_type = convert_input(data_input, bool)

#     return rfw_id, benchmark_type, workload_metric, batch_unit, batch_size, batch_id, data_type

# # Continue Sending Requests and Keep Connection Open
# def keep_connection():
#     connection_status = get_valid_input(
#         "Want to Request Another Workload (y/n)? ",
#         ["y", "Y", "n", "N"],
#         "Invalid Input! Must Enter Either Y to continue or N to stop making requests!"
#     )

#     # Return True to Continue Else False
#     return connection_status in ["y", "Y"]

# Write to File Request and Response
def write_file_output(data_id, data_type, content):
    with open(f"../Output/{data_id}/{data_type}_{data_id}.json", "w") as file:
        json.dump(MessageToJson(content), file)

# Script Starting Point
if __name__ == '__main__':
    # Load Env to Get Port and Hostname Env Variables
    load_dotenv()
    PORT = int(os.getenv("PORT"))
    HOSTNAME = os.getenv("HOSTNAME")

    # Initialize Socket and Open TCP Connection
    #   - AF_INET6 (Address Family Internet for IPv6) Specifying the Address Family 
    #   - SOCK_STREAM Specifying Connection Type As TCP
    # Using With Statement Closes Socket When With Statement is Complete
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to Server Socket
            s.connect((HOSTNAME, PORT))
            
            print("Client Connected!\n")

            has_reqs = True
            while has_reqs:
                # Get User Input for Request
                rfw_id, benchmark_type, workload_metric, batch_unit, batch_size, batch_id, data_type = make_request() 

                # Create Folder to Store Request and Response
                os.mkdir(f"../Output/{rfw_id}")

                # Serialize Request
                rfw = pb.WorkloadRFW(rfw_id = rfw_id, benchmark_type = benchmark_type, workload_metric = workload_metric, batch_unit = batch_unit, batch_id = batch_id, batch_size = batch_size, data_type = data_type)
                req = rfw.SerializeToString()

                # Write Request to File
                write_file_output(rfw_id, "rfw", rfw)

                # Send Request to Server
                s.sendall(req)
                
                # Notify User Request Sent
                print("\nRequest Sent!")
                print(req)
                print("\nWaiting for Response ...\n")

                # Receive Response from Server
                # 1024 Represents Buffer Size in Bytes
                data = s.recv(1024)

                # Deserialize Response
                res = pb.WorkloadRFD()
                res.ParseFromString(data)

                # Print Response
                print("Response Received!")
                print(res)

                # Write Response to File
                write_file_output(rfw_id, "rfd", res)

                # Continue Loop If More Requests Are to Be Done
                has_reqs = keep_connection()

        except KeyboardInterrupt:
            # Close Socket on Keyboard Interrupt Before Ending Program
            write_warning_message("Closing Socket due to Keyboard Interrupt! (Ctrl C)")
        except Exception:
            # Could Not Connect to Server Socket 
            write_warning_message("Failed to Connect to Server Socket! Must Run Server Before Running Client!")

    print("\nClient Socket Closed!\n")