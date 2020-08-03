import requests

if __name__ == "__main__":
    url = 'http://15.207.99.158:6000/gettoxic'

    response =  requests.post(url)
    import pdb; pdb.set_trace()
    result = response.json()
    print(result)