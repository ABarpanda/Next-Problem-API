import requests
from dotenv import load_dotenv
import json
import os

# region # User processes

def get_user_account_by_handle(username:str, resource_id:int)->str:
    """
    Generates a URL to access user account details from the clist.by API, given a username and a resource ID.

    Parameters:
    - username (str): The handle or username of the user whose account information is being requested.
    - resource_id (int): The ID of the resource associated with the user.

    Returns:
    - str: The complete API URL for fetching the user's account details.
      If an exception occurs, a fallback URL ("https://clist.by/api/v4/json/") is returned, and an error message is printed.

    Implementation Details:
    - Constructs the URL using the base endpoint of the clist.by API.
    - Uses environment variables for API credentials (clist_username and clist_api_key) to ensure secure and dynamic configuration.
    - Catches any exceptions during URL generation and logs a generic error message.

    Example:
    >>> get_user_account_by_handle("example_user", 123)
    """
    try:
        url = f"https://clist.by/api/v4/json/account/?username={os.getenv("clist_username")}&api_key={os.getenv("clist_api_key")}&handle={username}&resource_id={resource_id}"
        # print(url)
        return url
    except:
        print(f"The problem is in get_user_account_by_handle")
        return "https://clist.by/api/v4/json/"
    
def get_user_url_by_id(user_id:int)->str:
    """
    Generates a URL to access resource details from the clist.by API, given a user ID.

    Parameters:
    - user_id (int): The ID of the user whose resource information is being requested.

    Returns:
    - str: The complete API URL for fetching the resource details.
      If an exception occurs, a fallback URL ("https://clist.by/api/v4/json/") is returned, and an error message is printed.

    Implementation Details:
    - Constructs the URL using the base endpoint of the clist.by API.
    - Uses environment variables for API credentials (clist_username and clist_api_key) to ensure secure and dynamic configuration.
    - Catches any exceptions during URL generation and logs a generic error message.

    Example:
    >>> get_user_url_by_id(123)
    """
    try:
        url = f"https://clist.by/api/v4/json/resource/{user_id}/?username={os.getenv("clist_username")}&api_key={os.getenv("clist_api_key")}"
        return url
    except:
        print(f"The problem is in get_user_url_by_id")
        return "https://clist.by/api/v4/json/"

def get_user_id_by_handle(handle:str,resource_id:int)->int:
    """
    Retrieves the user ID associated with a specific handle and resource ID using the clist.by API.

    Parameters:
    - handle (str): The handle or username of the user.
    - resource_id (int): The ID of the resource associated with the user.

    Returns:
    - int: The user ID retrieved from the API response.
      If an exception occurs, logs an error message and returns 0.

    Implementation Details:
    - Uses a helper function `processing` to fetch and parse API data.
    - Extracts and returns the "id" field from the JSON response.

    Example:
    >>> get_user_id_by_handle("example_user", 123)
    """
    try:
        json_data = processing(handle,1,resource_id)
        return json_data["id"]
    except:
        print(f"The problem is in get_user_id_by_handle")
        return 0
    
def get_user_rating_by_handle(username:str, resource_id:int)->int:
    """
    Retrieves the user rating associated with a specific handle and resource ID using the clist.by API.

    Parameters:
    - username (str): The handle or username of the user.
    - resource_id (int): The ID of the resource associated with the user.

    Returns:
    - int: The user rating retrieved from the API response.
      If an exception occurs, logs an error message and returns 0.

    Implementation Details:
    - Uses a helper function `processing` to fetch and parse API data.
    - Extracts and returns the "rating" field from the JSON response.

    Example:
    >>> get_user_rating_by_handle("example_user", 123)
    """
    try:
        json_data = processing(username,1,resource_id)
        return json_data["rating"]
    except:
        print(f"The problem is in get_user_rating_by_handle")
        return 0

def access_user_data(username:str, resource_id:int)->str:
    """
    Accesses and retrieves detailed user data from the clist.by API in a JSON formatted string.

    Parameters:
    - username (str): The handle or username of the user.
    - resource_id (int): The ID of the resource associated with the user.

    Returns:
    - str: A JSON formatted string containing the user's account data.

    Implementation Details:
    - Calls `configure` to set up necessary configurations.
    - Initializes a `requests.Session` for HTTP requests.
    - Uses `get_user_account_by_handle` to fetch the user's account data.
    - Processes the response data using `pre_processing`.
    - Converts the processed data to a formatted JSON string.

    Example:
    >>> access_user_data("example_user", 123)
    """
    configure()
    s = requests.Session()
    # username = "{os.getenv("username")}_Barpanda"
    method = get_user_account_by_handle(username,resource_id)
    account_by_handle = pre_processing(s, method)
    final = json.dumps(account_by_handle, indent=4)
    return final
    # with open("clist_result.json", "w") as outfile:
    #     outfile.write(final)

