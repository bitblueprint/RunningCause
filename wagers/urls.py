from django.conf.urls import url
from wagers import views


urlpatterns = [
    url(r'^feedback/(?P<wager_id>\d+)/$', views.feedback_wager,
        name='update_wager'),

    url(r'^invite-sponsor-to-wager/(?P<person_id>\d+)$',
        views.invite_sponsor_to_wager,
        name='invite_sponsor_to_wager'),
    url(r'preview-invitation-wager/(?P<token>[a-z0-9]{32})/$',
        views.preview_invitation_wager, name='preview-invitation-wager'),

    url(r'^challenge-runner/(?P<person_id>\d+)/$',
        views.challenge_runner,
        name='challenge_runner'),
    url(r'preview-challenge/(?P<token>[a-z0-9]{32})/$',
        views.preview_challenge, name='preview_challenge'),
]
