# Data Types in Python
#-----STR
print("Kelimeler için kullanılan veri tipleri :=: \n")

string = 'kelime'
print(f"Bu {string} string veri tipindedir. Bu tür kelimeleri yazmak için kullanılır.")

#-----NUM
print("\nSayısal veri tipleri :=: \n")

integer = 1
print(f"Bu sayı {integer} : integer veri tipindedir ve tam sayılar için kullanılır.")

Float = 10.345
print(f"Bu sayı {Float} : float veri tipindedir ve virgüllü sayılar için kullanılır.")

compleX = 100+345j
print(f"Bu sayı {compleX} : complex veri tipindedir ve karmaşık sayılar için kullanılır.")

#-----Bool
print("\nBoolean cinsi veri tipi :=: \n")

boolT = True
boolF = False

print(f"Bu veri tipi sadece iki değer alır bunlar ise {boolT} ve {boolF}. Genelde bi işlemin doğru ya da yanlış olduğunu belirtmek için kullanılır.")

#-----List
print("\nListeler için kullanılan veri tipleri :=:  \n")
List = ["Araba", 2023, "Elma", True]

print(f"Bu veri tipi liste oluşturmak için kullanılır.{List} şeklinde ve istersek bu listenin ilk: {List[0]}, ikinci:{List[1]} veya sonuncu {List[-1]} elemanlarını seçebiliriz ve istersek bu liste üzerinde değişiklikler yapabiliriz.")

Tuple = ("Araba", 2023, "Elma", True)
print(f"\nBu veri tipi list veri tipi gibidir. {Tuple} : şeklinde ancak bu tipte listteki gibi değişiklik yapamayız.")

Dict = {'Kelime':"Araba", 'Sayı':2023, 3: "Elma", 'Bool':True}
print(f"\nBu veri tipi ise sözlük oluşturmak için kullanılır ve tanımladığımız değerleri kullanarak o değerin karşılığı olan değere erişmek için kullanılr. Mesela Kelime = {Dict['Kelime']} şeklinde")

#---------------------Kodlama-IO da ki veri tipleri----------------------#
#---STRING---#
Ust_Baslik = 'Kurslarım'
#---INTEGER---#
Kullanici_Id = 1
#---Boolean---#
Kursa_Kayıtlı = True
#---List---#
Kurs_Basliklari = ['Yaılım Geliştirici Yetiştirme Kampı(JAVA + REACT)',
                   '(2022) Yaılım Geliştirici Yetiştirme Kampı -JAVA',
                   'Yaılım Geliştirici Yetiştirme Kampı(JavaScript)',
                   'Yaılım Geliştirici Yetiştirme Kampı(C# + ANGULAR)',
                   '(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium',
                   'Senior Yaılım Geliştirici Yetiştirme Kampı(.Net)' ]
print(f'Kodlama io sitesimde birden fazla veri tipi kullanılmıştır. Bunlar ise:\nString = {Ust_Baslik}\n'
      f'Integer = {Kullanici_Id}\nBoolean = {Kursa_Kayıtlı}\n ve List e şeklindedir = {Kurs_Basliklari}')