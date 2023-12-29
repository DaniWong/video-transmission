from django.contrib import admin


class AuditableAdmin(admin.ModelAdmin):
    readonly_fields = ("created_by", "timestamp", "updated_by", "updated_on")

    def get_list_display(self, request):
        return self.list_display + self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'created_by'):
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
