from import_export import resources
from .models import Parent1, Parent2, Kid

class Parent1Resource(resources.ModelResource):
    class Meta:
        model = Parent1

class Parent2Resource(resources.ModelResource):
    class Meta:
        model = Parent2


class KidResource(resources.ModelResource):
    class Meta:
        model = Kid