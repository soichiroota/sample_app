from django.views.generic.base import TemplateView


class HelpView(TemplateView):
    template_name = 'static_pages/help.html'


help = HelpView.as_view()

class HomeView(TemplateView):
    template_name = 'static_pages/home.html'


home = HomeView.as_view()