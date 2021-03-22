from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from django.urls import reverse
from django.shortcuts import redirect

from main.models.user import UserRegistrationForm
from main.views import Page, get_navbar


class MyRegisterFormView(FormView):
    """отображение регистрации"""

    form_class = UserRegistrationForm
    template_name = Page.registration
    context = {'title': 'Registration', 'page_name': 'Регистрация'}

    def get(self, request, *args, **kwargs):
        self.context['navbar'] = get_navbar(request)
        self.context['form'] = self.get_context_data()['form']
        return self.render_to_response(self.context)

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.data.get('username'), password=form.data.get('password2'))
        login(self.request, user)
        return redirect(reverse('index'))
