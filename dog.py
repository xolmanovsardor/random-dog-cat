import requests 

from config import TOKEN


class DogClient:

    def __init__(self) -> None:
        self.base_url = 'https://api.thedogapi.com'
        self.token = TOKEN

    def get_random_dog(self) -> str:
        url = f"{self.base_url}/v1/images/search?limit=2"
        headers = {
            'x-api-key': self.token
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            dog_url = data[0]['url']

            return dog_url
        else:
            raise Exception("No Dog Found")
    

dog_client = DogClient()
print(dog_client.get_random_dog())

