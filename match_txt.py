
def first_step():
    file1 = open("arg_sh.txt", "r")
    lines = file1.readlines()

    attribs = []
    keys = []
    for line in lines:
        tmp = line.split(' ')[0]
        key = line.split(' ')[1]
        attribs.append(tmp[2:])
        keys.append(key[1:])
    file1.close()


    file2 = open("arg_full.txt", "r")
    lines = file2.readlines()
    key_list = [] # unique
    values = []
    for line in lines:
        tmp = line.split('=')[0]
        value = line.split('=')[1]
        key_list.append(tmp)
        values.append(value)
    file2.close()

    final_results = []
    for i in range(len(attribs)):
        tmp = values[key_list.index(keys[i])]
        final_results.append(tmp)

    with open('final.txt', 'w') as file:
        for attrib, val in zip(attribs, final_results):
            string = '--' + attrib + ' ' + val
            file.write(string)


def second_step():
    file1 = open("final.txt", "r")
    lines = file1.readlines()

    new_string = []
    for line in lines:
        segs = line.split(' ')
        key = segs[0]
        if len(segs) > 2:
            value = segs[1]
            for i in range(2, len(segs), 1):
                value = value + ' ' + segs[i]                  
        else:
            value = segs[-1]
        value = value[:-1] # leave \n
        
        if value.startswith("\""):
            new_string.append("\"" + key + "\", " + value + ",\n")
        elif value.startswith("\'"):
            value = value[1:-1]
            new_string.append("\"" + key + "\", \"" + value + "\",\n")
        else:
            new_string.append("\"" + key + "\", \"" + value + "\",\n")
    file1.close()
    
    with open("final_copy", 'w') as file:
        # Write each line of the string to the file
        for string in new_string:
            file.write(string)

second_step()