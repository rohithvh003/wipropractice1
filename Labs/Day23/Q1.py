import requests
import threading
import time


urls = [
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.rediff.com",
    "https://www.amazon.in"
]


def downloadfiles(url):
    try:
        response = requests.get(url)
        name = url.replace("https://", "").replace("http://", "").replace("/", "_")
        filename = f"{name}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded: {filename}")

    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")


# Sequential
starttime = time.time()

for url in urls:
    downloadfiles(url)

sequentialtime = time.time() - starttime
print(f"\nSequential download time: {sequentialtime}")


# Threading
threads = []
starttime1 = time.time()

for url in urls:
    thread = threading.Thread(target=downloadfiles, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

threadingtime = time.time() - starttime1
print(f"\nThreading download time: {threadingtime}")
