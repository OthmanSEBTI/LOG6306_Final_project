class logger :
   
    __warning = 'WARNING :'
    __error = 'ERROR :'
    count = 0

    def __init__(self,name) :
        logger.count +=1
        self.__name = name
    
    def __log__(self,type,message) :  
        self.__type = type
        if (self.__type == 'Warning'):
            print(self.__warning + message)
        if (self.__type == 'Error'):
            print(self.__error + message)


class DirectoryUser :

    def __init__(self,user,permission) :
        self.__user = user
        self.__permission = permission

    def __access_log__(self):
        if self.__permission == False :
            AccessLogger = logger('logger1')
            AccessLogger.__log__('Warning',f"{self.__user} cannot acces files in directory A")

class FileUser :

    def __init__(self,user,permission) :
        self.__user = user
        self.__permission = permission

    def __access_log__(self):
        if self.__permission == False :
            AccessLogger = logger('logger2')
            AccessLogger.__log__('Warning',f"{self.__user} cannot acces file A/file_a in directory A")

# suppose we have a user accessing the directory and the the files in directory


DirectoryUser('user A',False).__access_log__()
FileUser('user A',False).__access_log__()
print(logger.count)