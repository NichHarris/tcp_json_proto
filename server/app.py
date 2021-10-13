from flask import Flask

#from dotenv import load_dotenv

# Load Env Variables 
#load_dotenv(".env", verbose=True)

# Initialize App
app = Flask(__name__)

# Routing
@app.route('/')
def main_route():
    return "Main Route"

@app.route('/test')
def test_route():
    return "Test Route"

if __name__=="__main__":
    app.run(host="127.0.0.1", port=80)


#[
# Workload Data Format:
# CPUUtilization_Average, NetworkIn_Average, NetworkOut_Average, MemoryUtilization_Average
#
# Client Sends Request for Workload (RFW) Containing:
# RFW Id (int)
# Benchmark Type - Dvd Store, NDBench (boolean)
# Workload Metric - CPU, Network In, Network Out, Memory ()
# Batch Unit - Number of Samples Per Batch (int)
# Batch Id (int)
# Batch Size - Number of Batches to Return (int)
# Data Type - Training or Testing Data (boolean)
#
# Server Replies with Response for Data (RFD) Containing:
# RFW Id (int)
# Last Batch Id (int)
# Data Samples Requested (List<String>)
# 
# Design Data Model in MySQL Database or Stored in Files
# Design Data Communication with:
# - Text Based Deserialization using JSON
# - Binary Deserialization using Protocol Buf or Thrift
# Deploy server on cloud AWS instance
# ]
