my_dic={"sell":"to give something someone exchange with money",
     "laptop":"machine which perform difficult task",
     "c++":"computer learning language",
     "led":"an output device"}
print("Here are the words :",end=" ")
print(my_dic.keys())
print("Please Enter your word : ",end=" ")
user=input()
print("Meaning of your word is : ",end=" ")
print(my_dic[user])