#დავალება:
#მომხმარებელს შემოატანინეთ ორი რიცხვი 
# 1) ასზე დიდი 
# 2) ათსა და ოცს შორის

# თუ ვერ შეასრულებს ამ ორ პირობას იუზერი, მაშინ დაუწერეთ რომ ის დებილია
# თუ არადა, გამოიტანეთ ეკრანზე, რამდენჯერ მოთავსდება რიცხვი 2 სრულად რიცხვ1-ში. 

#105 -ში  16 მოთავსდა 6-ჯერ , და  ნაშთი არის 9

#google // in python  %იც

Number_over_houndred = int(input("Enter Number That Equals Over Houndred : "))
Number_Between_Ten_Twenty = int(input("Enter Number Between Ten and Twenty : "))


if  Number_over_houndred < 100:
    print("დებილი ხარ")
if Number_Between_Ten_Twenty < 10 > 20:
    print("დებილი ხარ")


Divizion = Number_over_houndred // Number_Between_Ten_Twenty
Modulus = Number_over_houndred % Number_Between_Ten_Twenty


if Number_over_houndred > 100 and Number_Between_Ten_Twenty >10 <20:
    print("{}-ში {} მოთავსდება {}-ჯერ , და ნაშთი არის {}".format(Number_over_houndred,
    
    Number_Between_Ten_Twenty,
    Divizion, Modulus ))




