from django.shortcuts import render
from .models import Artifact

def all_artifacts(request):
    artifacts = Artifact.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts})
