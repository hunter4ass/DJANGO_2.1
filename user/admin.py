from django.contrib import admin
from .models import Request, Category

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'user', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'category', 'user', 'status')
        }),
        ('Медиа', {
            'fields': ('photo',)
        }),
        ('Дополнительно', {
            'fields': ('comment', 'created_at')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        # Если админ создает заявку и пользователь не указан, назначаем текущего админа
        if not change and not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name']
    ordering = ['name']
