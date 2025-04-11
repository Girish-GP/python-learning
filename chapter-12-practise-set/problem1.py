#write a program to open three files 1.txt , 2.txt , 3.txt if any of those files are not present a message should be printed prompting the the user about the same without existing the program

def check_write_file_content(filename:str,default_content:str):
    try:
        with open(filename) as f1:
            print(f"{filename} opened in read mode with content: {f1.read()}")
    except FileNotFoundError as e:
        print(f"File {filename} not found. Creating the file with default content")    
        with open(filename,"w") as f1:
            f1.write(default_content)

check_write_file_content("1.txt","File 1")
check_write_file_content("2.txt","File 2")
check_write_file_content("3.txt","File 3")

