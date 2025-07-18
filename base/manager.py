from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class BaseManager(models.Manager):
    def create_obj(self, **kwargs):
        return self.create(**kwargs)
    
    def get_all(self):
        return self.all()

    def get_obj_by_id(self, obj_id):
        try:
            return self.get(id = obj_id)
        except ObjectDoesNotExist:
            return None
        
    def update_obj(self, obj_id, **kwargs):
        obj = self.get_obj_by_id(obj_id)
        if obj:
            for field, value in kwargs.items():
                setattr(obj ,field,value)
            obj.save()
            return obj
        return None
    
    def delete_obj(self, obj_id):
        obj = self.get_obj_by_id(obj_id)
        if obj:
            obj.delete()
            return True
        return False