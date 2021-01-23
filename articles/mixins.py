from django.core.exceptions import ImproperlyConfigured

class PageTitleMixin:
    page_title=''

    def get_page_title(self):
        return self.page_title

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['page_title']=self.get_page_title()
        return context
    


class PublicMixin:
    is_public_field='is_public'

    @property
    def get_is_public(self):
        return {self.is_public_field:True}

    def get_queryset(self):
        if self.model:
            return self.model._default_manager.filter(**self.get_is_public)
        elif self.queryset:
            return self.queryset.filter(**self.get_is_public)
        else:
            raise ImproperlyConfigured(
                '%(cls)s model is missing. Define '
                'queryset.' %{'cls': self.__class__.__name__}
            )