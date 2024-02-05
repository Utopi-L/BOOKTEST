def main():
    file1=open('E:/VS codew/py4/py4.3.py/TeleAddressBook.txt',encoding='utf-8')
    file2=open('E:/VS codew/py4/py4.3.py/EmailAddressBook.txt',encoding='utf-8')
    file1.readline()
    file2.readline()
    lines1=file1.readlines()
    lines2=file2.readlines()
    list1_name=[]
    list1_tele=[]
    list2_name=[]
    list2_email=[]
    for line in lines1:
        elements =line.split()
        list1_name.append(elements[0])
        list1_tele.append(elements[1])
    for line in lines2:
        elements=line.split()
        list2_name.append(elements[0])
        list2_email.append(elements[1])
    lines=[]
    lines.append('姓名\t  电话\t  邮箱\n')
    for i in range(len(list1_name)):
        s=''
        if list1_name[i] in list2_name:
            j=list2_name.index(list1_name[i])
            s='\t'.join([list1_name[i],list1_tele[i],list2_email[j]])
            s+='\n'
        else:
            s='\t'.join([list1_name[i],list1_tele[i],'   -----   '])
            s+='\n'
        lines.append(s)
    for i in range(len(list2_name)):
        s=''
        if list2_name[i] not in list1_name:
            s='\t';join([list2_name[i],'  -----   ',list2_email[i]])
            s+='\n'
        lines.append(s)
    file3=open('E:/VS codew/py4/py4.3.py/AddressBook.txt','w',encoding='utf-8')
    file3.writelines(lines)
    file3.close()
    file1.close()
    file2.close()
    print("地址簿合并完成！")
if __name__ == "__main__":
    main()


