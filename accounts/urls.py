from django.urls import path
from .views import (
    logoutUser,
    LoginView,
    RegisterTranslatorView,
    UserDetails,
    RegisterProofView,
    RegisterDesignerView,
    RegisterPublisherView,
DashboardView ,
RegisterTypesView
)
from books.views import AddUserInfoView

urlpatterns = [
    path('register/translator', RegisterTranslatorView.as_view(), name='register-translator'),
    path('register/proof', RegisterProofView.as_view(), name='register-proof'),
    path('register/design', RegisterDesignerView.as_view(), name='register-design'),
    path('register/publisher', RegisterPublisherView.as_view(), name='register-publisher'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterTypesView.as_view(), name='register'),
    path('logout', logoutUser, name='logout'),
    path('details/<int:pk>', UserDetails.as_view(), name='user-details'),
    path('dashabord', DashboardView.as_view(), name='dashboard'),
    path('userinfo/add', AddUserInfoView.as_view(), name='user-info'),

]
