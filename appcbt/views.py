from django.shortcuts import render
from django.views.generic.base import TemplateView
import re
# Create your views here.


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
    keywords['내과']=['내과']
    keywords['이비인후과']=['이비인후과']
    keywords['정신과']=['정신과']
    keywords['가정의학과']=['가정의학과']
    keywords['안과']=['안과']
    keywords['피부과']=['피부과']
    keywords['치과']=['치과']
    keywords['한의원']=['한의원']

    keywords['내과검색'] = ['배', '감기', '속']
    keywords['이비인후과검색'] = ['코', '목', '귀']
    keywords['정신과검색'] = ['우울증','불면']#'정신'은 '정신과'와 중복됨.
    keywords['가정의학과검색'] = ['감기', '종합']
    keywords['안과검색'] = ['눈','시력']
    keywords['피부과검색'] = ['피부가','여드름','가려움']
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

        '내과':[{'name':'강호경내과의원', 'location':'서울 동작구 상도로 348 평강빌딩','call':"02-825-6657",'time':'09:00 ~ 18:00 (13:00~14:00 휴게)','link':'none'},
                {'name':'아산바른내과의원', 'location':'서울 동작구 상도로 345 3층','call':"02-817-0028",'time':'09:00 ~ 18:00 (13:00~14:00 휴게)','link':'https://blog.naver.com/sorhk0901'},
                {'name':'유내과의원', 'location':'서울 동작구 상도로37길 74','call':"02-825-2303",'time':'09:00 ~ 18:00 (13:00~14:00 휴게)','link':'none'},
                {'name':'연세의원', 'location':'서울 동작구 상도로45길 4','call':"02-817-9226",'time':'09:00 ~ 18:00 (13:00~14:00 휴게)','link':'none'}
        ],
        '이비인후과':[{'name':'에코이비인후과의원', 'location':'서울 동작구 상도로 356 교동빌딩 2층','call':"02-814-8899",'time':'09:00 ~ 19:00 (13:00~14:00 휴게)','link':'https://www.instagram.com/ecoent_clinic'},
                {'name':'동작성모이비인후과의원', 'location':'서울 동작구 상도로 345 미사랑빌딩 2층','call':"02-825-1550",'time':'09:00 ~ 19:00 (13:00~14:00 휴게)','link':'http://www.dongjaksment.com'},
                {'name':'클린이비인후과의원', 'location':'서울 동작구 양녕로 264','call':"02-822-1000",'time':'09:10 ~ 18:30 (13:00~14:00 휴게)','link':'none'}
        ],
        '정신과':[{'name':'삼성공감정신건강의학과 동작점', 'location':'서울 동작구 상도로 345 5층','call':"02-826-9647",'time':'09:30 ~ 18:30 (13:00~14:00 휴게)','link':'http://www.sgclinic.net/sub/index.php'},
                {'name':'상도연세정신건강의학과의원', 'location':'서울 동작구 상도로 264 주유노빌딩 2층','call':"02-822-0345",'time':'09:30 ~ 18:30 (13:00~14:00 휴게)','link':'https://blog.naver.com/verydoc'}
        ],
        '가정의학과':[{'name':'정제경가정의원', 'location':'서울 동작구 상도로 297-1 김엔한스 가 3층','call':"02-815-0336",'time':'09:00 ~ 18:00 (13:00~14:00 휴게)','link':'none'},
                {'name':'연세가정의원', 'location':'서울 동작구 상도로 345 미사랑빌딩 2층','call':"02-883-7575",'time':'09:00 ~ 18:30 (13:00~14:00 휴게)','link':'http://yonseifm.modoo.at/'},
                {'name':'상도사랑가정의학과의원', 'location':'서울 동작구 양녕로 264','call':"02-822-9911",'time':'09:00 ~ 18:30 (13:00~14:00 휴게)','link':'https://blog.naver.com/sangdo268'}
        ],

        '안과':[{'name':'상도밝은안과의원', 'location':'서울 동작구 상도로 301 의암빌딩 2층','call':"02-812-2375",'time':'9:30-19:00(13:00-14:00휴게시간)','link':'https://naver.me/5pNHOhyV'},
                {'name':'드림아이안과의원', 'location':'서울 동작구 사당로 230-1','call':"0507-1441-5091",'time':'9:30-18:30(13:00-14:00휴게시간)','link':'https://naver.me/FHYu1fpG'},
                {'name':'연세안과의원', 'location':'서울 관악구 관악로 203 엔젤빌딩','call':"02-886-3800",'time':'9:00-18:30(13:00-14:00휴게시간)','link':'https://naver.me/F8Kn8ewK'},
                {'name':'연세안과의원', 'location':'서울 동작구 서달로 150 이랜드해가든 213호','call':"02-815-5008",'time':'9:30-18:30(13:00-14:00휴게시간)','link':'https://naver.me/G8UhSAEk'},
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
        '내과검색':[{'suggest':'내과 방문을 추천합니다. 저에게 내과를 물어보세요.'}],
        '이비인후과검색':[{'suggest':'이비인후과 방문을 추천합니다. 저에게 이비인후과를 물어보세요.'}],
        '정신과검색':[{'suggest':'정신과 방문을 추천합니다. 저에게 정신과를 물어보세요.'}],
        '가정의학과검색':[{'suggest':'가정의학과 방문을 추천합니다. 저에게 가정의학과를 물어보세요.'}],
        '안과검색':[{'suggest':'안과 방문을 추천합니다. 저에게 안과를 물어보세요.'}],
        '피부과검색':[{'suggest':'피부과 방문을 추천합니다. 저에게 피부과를 물어보세요.'}],
        '치과검색':[{'suggest':'치과 방문을 추천합니다. 저에게 치과를 물어보세요.'}],
        '한의원검색':[{'suggest':'한의원 방문을 추천합니다. 저에게 한의원을 물어보세요.'}],

        'fallback':'I dont quite understand. Could you repeat that?',
    }


    while (True):
        #홈화면으로부터 사용자 입력 문장을 입력받는다.
        user_input = request.GET.get('query')

        matched_intent = None
        for intent,pattern in keywords_dict.items():
            #정규식을 사용해 사용자 입력에서 키워드 추출
            if re.search(pattern, user_input):
                #키워드가 매칭되면, keyword_dict 에서 의도를 고른다.
                matched_intent=intent

        # The fallback intent is selected by default
        key='fallback'
        if matched_intent in responses:
            #키워드가 매칭되면, 응답 딕셔너리의 키로 사용된다.
            key = matched_intent

        #응답을 rsp에 저장해 home 화면으로 보낸다.
        rsp=responses[key]
        break
    return render(request,'home.html',{'response':rsp})