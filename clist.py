from typing import List
import random
import clist_api
import clist_search #todo: List all the resources and their ids sorted according to their popularity(n_accounts)

'''
codeforces = 1
leetcode = 102
codechef = 2
atcoder = 93
geeksforgeeks = 126
'''

def print_problem_info(problem_data):
    print("\n")
    print(f"Problem name :- {problem_data["name"]}")
    print(f"Problem link :- {problem_data["url"]}")
    print(f"Problem rating :- {problem_data["rating"]}")

def print_account_info(accounts):
    print("\n")
    print(f"Handle -> {accounts["handle"]}")
    print(f"Account id -> {accounts["id"]}")
    print(f"Resource -> {accounts["resource"]}")
    print(f"Resource id -> {accounts["resource_id"]}")

print("If you don't know your username, type your name. \n Then input the method number as 3 \n")
handle = str(input("Please input the username -> "))
resource_id = int(input("Please input the resource id -> "))

method = int(input("Please enter the method number -> "))

if method == 101:  #? To find the questions near your rating
    # method = 101 # int(input("Now input the method number -> "))
    rating_delta = 100
    problem_list:List = clist_api.main(handle,101,resource_id,rating_delta)
    # problem_list.sort(key=lambda x: x["rating"],reverse=False)

    for i in problem_list:
        if i["user_solved"]=="true":
            problem_list.pop(i)

    l = len(problem_list)
    random_question_numbers_list:List =  [random.randint(0, l-1) for _ in range(10)]
    for i in random_question_numbers_list:
        print_problem_info(problem_list[i])
elif method==3:
    data = clist_api.main(handle,method,resource_id)[0]
    print("\n")
    print(f"Your handle(name) is {data["handle"]}")
    print(f"Your coder id is {data["id"]}")
    print(f"You have {data["n_accounts"]} accounts")
    for i in (data["accounts"]):
        print_account_info(i)
elif method == 11:
    '''
    arr = clist_api.main(handle,method,resource_id)
    solved_in_contest = 0
    problems_in_contest = 0
    upsolved = 0
    tried = 0
    for i in arr:
        mydict = i["problems"]
        print("mydict = ",mydict)
        for letter in mydict:
            print(f"letter = {letter}")
            try:
                print(mydict["letter"]["result"])
                if "+" in (letter["result"]):
                    solved_in_contest+=1
                problems_in_contest+=1
                tried+=1
            except:
                print(mydict["letter"])
                k = mydict["letter"]["upsolving"]
                if int(k["result"])>0:
                    upsolved+=1
                tried+=1
    print(f"Problems solved in contest = {solved_in_contest}")
    print(f"Problems attempted in contest = {problems_in_contest}")
    print(f"Problems upsolved = {upsolved}")
    print(f"Problems tried = {tried}")
    '''
    print("Please wait for the next update to access this method")
else:
    print(clist_api.main(handle,method,resource_id))

