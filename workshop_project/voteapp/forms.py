
from django import forms
from .models import Party
'''
from django.utils.safestring import mark_safe
class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        html =  Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value)
'''
# Create your tests here.
class PartyForm(forms.ModelForm):
	leader = forms.ImageField()
	party_logo = forms.ImageField()
	party_name =forms.CharField(max_length=200)
	date_of_est = forms.DateField()
	moto = forms.CharField(max_length=400)
	party_leader = forms.CharField(max_length=200)
	founded_by = forms.CharField(max_length=200)
	party_logo_name = forms.CharField(max_length=200)
	
	class Meta:
		model = Party
		fields = ('party_name','date_of_est','moto','party_leader','founded_by','party_logo_name','party_logo','leader',)

