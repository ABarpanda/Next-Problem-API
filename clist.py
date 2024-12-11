from typing import List
import json
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

class Main:
    def __init__(self, handle, method, resource_id):
        self.handle = handle
        self.method = method
        self.resource_id = resource_id

    def return_item(self, method:int):
        if method == 101:  #? To find the questions near your rating
            """
            Fetches a list of problems near the user's rating, filters unsolved problems, 
            and returns 10 random problems with details.

            How it works:
            - Fetches problems within a `rating_delta` range around the user's rating.
            - Removes problems already solved by the user.
            - Randomly selects 10 problems from the remaining list.
            - Prepares and returns a list of dictionaries containing details of each problem.
            
            Args:
                method (int): The method identifier (101) to fetch problems.
            
            Returns:
                List[dict]: A list of 10 problems, each represented as a dictionary with the following keys:
                    - "Problem name": The name of the problem.
                    - "Problem link": The URL to the problem.
                    - "Problem rating": The difficulty rating of the problem.
            """
            rating_delta = 200
            problem_list:List = clist_api.main(self.handle,101,self.resource_id,rating_delta)
            # problem_list.sort(key=lambda x: x["rating"],reverse=False)

            for i in problem_list:
                if i["user_solved"]=="true":
                    problem_list.pop(i)

            l = len(problem_list)
            random_question_numbers_list:List =  random.sample(range(l), 10)
            # print(random_question_numbers_list)
            return_list = []
            for i in random_question_numbers_list:
                # print_problem_info(problem_list[i])
                dict_with_data_of_one_question_of_the_output = {}
                problem_data = problem_list[i]
                dict_with_data_of_one_question_of_the_output["Problem name"] = problem_data["name"]
                dict_with_data_of_one_question_of_the_output["Problem link"] = problem_data["url"]
                dict_with_data_of_one_question_of_the_output["Problem rating"] = problem_data["rating"]
                return_list.append(dict_with_data_of_one_question_of_the_output)
            # print(return_list)
            return return_list
        elif method == 100: # dict #? Retrieve a user's rating for a specific resource
            return {"User Rating" : clist_api.main(self.handle,100,self.resource_id)}
        # elif method == 1: # dict
        #     return clist_api.main(self.handle,1,self.resource_id)
        # elif method == 2: # int
        #     return clist_api.main(self.handle,2,self.resource_id)
        # elif method == 3: 
        else:
            return clist_api.main(self.handle,self.method,self.resource_id)