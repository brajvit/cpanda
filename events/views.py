from django.shortcuts import render
from .models import Event
from .forms import EventForm, HostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# Create your views here.


@login_required
def event(request):
    model = Event
    event = Event.objects.all()

    # Handle file upload
    if request.method == 'POST':
        form = EventForm(request.POST , request.FILES)
        if form.is_valid():
            event = Event(user=request.user, snap=request.FILES['snap'], eventtype = request.POST['eventtype'],duration = request.POST['duration'],dresscode = request.POST['duration'],date_event = request.POST['date_event'], description = request.POST['description'], place = request.POST['place'],)
            event.save()

            # Redirect to the document list after POST
            return redirect('events.views.event')
    else:
        form = EventForm() # A empty, unbound form
    
    event = Event.objects.all()
   # Load documents for the list page
    
    # Render list page with the documents and the form
    return render_to_response(
        'events/event.html',
        { 'event': event,'form': form,},
        context_instance=RequestContext(request)
    )


def event_detail(request, pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)
    user_id=event.user.id
    return render(request,  'events/eventdetail.html', {'event': event })

@login_required
def host(request):
    # Handle file upload
    if request.method == 'POST':
        form = EventForm(request.POST , request.FILES)
        if form.is_valid():
            event = Event(user=request.user, snap=request.FILES['snap'], eventtype = request.POST['eventtype'],duration = request.POST['duration'],dresscode = request.POST['duration'],date_event = request.POST['date_event'], description = request.POST['description'], place = request.POST['place'],)
            event.save()

            # Redirect to the document list after POST
            return redirect('events.views.host_detail', pk=event.pk)
    else:
        form = EventForm() # A empty, unbound form

   # Load documents for the list page
    event = Event.objects.all()   

    # Render list page with the documents and the form
    return render_to_response(
        'events/hostevent.html',
        {'event': event,'form': form},
        context_instance=RequestContext(request)
    )

@login_required
def host_detail(request, pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)
    return render(request,  'events/host_detail.html', {'event': event })

def host_edit(request,pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)    
    # Handle file upload
    if request.method == 'POST':
        form = HostForm(request.POST,request.FILES, instance=event )
        if form.is_valid():
            event.user = request.user
            event.save()
            # Redirect to the document list after POST
            return redirect('events.views.host_detail', pk=event.pk)
    else:
        form = HostForm(instance=event) # A empty, unbound form
# Render list page with the documents and the form
    return render(request,
        'events/hostevent.html',{'form': form})