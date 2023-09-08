
rank = []
firstnames = []
lastnames = []
employees = {"jose":"electricista","valentina":"ingeniera","juli":"doctora","jack":"bombero"}

for key,value in employees.items():
    print("-----------")
    print("name: " + key)
    print("job: " + value)

with open("girl_boy_names_2004.csv","r") as names_csv:
        lines = names_csv.readlines()

        for i in lines:
            new_list = i.split(",")
            rank.append(new_list[0])
            firstnames.append(new_list[1])
            lastnames.append(new_list[2])
        for i in range(len(firstnames)):
            print ("----------")
            print ("rank: " + rank[i])
            print ("girl name: " + firstnames[i])
            print ("boy name: " + lastnames[i])