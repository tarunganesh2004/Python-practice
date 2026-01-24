# lex_auth_012693816757551104165


def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here
    # res=""
    # pcount,ocount,ecount=0,0,0
    # for i in range(len(patient_medical_speciality_list)):
    #     if patient_medical_speciality_list[i]=="P":
    #         pcount+=1
    #     elif patient_medical_speciality_list[i]=="O":
    #         ocount+=1
    #     elif patient_medical_speciality_list[i]=="E":
    #         ecount+=1
    # maxcount=max(pcount,ocount,ecount)
    # if maxcount==pcount:
    #     res=medical_speciality["P"]
    # elif maxcount==ocount:
    #     res=medical_speciality["O"]
    # else:
    #     res=medical_speciality["E"]
    # return res

    # optimized 
    count={"P":0,"O":0,"E":0}
    # speciality codes are at odd indices
    for i in range(1,len(patient_medical_speciality_list),2):
        count[patient_medical_speciality_list[i]]+=1
    maxcount=0
    res=""
    for key in count:
        if count[key]>maxcount:
            maxcount=count[key]
            res=medical_speciality[key]
    return res


# provide different values in the list and test your program
patient_medical_speciality_list = [301, "P", 302, "P", 305, "P", 401, "E", 656, "E"]
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)
