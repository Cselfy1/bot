import requests

def get_random_dog():
    endpoint = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(endpoint)
    data = response.json() 
    return data['message']

# def get_random_picture(category):
#     endpoint = f'https://api.api-ninjas'
#     response = requests.get(endpoint)
#     data = response.json() 
#     return data['message']

def get_random_picture(category):
    endpoint = f'https://picsum.photos/200/300?{category}'
    response = requests.get(endpoint)
    return response.url
