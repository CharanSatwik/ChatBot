import re
import long_responses as long


def msg_prob(user_msg,recognised_words,single_response=False,required_words=[]):
    message_certainity = 0
    has_req_words = True   

    #Calculates how many words are present in each predefined message
    for word in user_msg:
        if word in recognised_words:
            message_certainity += 1
    
    #Calculates the percent of required words in a user message
    percentage = float(message_certainity)/float(len(recognised_words))

    for word in required_words:
        if word not in user_msg:
            has_req_words = False
            break

    if has_req_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_msgs(message):
    highest_prob_list = {}

    #simplifies adding items to dictionary
    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = msg_prob(message,list_of_words,single_response,required_words)

    response("Hello",["hello","hi","sup","hey","heyo"],single_response=True)
    response("I\"m doing fine, and you?",["how","are","you","doing"],required_words=["how"])
    response("Thank you",["you","are","a","good","bot"],required_words=["good","bot"])
    response("See you!",["bye", "goodbye"],single_response=True)
    response("Thank you",["thanks","thank"],single_response=True)
    response(long.r_eating,["what","you","eat"],required_words=["you","eat"])
    response("I am Stacy, a simple python bot.",["who","are","you"],required_words=["who"])
    response(long.r_advice,["can","give","advice","help"],required_words=["advice"])
    response(long.r_anime,["what","best",["anime"]],required_words=["anime","is"])
    best_match = max(highest_prob_list,key=highest_prob_list.get)
    # print(highest_prob_list)  
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match 

def get_response(user_input):
    split_msg = re.split(r"\s+|[,;?!.-]\s*",user_input.lower())
    response = check_all_msgs(split_msg)
    return response
while True:
    print("Stacy: " + get_response(input("You: ")))