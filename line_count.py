import argparse
import os.path
from os import listdir


def count_line(path, postfix):
    line_count = 0
    if os.path.isfile(path) and str(path).endswith(postfix):
        with open(path, encoding='utf-8') as fr:
            for line in fr:
                if line.strip():
                    line_count = line_count + 1
    else:
        if os.path.isdir(path):
            for sub_path in listdir(path):
                sub_path = path + '\\' + sub_path
                line_count = line_count + count_line(sub_path, postfix)
    return line_count


parser = argparse.ArgumentParser(description='Receive file postfix.')
parser.add_argument('path', type=str)
parser.add_argument('postfix', type=str, default='.py')


args = parser.parse_args()
postfix_arg = args.postfix
path_arg = args.path
print(count_line(path_arg, postfix_arg))
