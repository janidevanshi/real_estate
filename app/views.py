from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact, Commercial, PostImage, Residential, PostRESIImage
from django.contrib import messages
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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


def commercial_single_view(request, sno):

    property_data = Commercial.objects.filter(sno=sno)

    post = get_object_or_404(Commercial, sno=sno)
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


def residential_single_view(request, sno):
    property_data = Residential.objects.filter(sno=sno)
    post = get_object_or_404(Residential, sno=sno)
    photos = PostRESIImage.objects.filter(post=post)
    context = {
        'property_data': property_data,
        'photos': photos,

    }
    return render(request, "residential_single.html", context)


# @login_required(redirect_field_name='next')
def addcommproperty_view(request, *args, **kwargs):

    ImageFormSet = modelformset_factory(PostImage,
                                        form=ImageForm, extra=10)
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
            return redirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = CommercialForm()
        formset = ImageFormSet(queryset=PostImage.objects.none())
    return render(request, 'add_comm_property.html',
                  {'postForm': postForm, 'formset': formset})


def addresiproperty_view(request, *args, **kwargs):

    ImageFormSet = modelformset_factory(PostRESIImage,
                                        form=ImageForm, extra=10)
    if request.method == 'POST':
        postForm = ResidentialForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=PostRESIImage.objects.none())

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
                    photo = PostRESIImage(post=post_form, images=images)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return redirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = ResidentialForm()
        formset = ImageFormSet(queryset=PostRESIImage.objects.none())
    return render(request, 'add_resi_property.html',
                  {'postForm': postForm, 'formset': formset})


def delete_view(request, sno):
    # dictionary for initial data with
    # field names as keys

    # fetch the object related to passed id
    obj = get_object_or_404(Commercial, sno=sno)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("../commercial")
    context = {
        'obj': obj
    }
    return render(request, "delete_view.html", context)


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
                return redirect("../")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("../")
