class BaseRouter(object):

    def db_for_read(self, model, **hints):
        return None

    def db_for_write(self, model, **hints):
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        try:
            if model._meta.db_tablespace :
                return db == model._meta.db_tablespace
        except Exception, e:
            pass

        return db == 'default'
