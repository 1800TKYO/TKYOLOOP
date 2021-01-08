from django.shortcuts import render
from django.http import HttpResponse
from .models import Sample, ClubImage
# Create your views here.
def index(request):
    return render(request,'tokyoloop/index.html')

def Samples(request):
    user_list = Sample.objects.order_by('sample_name')
    user_dict = {"samplelist":user_list}
    return render(request,'tokyoloop/users.html',context=user_dict)

def ClubImage(request):
    img_list = ClubImage.objects.order_by('image')
    img_dict = {"imagelist":img_list}
    return render(request,'tokyoloop/users.html',context=img_dict)
