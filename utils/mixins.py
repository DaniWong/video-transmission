

class AuditableFormMixin(object):
    def form_valid(self, form):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AuditableFormMixin, self).form_valid(form)


class AuditableSerializerMixin(object):

    def to_representation(self, instance):
        representation = super(AuditableSerializerMixin, self).to_representation(instance)
        representation['created_by'] = instance.created_by.username
        representation['timestamp'] = instance.timestamp
        representation['updated_by'] = instance.updated_by.username
        representation['updated_on'] = instance.updated_on
        return representation


class AuditableViewSetMixin(object):

    def perform_create(self, serializer):
        created_by = serializer.validated_data.get('created_by')
        current_user = self.request.user
        extra_params = {
            'updated_by': current_user
        }
        if not created_by:
            extra_params['created_by'] = current_user
        serializer.save(**extra_params)
