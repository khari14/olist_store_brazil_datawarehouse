import pyspark
import os


def load_data():
    for root, dirs, files in os.walk("H:\PyCharmProjects\olist_dw"):
        print(files)


if __name__ == '__main__':
    load_data()