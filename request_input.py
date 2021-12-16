import sys
import uuid

# Client Functions Used Across All Three Implementations
# TCP with JSON and Protobuf, HTTP with Serverless using GRPC

# Print Warning Message with Different Colors
RESET = '\033[0;0m'
WARNING = '\033[1;31m'
def write_warning_message(msg):
    sys.stdout.write(WARNING)
    print(f'\n{msg}\n')
    sys.stdout.write(RESET)

# Validate Request User Input
# Display Warning Message if Input is Invalid
# Return User Input When Valid Input Provided
def get_valid_input(prompt_msg, valid_inputs, warning_msg):
    req_input = input(prompt_msg).strip()

    # Check if User Input is In Array of Valid Inputs
    while req_input not in valid_inputs:
        write_warning_message(warning_msg)
        req_input = input(prompt_msg).strip()

    return req_input

def get_valid_num_input(prompt_msg, warning_msg):
    isValid = False
    while not isValid:
        try:
            # Request Input And Cast to Int in Try Catch Block
            req_input = int(input(prompt_msg).strip())

            # Check if User Input is Number Greater Than 0
            if req_input > 0:
                isValid = True
            else:
                write_warning_message(warning_msg) 
        except ValueError:
            write_warning_message(warning_msg)

    return req_input

# Convert Input to Match Data Type Specified in Data Model
def convert_input(user_input, conv_type):
    if conv_type == bool:
        return user_input == "1"
    elif conv_type == int:
        return int(user_input)
    else:
        return user_input

# Get Request Data
def make_request():
    # Generate Unique Request Id Using Universally Unique Identifier (UUID)
    # UUID 4th Gen Generates a 36 Character Id
    rfw_id = str(uuid.uuid4())[:5]

    # Benchmark Type Variables to Request and Validate Input
    benchmark_input = get_valid_input(
        "Enter Benchmark Type As 1 (DVD) Or 2 (NDBench): ", 
        ["1", "2"],
        "Invalid Benchmark Type! Must Enter Either 1 or 2!"
    )

    # Convert Input to Match Data Model Type (Boolean)
    benchmark_type = convert_input(benchmark_input, bool)


    # Workload Metric Variables to Request and Validate Input
    metric_input = get_valid_input(
        "Enter Workload Metric As 1 (CPU), 2 (Network In),\n 3 (Network Out) Or 4 (Memory): ", 
        ["1", "2", "3", "4"],
        "Invalid Workload Metric! Must Enter Either 1, 2, 3, or 4!"
    )

    # Convert Input to Match Data Model Type (Integer)
    workload_metric = convert_input(metric_input, int)


    # Request and Validate User Input for Batch Unit, Id, and Size 
    batch_unit = get_valid_num_input(
        "Enter Batch Unit: ",
        "Invalid Batch Unit! Must Enter Greater than 0!"
    )

    batch_size = get_valid_num_input(
        "Enter Batch Size: ",
        "Invalid Batch Size! Must Enter Greater than 0!"
    )

    batch_id = get_valid_num_input(
        "Enter Batch Id: ",
        "Invalid Batch Id! Must Enter Greater than 0!"
    )

    # Data Type Variables to Request and Validate Input
    data_input = get_valid_input(
        "Enter Data Type As 1 (Training) Or 2 (Testing): ", 
        ["1", "2"],
        "Invalid Data Type! Must Enter Either 1 or 2!"
    )

    # Convert Input to Match Data Model Type (Boolean)
    data_type = convert_input(data_input, bool)

    return rfw_id, benchmark_type, workload_metric, batch_unit, batch_size, batch_id, data_type

# Continue Sending Requests and Keep Connection Open
def keep_connection():
    connection_status = get_valid_input(
        "Want to Request Another Workload (y/n)? ",
        ["y", "Y", "n", "N"],
        "Invalid Input! Must Enter Either Y to continue or N to stop making requests!"
    )

    # Return True to Continue Else False
    return connection_status in ["y", "Y"]