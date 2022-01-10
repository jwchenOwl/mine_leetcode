import os
from

def start():
    for root, dirs, files in os.walk('/Users/jwchen/Downloads/监测数据表'):
        for file in files:
            print(root + file)


if __name__ == '__main__':
    start()
