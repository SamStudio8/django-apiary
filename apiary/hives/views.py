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

def compare(request, inspection_id_a, inspection_id_b):
    inspection_a = get_object_or_404(Inspection, pk=inspection_id_a)
    inspection_b = get_object_or_404(Inspection, pk=inspection_id_b)

    pairs = Inspection.pair_frames(inspection_a, inspection_b)
    return render(request, 'compare.html', {
        'inspection_a': inspection_a,
        'inspection_b': inspection_b,
        'pairs': pairs,
    })
