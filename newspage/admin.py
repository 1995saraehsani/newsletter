from django.contrib import admin
from newspage.models import AuthorSportPage, AuthorTechnologyPage ,AuthorPoliticPage
# Register your models here.
admin.site.register(AuthorSportPage)
admin.site.register(AuthorTechnologyPage)
admin.site.register(AuthorPoliticPage)