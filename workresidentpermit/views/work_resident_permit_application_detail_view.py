from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from app.classes.application_summary import ApplicationSummary

from ..classes import WorkResidentPermitData
from ..api import WorkResidentPermitDataSerializer


def get_app_labels():
    return [
        "workresidentpermit.WorkPermit",
        "workresidentpermit.ResidencePermit",
        "base_module.Child",
        "base_module.Spouse",
        "app.SecurityClearance",
        "board.BoardDecision",
    ]


class WorkResidentPermitApplicationDetailView(APIView):

    def get(self, request, document_number, format=None):
        """
        Retrieve work resident permit details.
        """
        # document_number = request.query_params.get('document_number', None)

        if document_number is not None:
            app_summary = ApplicationSummary(document_number, get_app_labels())
            return Response(data=app_summary.data())
        return Response({})
