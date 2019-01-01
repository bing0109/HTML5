# _*_ coding: utf-8 _*_
__author__ = 'bing'
from django.conf import settings
DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING

class MyReadWriter():
    def db_for_write(self,model,**hints):
        if model._meta.app_label == 'wr_separate':
            return 'db_write1'
        if model._meta.app_label == 'wr2':
            import random
            return random.choice('db_write1')

    def db_for_read(self,model,**hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None