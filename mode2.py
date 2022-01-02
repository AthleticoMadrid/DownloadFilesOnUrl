import requests
import wget

images_wget_url = 'https://i.artfile.me/wallpaper/05-04-2018/1600x900/politehnica-timisoara-fc-sport-emblemy-k-1324408.jpg'
video_wget_url = 'https://youtu.be/hJQo5-xOi1A'


def download_wget(url='', file_type='video'):
    try:
        if file_type == 'video':
            wget.download(url=url, out=f'wget_{file_type}.mp4')           #out - имя файла которое задаём сами
        else:
            wget.download(url=url, out=f'wget_{file_type}.jpg')
    except Exception as _ex:
        return 'Upps... Check the URL please!'


def main():
    download_wget(url=images_wget_url, file_type='img')
    download_wget(url=video_wget_url, file_type='video')

if __name__ == '__main__':
    main()