
# Register your models here.
from django.contrib import admin

from .models import Commercial, PostImage, Contact, PostRESIImage, Residential

admin.site.register(Contact)


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Commercial)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Commercial


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


class ResidentialImageAdmin(admin.StackedInline):
    model = PostRESIImage


@admin.register(Residential)
class ResidentialAdmin(admin.ModelAdmin):
    inlines = [ResidentialImageAdmin]

    class Meta:
        model = Residential


@admin.register(PostRESIImage)
class ResidentialImageAdmin(admin.ModelAdmin):
    pass
