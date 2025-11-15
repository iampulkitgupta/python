import requests

def get_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        random_user = response.json().get('data')
        print("Random User:")
        print(f"Name: {random_user['name']['title']} {random_user['name']['first']} {random_user['name']['last']}")
        print(f"Username: {random_user['login']['username']}")
        print(f"Email: {random_user['email']}")
        print(f"Phone: {random_user['phone']}")
        print(f"Country: {random_user['location']['country']}")
    else:
        return None

def get_random_stock():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    headers = {"aceept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        random_stock = response.json().get('data')
        print("Random Stock:")        
        print(f"Name: {random_stock['Name']}")
        print(f"Symbol: {random_stock['Symbol']}")
        print(f"Market Cap: {random_stock['MarketCap']}")
        print(f"Current Price: {random_stock['CurrentPrice']}")        

def main():
    try:
        get_random_user()
        print("*"*50)
        get_random_stock()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
