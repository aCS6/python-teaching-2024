import sys
import os


file_path = os.path.abspath(__file__)
parent_path = os.path.dirname(file_path)
root_path = os.path.dirname(parent_path)

# print(parent_path)
# print(root_path)


sys.path.append(root_path)
from server.one import hello

hello("python")