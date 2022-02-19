import os

#print(dir(os)) # this shows all the attributes & methods that we have within the module

#print(os.getcwd())
# cwd = os.getcwd() # O/P: current working directory: C:\Users\Avinash\PycharmProjects\pythonProject\Examples\os_module_practice
# print("current working directory:",cwd)

#
# os.chdir(r'C:/Users/Avinash/PycharmProjects/pythonProject/Examples/os_module_practice')
# print(os.getcwd()) # same as below it also works same but in this we need to copy the path here

# os.chdir('../') # or by using below method we can go one level back from current level
# print(os.getcwd())


# os.chdir(r'C:/Users/Avinash/PycharmProjects/pythonProject/Examples')
# print(os.listdir()) # o/p: ['.idea', '.pytest_cache', '25-12-2021_visu_programs', 'calculator.py', 'check_the_sum_of_num.py', 'datastructures_list_practice.py', 'datastructures_set.py', 'data_structures_dictionary_practice.py', 'date_structures_tuple.py', 'date_time program.py', 'date_time_module', 'different_print functions.py', 'exam.py', 'Exercises_geeksforgeeks.py', 'file.txt', 'interview_files', 'j1.py', 'jason.json', 'json_basics.py', 'json_practise.py', 'keywords_explaination.py', 'lambda_expressions-practice', 'mood_level.py', 'natural_num.py', 'nested_for_loop_programs.py', 'oops_practice', 'os_module_practice', 'output1.txt', 'palindrome.py', 'practice.py', 'printing_pyramid_pattern.py', 'programiz_programs.py', 'programs_practice', 'pytestpractice', 'python_type_casting.py', 'random_module.py', 'random_module_examples.py', 'rough.py', 'string_introduction.py', 'subprocess_example.py', 'task.py']
# it gives whatever the files or folders present path of the given directory


#os.chdir(r'C:/Users/Avinash/PycharmProjects/pythonProject/Examples')
# os.chdir(r"C:\Users\Avinash\Desktop")
# os.mkdir("Avinash_1/Avinash_2/ahdwjd") # it is used to create folder in the required directory
# os.makedirs("Avi_1/Avi_2/dbwbdwkjbd") # it can create more folders one inside the one in the required directory
# print(os.listdir())
# print(os.listdir())



# os.chdir(r"C:\Users\Avinash\Desktop")
# os.rmdir("Avinash_1/kfkf/jjs") # it is used to remove the last folder required folder/directory
#os.removedirs("Avi_1/Avi_2/dbwbdwkjbd/kskud/kkuuw/wbukwdwb/wdwkwhw/wwqkbkwb/wdwjbwjb/dkjdbkj") # it will remove all the folders at a time from the required directory
#print(os.listdir())
#print(os.listdir())



# os.chdir(r"C:\Users\Avinash\Desktop")
# os.rename("Avinash_1","demo_134") # it will change the current folder name with the given revised name
# print(os.listdir())

#
# os.chdir(r"C:\Users\Avinash\Desktop")
# os.mkdir("Avinash_1")
# print(os.listdir())
# print(os.stat("Avinash_1")) #by using this we get the total info of the directory and folders having in it


# by using this os.walk() method weget the details individually according to the folder and weget the details of folders inside the folders and also files inside it
# for dirpath,dirnames,filenames in os.walk(r"C:\Users\Avinash\Desktop"):
#     print(dirpath)
#     print(dirnames)
#     print(filenames)



#os.chdir(r"C:\Users\Avinash\Desktop") # this line is not mandatory
# file_path=os.path.join(r"C:\Users\Avinash\Desktop","Avinash_1") # this method is used to join the file to the path
# print(file_path) # o/p: C:\Users\Avinash\Desktop\Avinash_1


# absolute path
# if os.path.exists(r"C:\Users\Avinash\Desktop\Avinash_1"):
#     print("File already exist, no need to create.")
# else:
#     os.mkdir(r"C:\Users\Avinash\Desktop\Avinash_1")
#     print("Avinash_1 folder created.")


#os.chdir(r"C:\Users\Avinash\Desktop\Avinash_1")
file_directory=r"C:\Users\Avinash\Desktop\Avinash_1"
file_names=r"Avinash.txt",r"mahesh.txt",r"bharath.txt",r"sumanth.txt",r"visu.txt"
for file in file_names:
    file_create=os.path.join(file_directory,file)
    print(file_create)
