print("                                         ********* Health Management System *********")
profile_option= 0
health_option= 0
file_name='\0'
def get_time():
    """This Function is for Get time and Data"""
    import datetime
    return datetime.datetime.now()
def profile():
    """This Function is for take Profile"""
    print("Please Seclect Your Profile ")
    print("Press 1 for Harry")
    print("Press 2 for Rohan")
    print("Press 3 for Hammad")
    profile_option=int(input())
    if profile_option==1:
        return "Harry"
    elif profile_option==2:
        return "Rohan"
    elif profile_option==3:
        return "Hammad"
def health():
    """This Function is for Choice """
    print("Please Choice Your Health Care")
    print("Press 1 for Diet")
    print("Press 2 for Exercise")
    health_option=int(input())
    if health_option==1:
        return "Diet"
    elif health_option==2:
        return "Exercies"
flag=True
while(flag==True):
    print("Please Enter the Mode of Working")
    print("Press 1 for Read Data ")
    print("Press 2 for Write Data ")
    file_option=int(input())
    if(file_option==2):
         print("Welcome to Write Mode")
         id_name=profile()
         plan=health()
         print("Profile Name : ",end=' ')
         print(id_name)
         file_name=str(id_name)+str(plan)+".txt"
         f=open(file_name,'a')
         Date_time=get_time()
         print("Enter Your ",plan)
         print(Date_time,end="  :  ")
         data_input=input()
         store_file=str(Date_time)+" : "+str(data_input)+'\n'
         f.write(store_file)
         f.close()
         print("Data Saved")
         break
     
     
    elif(file_option==1):
         print("Welcome to Read Mode")
         id_name=profile()
         plan=health()
         file_name=str(id_name)+str(plan)+".txt"
         print("Profile Name : ",end=' ')
         print(id_name)
         f=open(file_name,'r')
         print(f.read())
         f.close()
         break
    else:
        print("Invalid Input  Enter Again : ")
