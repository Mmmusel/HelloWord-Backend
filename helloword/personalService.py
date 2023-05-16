
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json
import datetime
from helloword.models import Word,UserInfo,FileInfo,UserStudyWordInfo
from helloword.models import WordList,WordListItem,UserStudyList,UserStudyListItem
from helloword.userInfo import checkCookie, wrapRes
from chatgpt import client
from chatgpt.tools import wordlist, utils
import pdfplumber
import re
from zhon.hanzi import punctuation


def get_wordList_smart_from_file(request):

    response = {}
    response['state'] = False

    try:
        file = request.FILES.get('file')
        newfile = FileInfo(file_info=file)
        newfile.save()

        filepath = 'media/'+str(newfile.file_info)
        print(filepath)

        content = ''
        with pdfplumber.open(filepath) as pdf:
            page_num = 1
            words = []
            for page in pdf.pages:
                if page_num > 3:
                    break
                else:
                    page_num += 1
                mv_chinese = re.sub('[\u4e00-\u9fa5]', '', page.extract_text())
                words.append(re.sub("[{}]+".format(punctuation), "", mv_chinese))

            content=' '.join(words)
            print(content)

        message = wordlist.gen_wordlist_from_passage(words)
        rcv_message = client.Client().send_message(message)
        extract_words = str(re.findall(r"[(](.*?)[)]", rcv_message)[0]).split(',')

        lower_extract_words=[]
        for i in extract_words:
            lower_extract_words.append(i.lower())

        response['words']=lower_extract_words

        ret = []
        word_list = Word.objects.filter(word__in=lower_extract_words)
        if word_list.count()==0:
            response['msg']='输入文件不包含有效单词'
            return JsonResponse(response)

        for k in word_list:
            cur = {
                'wordId':k.id,
                'word':k.word,
                'meaning':k.definition_cn.replace("\\n","\n").replace("\\r","")
            }
            ret.append(cur)

        response['wordlist']=ret
        response['state'] = True
        response['msg'] = '词单导入成功'


    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)