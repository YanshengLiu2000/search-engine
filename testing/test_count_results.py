num=0
print("Start working!")
with open ('test_result_1.csv', 'r') as f:
    l=f.readlines()
    for line in l:
        if 'can not find this file in results' in line:
            num+=1
            print(num)
print("End of the test")
