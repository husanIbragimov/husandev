from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = RichTextField(
        config_name='default',
        blank=True, null=True,
        extra_plugins=['codesnippet'],
        external_plugin_resources=[('codesnippet', '/static/ckeditor/ckeditor/plugins/codesnippet/', 'plugin.js')]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
