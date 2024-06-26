import os
import re
from google_drive_downloader import GoogleDriveDownloader as gdd



def get_id(url):
    # Шаблон для пошуку ID у URL Google Drive
    pattern = r'/file/d/([^/]+)/'

    # Пошук за допомогою регулярного виразу
    match = re.search(pattern, url)
    print('try to get id')

    # Перевірка, чи було знайдено ID
    if match:
        return match.group(1)  # Повертаємо знайдений ID
    else:
        return None  # Повертаємо None, якщо ID не знайдено


def download_photo(url):
    print("try to download photo")
    file_id = get_id(url)
    if not file_id:
        print("Error: Could not extract file ID from the URL.")
        return False

    dest_path = os.path.join('templates', 'uploads', 'photo.jpg')

    try:
        print('before download')
        gdd.download_file_from_google_drive(file_id=file_id, dest_path=dest_path, overwrite=True)
        print('after download')
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
            print(f"File downloaded successfully to {dest_path}")
            return True
        else:
            print(f"Error: File was not downloaded correctly to {dest_path}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

