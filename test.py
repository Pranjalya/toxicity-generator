import requests

if __name__ == "__main__":
    url = 'http://127.0.0.1:5000/gettoxic'

    response =  requests.post(url)
    result = response.json()
    pritn(result)