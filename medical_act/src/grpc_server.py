from concurrent import futures

import grpc

import dof_mx_legal_norms.services.grpc_legal_norm_service
import resources.protos.extractnomfromurlpb.extractnomfromurlpb_pb2_grpc as grpc_proto_extract_nom


def serve():
    """
    :return:
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_proto_extract_nom.add_ExtractNomServiceServicer_to_server(
        dof_mx_legal_norms.services.grpc_legal_norm_service.LegalNorm(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server started on port 50051")
    server.start()
    server.wait_for_termination()
