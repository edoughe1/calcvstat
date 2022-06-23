import requests
import random

def get_gif(choice):
  response = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key=S0DPm2zVyeSFiD6lOG5fwP9zJKvCUeFu&q={choice}&limit=25&offset=0&rating=g&lang=en').json()
  #print(response["data"][0]["images"]["original"]["url"])
  
  num = random.randint(0,25)
  print (num)
  
  return response["data"][num]["images"]["downsized"]["url"]


def get_recommend(course, major):
  results_dict = {}
  # results_dict['src'] = get_gif('statistics')
  
  # print(response[num])
  if course == "Algebra 2" and major == "Business" or major == "Social Studies and the Humanities":
    results_dict['name'] = "Statistics"
    
  elif course == "Algebra 2" and major == "Science, Technology, Engineering, or Math" or major == "Natural Sciences":
    results_dict['name'] = "Pre-Calculus"
  elif course == "Pre-Calculus" and major == "Science, Technology, Engineering, or Math" or major == "Natural Sciences":
    results_dict['name'] = "Calculus"
  elif course == "Pre-Calculus" and major == "Business" or major == "Social Studies and the Humanities":
    results_dict['name'] = "Statistics"
  else:
    results_dict['name'] = "Either would be great for you"
  results_dict['src'] = get_gif(results_dict['name'])
  return results_dict
    