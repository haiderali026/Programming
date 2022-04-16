lst={"Apple","Tesla","Net Sole","Jio","Istumbul"}
lst1={"Apple":"United State Of America","Tesla":"United State Of America",
      "Net Sole":"Pakistan","Jio":"India","Istambul":"Turkey"}
def fun1(*lst,**lst1):
    for item in lst:
        print(item)
    print("\nThese are the Richest and Beautyful Place\n")
    for key,value in lst1.items():
        print(f"{key} is in {value}")

fun1(*lst,**lst1)