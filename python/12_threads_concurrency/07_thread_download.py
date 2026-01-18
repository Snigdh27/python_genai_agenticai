import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url},size: {len(resp.content)} bytes")

urls = [
    "https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsmOblbtom1QOVmsZP6wII94Rko24VuQNIvA&s",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"All downloads done in {end-start:.2f} seconds")