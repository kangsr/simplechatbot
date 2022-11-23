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