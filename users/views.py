from django.shortcuts import render,HttpResponse
from .forms import OutLetCreationForm,AdminstratorCreationForm
from .models import OutLet,Adminstrator,User
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login
# Create your views here.

class OutLetCreateView(CreateView):
	model=User
	form_class=OutLetCreationForm
	template_name='users/outletsignup.html'

	def form_valid(self,form):
		user=form.save()
		return HttpResponse('Outlet Added')
class AdminstratorCreateView(CreateView):
	model=User
	form_class=AdminstratorCreationForm
	template_name='users/adminsignup.html'

	def form_valid(self,form):
		user=form.save()
		return HttpResponse(' Admin Added')

def login_user(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			print(user.is_outlet)
			if user.is_adminstrator:
				return HttpResponse('admin side')
			elif user.is_outlet:
				return HttpResponse('oulet side')
			# return HttpResponse('login succesfuul')

	return render (request,'users/login.html')