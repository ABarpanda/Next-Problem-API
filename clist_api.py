import requests
from dotenv import load_dotenv
import json
import os

# region # User processes

def get_user_account_by_handle(username:str, resource_id:int):
    '''
    This 
    '''
    try:
        url = f"https://clist.by/api/v4/json/account/?username=Amritanshu&api_key={os.getenv("clist_api_key")}&handle={username}&resource_id={resource_id}"
        return url
    except:
        print(f"The problem is in get_user_account_by_handle")
        return "https://clist.by/api/v4/json/"
    
def get_user_url_by_id(user_id:int):
    try:
        url = f"https://clist.by/api/v4/json/resource/{user_id}/?username=Amritanshu&api_key={os.getenv("clist_api_key")}"
        return url
    except:
        print(f"The problem is in get_user_url_by_id")
        return "https://clist.by/api/v4/json/"

def get_user_id_by_handle(handle:str,resource_id:int)->int:
    try:
        json_data = processing(handle,1,resource_id)
        return json_data["id"]
    except:
        print(f"The problem is in get_user_id_by_handle")
        return 0
    
def get_user_rating_by_handle(username:str, resource_id:int)->int:
    try:
        json_data = processing(username,1,resource_id)
        return json_data["rating"]
    except:
        print(f"The problem is in get_user_rating_by_handle")
        return 0

def access_user_data(username:str, resource_id:int)->str:
    configure()
    s = requests.Session()
    # username = "Amritanshu_Barpanda"
    method = get_user_account_by_handle(username,resource_id)
    account_by_handle = pre_processing(s, method)
    final = json.dumps(account_by_handle, indent=4)
    return final
    # with open("clist_result.json", "w") as outfile:
    #     outfile.write(final)

# endregion

# region # Resource processes

def get_resource_url_by_id(resource_id:int)->str:
    try:
        url = f"https://clist.by/api/v4/json/resource/{resource_id}/?username=Amritanshu&api_key={os.getenv("clist_api_key")}"
        # print(f"url = {url}")
        return url
    except:
        print(f"The problem is in get_resource_url_by_id")
        return "https://clist.by/api/v4/json/"
    
def get_resource_name_by_id(resource_id:int)->str:
    handle = "Something"
    try:
        json_data = processing(handle,9,resource_id)
        return json_data["name"]
    except:
        print(f"The problem is in get_resource_name_by_id")
        return 0

def access_resource_data(resource_id:int)->str:
    configure()
    s = requests.Session()
    # username = "Amritanshu_Barpanda"
    resource_url = get_resource_url_by_id(resource_id)
    resource_url_by_id = pre_processing(s, resource_url)
    final = json.dumps(resource_url_by_id, indent=4)
    return final

# endregion

# region # Problems and coder processes

def get_problems_by_handle(handle:str, resource_id:int,lt:int, gt:int,limit:int=100):
    try:
        resource_name = get_resource_name_by_id(resource_id)
        url = f"https://clist.by/api/v4/json/problem/?username=Amritanshu&api_key={os.getenv("clist_api_key")}&limit={limit}&total_count=true&resource={resource_name}&rating__gt={gt}&rating__lt={lt}"
        # print(url)
        return url
    except:
        print(f"The problem is in get_problems_by_handle")
        return "https://clist.by/api/v4/json/"

def access_problems_data(resource_id:int,lt:int,gt:int)->str:
    configure()
    s = requests.Session()
    # username = "Amritanshu_Barpanda"
    limit = 50
    problems_url = get_problems_by_handle("Something",resource_id,lt,gt,limit)
    # print(problems_url)
    problems_url_by_id = pre_processing(s, problems_url)
    final = json.dumps(problems_url_by_id, indent=4)
    return final

def get_coder_id_by_name(name:str)->str:
    try:
        url = f"https://clist.by/api/v4/json/coder/?username=Amritanshu&api_key={os.getenv("clist_api_key")}&handle={name}"
        # print(url)
        return url
    except:
        print(f"The problem is in get_coder_id_by_name")
        return "https://clist.by/api/v4/json/"

def access_coder_data(handle:str)->str:
    configure()
    s = requests.Session()
    # username = "Amritanshu_Barpanda"
    limit = 50
    url = get_coder_id_by_name(handle)
    # print(url)
    url_by_name = pre_processing(s, url)
    final = json.dumps(url_by_name, indent=4)
    return final

def get_problem_stats(handle:str, resource_id:int)->str:
    try:
        account_id = get_user_id_by_handle(handle,resource_id)
        url = f"https://clist.by/api/v4/json/statistics/?username=Amritanshu&api_key={os.getenv("clist_api_key")}&with_problems=true&account_id={account_id}"
        print(url)
        return url
    except:
        print(f"The problem is in get_problem_stats")
        return "https://clist.by/api/v4/json/"

def no_of_problems_solved(handle:str,resource_id:int)->str:
    configure()
    s = requests.Session()
    # username = "Amritanshu_Barpanda"
    problems_url = get_problem_stats(handle,resource_id)
    # print(problems_url)
    problems_url_by_id = pre_processing(s, problems_url)
    final = json.dumps(problems_url_by_id, indent=4)
    return final

# endregion

# region # API Processes

def configure():
    load_dotenv()

def pre_processing(session,url):
    r = session.get(url)
    try:
        return r.json()
    except:
        print(r.text)

def save_to_file(data):
    with open("clist_result.json", "w") as outfile:
        outfile.write(data)

def processing(handle:str,method:int,resource_id:int, rating_delta:int=100):
    if method==100: #int
        return get_user_rating_by_handle(handle,resource_id)
    if method==101: #json
        rating = processing(handle,100,resource_id)
        print("rating = ",rating)
        lt = rating + rating_delta
        gt = rating - rating_delta
        data = access_problems_data(resource_id, lt, gt)
        save_to_file(data)
        json_data = json.loads(data)
        answer = json_data["objects"]
        return answer
    if method==1: #json
        data = access_user_data(handle,resource_id)
        # print(data)
        save_to_file(data)
        json_data = json.loads(data)
        # print(type(json_data))
        answer = json_data["objects"][0]
        return answer
    if method == 2: #int
        return get_user_id_by_handle(handle,resource_id)
    if method == 3: #json
        data =  access_coder_data(handle)
        # print(data)
        save_to_file(data)
        json_data = json.loads(data)
        # print(type(json_data))
        answer = json_data["objects"]
        return answer
    if method == 9: #json
        # print(f"Resource id = {resource_id}")
        # print(type(resource_id))
        data = access_resource_data(resource_id)
        save_to_file(data)
        json_data = json.loads(data)
        # print(type(json_data))
        answer = json_data
        return answer
    if method == 10: #str
        return get_resource_name_by_id(resource_id)
    if method == 11: #json
        data =  no_of_problems_solved(handle,resource_id)
        # print(data)
        save_to_file(data)
        json_data = json.loads(data)
        # print(type(json_data))
        answer = json_data["objects"]
        return answer

# endregion

# handle = input("Please input the username -> ")
# resource_id = int(input("Please input the resource id -> "))
# method = int(input("Now input the method number -> "))
def main(handle:str,method:int,resource_id:int,rating_delta:int=100):
    return processing(handle,method,resource_id,rating_delta)

# if __name__ =="__main__":
#     main()