# Программа для скачивания изображений и видеофайлов с интернета
(Самостоятельное практическое занятие (материал взят с Youtube-канала PythonToday))

## Первый (главный) способ - main.py
Функции download_images() и download_video() с помощью библиотеки requests и по средством работы с URL-адресом файлов, скачивают разномасштабные видеофайлы и изображения. Для больших видеофайлов используется chunk, а размер в параметре chunk_size=1024 * 1024 - означает что разбивка при скачивании многомбайтного файла будет проходить по 1 МБайту

## Способ №2 - mode2.py
Во 2ом способе скачивание файлов происходит при помощи библиотеки wget и её функционала. Этот способ является неявным и имеет некоторые недостатки, особенно при работе с большими файлами.
