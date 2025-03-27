from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('news_list')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

# users/views.py
from django.shortcuts import render

def profile(request):
    return render(request, 'users/profile.html')  # Страница профиля

