from django.shortcuts import render
from .models import Info, Work, Course

info = Info.objects.get(name="Franco Miguez")

# Create your views here.
def index(request):
    works = Work.objects.all()
    courses = Course.objects.all()
    return render(request, 'about-me.html',{
                                            'info':info,
                                            'works':works,
                                            'courses':courses,
                                            }
                  )