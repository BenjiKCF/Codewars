def is_audio(file_name):
    while ' ' not in file_name:
        if '.mp3' in file_name or '.flac' in file_name or '.alac' in file_name or '.aac' in file_name:
            return True
    else:
        return False

def is_img(file_name):
    while ' ' not in file_name:
        if '.jpg' in file_name or '.jpeg' in file_name or '.png' in file_name or '.bmp' in file_name or '.gif' in file_name:
            return True
    else:
        return False

print is_audio(" Amon Tobin.aac")
