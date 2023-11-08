from django.urls import path
from . import views

urlpatterns = [
    path(
        "addreview/",
        views.addreview,
        name="review",
    ),
    
]