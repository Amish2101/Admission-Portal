from django.contrib import admin
from .models import Admin, Faculty
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.db.models import Q
# Register your models here.

class AdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput) 

    class Meta:
        model = Admin
        fields = ('email',)
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class AdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Admin
        fields = ('firstname', 'lastname', 'email', 'mobile_no', 'gender', 'date_of_birth')

class AdminUserAdmin(BaseUserAdmin):
    form = AdminChangeForm
    add_form = AdminCreationForm

    def get_queryset(self, request):
        return self.model.objects.filter(Q(is_staff=True) | Q(is_superuser=True))

    list_display = ('email','firstname', 'mobile_no', 'date_of_birth')
    fieldsets = (
        (None, {
            "fields": (
                'email','password','firstname', 'lastname', 'mobile_no', 'date_of_birth', 'is_active', 'is_staff'               
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'firstname', 'lastname', 'gender', 'date_of_birth', 'mobile_no'),
        }),
    )

    list_filter= ('email',)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class FacultyCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = Faculty
        fields = ('email', 'firstname', 'lastname', 'gender', 'date_of_birth', 'mobile_no')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit: True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FacultyChangeForm(forms.ModelForm):
    
    class Meta:
        model = Faculty
        fields = ('firstname', 'lastname', 'email', 'mobile_no', 'gender', 'date_of_birth')

class FacultyAdmin(BaseUserAdmin):
    form = FacultyChangeForm
    add_form = FacultyCreationForm

    def get_queryset(self, request):
        return self.model.objects.filter(Q(is_staff=False) | Q(is_superuser=False))

    list_display = ('firstname', 'email', 'mobile_no', 'date_of_birth')

    fieldsets = (
        (None, {
            "fields": (
            'email','password','firstname', 'lastname', 'mobile_no', 'gender', 'date_of_birth', 'is_active', 'is_staff'
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'firstname', 'lastname', 'gender', 'date_of_birth', 'mobile_no'),
        }),
    )

    list_filter= ('email',)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    



admin.site.register(Admin, AdminUserAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.unregister(Group)
    
