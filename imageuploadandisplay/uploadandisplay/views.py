from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from .forms import myform
from .models import ImageModel
from imageuploadandisplay.settings import MEDIA_ROOT

import os
# Create your views here.\
p=''
def home(request):
    if request.method == 'POST':

        form = myform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    images = ImageModel.objects.order_by('-date')[:1]
    form = myform()
    files=os.listdir(MEDIA_ROOT+'/images/')
    #file=max(files,key=os.path.getctime)

    context = {'form':form,'images':images
    }

    return render(request,'uploadandisplay/Homepage.html',context)

import cv2
import math
import test
import os
from .ml_model import  test
import glob
import os.path



def run(request):
    if request.method=='POST':
        #p=request.POST.get('url')
        #obj = ImageModel.objects.order_by('-date')[:1]
        pic = ImageModel.objects.order_by('-date')[0]
        pic1 = ImageModel.objects.order_by('-date')[:1]

        print(pic.Image)
        a=str(pic.Image)

       # path = 'C:\Users\muham\Desktop\Django-Image-upload-and-display-project\imageuploadandisplay\media\images\girl2.jpg'
        image = test.run('./media/'+a)

        # return HttpResponseRedirect('uploadandisplay/Homepage.html')
        return render(request,'uploadandisplay/Homepage.html',{'obj':pic1})
       # json_resp = {'image_url':'/media/detected.jpg', 'image_result':"man"}
       # return HttpResponse(json_resp)





