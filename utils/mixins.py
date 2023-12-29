

class AuditableFormMixin(object):
    def form_valid(self, form):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AuditableFormMixin, self).form_valid(form)
