from django.contrib import admin
from django.utils.html import format_html

from member.models import Contact


class YearFilter(admin.SimpleListFilter):
    title = 'user'
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        return Contact.objects.values_list('join_year', 'join_year').distinct()

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(join_year=self.value())
        else:
            return queryset


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ContactAdmin, self).get_queryset(request)
        qs = qs.order_by('id')
        return qs

    # def thumbnail_img(self, obj):
    #     return format_html(f'<img src="{obj.thumbnail}" height="45" width="80" style="object-fit: cover;" />') if obj.thumbnail else None
    # thumbnail_img.short_description = 'thumbnail'
    # thumbnail_img.admin_order_field = 'thumbnail'

    # def user(self, obj: Contact):
    #     user: TwitterUser = TwitterUser.objects.get(
    #         user_id=obj.author_id)
    #     return format_html(f'<a href="{user.url}" target="_blank">{user.name}</a>')
    # user.short_description = 'user'
    # user.admin_order_field = 'author_id'

    # def title_link(self, obj: Contact):
    #     return format_html(f'<a href="{obj.url}" target="_blank">{obj.title}</a>')
    # title_link.short_description = 'title'
    # title_link.admin_order_field = 'title'

    # def duration_str(self, obj: Contact):
    #     return time.strftime('%H:%M:%S', time.gmtime(obj.duration))
    # duration_str.short_description = 'duration'
    # duration_str.admin_order_field = 'duration'

    # def comments(self, obj: Contact):
    #     return f'{obj.comment_count:,}' if obj.comment_count else '-'
    # comments.short_description = 'comments'
    # comments.admin_order_field = 'comment_count'

    # def views(self, obj: Contact):
    #     return f'{obj.view_count:,}' if obj.view_count else '-'
    # views.short_description = 'views'
    # views.admin_order_field = 'view_count'

    # def likes(self, obj: Contact):
    #     return f'{obj.like_count:,}' if obj.like_count else '-'
    # likes.short_description = 'likes'
    # likes.admin_order_field = 'like_count'

    list_display = [
        'id', 'name', 'student_id', 'join_year', 'role',
        'birth', 'email', 'mobile', 
        'major', 'grade', 'status', 'study_class', 
        'boj_handle', 'memo',
    ]

    list_filter = [
        YearFilter,
    ]

    # readonly_fields = [field.name for field in Contact._meta.fields]

    search_fields = [
        'name', 'mobile', 'email', 'student_id', 'major', 'role',
    ]
