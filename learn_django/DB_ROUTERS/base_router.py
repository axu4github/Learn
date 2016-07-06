
class BaseRouter(object):

    def db_for_read(self, model, **hints):
        
        if not model._meta.managed :
            return 'metadata'

        return None
