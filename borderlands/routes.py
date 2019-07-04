from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateCitizenView, CitizenView, LastCitizenView


urlpatterns = [
    path('', CreateCitizenView.as_view()),
    path('<slug:citizen_id>/', CitizenView.as_view()),
    path('last-citizen', LastCitizenView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
