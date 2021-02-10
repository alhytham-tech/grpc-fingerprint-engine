secureng-fingerprint
=========================

secureng-fingerprint is a gRPC implementation of the DigitalPersona Fingerprint engine, to allow for usage with any programming language (php, python, js, c++ e.t.c). The assumption is that you have setup the fingerprint device on the client side and you are able to obtain FMDs (Fingerprint Minutiae Data) but need a flexible way to work with the data without the programming language limitations of the DigitalPersona SDK, if you haven't setup the device on the client side you can check [here](https://github.com/Ethic41/FingerPrint).

How to Use
===============
The project basically provides a server which is just a grpc c++ wrapper to enroll, identify and verify FMDs and sample client side code that communicate with the server in any language. So the idea is you may want to write your code in a language of your choice, say maybe python, or js using the DigitalPersona fingerprint device, but the SDK is limited to C, C++ or Java, the solution is this project, you can generate the client code which receives fingerprint data (FMD) from a user (e.g from the browser), you can then use your generated code to send the data to the server which can perform enrollment, verification or identification. To start using:

## Setup the FingerPrint Engine Server
To setup the fingerprint engine server you can either build from source or use our generated binaries (we assume a linux server)

## Build from Source
[Setup & Install gRPC globally](https://grpc.io/docs/languages/cpp/quickstart/#setup), then 
 
```bash

# clone this repository
git clone https://github.com/Ethic41/secureng-fingerprint

# move into server directory
cd secureng-fingerprint/src/cpp/

# create and move into the server build directory
mkdir build && cd build

# run cmake
cmake ../

# make and build
make -j

# start the server
./fingerprint_server

```
## Use Generated Binaries
Simply [Download]() and start the server

# 

## Setup the Server Clients
This is basically the heart of the project, the ability to generate code in the language of your choosing that can communicate with the Fingerprint Engine Server. You can generate client code from the ***.proto*** file(s) [here]() for any language of your choosing if it's supported by gRPC.

## Setting up Python client code
We assume ***Python 3.7*** other versions should work, but haven't been tested
```bash

# if you don't already have pip installed
sudo apt install python3-pip

# if you don't have venv installed
sudo apt install python3-venv

# globally install python grpc and grpc-tools
sudo python3 -m pip install -r requirements.txt

# move into client code directory
cd secureng-fingerprint/src/python

# create a virtual environment (named grpcenv)
python3 -m venv grpcenv

# activate the environment
chmod u+x grpcenv/bin/activate
source grpcenv/bin/activate

# install python grpc tools in the new environment
python -m pip install -r requirements.txt

# [optional step] regenerate the client code
python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/fingerprint.proto

# add the url_base64encoded fmds into the fingerprint_client.py file as required
# then run the client
python fingerprint_client.py

```
