import json
import random
import clist_api
import clist_search #todo: List all the resources and their ids sorted according to their popularity(n_accounts)
import timeit

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

            Args:
                method (int): The method identifier (101) to fetch problems.
            
            Returns:
                List[dict]: A list of 10 problems, each represented as a dictionary with the following keys:
                    - "Problem name": The name of the problem.
                    - "Problem link": The URL to the problem.
                    - "Problem rating": The difficulty rating of the problem.
            """
            rating_delta = 200
            problem_list = clist_api.main(self.handle, 101, self.resource_id, rating_delta)

            # Filter out solved problems
            unsolved_problems = []
            for problem in problem_list:
                if problem["user_solved"] != "true":
                    unsolved_problems.append(problem)

            # print(f"Unsolved problems: {unsolved_problems}")

            # Handle case where there are fewer than 10 problems
            num_to_sample = min(len(unsolved_problems), 10)

            # Randomly select problems
            sampled_problems = random.sample(unsolved_problems, num_to_sample)
            # print(f"Sampled problems: {sampled_problems}")

            # Prepare the return list
            return_list = []
            for problem in sampled_problems:
                dict_with_data_of_one_question_of_the_output = {
                    "Problem name": problem["name"],
                    "Problem link": problem["url"],
                    "Problem rating": problem["rating"],
                }
                return_list.append(dict_with_data_of_one_question_of_the_output)
 
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

if __name__=="__main__":
    start = timeit.default_timer()
    print(Main("Amritanshu_Barpanda",101,1).return_item(101))
    end = timeit.default_timer()
    print(f"Time taken to execute the code is {end-start}")