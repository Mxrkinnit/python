#list in python
myclassmate=["Erick", "Joan", "Michael", "Victor"]
mynos=[3,7,9,2,6,0,8]
mynos.sort()
myclassmate[0]="sylvia"
myclassmate.append("daniel")
myclassmate.insert(2, "christine")
myclassmate.sort()
print(myclassmate)
print(type(myclassmate))
print(mynos)
print("My name is " +myclassmate[0])


#tuple in python
myfavfruits=("mangoes", "apples", "pineapples")
print(myfavfruits)

print(myfavfruits[0])

#set datastructure
myfavccars={"Toyota","mercedes","nissan","vw"}
myfavccars.add("peugeot")
print(myfavccars)

#dictionaries in python
magari={
    "Name":"Toyota",
    "model":"Premio",
    "year":2020

}
print(magari)
print(magari["model"])
8