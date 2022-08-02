from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_recent_blogs(self):
        max_count = 9 # max count for displaying post
        return Article.objects.all().order_by('-first_published_at')[:max_count]



class Article(Page):

    body = RichTextField(blank=True)

    frontImage = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("frontImage"),
        FieldPanel('body', classname="full"),
    ]





