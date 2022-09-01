# 1. Import the requests library
import requests

# setup CID's data
music = {
    "Electric": "QmT6bCVUGA5ahw117K9zW3yUrPGGk3TU19rk45B1XHacxy",
    "Noise": "QmYeCvcTEwAax8ANZv1MmT7f9hh43jpKpA1nTPh5ipWbWX",
    "sos": "QmWPNXrAGTv4qCMfTAJedYbpjaRACVG6b6fJq4Yay1Vn8m",
    "Police_radio": "QmSeCYZrVfkAQpvs6F9zqd915mGB6aYEcgJVwDCsm5RuSU",
    "Baseball_organ": "Qma4uyNicE6qcTwCsh28WqPD7kzpL7g7S96JG7TWBLHequ"
}

for name, cid in music.items():
    URL = "https://gateway.pinata.cloud/ipfs/" + cid
    # 2. download the data behind the URL
    response = requests.get(URL)
    # 3. Open the response into a new file called instagram.ico
    open(name + ".mp3", "wb").write(response.content)
    print("\nDescargando " + name)

print("\nTodos los CID fueron descargados")