# endregion

# region # Resource processes

def get_resource_url_by_id(resource_id:int)->str:
    """
    Generates a URL to access resource details from the clist.by API, given a resource ID.

    Parameters:
    - resource_id (int): The ID of the resource to fetch information for.

    Returns:
    - str: The complete API URL for fetching the resource details.
      If an exception occurs, a fallback URL ("https://clist.by/api/v4/json/") is returned, and an error message is printed.

    Implementation Details:
    - Constructs the URL using the base endpoint of the clist.by API.
    - Uses environment variables for API credentials (clist_username and clist_api_key) to ensure secure and dynamic configuration.
    - Catches any exceptions during URL generation and logs a generic error message.

    Example:
    >>> get_resource_url_by_id(123)
    """
    try:
        url = f"https://clist.by/api/v4/json/resource/{resource_id}/?username={os.getenv("clist_username")}&api_key={os.getenv("clist_api_key")}"
        # print(f"url = {url}")
        return url
    except:
        print(f"The problem is in get_resource_url_by_id")
        return "https://clist.by/api/v4/json/"
    
def get_resource_name_by_id(resource_id:int)->str:
    """
    Retrieves the resource name associated with a specific resource ID using the clist.by API.

    Parameters:
    - resource_id (int): The ID of the resource to fetch the name for.

    Returns:
    - str: The resource name retrieved from the API response.
      If an exception occurs, logs an error message and returns "0" as a fallback value.

    Implementation Details:
    - Uses a helper function `processing` to fetch and parse API data.
    - Extracts and returns the "name" field from the JSON response.

    Example:
    >>> get_resource_name_by_id(123)
    """
    handle = "Something"
    try:
        json_data = processing(handle,9,resource_id)
        return json_data["name"]
    except:
        print(f"The problem is in get_resource_name_by_id")
        return 0

def access_resource_data(resource_id:int)->str:
    """
    Accesses and retrieves detailed resource data from the clist.by API in a JSON formatted string.

    Parameters:
    - resource_id (int): The ID of the resource to fetch detailed information for.

    Returns:
    - str: A JSON formatted string containing the resource data.

    Implementation Details:
    - Calls `configure` to set up necessary configurations.
    - Initializes a `requests.Session` for HTTP requests.
    - Uses `get_resource_url_by_id` to fetch the resource URL.
    - Processes the response data using `pre_processing`.
    - Converts the processed data to a formatted JSON string.

    Example:
    >>> access_resource_data(123)
    """
    configure()
    s = requests.Session()
    # username = "{os.getenv("username")}_Barpanda"
    resource_url = get_resource_url_by_id(resource_id)
    resource_url_by_id = pre_processing(s, resource_url)
    final = json.dumps(resource_url_by_id, indent=4)
    return final

# endregion

# region # Problems and coder processes

def get_problems_by_handle(handle:str, resource_id:int,lt:int, gt:int,limit:int=100):
    """
    Generates a URL to fetch problems associated with a specific handle and resource, filtered by rating range.

    Parameters:
    - handle (str): The handle or username to filter problems by.
    - resource_id (int): The ID of the resource to filter problems.
    - lt (int): The upper limit for problem ratings.
    - gt (int): The lower limit for problem ratings.
    - limit (int): The maximum number of problems to fetch. Default is 100.

    Returns:
    - str: The API URL for fetching the problems.
      If an exception occurs, logs an error message and returns a fallback URL.

    Example:
    >>> get_problems_by_handle("example_user", 123, 2000, 1500, 50)
    """
    try:
        resource_name = get_resource_name_by_id(resource_id)
        url = f"https://clist.by/api/v4/json/problem/?username={os.getenv("clist_username")}&api_key={os.getenv("clist_api_key")}&limit={limit}&total_count=true&resource={resource_name}&rating__gt={gt}&rating__lt={lt}"
        # print(url)
        return url
    except:
        print(f"The problem is in get_problems_by_handle")
        return "https://clist.by/api/v4/json/"

