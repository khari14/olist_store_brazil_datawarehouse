import pyspark
import os


def load_data():
    for root, dirs, files in os.walk('.'):
        print(files)
        print(dirs)


if __name__ == '__main__':
    load_data()
