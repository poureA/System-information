from os import system , getcwdb , remove 
def make_txt()->str :
    '''function docstring'''
    file_path = f'{getcwdb().decode()}\\temp.txt'
    file_temp = open(file_path,'w')
    file_temp.close()
    system(f'systeminfo > {file_path}')
    return file_path

def show_info(Dir)->dict:
    '''function docstring'''
    info = dict()
    with open(Dir , 'r') as file :
        lines = file.readlines()
        mul = 1
        for i in lines :
            idx = 0
            key = ''
            val = ''
            for ch in i :
                if ch == ':' :
                    idx = i.index(ch)
                    idx2 = int(str(idx))
                    for sub in i[idx+1:] :
                        if sub != ' ' :
                            val += i[idx2:]
                            idx2 = 0
                            break
                        idx2 += 1
                    break
                key += ch
            if key not in info.keys() :
                info[key] = val[:-1]
            else :
                add = '_'*mul
                key += add
                info[key] = val[:-1]
                mul += 1
    del info['\n']
    virtual_memory_names_old = list()
    virtual_memory_names = list()
    virtual_memory_vals = list()
    for k in info :
        if 'Virtual Memory' in k :
            if 'Max' in info[k] :
                virtual_memory_names_old.append(k)
                virtual_memory_names.append('Virtual Memory_Max')
                virtual_memory_vals.append(info[k])
            elif 'Available' in info[k] :
                virtual_memory_names_old.append(k)
                virtual_memory_names.append('Virtual Memory_Available')
                virtual_memory_vals.append(info[k])
            else :
                virtual_memory_names_old.append(k)
                virtual_memory_names.append('Virtual Memory_In_use')
                virtual_memory_vals.append(info[k])
    for i in range(len(virtual_memory_names)) :
        info[virtual_memory_names[i]] = virtual_memory_vals[i]
        del info[virtual_memory_names_old[i]]
    return info

text_file_dir = make_txt()
information = show_info(text_file_dir)
inputs = list(information.keys())
filtered_inputs = [key for key in inputs if key[0]!=' ']
print(filtered_inputs)
while ask:=input('\nSelect a factor .\nFor clear the screen please input "cls".\nfor exit please enter "exit":') :
        if ask in inputs :
            system('cls')
            print(filtered_inputs)
            print('\n')
            print(information[ask])
            idx = inputs.index(ask)
            for i in inputs[idx+1:] :
                if i[0] == ' ' :
                    print(''.join(i.split()),':')
                    print(information[i])
                else :
                    break
        else :
            if ask == 'exit' :
                remove(text_file_dir)
                break
            elif ask == 'cls' :
                system(ask)
            else :
                system('cls')
                print(filtered_inputs)
                print('\n')
                print('Please enter a valid key .')
remove(text_file_dir)