import csv
import os
import sys
sys.path.append('..')
from webapp import search_function
from webapp import load_models




# os.environ['PYTHONHASHSEED']=0
# This is a short instruction of this file. And change the path(you can find it in line 11) and max_num if you want. Then you can run this in your computer.

path = "/home/da_comp9900/Documents/parsed_data/"  # you should past the absolute directory of the parsed_data folder here.
max_num = 2000  # This number means how many txt files do you want to test.


def read_file(file_dir):#use transfer a txt file to a string which contains all info in the txt file.
    content_string=""
    with open(file_dir,'r') as f:
        lines=f.readlines()
        for l in lines:
            content_string+=l
    return content_string



if __name__=='__main__':
    os.environ['PYTHONHASHSEED']='0'
    print("test",os.environ['PYTHONHASHSEED'])
    index = 0#count how many files have been checked
    cant_find_num=0#count how many files have not be find in the result list.
    not_first_appear=0#count how many files have been find but not in rank #0.
    cant_find_file_name=""
    not_first_appear_file_name=""

    with open('test_result.csv','w') as f:
        writer=csv.writer(f)
        writer.writerow(['index','file_name','rank','numpy_distance','sklearn_distance'])

        for file_name in os.listdir(path):
            index += 1
            print(index)
            file_dir =os.path.join(path,file_name)
            file_content=read_file(file_dir)#read txt file
            output_result=search_function.get_results(file_content,load_models.model, load_models.dataset)
            flag = 0
            for elem in output_result:
                if elem['file_name'].replace('html','txt') == file_name:
                    if elem['rank'] != 0:
                        not_first_appear_file_name=not_first_appear_file_name+", "+file_name
                        not_first_appear+=1
                    writer.writerow([str(index), file_name, str(elem['rank']), str(elem['numpy_distance']), str(elem['sklearn_distance'])])
                    flag=1
                    break
            if not flag:
                cant_find_num+=1
                cant_find_file_name=cant_find_file_name+", "+file_name
                writer.writerow([str(index), file_name, 'can not find this file in results.'])
            if index >= max_num:
                string1=str(cant_find_num)+" files are not find in search result"
                string2=str(not_first_appear)+" files are not in the first position of the result."
                writer.writerow([string1,string2])
                writer.writerow(["Cant find list:",cant_find_file_name])
                writer.writerow(["Not in first position list:",not_first_appear_file_name])
                break

    print("test complete!")
    print(cant_find_num)
    print(not_first_appear)
    print("{} files are not find in search result       {} files are not in the first position of the result. ".format(cant_find_num,not_first_appear))






