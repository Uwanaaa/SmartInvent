from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class BaseRepo:
    def __init__(self,model:models.Model):
        self.model = model
    def get_all(self):
        return self.model.objects.all()
    def get_one_id(self,id):
        try:
            return self.model.objects.get(id=id)
        except ObjectDoesNotExist:
            return None
    def filter(self,*args):
        return self.model.objects.filter(*args)
    def create(self,**kwargs):
        return self.model.objects.create(**kwargs)
    def update(self,id, **kwargs):
        obj = self.get_one_id(id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None
    def delete(self,id):
        obj = self.get_one_id(id)
        if obj:
            obj.delete()
            return True
        return False