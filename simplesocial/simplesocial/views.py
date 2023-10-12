from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class FAQView(TemplateView):
    template_name = 'FAQ.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'

class BaseDemoView(TemplateView):
    template_name = 'base_demo.html'        