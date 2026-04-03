import httpx

def get_quote():
    response = httpx.get(url="https://stoic.tekloon.net/stoic-quote")
    quote = response.json()["data"]["quote"]
    return quote

if __name__ == "__main__":
    get_quote()