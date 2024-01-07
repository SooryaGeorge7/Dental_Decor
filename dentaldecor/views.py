from django.shortcuts import render
from django.core.exceptions import PermissionDenied


""" Error handling """

def handler404(request, exception):
    """Rendering the 404 page."""
    return render(request, '404.html', status=404)

