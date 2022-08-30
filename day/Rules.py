#def bool_to_word(boolean):
    #if boolean == True:
       # return("Yes")
   # elif boolean == False:
    #    return("No")


#my_list = ["ana", "gio", "vako", 10, 3.5, True]

#my_list.reverse()    თუ გვინდა შევატრიალოთ სია
#print(my_list)

#name = my_list[2]           თუ ჩვენ გვინდა, რომ ლისტიდან ამოვიღოთ ერთი ელემენტი, მაშინ შემოვიტანოთ ცვლადი 
#print(name)                 და მივანიჭოთ ლისტის სახელი. შემდეგ ოთხკუთხედ ფრჩხილებში ჩავწეროთ იმ მონაცემის                             #რომელიც ჩვენ გვჭირდება 
#                            ინდექსი, რომელიც ჩვენ გვინდა



#len() lenght-სიგრძე 
#print(len(my_list))  



#changeble - ცვალებადი
#my_list[1] = 7895678953             
#print(my_list)



#ლისტის ბოლო ელემენტი შეგვიძლია მივიღოთ შემდეგნაერად
#n = len(my_list)
#print(my_list[n - 1])


#თუ ჩვენ გვინდა რომ დავამატოტ ლისტში რაიმე ახალი მონაცემი მაშინ: ლისტის სახელი.append()
#my_list.append("Tbilisi")
#print(my_list)



#თუ ჩვენ გვინდა ლისტში არსებული რომელიმე მონაცემის წაშლა მაშინ: ლისტსის სახელი.pop()
#my_list.pop(0)           თუ არაფერს არ ჩავწერთ ფჩხილებში მაშინ ის ავტომატურად წაშლის ბოლო მონაცემს
#print(my_list)
 
#ასევე არის მეორე ნაერი კოდი: ლისტის სახელი.remove(ლისტში მყოფი რომელიმე მონაცემის სახელი)
#my_list.remove("gio")
#print(my_list)

#myset = {1.5, 10, "gio", "saqartvelo"}

#set - სიმრავლე, შიგნით მოცემულ მონაცემებს არააქვს თავიანთი ინდექსი

#myset = {1.5, 10, "gio", "saqartvelo"}  #რადგან ისინი დალაგებულები არ არიან თანმიმდევრობით როგორც ლისტში
#print(myset)             ასევე set_ში შეუძლებელია დუპლიკატი ანუ არ შეიძლება ორი ერთი და იმავე მონაცემის შეყვანა

#კიდევ არ შეიძლება change_ს გაკეთება

#ჩვენ შეგვიძლია list გადავაქციოთ set_ად:
#name_list = ["ako", "luka", "giorgi", "ako"]
#name_set = set(name_list)     
#print(name_set)

#შეგვძლია ასევე დავამატოთ set_ში მონაცემი ახალი:
#myset.add("vako")
#print(myset)
#იგივი პრინციპია remove_ზე
 
#names = {"Qeti", "Irakli", "Sopo"}
#numbers = {10, 9, 8 ,7}                 ფუნქცია .union() აერთიანებს ორ set_ს ამ შემთხვევაში
#names_numbers = names.union(numbers)    names და numbers და ერთში ახვედრებს ორივეს names_numbers
#print(names_numbers)                    იგივეს აკეთებს ფუნქცია .update()
#                                        names.update(numbers) 



#mytuple = (1, 1.5, "gio", "nika", True)    #ჩვენ ამ მოქმედებით ტუპლი გადავაკეთეთ სიად
#mylist = list(mytuple)                     #და შემდეგ შეგვეძლება ისეთი მოქმედებების ჩატარება როროგრც ლისტზე
#mylist.append("vako")
#print(mylist)
#ტუპლების ერთმანეთზე დამატება
#mytuple = (1, 1.5, "Gio", "Nika", True)
#histuple = (False, "Saqartvelo", "Poti")
#hertuple = mytuple + histuple
#print(hertuple)
#როგორ გავიგოთ index ტუპლში:
#mytuple = (1, 1.5, "Gio", "Nika", True)
#print(mytuple.index("Gio"))



#DICTIONARI - ლექსიკონი
#dosnt allow doplicate, changeble, ordered-დაულაგებელი

#cars = {"Brend": "Ford",
#        "Model": "Bmw",
#        "year": 2006
#}
#print(type(cars))
#print(len(cars))

#დამატება მონაცემის                           
#cars["color"] = "Green"    
#                         ან 
#cars.update({"Qeti": "Irakli"})

#  რამოდენიმე მონაცემის დამატება თუ გვსურს მაშინ:                  
#cars["color"] = ["Black", "Green", "Red"]
#print(cars)

#თუ გვინდა რომ მოგვცეს რაიმე value მაშინ
#print(cars.get("Brend"))

#თუ გვინდა მოშრება რაიმე მონაცემის მაშინ:
#cars.pop("Model")
#print(cars)

#თუ გვინდა ჩანაცვლება მაშინ:
#cars["Model"] = "Mercedes"
#print(cars)

#txt ="ragaca ris itogshi"
#x = txt.split()  split - დაყოფა, შემდეგ ქმნის სიას
#print(x)
#capitalize - ადიდებს პირველ ასოებს


#####################################################################################################################

#while loop

""" n = 100
i = 0
while i <= n:
    print(i)
    i += 1 """

#For Loop
""" n = 100
number = []
numbers_even = []
for i in range(100):
    if i % 2 == 0:
        number.append(i**3)
    elif i % 2 == 1:
        numbers_even.append(i**2)
print(number)
print(numbers_even)
 """

