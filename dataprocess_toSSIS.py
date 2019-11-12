import pyspark
import os


def main():
    current_folder = os.walk('.')

    print(current_folder)
    load_data(current_folder)


def load_data(current_folder):
    for root, dirs, files in current_folder:
        print(files)


if __name__ == '__main__':
    main()
