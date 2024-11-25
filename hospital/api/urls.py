from django.urls import path
from .views import DoctorView, PatientView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        'doctor/',
         DoctorView.as_view({
             'get': 'list',
             'post': 'create'

         })
    ),
    path(
        'doctor/<int:id>/',
        DoctorView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:id>/patient/',
        DoctorView.as_view({
             'get': 'list_patient',
        })
     ),
    path(
        'patient/',
         PatientView.as_view({
             'get': 'list',
             'post': 'create'

         })
    ),
    path(
        'patient/<int:id>/',
        PatientView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
        })
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]







# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import DoctorView
#
# urlpatterns = [
#     path(
#         'doctor/',
#         DoctorView.as_view({
#             'get': 'list',
#             'post': 'create'
#         }),
#         name='doctor-list-create'  # имя маршрута
#     ),
#     path(
#         'doctor/<int:doctor_id>/',  # заменили id на doctor_id
#         DoctorView.as_view({
#             'get': 'retrieve',
#             'put': 'update',
#             'delete': 'destroy'
#         }),
#         name='doctor-detail'
#     ),
#     path(
#         'doctor/<int:doctor_id>/patient/',
#         DoctorView.as_view({
#             'get': 'list_patient',  # убедитесь, что метод list_patient реализован
#         }),
#         name='doctor-patient-list'
#     ),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]






















