from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/home.html')
