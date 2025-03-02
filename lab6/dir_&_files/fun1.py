import os
path = input("Enter the path: ")
list_directories=[name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
list_files=[name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
list_all=os.listdir(path)
print(list_directories)
print(list_files)
print(list_all)