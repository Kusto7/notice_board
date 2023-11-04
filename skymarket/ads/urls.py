from django.urls import path
from rest_framework.routers import DefaultRouter

from ads.apps import SalesConfig
from ads.views import AdViewSet, UserAdsListView, AdCommentsView, AdCommentRetrieve

ad = DefaultRouter()
ad.register(r"ads", AdViewSet, basename="ads")
app_name = SalesConfig.name

urlpatterns = [
    path("ads/me/", UserAdsListView.as_view(), name="me_ads"),
    path(
        "ads/<int:ad_id>/comments/",
        AdCommentsView.as_view({"get": "list", "post": "create"}),
        name="ad_comments",
    ),
    path(
        "ads/<int:ad_id>/comments/<int:comment_id>/",
        AdCommentRetrieve.as_view({"get": "retrieve", "patch": "change", "delete": "destroy"}),
        name="ad_comment",
    ),
] + ad.urls
