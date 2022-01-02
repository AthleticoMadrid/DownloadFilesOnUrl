import requests

# ссылка на картинку:
images_url = 'https://i.artfile.me/wallpaper/05-04-2018/1600x900/voluntari-fc-sport-emblemy-klubov-romani-1324410.jpg'
video_url = 'https://youtu.be/bo2TZdbSqqE'

# функция скачивающая изображения:
def download_images(url=''):
    try:
        response = requests.get(url=url)                    #отправляется запрос на url
        # сохранение скачанного в файл:
        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)
        return 'Image successfully downloaded!'

    except Exception as _ex:
        return 'Upps... Check the URL please!'


# функция скачивающая видео:
def download_video(url=''):
    try:
        #response = requests.get(url=url)                    #отправляется запрос на url
        # сохранение скачанного в файл:
        #with open('req_video.mp4', 'wb') as file:
        #    file.write(response.content)

        #поэтапная запись большого файла (chunk_size=1024 * 1024) - размер в байтах(1 МБайт):
        response = requests.get(url=url, stream=True)
        with open('req_video.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)
        return 'Video successfully downloaded!'

    except Exception as _ex:
        return 'Upps... Check the URL-video please!'


def main():
    print(download_images(url=images_url))
    print(download_video(url=video_url))


if __name__ == '__main__':
    main()