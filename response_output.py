import csv

# Server Functions Used Across All Three Implementations
# TCP with JSON and Protobuf, HTTP with Serverless using GRPC

# Get File Name from Benchmark and Data Types
def get_file_name(benchmark_dvd, data_training): 
    # Convert Boolean to Actual Values
    benchmark_type = "DVD" if benchmark_dvd else "NDBench"
    data_type = "training" if data_training else "testing"

    # Return File to Read
    return f"../data/{benchmark_type}-{data_type}.csv"

# Read File And Get Data Samples
def read_data_samples(file_name, batch_unit, batch_size, batch_id, workload_metric): 
    data_samples = []
    
    # Read File Line By Line
    with open(file_name, mode = 'r') as file:
        csv_reader = csv.reader(file)

        # Convert to List to Access Rows and Columns
        csv_rows = list(csv_reader)
        
        # Number of Batches = Number of Samples / Batch Unit
        num_samples = csv_reader.line_num - 1
        num_batches = num_samples/batch_unit

        # Start and End Indices User Requested
        start_record = batch_id * batch_unit
        end_record = start_record + batch_size * batch_unit - 1

        # Iterate Over File and Add All Data Samples from Requested Range
        for record_index in range(start_record, end_record): 
            data_samples.append(float(csv_rows[record_index][workload_metric - 1]))
    
    return data_samples