def access_problems_data(resource_id:int,lt:int,gt:int)->str:
    """
    Accesses and retrieves problem data filtered by resource ID and rating range from the clist.by API.

    Parameters:
    - resource_id (int): The ID of the resource to filter problems.
    - lt (int): The upper limit for problem ratings.
    - gt (int): The lower limit for problem ratings.

    Returns:
    - str: A JSON formatted string containing the problems data.

    Example:
    >>> access_problems_data(123, 2000, 1500)
    """
    configure()
    s = requests.Session()
    # username = "{os.getenv("username")}_Barpanda"
    limit = 50
    problems_url = get_problems_by_handle("Something",resource_id,lt,gt,limit)
    # print(problems_url)
    problems_url_by_id = pre_processing(s, problems_url)
    final = json.dumps(problems_url_by_id, indent=4)
    return final

def get_coder_id_by_name(name:str)->str:
    """
    Generates a URL to fetch coder information by name from the clist.by API.

    Parameters:
    - name (str): The name or handle of the coder.

    Returns:
    - str: The API URL for fetching coder information.
      If an exception occurs, logs an error message and returns a fallback URL.

    Example:
    >>> get_coder_id_by_name("example_coder")
    """
    try:
        url = f"https://clist.by/api/v4/json/coder/?username={os.getenv("clist_username")}&api_key={os.getenv("clist_api_key")}&handle={name}"
        # print(url)
        return url
    except:
        print(f"The problem is in get_coder_id_by_name")
        return "https://clist.by/api/v4/json/"

def access_coder_data(handle:str)->str:
    """
    Accesses and retrieves coder information by handle from the clist.by API.

    Parameters:
    - handle (str): The handle or username of the coder.

    Returns:
    - str: A JSON formatted string containing the coder data.

    Example:
    >>> access_coder_data("example_handle")
    """
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
    """
    Generates a URL to fetch problem statistics for a specific user handle and resource ID.

    Parameters:
    - handle (str): The handle or username of the user.
    - resource_id (int): The ID of the resource to filter statistics.

    Returns:
    - str: The API URL for fetching problem statistics.
      If an exception occurs, logs an error message and returns a fallback URL.

    Example:
    >>> get_problem_stats("example_handle", 123)
    """
    try:
        account_id = get_user_id_by_handle(handle,resource_id)
        url = f"https://clist.by/api/v4/json/statistics/?username=Amritanshu&api_key={os.getenv("clist_api_key")}&with_problems=true&account_id={account_id}"
        # print(url)
        return url
    except:
        print(f"The problem is in get_problem_stats")
        return "https://clist.by/api/v4/json/"

def no_of_problems_solved(handle:str,resource_id:int)->str:
    """
    Accesses and retrieves the number of problems solved by a user from the clist.by API.

    Parameters:
    - handle (str): The handle or username of the user.
    - resource_id (int): The ID of the resource to filter statistics.

    Returns:
    - str: A JSON formatted string containing the solved problems data.

    Example:
    >>> no_of_problems_solved("example_handle", 123)
    """
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
    """
    Configures the environment by loading environment variables from a .env file.
    This function uses the load_dotenv function to load any environment variables 
    defined in a .env file into the program's environment.
    This is typically used to securely manage sensitive information like API keys 
    or database credentials in a separate file, preventing them from being hardcoded 
    in the codebase.
    """
    load_dotenv()

