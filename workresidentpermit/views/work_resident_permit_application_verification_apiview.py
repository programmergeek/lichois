from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.api.serializers import ApplicationVerificationRequestSerializer
from app.api import ApplicationVerificationRequest

from ..validators import WorkResidentPermitVerificationValidator
from ..classes import WorkResidentPermitApplication


class WorkPermitApplicationVerificationAPIView(APIView):

    def post(self, request, document_number):
        serializer = ApplicationVerificationRequestSerializer(data=request.data)
        if serializer.is_valid():
            validator = WorkResidentPermitVerificationValidator(document_number=document_number)
            if validator.is_valid():
                print("verification_request=serializer.data: ", serializer.data)
                verification_request = ApplicationVerificationRequest(**serializer.data)
                application = WorkResidentPermitApplication(
                    document_number=document_number, verification_request=verification_request)
                data = application.submit_verification().result()
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(validator.response.result(), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
