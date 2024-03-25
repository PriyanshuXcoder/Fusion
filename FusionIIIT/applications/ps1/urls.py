from django.conf.urls import url

from . import views

app_name = 'ps1'

urlpatterns = [

    url(r'^$', views.ps1, name='ps1'),
    url(r'^create_proposal/$', views.create_proposal, name='create_proposal'),
    # url(r'^compose_indent/$', views.compose_indent, name='compose_indent'),
    url(r'^composed_indents/$', views.composed_indents, name='composed_indents'),
    url(r'^indentview/(?P<id>\d+)$', views.indentview, name='indentview'),
    url(r'^drafts/$', views.drafts, name='drafts'),
    url(r'^draftview/(?P<id>\d+)$', views.draftview, name='draftview'),
    url(r'^inwardIndent/$', views.inward, name='inward'),
    url(r'^indentview2/(?P<id>\d+)$', views.indentview2, name='indentview2'),
    url(r'^confirmdelete/(?P<id>\d+)$', views.confirmdelete, name='confirm_delete'),
    url(r'^delete/(?P<id>\d+)$',views.delete, name='delete'), 
    url(r'^forwardindent/(?P<id>\d+)/$', views.forwardindent, name='forwardindent'),
    url(r'^createdindent/(?P<id>\d+)/$', views.createdindent, name='createdindent'),
    url(r'^entry/$', views.entry, name='entry'),
    url(r'^StockEntry/$', views.Stock_Entry, name='Stock_Entry'),

    # stock_view is now stock_entry_view which will tell us about the new stock that is entered in any department.
    url(r'^stock_entry_view/$', views.stock_entry_view, name='stock_view'),

    # current_stock_view will tell us about the current situation of stocks present in any department (both transferred to the department and new stocks added to the department)
    url(r'^current_stock_view/$', views.current_stock_view, name='current_stock_view'),

    # to display individual items situation from stock_entry_view page.
    url(r'^stock_entry_item_view/$', views.stock_entry_item_view, name='stock_entry_item_view'),



    url(r'^stock_delete/$', views.stock_delete, name='stock_delete'),
    url(r'^stock_edit/$', views.stock_edit, name='stock_edit'),
    url(r'^stock_update/$', views.stock_update, name='stock_update'),
    url(r'^stock_login/$', views.dealing_assistant, name='dealing_assistant'),
    url(r'^generate_report/$', views.generate_report, name='generate_report'),
    url(r'^report/$', views.report, name='report'), # !not clear 
    url(r'view-bill/<int:stock_entry_id>/$', views.view_bill, name='view_bill'),
    url(r'^perform_transfer/$', views.perform_transfer, name='perform_transfer'),
    url(r'^stock_transfer/$', views.stock_transfer, name='stock_transfer'),
    url(r'^outboxview2/$', views.outboxview2, name='outboxview2'),
    url(r'^outboxview/$', views.outboxview, name='outboxview')

]