def pre_processing(session, url):
    """
    Fetches data from a given URL and attempts to parse the response as JSON.
    This function makes an HTTP GET request to the specified URL using the provided session.
    If the response can be successfully parsed as JSON, the function returns the parsed data.
    If parsing fails, the function handles exceptions gracefully and logs the issue.
    
    Parameters:
    - session (requests.Session): The session object to use for making HTTP requests.
    - url (str): The URL from which to fetch the data.

    Returns:
    - dict: The parsed JSON data if the request is successful and valid.
    - None: If the request fails or the JSON parsing fails, returns None.
    """
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON parsing error occurred: {json_err}")
        print(f"Response text: {response.text}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    return None

def save_to_file(data):
    """
    Saves the given data to a JSON file.
    This function takes the input data, converts it to a JSON string, and writes it to 
    a file named "clist_result.json". If the file does not already exist, it will be created.
    The function is useful for persisting data that was retrieved, allowing it to be 
    loaded later for further processing or analysis.
    
    Parameters:
    - data (str): The data to save, which is expected to be a string.
    """
    with open("clist_result.json", "w") as outfile:
        outfile.write(data)

def processing(handle: str, method: int, resource_id: int, rating_delta: int = 200):
    """
    Processes various tasks based on the method argument.
    
    Args:
        handle (str): User handle or identifier.
        method (int): Method number to specify the operation to perform.
        resource_id (int): Identifier for the resource or problem.
        rating_delta (int, optional): The range for filtering problems by rating. Default is 200.
    
    Returns:
        Depends on the method chosen, can be an integer, JSON data, or a string.
    
    Methods:
        100: Retrieve a user's rating for a specific resource.
        101: Retrieve problems based on the user's rating and rating_delta range.
        1:   Retrieve detailed user information for a specific resource.
        2:   Retrieve a user ID based on the user handle.
        3:   Retrieve coder data based on the user handle.
        9:   Retrieve data about a specific resource.
        10:  Retrieve the name of a resource by its ID.
        11:  Retrieve the number of problems solved by the user for a specific resource.
    """
    if method == 100:  # int
        """
        Retrieves a user's rating for a specific resource.
        
        Args:
            handle (str): User handle.
            resource_id (int): Identifier for the resource.
        
        Returns:
            int: User's rating.
        """
        return get_user_rating_by_handle(handle, resource_id)
    if method == 101:  # json
        """
        Retrieves problems within a rating range based on the user's rating.
        
        Args:
            handle (str): User handle.
            resource_id (int): Identifier for the resource.
        
        Returns:
            list: A list of problems in JSON format within the specified rating range.
        """
        rating = processing(handle, 100, resource_id)
        # print("rating = ", rating)
        lt = rating  # + rating_delta
        gt = rating - rating_delta
        data = access_problems_data(resource_id, lt, gt)
        save_to_file(data)
        json_data = json.loads(data)
        answer = json_data["objects"]
        return answer
    if method == 1:  # json
        """
        Retrieves detailed user information for a specific resource.
        
        Args:
            handle (str): User handle.
            resource_id (int): Identifier for the resource.
        
        Returns:
            dict: User information in JSON format.
        """
        data = access_user_data(handle, resource_id)
        save_to_file(data)
        json_data = json.loads(data)
        answer:dict = json_data["objects"][0]
        return answer
    if method == 2:  # int
        """
        Retrieves a user ID based on the user handle.
        
        Args:
            handle (str): User handle.
            resource_id (int): Identifier for the resource.
        
        Returns:
            int: User ID.
        """
        return get_user_id_by_handle(handle, resource_id)
    if method == 3:  # json
        """
        Retrieves coder data based on the user handle.
        
        Args:
            handle (str): User handle.
        
        Returns:
            list: Coder data in JSON format.
        """
        data = access_coder_data(handle)
        save_to_file(data)
        json_data = json.loads(data)
        answer = json_data["objects"]
        return json_data
    if method == 9:  # json
        """
        Retrieves data about a specific resource.
        
        Args:
            resource_id (int): Identifier for the resource.
        
        Returns:
            dict: Resource data in JSON format.
        """
        data = access_resource_data(resource_id)
        save_to_file(data)
        json_data = json.loads(data)
        answer = json_data
        return answer
    if method == 10:  # str
        """
        Retrieves the name of a resource by its ID.
        
        Args:
            resource_id (int): Identifier for the resource.
        
        Returns:
            str: Resource name.
        """
        return get_resource_name_by_id(resource_id)   
    if method == 11:  # json
        """
        Retrieves the number of problems solved by the user for a specific resource.
        
        Args:
            handle (str): User handle.
            resource_id (int): Identifier for the resource.
        
        Returns:
            list: Problems solved data in JSON format.
        """
        data = no_of_problems_solved(handle, resource_id)
        save_to_file(data)
        json_data = json.loads(data)
        answer = json_data["objects"]
        return answer
# endregion

# handle = input("Please input the username -> ")
# resource_id = int(input("Please input the resource id -> "))
# method = int(input("Now input the method number -> "))

def main(handle:str,method:int,resource_id:int,rating_delta:int=100):
    return processing(handle,method,resource_id,rating_delta)

if __name__ =="__main__":
    print(main("Amritanshu_Barpanda",101,1))