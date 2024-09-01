from django.urls import path
from user_management.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    # signup and login api
    path('login/', UserToken.as_view()),
    path('signup/', SignupView.as_view()),

    # user search api
    path('search/', UserSearchView.as_view(), name='user-search'),

    # friend request apis
    path('friend-request/send/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('friend-request/manage/<int:request_id>/', ManageFriendRequestView.as_view(), name='manage_friend_request'),
    path('friends/', ListFriendsView.as_view(), name='list_friends'),
    path('friend-requests/pending/', ListPendingFriendRequestsView.as_view(), name='list_pending_friend_requests'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)