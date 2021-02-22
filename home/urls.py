from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("mrc/", views.mrc, name="mrc"),
    path("rules/", views.rules, name="rules"),
    path("staff/", views.staff, name="staff"),
    path("SRCrules/", views.src_rules, name="SRCrules"),
    path("STCrules/", views.stc_rules, name="STCrules"),
    path("MRCrules/", views.mrc_rules, name="MRCrules"),
    path("register/", views.register_page, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("user/settings", views.user_settings, name="usersettings"),
    path("user/<str:username>/", views.user_profile, name="userprofile"),
    path("discord/", views.discord, name="discord"),
    path("6mans/", views.sixmans, name="6mans"),
    path("hall-of-fame/", views.hall_of_fame, name="hall of fame"),
    path("merch/", views.merch, name="merch"),
    path("privacy/", views.privacy, name="privacy"),
    path("logopack/", views.logos, name="logos"),
]
