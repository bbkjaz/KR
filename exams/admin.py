from django.contrib import admin
from .models import ikexam

class ikexamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'exam_date', 'is_public')
    
    search_fields = ('title', 'users__email')
    
    list_filter = ('is_public', 'created_date', 'exam_date')
    

    filter_horizontal = ('users',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'is_public')
        }),
        ('Даты', {
            'fields': ('created_date', 'exam_date')
        }),
        ('Медиа', {
            'fields': ('image',)
        }),
        ('Пользователи', {
            'fields': ('users',)
        }),
    )
    

    date_hierarchy = 'exam_date'

admin.site.register(ikexam, ikexamAdmin)