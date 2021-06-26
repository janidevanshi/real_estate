from django.contrib import admin

from .models import Commercial, PostImage, Contact

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

# from .models import Commercial, CommercialImage
# from django.contrib import admin
# from .models import Commercial, Contact
# # Register your models here.

# admin.site.register(Contact)
# # admin.site.register(Commercial)


# class CommercialImageAdmin(admin.StackedInline):
#     model = CommercialImage


# @admin.register(Commercial)
# class CommercialAdmin(admin.ModelAdmin):
#     inlines = [CommercialImageAdmin]

#     class Meta:
#         model = Commercial


# @admin.register(CommercialImage)
# class CommercialImageAdmin(admin.ModelAdmin):
#     pass
