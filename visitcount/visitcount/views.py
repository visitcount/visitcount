from django.db import transaction
from django.views.generic import DetailView

from .models import Item, ItemView
from .common.user_uid import get_user_uid, make_user_uid, set_user_uid_cookie


class ItemDetail(DetailView):

    model = Item

    def get(self, *args, **kwargs):
        with transaction.atomic():
            self.object = self.get_object()
            
            cookie_is_set = True
            user_uid = get_user_uid(self.request)
            if user_uid is None:
                cookie_is_set = False
                user_uid = make_user_uid(self.request)
            counted_view, created = ItemView.objects.get_or_create(item=self.object, user_uid=user_uid)
            if created:
                self.object.view_count += 1
                self.object.save()
        
        context = self.get_context_data(object=self.object)
        response = self.render_to_response(context)
        
        if not cookie_is_set:
            set_user_uid_cookie(response, user_uid)

        return response

    def get_queryset(self):
        return self.model._default_manager.select_for_update()
