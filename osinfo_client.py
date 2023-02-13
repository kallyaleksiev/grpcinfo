from __future__ import print_function

import logging
from datetime import datetime

import grpc
import osinfo_pb2
import osinfo_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = osinfo_pb2_grpc.OSInfoProviderStub(channel=channel)

        # quick and dirty input
        while True:
            command = input("OS or PIDS= Query? > ")
            if command == "OS":
                query = osinfo_pb2.OSQuery()
                osinfo = stub.GetOSInfo(query)
                print(
                    f"Server running on {osinfo.osname} and has {osinfo.totalRAM // 1000**3}GB total ram")

            else:  # command = 'PIDS=x_1,x_2,..'
                pids = command.split("=")[1].split(',')

                def pids_req_iter():
                    for pid in pids:
                        yield osinfo_pb2.ProcessQuery(pid=int(pid))
                pids_info_iter = stub.ListProcessInfo(pids_req_iter())

                for proc in pids_info_iter:
                    print(
                        f"Process with PID: {proc.pid} has \
                        username: {proc.username}, \
                        creation time: {datetime.utcfromtimestamp(proc.creationTime).strftime('%Y-%m-%d %H:%M:%S')}, \
                        and number of children: {len(proc.children)}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
