from django import forms
from .models import (
    UserProfile,
    Book,
    PublisherNeeds

)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user',)
        labels = {
            'about_you': 'نبذه عنك ',
            'contact_info': 'رقم التواصل',
            'city': 'المدينة',
            'source': 'النص المصدر',
            'study': 'مؤهلك التعليمي',
            'mother_language': 'اللغة الأم',
            'field_concern': 'مجال الاهتمام',

        }


class PublisherNeedsForm(forms.ModelForm):
    class Meta:
        model = PublisherNeeds
        exclude = ('publisher',)
        labels = {
            'needs': 'الوظيفة'
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('user', 'is_completed', 'is_open_download')
