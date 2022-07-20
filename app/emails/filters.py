from django_filters import FilterSet

from .models import Recipient


class RecipientFilter(FilterSet):



    class Meta:
        model = Recipient
        fields = {
            'last_name': ['icontains'],
            'company': ['exact'],
            'position': ['exact'],
        }
