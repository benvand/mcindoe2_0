from django.views.generic import DetailView

from .models import StaticPage

class StaticPageView(DetailView):

    template_name='staticpage/staticpage.html'

    def get_object(self):
        return StaticPage.objects.get(page_name=self.kwargs['page_name'])