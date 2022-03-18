from django.contrib import admin
from .models import Post


#admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)

@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message','message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['id', 'message']

    # def message_length(self, post): 
    #     return len(post.message)
    # message_length.short_description = '메시지 글자수'