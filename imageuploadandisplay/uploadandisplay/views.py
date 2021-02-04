from django.shortcuts import render
from .forms import myform
from .models import ImageModel
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = myform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    images = ImageModel.objects.all()
    form = myform()
    context = {'form':form,'images':images
    }
    return render(request,'uploadandisplay/home.html',context)