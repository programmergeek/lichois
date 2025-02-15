import logging
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse

from app.api.common.web.api_error import APIMessage
from workresidentpermit.api.serializers import RequestDeferredApplicationDTOSerializer
from ..api.dto import RequestDeferredApplicationDTO

from ..classes.service import DeferredApplicationService

logger = logging.getLogger(__name__)


class DeferredApplicationView(APIView):
    """
    POST {
        document_number = "required"
        comment = ""
        deferred_from = "BOARD/COMMISSIONER/MINISTER"
        expected_action = "Reason for deferrement"
        batch_id = "required"
    }
    """

    def post(self, request, document_number):
        serializer = RequestDeferredApplicationDTOSerializer(data=request.data)
        if serializer.is_valid():
            request_deferred_application_dto = RequestDeferredApplicationDTO(
                **serializer.data
            )

            # Get user logged in
            request_deferred_application_dto.deferred_from = request.user.username

            service = DeferredApplicationService(
                request_deferred_application_dto=request_deferred_application_dto
            )
            if service.validate():
                service.create()
                return JsonResponse(
                    APIMessage(
                        code=200,
                        message="Deferred Application created successfully",
                    ).to_dict(),
                    status=status.HTTP_200_OK,
                )
            else:
                return JsonResponse(
                    data=service.response.data,
                    status=status.HTTP_400_BAD_REQUEST,
                    safe=False,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompleteDeferredApplicationView(APIView):
    """
    POST {
        document_number = "required"
        comment = ""
        deferred_from = "BOARD OR COMMISSIONER"
        expected_action ="Reason for deferment"
        batch_id = "required"
    }
    """

    def post(self, request, document_number):
        try:
            serializer = RequestDeferredApplicationDTOSerializer(data=request.data)
            if serializer.is_valid():
                request_deferred_application_dto = RequestDeferredApplicationDTO(
                    **serializer.data
                )

                service = DeferredApplicationService(
                    request_deferred_application_dto=request_deferred_application_dto
                )
                if not service.validate():
                    service.complete_deferred_application()
                else:
                    return JsonResponse(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            logger.error("Invalid JSON in request body")
            return JsonResponse(
                {"error": "Invalid JSON in request body"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
            return JsonResponse(
                {"detail": f"Something went wrong. Got {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
