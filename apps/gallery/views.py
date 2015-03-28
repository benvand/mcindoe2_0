from django.views.generic import DetailView

from .models import Gallery

class GalleryView(DetailView):

    template_name='gallery/gallery.html'

    def get_object(self):
        return Gallery.objects.get(page_name=self.kwargs['page_name'])