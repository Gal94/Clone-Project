from django.shortcuts import render
from django.contrib.auth import mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember
from django.shortcuts import get_object_or_404
from . import models

class CreateGroup(mixins.LoginRequiredMixin,generic.CreateView):
    fields=('name', 'description') #users will be able to edit name and desc of group
    model = Group

class SingleView(generic.DetailView):
    model = Group



class ListGroup(generic.ListView):
    model = Group

class JoinGroup(generic.RedirectView, LoginRequiredMixin):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group) #try to add the user to the group
        except:
            messages.warning(self.request,('Already a member'))
        else:
            messages.success(self.request,'Welcome')

        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user, group__slug=self.kwargs.get('slug')).get()#try to get a membership

        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, "You're not in the group")
        else:
            membership.delete()
            messages.success(self.request,'Left Group')

        return super().get(request,*args,**kwargs)