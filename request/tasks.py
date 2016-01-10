import requests


def req_url(file_name):
    """
    Функция считывает урл из файла и делает гет запросы пока не перейдет по адресу, ответ которого
    будет содержать слово "We" и выводит содержимое этого файла
    """
    with open(file_name) as inf:
        line = inf.readline().strip()

    r = requests.get(line)
    req = r.text
    while req[0] != 'W':
        url = line[:-10]+req
        r = requests.get(url)
        req = r.text
        #print(req)
    print(req)

req_url('dataset_3378_3.txt')


