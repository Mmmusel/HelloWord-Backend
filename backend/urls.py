"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from helloword import userInfo as userview
from helloword import initadd as initview

from helloword import wordlist as listview
from helloword import word as wordview
import os
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from helloword import chat as chatview
from helloword import review as reviewview
from helloword import feedback as feedbackview
from helloword import email_send as emailview
from helloword import personalService as personalView
from helloword import publicList as publicListView
from helloword import reviewHistory as reviewHistoryView
from helloword import Message as messageView

urlpatterns = [
    path("admin/", admin.site.urls),

    # media
    re_path(r'^media/user_avatar/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.MEDIA_ROOT, 'user_avatar/')}),
    re_path(r'^media/user_file/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.MEDIA_ROOT, 'user_file/')}),
    re_path(r'^media/user_voice/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.MEDIA_ROOT, 'user_voice/')}),

    # personalService
    path("get_wordList_smart_from_file/", personalView.get_wordList_smart_from_file),
    path("get_wordlist_from_tags/",personalView.get_wordlist_from_tags),

    # publicList
    path("submit_official_wordlist/", publicListView.submit_official_wordlist),
    path("get_submit_wordlist/", publicListView.get_submit_wordlist),
    path("reject_submit_wordlist/",publicListView.reject_submit_wordlist),
    path("accept_submit_wordlist/",publicListView.accept_submit_wordlist),
    path("get_user_submit_wordlists/",publicListView.get_user_submit_wordlists),
    path("get_feedbacks/",publicListView.get_feedbacks),
    path("set_read_message/",publicListView.set_read_message),

    # message
    path("send_to_all/",messageView.send_to_all),
    path("send_message_to_user/",messageView.send_message_to_user),
    path("get_messages/",messageView.get_messages),
    path("set_message_state/",messageView.set_message_state),

    # reviewHistory
    path("get_record_info/",reviewHistoryView.get_record_info),
    path("get_history_record_id/",reviewHistoryView.get_history_record_id),
    path("get_story_record/",reviewHistoryView.get_story_record),
    path("get_writing_record/",reviewHistoryView.get_writing_record),
    path("get_blank_record/",reviewHistoryView.get_blank_record),

    # user
    path("login/", userview.login),
    path("register/", userview.register),
    path("cookie_login/", userview.cookie_login),
    path("get_verify_img/", userview.get_verify_img),
    path("adminLogin/", userview.adminLogin),
    path("get_vip_info/",userview.get_vip_info),
    path("logout/",userview.logout),


    path("submit_image/",userview.submit_image),
    path("change_pwd/",userview.change_pwd),
    path("get_user_info/",userview.get_user_info),
    path("get_recommend_tags/",userview.get_recommend_tags),
    path("submit_info/",userview.submit_info),
    #path("check_email_code/",emailview.check_email_code),
    path("send_email_code/",emailview.send_email_code),
    path("reset_password/", userview.reset_password),
    path("send_reset_password_email_code/", emailview.send_reset_password_email_code),
    path("change_custom/", userview.change_custom),

    # wordlist
    path("get_user_wordlists/",listview.get_user_wordlists),
    path("get_wordlist_info/",listview.get_wordlist_info),
    path("get_words_info/",listview.get_words_info),
    path("edit_wordlists/",listview.edit_wordlists),
    path("get_wordlists/",listview.get_wordlists),
    path("get_official_wordlists/",listview.get_official_wordlists),
    path("get_wordList_from_file/",listview.get_wordList_from_file),
    path("get_today_learned_words_sum/",listview.get_today_learned_words_sum),


    path("update_learn_wordlist/", listview.update_learn_wordlist),
    path("add_wordlist_from_official/", listview.add_wordlist_from_official),
    path("get_wordList_from_file/",listview.get_wordList_from_file),
    path("add_wordlist_from_file/",listview.add_wordlist_from_file),
    path("set_daily_num/",listview.set_daily_num),

    # learn word
    path("get_word_releation/", wordview.get_word_releation),
    path("group_word_learn_save/", wordview.group_word_learn_save),
    path("get_group_words_in_list/", wordview.get_group_words_in_list),
    path("get_search_word/", wordview.get_search_word),
    path("get_user_statistic/",wordview.get_user_statistic),
    path("get_new_example/",wordview.get_new_example),

    #path("reset_study_list/", wordview.reset_study_list),

    # init mysql
    #path("add_word/", initview.add_word),
    #path("add_public_list/", initview.add_public_list),
    #path("add_studylist_from_public/", initview.add_studylist_from_public),
    #path("add_relation/", initview.add_relation),
    #path("add_example/", initview.add_example),
    #path("file_to_public/",initview.file_to_public),

    # chat
    path("user_send/", chatview.user_send),
    path("submit_video/", chatview.submit_video),
    path("get_log_history/", chatview.get_log_history),
    path("get_video_history/",chatview.get_video_history),

    # review
    # blank text
    path("get_blank_text/", reviewview.get_blank_text),
    # story
    path("get_today_words/", reviewview.get_today_words),
    path("words_to_story/", reviewview.words_to_story),
    # writing
    path("writing_analysis/", reviewview.writing_analysis),
    path("sentence_analysis/", reviewview.sentence_analysis),

    path("add_feedback/",feedbackview.add_feedback),

]
