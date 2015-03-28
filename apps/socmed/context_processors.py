from .models import SocialMedia


def social_media_links(request):
    return {'social_media': SocialMedia.objects.all().order_by('-ordering')}