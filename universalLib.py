from os.path import exists,abspath, dirname
from os import listdir, rename, makedirs, system

def CreateDirectory(directory,path):
    try:
        if not exists(path+directory):
            makedirs(path+directory)
    except OSError:
        print ('Error: Creating directory. ' +  path+directory)

def AddZerosInFileNames(path):
    file_names = listdir(path)
    frame_file_names = [file_name for file_name in file_names if file_name[:6] == "frame_" and file_name[-4:] == ".png"]
    longest_frame_file_name_length = len(sorted(frame_file_names, key=len, reverse=True)[0])

    for file_name in frame_file_names:
        if len(file_name) < longest_frame_file_name_length:
            new_file_name = "frame_" + "0" * (longest_frame_file_name_length - len(file_name)) + file_name[6:]
            rename(f"{path}/{file_name}", f"{path}/{new_file_name}")

def PrintInTerminal(text):
    system("cls")
    print(text)

def TextSplitter(text, num_of_charadters):
    text = str(text)
    sentance_list = []
    if len(text) > num_of_charadters:
        words = []
        words = text.split(" ")

        for word in words:
            if len(word) > num_of_charadters:
                return False

        total_num_letters = 0
        sentance = ""
        for word in words:
            total_num_letters = total_num_letters + len(word) + 1
            if total_num_letters <= num_of_charadters:
                if sentance == "":
                    sentance = word
                else:
                    sentance = sentance + " " + word
            else:
                sentance_list.append(sentance)
                sentance = word
                total_num_letters = len(word)
        sentance_list.append(sentance)
    else:
        sentance_list.append(text)
    return sentance_list

def SetEnvironment(name):
    system(f"conda activate {name}")

def CreateEnvironment(name):
    system(f"conda create {name}")
    system(f"conda activate {name}")