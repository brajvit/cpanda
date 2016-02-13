from django.db.models import Q
from django.db import models
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import PostForm,ServiceForm
from .forms import  ServiceForm, Service1Form
from .forms import DocumentForm, EventForm ,EvtForm
from .models import Product, Service, Event


##########################################################################

##################################################################################for product list in product list
class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()


    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        # print context
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q")
        return context


#Basic search function
#using q import from django.db.models import Q
#
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
                )
            try:
                qs2 = self.model.objects.filter(
                Q(price=query)
                )
                qs = (qs | qs2).distinct()
            except:
                pass
        return qs


################################################################################## for show detail of product mail and dashboard
#Product Detail view for showing detail of donate............
class ProductDetailView(DetailView):
    model = Product
    def product_detail_view_func(request, id):
        product_instance =  get_object_or_404(Product, id=id)
        try:
            product_instance = Product.object.get(id=id)
        except Product.DoesNotExist:
            raise Http404
        except:
            raise Http404
        template = "donate/product_detail.html"
        context = {
        "object": product_instance
        }
        return render(request, template, context)

######################################################################################## for edit your product item fr history edit and product edit
@login_required
def post_edit(request, pk):
    
    post = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('donate.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'donate/post_edit.html', {'form': form })


########################################################################################## show the list of login user donate items history
@login_required
def post_history(request):
    model = Product
    posts = Product.objects.filter(user_id = request.user.id)
    
    return render(request, 'donate/post_list.html', {'posts': posts })


################################################################################## detail of perticular donate items have experidate ....

@login_required
def post_detail_history(request, pk):
    model = Product
    user_id=request.user.id
    post = get_object_or_404(Product_id=request.user.id, pk=pk)
    
    return render(request, 'donate/product_detail_history.html', {'post': post })

########################################################################################## show detail of recent donateitem
def list_detail(request):
    post = Product.objects.filter(date_created__lte=timezone.now()).order_by('-docfile')
    
    return render(request, "donate/product_list.html", {'post': post })


################################################################################## show donate item form
@login_required
def list(request):
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Product(user = request.user, title = request.POST['title'], docfile = request.FILES['docfile'], active = request.POST['active'], description = request.POST['description'], quantity = request.POST['quantity'], zip_Code = request.POST['zip_Code'], address = request.POST['address'], expire_date = request.POST['expire_date'])
            newdoc.save()
            return redirect('donate.views.post_detail_list', pk=newdoc.pk)
    else:
        form = DocumentForm() # A empty, unbound form

   # Load documents for the list page

    return render_to_response(
        'donate/list.html',
        {  'form': form},
        context_instance=RequestContext(request)
    )

##################################################################################
@login_required
def post_detail_list(request, pk):
    model = Product
    user_id=request.user.id
    #post = Product.objects.filter(user_id = request.user.id, pk=pk)
    post = get_object_or_404(Product_id=request.user.id, pk=pk)
    
    return render(request, 'donate/product_detail1.html', {'post': post })


################################################################################## edit form for history item
@login_required
def post_edit_list(request, pk):
    
    post = get_object_or_404(Product_id=request.user.id, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post )
        if form.is_valid():
            post.user = request.user
            post.save()
            return redirect('donate.views.post_detail_list', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'donate/post_edit.html', {'form': form })

##################################################################################

@login_required
def post_edit_service(request, pk):
    
    post = get_object_or_404(Service_id=request.user.id, pk=pk)
    if request.method == "POST":
        form = Service1Form(request.POST, instance=post )
        if form.is_valid():
            post.user = request.user
            post.save()
            return redirect('donate.views.post_detail_service', pk=post.pk)
    else:
        form = Service1Form(instance=post)
    return render(request, 'donate/post_edit_service.html', {  'form': form})
    

@login_required
def post_detail_service(request, pk):
    model = Service
    user_id=request.user.id
    #post = Product.objects.filter(user_id = request.user.id, pk=pk)
    post = get_object_or_404(Service_id=request.user.id, pk=pk)
    
    return render(request, 'donate/service_detail1.html', {  'post': post})


@login_required
def service(request):
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Service(user = request.user, title = request.POST['title'], docfile = request.FILES['docfile'], active = request.POST['active'], description = request.POST['description'], duraction = request.POST['duraction'], zip_Code = request.POST['zip_Code'], address = request.POST['address'], expire_date = request.POST['expire_date'])
            newdoc.save()
            return redirect('donate.views.post_detail_service', pk=newdoc.pk)
    else:
        form = ServiceForm() # A empty, unbound form

   # Load documents for the list page

    return render_to_response(
        'donate/service.html',
        {  'form': form},
        context_instance=RequestContext(request)
    )

@login_required
def service_detail_history(request, pk):
    model = Service
    user_id=request.user.id
    #post = get_object_or_404(Product_id=request.user.id, pk=pk)
    post = get_object_or_404(Service_id=request.user.id, pk=pk)
    
    return render(request, 'donate/service_detail_history.html', {'post': post })
    
def service_detail(request, pk):
    model = Service
    #user_id=request.user.id
    #post = Product.objects.filter(user_id = request.user.id, pk=pk)
    post = get_object_or_404(Service, pk=pk)
    #document = Document.objects.filter(user_id = request.user.id)[:1]
    return render(request, 'donate/service_detail.html', {'post': post})
    
@login_required
def service_history(request):
    model = Service
    posts = Service.objects.filter(user_id = request.user.id)
    
    return render(request, 'donate/service_list.html', {'posts': posts })
    
def servicelist(request):
    model = Service
    post = Service.objects.all()
    return render(request, 'donate/service_home.html', {'post': post})

def servicelist(request):
    model = Service
    post = Service.objects.all()
    return render(request, 'donate/service_home.html', {'post': post})

def service_detail_home(request, pk):
    model = Service, Document
    #user_id=request.user.id
    post = get_object_or_404(Service, pk=pk)

    #document = Document.objects.filter(user_id = request.user.id)[:1]
    return render(request, 'donate/service_detail_home.html', {'post': post })

def event(request):
    model = Event,User
    event = Event.objects.all()

    # Handle file upload
    if request.method == 'POST':
        form = EventForm(request.POST , request.FILES)
        if form.is_valid():
            event = Event(user=request.user, snap=request.FILES['snap'], eventtype = request.POST['eventtype'],duration = request.POST['duration'],dresscode = request.POST['duration'],date_event = request.POST['date_event'], description = request.POST['description'], place = request.POST['place'],)
            event.save()

            # Redirect to the document list after POST
            return redirect('donate.views.event')
    else:
        form = EventForm() # A empty, unbound form
    
    event = Event.objects.all()
   # Load documents for the list page
    
    # Render list page with the documents and the form
    return render_to_response(
        'donate/event.html',
        { 'event': event,'form': form,},
        context_instance=RequestContext(request)
    )

def event_detail(request, pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)
    user_id=event.user.id

    return render(request, 'donate/eventdetail.html', {'event': event    })

@login_required
def devent(request):
    
    # Handle file upload
    if request.method == 'POST':
        form = EventForm(request.POST , request.FILES)
        if form.is_valid():
            event = Event(user=request.user, snap=request.FILES['snap'], eventtype = request.POST['eventtype'],duration = request.POST['duration'],dresscode = request.POST['duration'],date_event = request.POST['date_event'], description = request.POST['description'], place = request.POST['place'],)
            event.save()

            # Redirect to the document list after POST
            return redirect('donate.views.uevent_detail', pk=event.pk)
    else:
        form = EventForm() # A empty, unbound form

   # Load documents for the list page
    event = Event.objects.all()
   

    # Render list page with the documents and the form
    return render_to_response(
        'donate/userevent.html',
        {'event': event, 'form': form},
        context_instance=RequestContext(request)
    )


@login_required
def devent_detail(request):
    model = Event,Document,User
    event = Event.objects.filter(user_id = request.user.id)
    
    return render(request, 'donate/detail.html', {'event': event  })

@login_required
def uevent_detail(request, pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)
    
    return render(request, 'donate/ueventdetail.html', {'event': event,'document': document })

def devent_edit(request,pk):
    model = Event
    event = get_object_or_404(Event, pk=pk)
    
    
    # Handle file upload
    if request.method == 'POST':
        form = EvtForm(request.POST,request.FILES, instance=event )
        if form.is_valid():
            event.user = request.user
            event.save()

            # Redirect to the document list after POST
            return redirect('donate.views.uevent_detail', pk=event.pk)
    else:
        form = EvtForm(instance=event) # A empty, unbound form

   # Load documents for the list page

   

    # Render list page with the documents and the form
    return render(request,
        'donate/userevent.html',{ 'form': form})







