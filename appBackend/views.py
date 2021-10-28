from django.views import generic

class LoginView(generic.TemplateView):
  template_name = 'appBackend/login.html'

class MenuView(generic.TemplateView):
  template_name = 'appBackend/menu.html'

