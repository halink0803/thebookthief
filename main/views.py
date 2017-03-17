# @Author: Hoang Ha
# @Date:   2017-03-17T15:16:57+07:00
# @Last modified by:   Hoang Ha
# @Last modified time: 2017-03-17T15:27:48+07:00


from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/home.html')
