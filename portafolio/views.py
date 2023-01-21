from django.shortcuts import render
from .models import Project
from about_me.models import Info

info = Info.objects.get(name="Franco Miguez")
# Create your views here.
def index(request):
    project_list = Project.objects.all()
    return render(request, 'index.html', {'page_name': "Portafolio",
                                        'projects' : project_list,
                                        'info':info,}
                                        
                  )

def proyect(request, id):
    project_info = Project.objects.get(id=id)
    return render(request, 'proyect.html', {'project': project_info,
                                            'info':info,})