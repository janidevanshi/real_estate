from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact, Commercial, PostImage, Residential, PostRESIImage
from django.contrib import messages
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this

# Create your views here.


def home_view(request):
    print(request.user)
    mainpagecomm_Properties = Commercial.objects.all()
    mainpageresi_Properties = Residential.objects.all()
    context = {
        'mainpagecomm_Properties': mainpagecomm_Properties,
        'mainpageresi_Properties': mainpageresi_Properties
    }
    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")


def contact_view(request, *args, **kwargs):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if len(name) < 2 or len(email) < 3 or len(subject) < 4:
            messages.error(request, "Please fill the form correctly.")

        else:
            if email.__contains__('.'):
                contact = Contact(name=name, email=email,
                                  subject=subject, message=message)
                contact.save()
                messages.success(
                    request, "Your messages has been successfully sent.")
            else:
                messages.error(request, "Please Enter Correct Email Address.")
    return render(request, "contact.html", {})


def commercial_view(request):

    allProperties = Commercial.objects.all()
    context = {
        'allProperties': allProperties
    }

    return render(request, "commercial.html", context)


def commercial_single_view(request, slug):
    property_data = Commercial.objects.filter(slug=slug)
    post = get_object_or_404(Commercial, slug=slug)
    photos = PostImage.objects.filter(post=post)
    context = {
        'property_data': property_data,
        'photos': photos,

    }
    return render(request, "commercial_single.html", context)


def residential_view(request):
    allProperties = Residential.objects.all()
    context = {
        'allProperties': allProperties
    }

    return render(request, "residential.html", context)


def residential_single_view(request, slug):
    property_data = Residential.objects.filter(slug=slug)
    post = get_object_or_404(Residential, slug=slug)
    photos = PostRESIImage.objects.filter(post=post)
    context = {
        'property_data': property_data,
        'photos': photos,

    }
    return render(request, "residential_single.html", context)


@login_required(redirect_field_name='next')
def addproperty_view(request, *args, **kwargs):

    ImageFormSet = modelformset_factory(PostImage,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':
        postForm = CommercialForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=PostImage.objects.none())

        if postForm.is_valid() and formset.is_valid():

            # form.save()
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()
            # this helps to not crash if the user
            # do not upload all the photos
            for form in formset.cleaned_data:
                if form:
                    images = form['images']
                    photo = PostImage(post=post_form, images=images)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = CommercialForm()
        formset = ImageFormSet(queryset=PostImage.objects.none())
    return render(request, 'add_property.html',
                  {'postForm': postForm, 'formset': formset})

    # else:
    #     form = CommercialForm()
    # return render(request, 'add_property.html', {'form': form})
    # if request.method == 'POST':
    #     newproperty = Commercial()
    #     newproperty.title = request.POST.get('title')
    #     newproperty.content = request.POST.get('content')
    #     newproperty.Area = request.POST.get('Area')
    #     newproperty.price = request.POST.get('price')
    #     newproperty.slug = request.POST.get('slug')
    #     newproperty.sell_or_rent = request.POST.get('sell_or_rent')
    #     newproperty.timestamp = request.POST.get('timestamp')
    #     newproperty.location = request.POST.get('location')
    #     newproperty.property_type = request.POST.get('property_type')
    #     newproperty.construction_status = request.POST.get(
    #         'construction_status')
    #     newproperty.main_image = request.FILES.get('main_image')
    #     newproperty.floorplan = request.FILES.get('floorplan')
    #     newproperty.images = request.POST.get('images')
    #     newproperty.amenities = request.POST.getlist('amenities')
    #     print(newproperty.amenities)
    # newproperty = Commercial(
    #     title=title, content=content, Area=Area, price=price, slug=slug, timestamp=timestamp, sell_or_rent=sell_or_rent, construction_status=construction_status, property_type=property_type, location=location, amenities=amenities)
    # print(title, content, slug, timestamp, sell_or_rent, Area,
    #       price, construction_status, property_type, location, amenities)
    # newproperty.save()


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect("../add_property")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
