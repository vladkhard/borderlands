from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateCitizenView, GetCitizenView


urlpatterns = [
    path('', CreateCitizenView.as_view()),
    path('<slug:citizen_id>/', GetCitizenView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
