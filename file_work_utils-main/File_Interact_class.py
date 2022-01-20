import io

class File_Interact():
    def __init__(self, file_path):
        self.__fileName = file_path
    
    def overwrite_file_with_content(self, content):
        f = io.open(self.__fileName, 'w', encoding = 'utf-8')
        f.write(content + '\n')
        f.close()
    
    def overwrite_file_with_list_content(self, list_content):
        f = io.open(self.__fileName, 'w', encoding = 'utf-8')
        f.write('\n'.join(list_content))
        f.close()

    def write_content_in_new_line(self, content):
        f = io.open(self.__fileName, 'a', encoding = 'utf-8')
        f.write('\n' + content + '\n')
        f.close()

    def write_list_content_in_new_line(self, list_content):
        f = io.open(self.__fileName, 'a', encoding = 'utf-8')
        f.write('\n')
        f.write('\n'.join(list_content))
        f.close()
    
    def read_content_file(self):
        f = io.open(self.__fileName, 'r', encoding ='utf-8')
        content = f.read()
        f.close()
        return content
    
    def read_list_content_file(self):
        f = io.open(self.__fileName, 'r', encoding ='utf-8')
        list_content = f.read()
        f.close()
        return list_content.split('\n')
