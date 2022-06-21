import os

def check_existing_project():
    arr = os.listdir()
    print(arr)
    for i in arr:
        if i.endswith(".json"):
            return True
        else:
            return False