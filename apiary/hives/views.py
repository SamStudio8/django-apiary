from django.shortcuts import render, get_object_or_404

from .models import Hive, Inspection

def index(request):
    hives = Hive.objects.all()
    return render(request, 'index.html', {"hives": hives})

def list(request, hive_id):
    hive = get_object_or_404(Hive, pk=hive_id)
    return render(request, 'list.html', {"hive": hive})

def detail(request, inspection_id):
    inspection = get_object_or_404(Inspection, pk=inspection_id)
    return render(request, 'detail.html', {'inspection': inspection})
