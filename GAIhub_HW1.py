
values=list()
for i in range(5):
    values.append(input("Enter Value {} : ".format(i+1)))
for v in values:
   print("Your {}th Value >> {} \nType of the value is {} ".format(values.index(v)+1,v,type(v)))

"""
 ---- Detailed solution as follows; -----
 
for v in values:
    if v.isdigit():
        print("Your {}th Value >> {} \nType of the value is {} ".format(values.index(v) + 1, v, type(int(v))))
    else:
        try:
            float(v)
            print("Your {}th Value >> {} \nType of the value is {} ".format(values.index(v) + 1, v, type(float(v))))

        except ValueError:
            print("Your {}th Value >> {} \nType of the value is {} ".format(values.index(v) + 1, v, type(v)))
"""
