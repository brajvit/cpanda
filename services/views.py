from django.shortcuts import render
from .models import Service
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
@login_required
def service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Service(user = request.user, title = request.POST['title'], docfile = request.FILES['docfile'], active = request.POST['active'], description = request.POST['description'], duraction = request.POST['duraction'], zip_Code = request.POST['zip_Code'], address = request.POST['address'], expire_date = request.POST['expire_date'])
            newdoc.save()
            return redirect('services.views.servicelist', pk=newdoc.pk)
    else:
        form = ServiceForm() # A empty, unbound form

   # Load documents for the list page

    return render_to_response(
        'products/service.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def servicelist(request):
    model = Service
    post = Service.objects.all()
    return render(request, 'services/service_home.html', {'post': post})

def service_detail_home(request, pk):
    model = Service
    #user_id=request.user.id
    post = get_object_or_404(Service, pk=pk)
    #document = Document.objects.filter(user_id = request.user.id)[:1]
    return render(request, 'services/service_detail_home.html', {'post': post })



