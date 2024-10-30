
import os
import subprocess
import datetime as dt

class CommandList:

    def all_files(self):
        p = subprocess.Popen("ls", shell = True, stdout = subprocess.PIPE)
        result = p.stdout.read()
        print(result.decode("utf-8"))

    def list_dirs(self):
        dirnames = [dir for dir in os.listdir(os.getcwd()) if os.path.isdir(dir)]
        for dirname in dirnames: 
            print(dirname)
        
        '''for dirname, dirnames, filenames in os.walk(os.getcwd()):
            for dirname in dirnames:
                print(dirname)'''

    def current_date(self):
        print(dt.datetime.now().strftime("%d-%b-%Y"))

    def current_time(self):
         print(dt.datetime.now().time().strftime("%H:%M:%S"))      

    def current_time_new(self, time_object):
        if time_object == '-hours':
            print(dt.datetime.now().time().strftime("%H"))

        elif time_object == '-mins':
            print(dt.datetime.now().time().strftime("%M"))

        elif time_object == '-secs':
            print(dt.datetime.now().time().strftime("%S"))

        else:
            raise InvalidCommand(time_object)    

    def cat_file(self, source_file):
        fobj = open(source_file, "r")
        for line in fobj:
            print(line, end="")
        fobj.close()  

    def head(self, num_items, source_file):
        fobj = open(source_file, "r")
        line = fobj.readlines()
        num_int = int(num_items.replace('-',""))
        for i in range(0, num_int):
            print(line[i])
        fobj.close()

    def tail(self, num_items, source_file):
        fobj = open(source_file, "r")
        line = fobj.readlines()
        num_int = int(num_items.replace('-',""))
        for i in range(len(line)-1, len(line)-1-num_int, -1):
            print(line[i])
        fobj.close()      

    def copy_file(self, source_file, dest_file):
        print("1")
        fobj1 = open(source_file, "r")  
        fobj2 = open(dest_file, "w") 
    
        for elem in fobj1:
            fobj2.write(elem)
        fobj1.close()
        fobj2.close()

    def remove_file(self, source_file):
        os.remove(source_file)    
        

    def empty_file(self, source_file):
        print(1)
        fobj1 = open(source_file, "w")
        fobj1.close()

    def ipconfig(self):
        p = subprocess.Popen("ipconfig getifaddr en0", shell = True, stdout = subprocess.PIPE) #MACOS
        #p = subprocess.Popen('ipconfig | findstr /i "ipv4"', shell = True, stdout = subprocess.PIPE) #WINDOWSOS

        result = p.stdout.read()
        print(result.decode("utf-8"))

        #print(os.system('ipconfig | findstr /i "ipv4"' if os.name == 'nt' else 'ipconfig getifaddr en0'))

    def pwd(self):
        return os.getcwd()

    def clear(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(f"Error: {e}")

class InvalidCommand(Exception):
    def __init__(self, element):
        self.element = element

    def __str__(self):
        return f"Shell cannot recognise {self.element} command"

def shell():
    cmd_list = CommandList()
    while True:
        command = input("shell> ").strip().split()
        newc = ' '.join(command)

        
        if len(command) == 1:
            cmd = command[0]

            if cmd == "list":
                cmd_list.all_files()
        
            elif cmd == "dirs":
                cmd_list.list_dirs()
        
            elif cmd == "date":
                cmd_list.current_date()
        
            elif cmd == "time":
                cmd_list.current_time()    
        
            elif cmd == "ipconfig":
                cmd_list.ipconfig()
        
            elif cmd == "pwd":
                print(cmd_list.pwd())
        
            elif cmd == "clear":
                cmd_list.clear()
        
            elif cmd == "exit":
                break
            
            else:
                raise InvalidCommand(newc)
        

        elif len(command) == 2:
            cmd = command[0]
            cmd1 = command[1]

            if cmd == 'time':
                cmd_list.current_time_new(cmd1)

            elif cmd == "cat":
                cmd_list.cat_file(cmd1)  
            
            elif cmd == "remove_file":
                cmd_list.remove_file(cmd1)

            elif cmd == "empty_file":
                cmd_list.empty_file(cmd1)  

            else:
                raise InvalidCommand(newc)    


        
        elif len(command) == 3:
            cmd = command[0]
            cmd1 = command[1]
            cmd2 = command[2]


            if cmd == "copy_file":
                cmd_list.copy_file(cmd1, cmd2)

            elif cmd == "head":
                cmd_list.head(cmd1, cmd2)

            elif cmd == "tail":
                cmd_list.tail(cmd1, cmd2)      

            else:
                raise InvalidCommand(newc)      

    
shell()
