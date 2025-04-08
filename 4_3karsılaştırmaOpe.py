#Kullanıcı adı ve şifre kontrolü için eşitlik kurulmalı ve doğru yanlış olacak şekilde kontrol sağlanmalı

a, b, c, d = 12, 8, "leman", 9
c1 = int(input("1. değişken: "))
c2 = int(input("2. değişken: "))
c3 = input("3. değişken: ") # bu yapı sürekli string yapıda olmasını sağlar. Karşılaştırma yaparken de tek doğru olan budur.
c4 = int(input("4. değişken: ")) # bu kod satırında input olsaydı string bir değer girmiş olacak ve tür eşitsizliğinden False sonucu olacaktı. integer bir değer giriyorsun ve liste yapısında da integer bir değer girildi.

result = a == c1, b == c2,c == c3, d == c4 #her birini tek tek değerlendirir doğru mu yanlış mı olarak ve yan yana yazar.
#PYTHONDA and or or not  İÇİN İŞARET KULLANILMIYOR..

derya=a==c1 and b==c2 and c==c3 and d==c4 #bu kontrollerin hepsini sağladığında kullanıcı adı ve şifre doğru olur.
print(derya)
print(result)
result= (d==c) # eşit mi olarak soruyoruz
print(result)
#EŞİTSİZLİK SORGULAMA
result= (a!= b)  #eşit değiller mi diye sorarsın çıktı True olur
print(result)
#Yazılımda True sayısal olarak 1 değerini döndürür. False 0 döndürür.

result= (a<b)
print(result)
result=(a<8)
print(result)
result= b<=d
print(result)
result=(b>= d)
print(result)

result1= True == 1
print(result1)

result2= False+ True+85
print(result2)
