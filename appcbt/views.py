from django.shortcuts import render
from django.views.generic.base import TemplateView
import re
# Create your views here.

class gohomeview(TemplateView):
    template_name = ''
def gohome(request):
    return render(request, 'home.html', {request:' '})
def userin(request):
    keywords={}
    keywords_dict={}

    #########################################
    keywords['내과']=['내과','내과의원']
    keywords['치과']=['치과','치과의원']
    keywords['내과검색'] = ['배']

    ##
    keywords['안과']=['안과']
    keywords['피부과']=['피부과']
    keywords['치과']=['치과']
    keywords['한의원']=['한의원']

    keywords['안과검색'] = ['눈','시력']
    keywords['피부과검색'] = ['여드름','가려움']
    keywords['치과검색'] = ['충치','잇몸']
    keywords['한의원검색'] = ['한약']
    ##
    #여기 키워드를 추가해주세요
    ###########################################

    for intent, keys in keywords.items():
        # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
        keywords_dict[intent]=re.compile('|'.join(keys))
        print (keywords_dict)
    responses={
        'greet':'Hello! How can I help you?',
        'timings':'We are open from 9AM to 5PM, Monday to Friday. We are closed on weekends and public holidays.',
        '내과':[{'name':'내과이름1', 'location':'숭실대근처','call':"02-1234-1234",'time':'시간','link':'https://blog.naver.com/mrtop2020'},
                {'name':'내과이름2', 'location':'숭실대근처','call':"02-1234-1234",'time':'시간','link':'https://blog.naver.com/mrtop2020'}
        ],
        '치과':[{'name':'치과이름1', 'location':'숭실대근처','call':"02-1234-1234",'time':'시간','link':'https://blog.naver.com/mrtop2020'},
                {'name':'치과이름2', 'location':'숭실대근처','call':"02-1234-1234",'time':'시간','link':'https://blog.naver.com/mrtop2020'}
        ],
        '내과검색':[{'suggest':'내과 방문을 추천합니다. 저에게 내과를 물어보세요.'}],
        ##
        '안과':[{'name':'상도밝은안과의원', 'location':'서울 동작구 상도로 301 의암빌딩 2층','call':"02-812-2375",'time':'9:30-19:00(13:00-14:00휴게시간)','link':'https://naver.me/5pNHOhyV'},
                {'name':'드림아이안과의원', 'location':'서울 동작구 사당로 230-1','call':"0507-1441-5091",'time':'9:30-18:30(13:00-14:00휴게시간)','link':'https://naver.me/FHYu1fpG'},
                {'name':'연세안과의원', 'location':'서울 관악구 관악로 203 엔젤빌딩','call':"02-886-3800",'time':'9:00-18:30(13:00-14:00휴게시간)','link':'https://naver.me/F8Kn8ewK'},
                {'name':'연세안과의원', 'location':'서울 동작구 서달로 150 이랜드해가든 213호','call':"02-815-5008",'time':'9:30-18:30(13:00-14:00휴게시간)','link':'https://naver.me/G8UhSAEk'},
                #{'name':'내과이름2', 'location':'숭실대근처','call':"번호",'time':'시간','link':'링크'},
        ],
        '피부과':[{'name':'삼성피부과산부인과', 'location':'서울 동작구 상도로 356','call':"02-816-3352",'time':'9:30-18:30(13:00-14:00휴게시간)','link':'https://naver.me/FZJ2bPvS'},
                {'name':'제일의원', 'location':'서울 동작구 양녕로 195 약수당약국','call':"02-815-0179",'time':'9:00-18:30(13:00-14:00휴게시간)','link':'https://naver.me/5X929rGF'},
                {'name':'마이닥터의원', 'location':'서울 동작구 사당로14길 13 골든빌딩 2층','call':"02-522-1020",'time':'10:00-20:00(13:00-14:00휴게시간)','link':'https://naver.me/56I21AGF'},
                {'name':'김재준피부과의원', 'location':'서울 관악구 관악로 231-1','call':"02-887-8517",'time':'10:00-18:30(13:00-14:00휴게시간)','link':'https://naver.me/51YnP8TE'},


        ],
        '치과':[{'name':'자작나무치과의원', 'location':'서울 동작구 상도로 347 2층','call':"번호",'02-825-7522':'10:00-18:00(13:00-14:00휴게시간)','link':'https://naver.me/5aVpGtoh'},
                {'name':'서울본치과의원', 'location':'서울 동작구 상도로53길 13 래미안상도3차아파트','call':"02-3280-2875",'time':'9:30-18:30(13:00-14:00휴게시간)','link':'https://naver.me/GNy3DAeB'},
                {'name':'서울미소치과의원', 'location':'서울 동작구 사당로 196 거묵프리미엄 상가','call':"02-598-2875",'time':'10:00-17:30(13:00-14:00휴게시간)','link':'https://naver.me/xnKngSW6'},
                {'name':'연세채움치과의원', 'location':'서울 동작구 상도로 356 교동빌딩 5층','call':"0507-1322-5753",'time':'9:30-18:30(13:00-14:00휴게시간)','link':'https://naver.me/FHYlxCNn'},

        ],
        '한의원':[{'name':'상도하늘애한의원', 'location':'서울 동작구 상도로 346 우일빌딩 2층','call':"0507-1489-1075",'time':'9:30-20:30(13:00-14:00휴게시간)','link':'https://naver.me/FUGL9bxH'},
                {'name':'정현한의원', 'location':'서울 동작구 상도로 376-1','call':"02-825-7575",'time':'9:30-20:30(13:00-14:00휴게시간)','link':'https://naver.me/IIfqouxd'},
                {'name':'인의한의원', 'location':'서울 동작구 상도로37길 76 리치타운','call':"02-824-0075",'time':'9:30-19:00(13:00-14:00휴게시간)','link':'https://naver.me/xpPaScrA'},
                {'name':'경희당한의원', 'location':'서울 동작구 상도로53길 13 래미안상도3차아파트','call':"02-826-7900",'time':'9:30-18:00(13:00-14:00휴게시간)','link':'https://naver.me/xmru9oo0'},

        ],
        '안과검색':[{'suggest':'안과 방문을 추천합니다. 저에게 안과를 물어보세요.'}],
        '피부과검색':[{'suggest':'피부과 방문을 추천합니다. 저에게 피부과를 물어보세요.'}],
        '치과검색':[{'suggest':'치과 방문을 추천합니다. 저에게 치과를 물어보세요.'}],
        '한의원검색':[{'suggest':'한의원 방문을 추천합니다. 저에게 한의원을 물어보세요.'}],
        ##여기 병원 정보를 추가해주세요
        #########################################################################
        'fallback':'I dont quite understand. Could you repeat that?',
    }


    print ("Welcome to MyBank. How may I help you?")
    print(request.GET)
    # While loop to run the chatbot indefinetely
    while (True):
        # Takes the user input and converts all characters to lowercase
        # user_input = input().lower()
        user_input = request.GET.get('query')
        # Defining the Chatbot's exit condition
        if user_input == 'quit':
            print ("Thank you for visiting.")
            break
        matched_intent = None
        for intent,pattern in keywords_dict.items():
            # Using the regular expression search function to look for keywords in user input
            if re.search(pattern, user_input):
                # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
                matched_intent=intent
        # The fallback intent is selected by default
        key='fallback'
        if matched_intent in responses:
            # If a keyword matches, the fallback intent is replaced by the matched intent as the key for the responses dictionary
            key = matched_intent
        # The chatbot prints the response that matches the selected intent
        print (responses[key])
        rsp=responses[key]
        break
    return render(request,'home.html',{'response':rsp})