from django.shortcuts import render
from artifacts.models import Artifact

def do_search(request):
    artifacts = rtifacts.objects.filter(name__icontains=request.GET['q'])
    return render(request, "artifacts.html", {"artifacts": artifacts})