from django.views.generic import CreateView, ListView

from .forms import UserInfoModelForm

from .models import UserInfo

class Create(CreateView):
    form_name = UserInfoModelForm
    template_name = 'classbased/create.html'
    success_url = '/c/list/'

class List(ListView):
    template_name = 'classbased/list.html'
    model = UserInfo
    context_object_name = 'data'



