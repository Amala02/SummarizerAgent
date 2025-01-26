import requests

# Your Hugging Face access token
access_token = "<ENTER_ACCESS_TOKEN"

def summarize_webpage(url):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    data = {
          "inputs": f"Summarize the content of the following URL: {url}"
      }
      
    response = requests.post(
        "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-Coder-32B-Instruct",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code} - {response.text}"


url = input("Enter url of page to be summarized")
summary = summarize_webpage(url)
print(summary)
