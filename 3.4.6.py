import re
import requests
A = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
B = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
#A, B = input().rstrip(), input().rstrip()

request = requests.get(A)
print(request.status_code)
print(request.content)
print(request.text)
if request.status_code == 200:
    lst = re.findall(r'<a href.*html+', request.text)
print(lst)
if len(lst) > 0:
    yes_result = False
    for _ in lst:
        link = re.search(r"http.*html+", _).group()
        print(link)
        request = requests.get(link)
        if request.status_code != 200:
            continue
        if 'a href="' + B in request.text:
            yes_result = True
            break
    print("Yes") if yes_result else print("No")