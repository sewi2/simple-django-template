from url_filter.filtersets import ModelFilterSet

from . import models


class UserFilterSet(ModelFilterSet):
    class Meta:
        model = models.User
