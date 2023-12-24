from django.shortcuts import render
from .models import Drawing

# Create your views here.


def home(request):
    drawings = Drawing.objects.all()
    context = {"drawings": drawings}

    return render(request, "whiteboard.html", context=context)


def drawing_detail(request, drawing_id):
    drawing = Drawing.objects.get(id=drawing_id)
    context = {"drawing": drawing,'drawing_id': drawing_id}

    return render(request, "drawing_detail.html", context=context)

