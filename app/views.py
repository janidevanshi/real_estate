from django.shortcuts import get_object_or_404, render
from .models import Contact, Commercial, PostImage
from django.contrib import messages
# Create your views here.


def home_view(request):
    mainpage_Properties = Commercial.objects.all()
    context = {
        'mainpage_Properties': mainpage_Properties
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
