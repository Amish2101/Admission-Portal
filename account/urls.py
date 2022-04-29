from django.urls import path
from .views import FacultyRegistrationClass

urlpatterns = [
    path('signup/', FacultyRegistrationClass.as_view(), name='faculty-signup'),
]
