import os


"""
https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
삭제한 파일 용량 확인용 함수
"""


def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


"""
!!!삭제된 파일은 복구되지 않습니다.
파일명(숫자).확장자 하는 형식이 중복으로 다운로드 받은 파일이며
삭제해도 되는 파일이라는 것이 확실할 때 실행하시기 바랍니다.
"""


def delete_duplicate_file(directory_path):
    cnt = 0
    size = 0
    if "\\" in directory_path:
        directory_path.replace("\\", "/")
    for file_name in os.listdir(directory_path):
        if ').' in file_name:
            rt = file_name.find(').')
            lt = (file_name[:rt].rfind('('))
            if file_name[lt + 1:rt].isdigit():
                file_path = directory_path + "\\" + file_name
                size += os.path.getsize(file_path)
                cnt += 0
                print(file_name)
                os.remove(file_path)
    else:
        print("삭제한 파일 수:", cnt, end=", ")
        print("삭제된 파일 총 용량:", size)


# 삭제하고픈 디렉토리 경로를 반드시 raw string으로 입력
delete_duplicate_file(r'C:\Users\l\PycharmProjects\please-delete-duplicate-files\test')

