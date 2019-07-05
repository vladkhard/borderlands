from django.urls import path
from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CreateCitizenView,
    CitizenView,
    LastCitizenView,
    ListCitizenView,
)


urlpatterns = [
    path('', TemplateView.as_view(template_name="about.html")),
    path('create-citizen', CreateCitizenView.as_view()),
    path('<slug:citizen_id>/', CitizenView.as_view()),
    path('last-citizen', LastCitizenView.as_view()),
    path('list-citizen', ListCitizenView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
