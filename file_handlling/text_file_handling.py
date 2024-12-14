file=open('text_file1.txt')
data=file.read()
print(data)
print("*****************************************")
seek_1=file.seek(0)
print(seek_1)
data_2=file.readline()
print(data_2)
tell=file.tell()
print(type(tell))
seek_2=file.seek(tell)
print(seek_2)
data_2=file.readline()
print(data_2)
print("*****************************************")
file.seek(0)
data_3=file.readlines()
print(data_3)
file.close()
print("*******************modes**********************")
file_2=open('text_file2.txt','r')
print(file_2.read())
file_2.close()

#print(file_2.read()) #ValueError: I/O operation on closed file.
#file_2.close()
file_2=open('text_file2.txt','r')
print(file_2.readlines())
file_2.close()
print("********************************************")
def read_file(fname,mode='r'):
    try:
        file_2 = open(fname,mode)
        return file_2.read()
    except FileNotFoundError:
        return f'{fname} File Not Found in the list'
    finally:
        file_2.close()
res=read_file('text_file2.txt', 'r')
print(res)

print("********************error handle************************")

def read_file(fname,mode='r'):
    try:
        file_2 = open(fname,mode)
        return file_2.readlines()
    except FileNotFoundError:
        return f'{fname} File Not Found in the list'
    except ValueError:
        return f'Invalid mode: {mode}. Please use a valid mode like "r".'
    except Exception as e:
        return f'Error: {e}'
    finally:
        file_2.close()
res=read_file('text_file2.txt', 'r')
print(res)

print("********************write************************")
def write_file(wfname,mode='r'):
    try:
        with open(wfname,mode) as w_data:
            return w_data.write("Mahatma Gandhi remains a global symbol of peace, \nresilience, and the power of truth and nonviolence. \nHis life and teachings continue to inspire movements for justice, equality, and freedom worldwide.")
    except ValueError:
        return f'your given this {mode} it is only take write mode'
    except Exception as e:
        f'error{e}'
res_write=write_file('test_file3','w')
print(res_write)# write() api only return num of char push the file

print("********************writeline and writelines************************")

def wline_lines(file,mode='r'):
    try:
        with open(file,mode) as fwl_wls:
            #return fwl_wls.write('hello world1\n')
            fwl_wls.writelines(["Hello, World!\n", "This is the second line.\n", "And here's the third line.\n"])
            #return fwl_wls.writelines('hello world3\n')
            return 'successfully written lines'
    except Exception as e:
        return f'file error {e}'
res_wl_wls=wline_lines('text_file.txt','w')
print(res_wl_wls)

print(open('text_file.txt').read())

print("********************append_file************************")

def apnd_file(file,mode='r'):
    try:
        with open(file,mode) as apend_data:
            apend_data.write('today is 13/12/2024 topic is cvs,json')
    except Exception as exe:
        return f'file is error {exe}'

res_apend=apnd_file('text_file.txt','a')
print(res_apend)

print("*******************r+************************")

def read_write(fff,m):
    try:
        with open(fff,m) as data_rw:
            cont=data_rw.read()
            data_rw.write('hello')
            return cont
    except Exception as e:
        return f'file error {e}'

res_rw=read_write('test_file3','r+')
print(res_rw)





print("*******************Final Task************************")
'''
use if and else condition then all 'r','w','a' modes run the code
'''

def read_fun(f_file,mode='r'):
    try:
        with open(f_file,mode) as ff:
            return ff.read()
    except Exception as e:
        return f'file error {e}'
def write_fun(f_file,mode='r'):
    user_inp=input("write something in your file: ")
    try:
        with open(f_file,mode) as ff:
            ff.write("\n")
            ff.write(user_inp)
            return 'written successfully'
    except Exception as e:
        return f'file error {e}'
def apnd_fun(f_file,mode='r'):
    user_inp = input("append something in your file: ")
    try:
        with open(f_file,mode) as ff:
            ff.write("\n")
            ff.write(user_inp)
            return 'append successfully'
    except Exception as e:
        return f'file error {e}'


inp_mode=input('enter mode: ')
if inp_mode.lower()=='r':
    res=read_fun('f_all.txt',inp_mode)
    print(res)
elif inp_mode.lower()=='w':
    res_w = write_fun('f_all.txt', inp_mode)
    print(res_w)
elif inp_mode.lower()=='a':
    res_a = apnd_fun('f_all.txt', inp_mode)
    print(res_a)