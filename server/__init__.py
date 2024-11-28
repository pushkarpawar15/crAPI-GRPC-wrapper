import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection 
from generated import identity_pb2, identity_pb2_grpc
from . import IdentityService as IdentityService
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    identity_pb2_grpc.add_IdentityServiceServicer_to_server(IdentityService(), server)

    # Enable server reflection
    SERVICE_NAMES = (
        identity_pb2.DESCRIPTOR.services_by_name['IdentityService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:5005")
    print("gRPC server running on port 5005 with reflection enabled")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
