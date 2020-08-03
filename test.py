import requests

if __name__ == "__main__":
    url = 'https://toxicity-generator.onrender.com/gettoxic'

    response =  requests.post(url)
    import pdb; pdb.set_trace()
    result = response.json()
    pritn(result)