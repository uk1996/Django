from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe


#admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)

@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message','message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['id', 'message']

    def photo_tag(self, post):
        if post.photo:
           return mark_safe(f"<img src = '{post.photo.url}' style='width: 75px;' />")
        return None

    # def message_length(self, post): 
    #     return len(post.message)
    # message_length.short_description = '메시지 글자수'