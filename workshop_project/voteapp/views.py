from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Party
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse
from .forms import PartyForm
from django.db.models import Max
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
class Index(generic.ListView):
	template_name = 'voteapp/index.html'
	context_object_name = 'all_party'

	def get_queryset(self):
		return Party.objects.all()
 
def view_party(request):
	obj1 = Party.objects.all()
	template = 'voteapp/viewparty.html'
	context = {'Party':obj1}
	return render(request,template,context)

def view_results(request):
	obj1 = Party.objects.all().order_by('-no_of_votes')
	template = 'voteapp/viewresults.html'
	context = {'Party':obj1}
	return render(request,template,context)

def view_info(request,id):
	p1 = Party.objects.get(id=id)
	template_name = 'voteapp/viewinfo.html'
	context_object_name = {'Party':p1}
	return render(request,template_name,context_object_name)

def del_party(request,id):
	p1 = Party.objects.get(id=id)
	p1.delete()
	template_name = 'voteapp/delete.html'
	context_object_name = {'Party':p1}
	return render(request,template_name,context_object_name)

def inc_vote(request,id):
	p1=Party.objects.get(id=id)
	p1.no_of_votes=p1.no_of_votes+1
	p1.save()
	template_name = 'voteapp/incvote.html'
	context_object_name = {'Party':p1}
	return render(request,template_name,context_object_name)

def new_party(request):
	if request.method == 'POST':
		form=PartyForm(request.POST, request.FILES)
		if form.is_valid():
			#p1 = Party.objects.get(pk=pk)
			form.party_logo = form.cleaned_data['party_logo']
			form.leader = form.cleaned_data['leader']
			#p1.save()
			form.save()
			#form=PartyForm()
			#messages.success(request,'saved')
			return HttpResponse('uploaded')
	else:
		form=PartyForm()
	return render(request, 'voteapp/newparty.html',{'form':form})

class ViewUpdatePost(UpdateView):
	model = Party
	template_name = 'voteapp/update1.html'
	fields = ['party_name','date_of_est','moto','party_leader','founded_by','party_logo_name','party_logo','leader']

	def get_object(self,queryset=None):
		id=self.kwargs['id']
		return self.model.objects.get(id=id)

	def form_valid(self, form):
		form.save()
		return HttpResponse("updated")

def declare_winner(request):
	obj1 = Party.objects.all().order_by('-no_of_votes')
	context = {'Party':obj1}
	context1 = list(obj1)[0]
	return HttpResponse(context1)

def declare_winner1(request):
	p1=Party.objects.all()
	p2=p1.aggregate(Max('no_of_votes'))
	data = serializers.serialize('json', p1)
	return HttpResponse(data)

def jresp(request):
	obj1=Party.objects.all().values('id','party_name','date_of_est','moto','party_leader','founded_by','party_logo_name')
	data=list(obj1)
	return JsonResponse(data,safe=False)
