from django.views.generic.base import TemplateView


class HelpView(TemplateView):
    template_name = 'static_pages/help.html'
    
    def get_context_data(self, **kwargs):
        context = super(HelpView, self).get_context_data(**kwargs)
        context['title'] = 'Help'
        return context


help = HelpView.as_view()

class HomeView(TemplateView):
    template_name = 'static_pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


home = HomeView.as_view()

class AboutView(TemplateView):
    template_name = 'static_pages/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'About'
        return context


about = AboutView.as_view()

class ContactView(TemplateView):
    template_name = 'static_pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context


contact = ContactView.as_view()