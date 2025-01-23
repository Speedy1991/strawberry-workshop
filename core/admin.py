from django.contrib import admin
from .models import Guest, Member, SocialClub, Product


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'social_club')
    list_filter = ['social_club']


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'rating', 'social_club')
    list_filter = ['social_club']


@admin.register(SocialClub)
class SocialClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'street', 'zip')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'social_club', 'price', 'quality')
    list_filter = ['social_club']
