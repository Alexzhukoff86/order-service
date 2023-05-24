import grpc
from utils import logger

from protopy import account_pb2
from protopy import account_pb2_grpc


class AccountClient:

    def __init__(self, addr):
        self.channel = grpc.insecure_channel(addr)
        self.stub = account_pb2_grpc.AccountServiceStub(self.channel)
        logger.info(f"Channel {self.channel}")

    def get_account(self, id):
        request = account_pb2.GetAccountRequest(
            id=id
        )
        logger.info(f"Request {request}")
        try:
            response = self.stub.GetAccount(request)
        except Exception as e:
            logger.info(f"error {e}")
        return response
