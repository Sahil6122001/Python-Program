# Setting up an Dictionary
myDict = {
    "fast" : "In a quick Manner",
    "Sahil" :"A Coder"

}
print(myDict["fast"])
print(myDict["Sahil"])
# Dictionary Keys
print(myDict.keys())
print(myDict.values())
print(list(myDict.keys()))
print(myDict.items())
updateDict = {
    "Ram": "Friend",
   "Shyam": "Friend",
   "Saurav": "Me"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("Sahil2"))#If not found simply return none
print(myDict["Sahil2"])# Has to be present in Dictionary otherwise it will show error
User = input("Enter the Word to be searched in Dictionary -")
if User in (myDict.keys()):
    print ("Correct")
else:
    print("Chup")
