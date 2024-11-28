import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection 
from generated import identity_pb2, identity_pb2_grpc,community_pb2,community_pb2_grpc,workshop_pb2,workshop_pb2_grpc
from .IdentityService import IdentityService
from .communityService import CommunityService
from .shopService import ShopService
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    identity_pb2_grpc.add_IdentityServiceServicer_to_server(IdentityService(), server)
    community_pb2_grpc.add_CommunityServiceServicer_to_server(CommunityService(),server)
    workshop_pb2_grpc.add_ShopServiceServicer_to_server(ShopService(),server)

    # Enable server reflection
    SERVICE_NAMES = (
        identity_pb2.DESCRIPTOR.services_by_name['IdentityService'].full_name,
        community_pb2.DESCRIPTOR.services_by_name['CommunityService'].full_name,
        workshop_pb2.DESCRIPTOR.services_by_name['ShopService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:5005")
    print("gRPC server running on port 5005 with reflection enabled")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()