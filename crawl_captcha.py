import requests
import os

def crawl_images(url, save_dir, num_images):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i in range(num_images):
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(save_dir, f'{i}.png'), 'wb') as f:
                f.write(response.content)
                print(f"Image {i} downloaded successfully.")
        else:
            print(f"Failed to download image {i}. Status code: {response.status_code}")

url = "https://www.minjok.hs.kr/members/captcha.php"
save_dir = "./images"
num_images = 100

crawl_images(url, save_dir, num_images)
