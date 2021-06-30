from django.shortcuts import get_object_or_404, render
from .models import Contact, Commercial, PostImage, Residential, PostRESIImage
from django.contrib import messages
# Create your views here.


def home_view(request):
    mainpagecomm_Properties = Commercial.objects.all()
    mainpageresi_Properties = Residential.objects.all()
    context = {
        'mainpagecomm_Properties': mainpagecomm_Properties,
        'mainpageresi_Properties': mainpageresi_Properties
    }
    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")


# def contact_view(request):
#     return render(request, "contact.html")
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
