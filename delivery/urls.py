from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.UserFormView.as_view(), name='login_user'),
    url(r'^manager/', views.AllTasksView.as_view(), name='task_list'),
url(r'^delivery/', views.delivery_person_tasks, name='delivery_person_tasks'),
url(r'^(?P<pk>[0-9]+)/$', views.task_detail, name='task_detail'),
url(r'^add/$', views.TaskCreate.as_view(), name='task_create'),
url(r'^logout/', views.logout_user, name='logout_user'),
url(r'^cancel/([0-9]+)/$', views.cancel_task, name='cancel_task'),
url(r'^accept/([0-9]+)/$', views.accept_task, name='accept_task'),
url(r'^complete/([0-9]+)/$', views.complete_task, name='complete_task'),
url(r'^decline/([0-9]+)/$', views.decline_task, name='decline_task'),
]
