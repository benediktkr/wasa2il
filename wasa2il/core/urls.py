from django.conf.urls import patterns
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from core.ajax.issue import issue_comment_send, issue_poll, issue_vote
from core.ajax.document import document_statement_new, document_statements_import, document_propose, document_propose_change, render_markdown, documentcontent_render_diff
from core.views import *
from core.ajax import *
from core.feeds import *
from core.models import Polity, Topic, Issue, Delegate

urlpatterns = patterns('',
    (r'^$', 'core.views.home'),
    (r'^polities/$',                    ListView.as_view(model=Polity, context_object_name="polities")),
    (r'^polity/new/$',                    login_required(PolityCreateView.as_view())),

    (r'^issue/(?P<pk>\d+)/edit/$',                        login_required(UpdateView.as_view(model=Issue, success_url="/issue/%(id)d/"))),
    (r'^issue/(?P<pk>\d+)/$',                            IssueDetailView.as_view()),

    (r'^polity/(?P<polity>\d+)/issue/new/(documentcontent/(?P<documentcontent>\d+)/)?$', login_required(IssueCreateView.as_view())),

    (r'^polity/(?P<polity>\d+)/document/$',                login_required(DocumentListView.as_view())),
    (r'^polity/(?P<polity>\d+)/document/new/$',            login_required(DocumentCreateView.as_view())),
    (r'^polity/(?P<polity>\d+)/document/(?P<pk>\d+)/$',        DocumentDetailView.as_view()),
    # (r'^polity/(?P<polity>\d+)/document/(?P<pk>\d+)/edit/$',    login_required(DocumentUpdateView.as_view())),

    (r'^polity/(?P<polity>\d+)/election/$',                ElectionListView.as_view()),
    (r'^polity/(?P<polity>\d+)/election/new/$',            login_required(ElectionCreateView.as_view())),
    (r'^polity/(?P<polity>\d+)/election/(?P<pk>\d+)/$',        ElectionDetailView.as_view()),
    (r'^polity/(\d+)/election/(?P<pk>\d+)/ballots/$', election_ballots),

    (r'^polity/(?P<pk>\d+)/edit/$',                login_required(UpdateView.as_view(model=Polity, success_url="/polity/%(id)d/"))),
    (r'^polity/(?P<pk>\d+)/(?P<action>\w+)/$',        login_required(PolityDetailView.as_view())),
    (r'^polity/(?P<pk>\d+)/$',                PolityDetailView.as_view()),

    (r'^polity/(?P<polity>\d+)/topic/new/$',        login_required(TopicCreateView.as_view())),
    (r'^polity/(?P<polity>\d+)/topic/(?P<pk>\d+)/edit/$',    login_required(UpdateView.as_view(model=Topic, success_url="/polity/%(polity__id)d/topic/%(id)d/"))),
    (r'^polity/(?P<polity>\d+)/topic/(?P<pk>\d+)/$',    TopicDetailView.as_view()),

    (r'^delegation/(?P<pk>\d+)/$',    login_required(DetailView.as_view(model=Delegate, context_object_name="delegation"))),

    (r'^feeds/json/(?P<polity>\d+)/(?P<item>.*)/$', feed_json),
    (r'^feeds/rss/(?P<polity>\d+)/(?P<item>.*)/$', feed_rss),

    (r'^api/polity/(?P<polity_id>\d+)/members/$', get_polity_members),

    (r'^api/topic/star/$', topic_star),
    (r'^api/topic/showstarred/$', topic_showstarred),

    (r'^api/issue/comment/send/$', issue_comment_send),
    (r'^api/issue/poll/$', issue_poll),
    (r'^api/issue/vote/$', issue_vote),

    (r'^api/election/poll/$', election_poll),
    (r'^api/election/vote/$', election_vote),
    (r'^api/election/candidacy/$', election_candidacy),
    (r'^api/election/showclosed/$', election_showclosed),

    (r'^api/document/statement/new/(?P<document>\d+)/(?P<type>\d+)/$', document_statement_new),
    (r'^api/document/statement/import/$', document_statements_import),
    (r'^api/document/propose/(?P<document>\d+)/(?P<state>\d+)/$', document_propose),
    (r'^api/document/propose-change/$', document_propose_change),
    (r'^api/document/render-markdown/$', render_markdown),

    (r'^api/documentcontent/render-diff/$', documentcontent_render_diff),

)

