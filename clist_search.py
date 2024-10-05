'''import requests
from dotenv import load_dotenv
import json
import os



def get_resource_url_by_id(resource_id:int)->str:
    try:
        url = f"https://clist.by/api/v4/json/resource/{resource_id}/?username=Amritanshu&api_key={os.getenv("clist_api_key")}"
        # print(f"url = {url}")
        return url
    except:
        print(f"The problem is in get_resource_url_by_id")
        return "https://clist.by/api/v4/json/"
    
# region # API Processes

def configure():
    load_dotenv()

def pre_processing(session,url):
    r = session.get(url)
    return r.json()

def access_resource_data(resource_id:int)->str:
    configure()
    s = requests.Session()
    # username = "Amritanshu_Barpanda"
    resource_url = get_resource_url_by_id(resource_id)
    resource_url_by_id = pre_processing(s, resource_url)
    final = json.dumps(resource_url_by_id, indent=4)
    return final

def processing(handle:str,method:int,resource_id:int):
    if method==0:
        return get_user_rating_by_handle(handle,resource_id)
    if method==1:
        data = access_user_data(handle,resource_id)
        save_to_file(data)
        json_data = json.loads(data)
        # print(type(json_data))
        answer = json_data["objects"][0]
        return answer
    if method == 2:
        return get_user_id_by_handle(handle,resource_id)
    if method == 9:
        data = access_resource_data(resource_id)
        save_to_file(data)
        json_data = json.loads(data)
        # print(type(json_data))
        answer = json_data
        return answer
    if method == 10:
        return get_resource_name_by_id(resource_id)

# endregion'''