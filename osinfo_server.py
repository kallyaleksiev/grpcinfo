
from concurrent import futures
import logging
import platform

import grpc
import osinfo_pb2
import osinfo_pb2_grpc

import psutil


class OSInfoProviderServicer(osinfo_pb2_grpc.OSInfoProviderServicer):

    def GetOSInfo(self, request, context):
        """Get holistic info about OS
        """
        full_plt = platform.platform().split("-")
        if len(full_plt) < 2:
            raise OSError("Unexpectedly cannot get useful name of OS")

        osname = " ".join(full_plt[:2])
        totalRam = psutil.virtual_memory().total

        return osinfo_pb2.OSInfo(osname=osname, totalRAM=totalRam)

    def ListProcessInfo(self, request_iterator, context):
        """Get info about a specific set (array) of processes
        """
        for process_query in request_iterator:
            pid = process_query.pid
            try:
                proc = psutil.Process(pid=pid)
            except:
                print(f"Process with PID: {pid} not found")
                continue 

            username = proc.username()
            creationTime = proc.create_time()
            children = [p.pid for p in proc.children()]

            yield osinfo_pb2.ProcessInfo(pid=pid,
                                         username=username,
                                         creationTime=creationTime,
                                         children=children)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    osinfo_pb2_grpc.add_OSInfoProviderServicer_to_server(
        OSInfoProviderServicer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
