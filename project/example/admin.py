import logging

from django.apps import apps
from django.contrib import admin

logger = logging.getLogger(__name__)

models = apps.get_models('project.example')

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered as e:
        logger.warning(e)

# class DocumentsSignsTaskCreationForm(forms.ModelForm):
#     class Meta:
#         model = example_models.User
#         fields = '__all__'
