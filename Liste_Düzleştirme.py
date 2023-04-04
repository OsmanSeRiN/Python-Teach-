liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list=list()

for i in liste:
    if type(i) is list:
        for x in i:
            if type(x) is list:
                for y in x:
                    if type(y) is list:
                        for z in y:
                            if type(z) is list:
                                print("!!!!!!!!")
                            else:
                                flatten_list.append(z)
                    else:
                        flatten_list.append(y)
            else:
                flatten_list.append(x)
    else:
        flatten_list.append(i)

print(flatten_list)