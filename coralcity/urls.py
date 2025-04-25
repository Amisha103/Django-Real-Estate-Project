
from django.contrib import admin
from django.urls import path,include
from graphene_django.views import GraphQLView
from blog.schema import schema
from pages import views
from listings import views
from accounts import views
from contacts import views
from Ages import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('AgesVerification/', include('Ages.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header ="Sky Livings panel"
admin.site.index_title ="Administrators dashboard"
admin.site.site_title ="Control panel"

