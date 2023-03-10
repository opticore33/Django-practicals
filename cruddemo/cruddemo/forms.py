from django.forms import ModelForm
from userinfo.models import user

class userInformation(ModelForm):
    class Meta:
        model = user
        fields = '__all__'