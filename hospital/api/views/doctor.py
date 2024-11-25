from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from api.mixin import HospitalGenericViewSet
from api.models import Patient, Doctor
from api.serializers.doctor import (
    DoctorListSerializer,
    DoctorRetrieveSerializer,
    DoctorCreateSerializer,
    DoctorUpdateSerializer,
)
from api.serializers.patient import PatientListSerializer
from api.filters import DoctorFilterset


class DoctorView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    lookup_field = "id"

    filter_backends = [DjangoFilterBackend]
    filterset_class = DoctorFilterset

    def get_action_permissions(self):
        if self.action in ("list", "retrieve"):
            self.action_permissions = ["view_doctor"]
        elif self.action == "list_patient":
            self.action_permissions = ["view_patient"]
        else:
            self.action_permissions = []

        # Ensure parent permissions are also applied
        return super().get_action_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return DoctorListSerializer
        elif self.action == "retrieve":
            return DoctorRetrieveSerializer
        elif self.action == "create":
            return DoctorCreateSerializer
        elif self.action == "update":
            return DoctorUpdateSerializer
        elif self.action == "list_patient":
            return PatientListSerializer

        raise AssertionError(f"Serializer not found for action: {self.action}")

    def get_queryset(self):
        if self.action == "list_patient":
            doctor_id = self.kwargs.get("id")
            if not doctor_id:
                raise ValidationError({"detail": "Doctor ID is required for the 'list_patient' action"})
            return Patient.objects.filter(visits__doctor_id=doctor_id)
        return Doctor.objects.all()

    @action(detail=True, methods=["get"], url_path="patients")
    def list_patient(self, request, id=None):
        if not id:
            return Response(
                {"detail": "Doctor ID is required to fetch patients"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)




























