import time

# Node class to create linked list nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# FileEntry class to represent file and directory entries
class FileEntry:
    def __init__(self, name, mode, f_type, current_directory, past_directory=None):
        self.time = time.time() #Current Time
        self.name = name
        self.type = f_type
        self.size = 0
        self.mode = mode
        self.current_directory = current_directory
        self.past_directory = past_directory

    def format_time(self):
        formatted_time = time.strftime("%m/%d/%Y %I:%M %p", time.localtime(self.time))
        return formatted_time
   
    def setCurrentTime(self):
        self.time = time.time()

    def returnType(self):
        return self.type    

    def ls(self):
        formatted_time = self.format_time()
        print(f"{self.mode}\t\t{formatted_time}\t{self.size}\t{self.name}")
# LinkedList class to manage linked list operations
class LinkedList:
    def __init__(self):
        self.head = None
        self.currentDir = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def changeCurrentDir(self, data):
        while current:
            current.data.returnType
            if data == current.data:
                self.currentDir = data
                break
            current = current.next

    def displayAll(self):
        current = self.head
        print(f"\n\nMode\t\tLastWriteTime\t\tLength\tName")
        print("-----------------------------------------------------")

        while current:
            current.data.ls()
            current = current.next
        print("\n\n\n")
        

    def displaySelected(self):
        current = self.head
        while current:
            print(current.data.display_selected())
            current = current.next

# Directory class to represents directories
class Directory:
    def __init__(self, name):
        self.name = name
        self.time = time.time() # Current time
        self.files = LinkedList()

    def add(self, mode, f_type, current_directory, past_directory=None):
        #self.name = name
        self.type = None
        self.size = 0
        self.mode = mode
        self.files = LinkedList()
        self.current_directory = current_directory
        self.past_directory = past_directory

    def format_time(self):
        formatted_time = time.strftime("%m/%d/%Y %I:%M %p", time.localtime(self.time))
        return formatted_time
   
    def returnType(self):
        return self.type    

    def ls(self):
        formatted_time = self.format_time()
        print(f"{self.mode}\t\t{formatted_time}\t{self.size}\t{self.name}")

# FileSystem class to manages file system operations
class FileSystem:
    def __init__(self):
        self.root = Directory("C:")
        self.current_directory = self.root
        self.current_path = "C:"

    def ls(self):
        self.current_directory.files.displayAll()

    def mkdir(self, name):
        new_directory = Directory(name)
        f_type = None
        mode = "d-----"
        new_directory.add(mode, f_type, self.current_path, None)
        self.current_directory.files.add(new_directory)

    def touch(self, name, f_type):
        current_node = self.current_directory.files.head
        found = False
        while current_node:
            if name in current_node.data.name:
                found = True
                break
            current_node = current_node.next
           
        if found:
            self.current_directory.files.head.data.setCurrentTime()
        else:
            mode = "-a----"
            new_file = FileEntry(name, mode, f_type, self.current_path, None,)
            self.current_directory.files.add(new_file)

    def cd(self, name):
        if name == "":
            if self.current_directory != self.root:
                subdirectories = self.current_path.split("\\")
                self.current_directory = self.root
                self.current_path = "\\".join(subdirectories[:-1])
            else:
                print("Already at the root directory.")
        else:
            found = False
            current_node = self.current_directory.files.head
            while current_node:
                if name in current_node.data.name:
                    self.current_directory = current_node.data
                    self.current_path = f"{self.current_path}\\{current_node.data.name}"
                    found = True
                    break
                current_node = current_node.next
            if not found:
                print(f"Directory '{name}' not found.")

def main():
    file_system = FileSystem()

    choice_to_method = {
        'mkdir': file_system.mkdir,
        'touch': file_system.touch,
        'cd': file_system.cd,
        'ls': file_system.ls,
        'exit': exit
    }

    while True:
        print(f"<{file_system.current_path}>", end='')
        choice = input()

        if ' ' in choice:
            choice_components = choice.split(' ')
            var1 = choice_components[0]
            var2 = choice_components[1]
            if '.' in choice:
                choice_components = choice.split('.')
                var3 = choice_components[1]
                choice_to_method[var1](var2, var3)
            else:
                if '/' in choice:
                    choice_components = choice.split('/')
                    var4 = choice_components[1]
                    choice_to_method[var1](var4)
                else:
                    if var1 in choice_to_method:
                        if var1 == 'exit':
                            choice_to_method[var1]()  # Calls the 'exit' function
                        else:
                            choice_to_method[var1](var2)  # Calls the corresponding method with var2 as an argument
                    else:
                        print("Invalid choice.")
        else:
            if choice in choice_to_method:
                choice_to_method[choice]()  # Calls the corresponding method based on the choice
            else:
                print("Invalid Input")

if __name__ == "__main__":
    main()

