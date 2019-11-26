from numpy.core.defchararray import upper

# In XYZ University, upper level math classes are numbered 300 and up. 
#  level English classes are numbered 200 and up. Upper level 
#  Psychology classes are 400 and up. Create two lists, upper and lower. 
#  Assign each course in classes to the correct list, upper or lower. 
# HINT: remember, you can convert some strings to different types!

classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper = []
lower = []
for cls in classes:
    cls_data = cls.split()
    if (cls_data[0].upper() == 'ENG'):
         upper.append(cls) if int(cls_data[1]) >= 200 else lower.append(cls)  
#         
    if (cls_data[0].upper() == 'MATH'): 
        upper.append(cls) if int(cls_data[1]) >= 300 else lower.append(cls)
        
    if (cls_data[0].upper() == 'PSYCH'): 
        upper.append(cls) if int(cls_data[1]) >= 400 else lower.append(cls)
print(upper)
print(lower)
        