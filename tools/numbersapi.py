import requests as req

def url(num:int, type:str=""):
    return(f"http://numbersapi.com/{num}/{type}")

result = [req.get(url(0, "?json")) for i in range(5)]

for i in range(5):
     
 print(result[i].text)