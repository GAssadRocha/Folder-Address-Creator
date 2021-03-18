import pathlib, os, sys

def directory_list_creator(everything_inside_directory):
    folders_in_this_directory = []
    for item in everything_inside_directory:
        if os.path.isdir(item):
            folders_in_this_directory.append(item)
    return folders_in_this_directory 

def create_file_on(current_folder):
    f= open("address_for_this_dir.txt","w+")
    f.write(str(current_folder))
    f.close()

def go_to(current_folder):
    os.chdir(current_folder)
    current_folder = os.getcwd()
    
address_of_starting_folder = pathlib.Path().absolute()

go_to(address_of_starting_folder)
create_file_on(address_of_starting_folder)
list_of_folders_of_starting_folder = directory_list_creator(os.listdir(os.getcwd()))
print("this is list of folders of starting folder")
print(list_of_folders_of_starting_folder)

def folder_runner(list_of_folders, parent_folder):
    if list_of_folders != 0:
        for folder in list_of_folders:
            folder = str(parent_folder) + "\\" + folder
            print("Going to folder: " + folder)
            go_to(folder)
            print("Creating txt file on: " + folder)
            create_file_on(folder)
            print("This is list of folders on folder: " + folder)
            print(directory_list_creator(os.listdir(os.getcwd())))
            list_of_folders = directory_list_creator(os.listdir(os.getcwd()))
            print("folder_runner is about to run with parent_folder = " + str(folder))
            folder_runner(list_of_folders, folder)
    else:
        print("Creating txt file on :" + parent_folder)
        create_file_on(parent_folder)


folder_runner(list_of_folders_of_starting_folder, address_of_starting_folder)            


