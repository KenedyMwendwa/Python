friendNames= {
    0: "Munaa1 namba imwe ni mum",
    "Mulinge": "Mbulwa ethaw'a munaa wakwa ki.",
    2: "Tii",
    3: "Kimuu",
    4: "Briyo",
    5: "Meshack",
    6: "Octo",
}


#checking whether we can check using user inputs
request=input("please imnput your return key: ")
if request=="0":
    print(friendNames[0])
elif request=="Mulinge":
    print(friendNames["Mulinge"])
else:
    print("wrong request")