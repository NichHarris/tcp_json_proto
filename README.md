# Protobuf and Json Data Models Over TCP/IP

- Developed Client/Server Applications using TCP/IP Sockets in Python
- Designed Data Models for Following Serialization and Deserialization Methods:
  - Text-Based with JavaScript Object Notation (JSON)
  - Binary-Based with Protocol Buffers (Protobuf, or Proto)
- Deployed on Google Cloud Platform
  - Set up a Compute Engine Instance with a VM

> Bonus: Developed a Serverless Application using gRPC over HTTP Channel

# Data Models

Considerations: Size and Type of Data Used in Relation to Speed and Efficiency of Transmitting Data Over Wire

## JSON - Text Based

Defined JSON Data Model in reqWorkload.json and resData.json

- Provided Type and Description for Each Property in Request and Response Models

## Protocol Buffers

Defined Proto Data Model in workload.proto

- Defined WorkloadRFW Message for Request for Workload (RFW)
- Defined WorkloadRFD Message for Response For Data (RFD)
- Defined WorkloadService Service with Remote Procedure Call (RPC)
  - Created Workload RPC to Receive a Request for Workload and Return a Reponse for Data

# TCP/IP Communication

> Server Socket First Initialized \
> Server Binds Hostname Address and Port Number to Server Side Socket \
> -> Start Listening for Client Side to Connect with Same Hostname and Port

> Client Socket Then Initialized \
> Client Socket Connects to Server Side Socket using Same Hostname and Port

> Once Server Accepts Connection, Client Can Create, Serialize and Send Request to Server \
> Server Receives and Deserializes Data to then Create, Serialize, and Send a Response to Client

> Client Receives and Deserializes Data, Receiving a Response for a Given Request

# Serverless using gRPC

> Created gRPC Server to Service Remote Procedure Calls (RPCs) \
> Opened Server Port to Serve and Handle RPCs using a Thread Pool

> Overrode Auto Generated Servicer and Defined Workload RPC to Handle Requests

> Client Creates HTTP Channel to Server via Server Address using gRPC \
> Client Then Creates Stub Using Channel to Server, Later Used to Call Workload RPC

> Client Can Create, Serialize and Pass Request to Workload RPC \
> Workload RPC Receives and Deserializes Data to then Create, Serialize, and Return a Response to Client

> Client Receives and Deserializes Data, Receiving a Response for a Given Request

# Setup Virtual Environment

## For Mac/Linux:

```
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

## For Windows:

```
pip install virtualenv
virtualenv env
~\env\Scripts\activate
```

## Install Dependencies:

```
pip install -r requirements.txt
```
