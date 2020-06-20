print(""" Enpara.com'a Hoşgeldiniz.

-- Hesabınızdaki Bakiyeyi Görüntülemek için 1'e

-- Para Transferi için 2'ye

-- Çıkış için 9'ya 

Basınız.
""")
Balance = 1200

while True:
    Operation_Code = int(input("Yapmak istediğiniz işlem kodunu giriniz : "))
    if Operation_Code == 1 :
        print(" Hesabınızda {} tl bulunmaktadır.".format(Balance))
    elif Operation_Code == 2 :
        print("""Nasıl Para transferi yapmak istiyorsunuz
        
        UYARI!! : Bu ATM'den şuan da sadece nakit para çekip yatırabilirsiniz. 
        
        Başka birine havale veya EFT yapmak için lütfen veznelere başvurunuz.
        """)
        Change = int(input("Para çekmek veya yatırmak için sırasıyla -,+ ifadelerini tuşladıktan sonra tutarı giriniz."))
        if ( Change < -Balance) :
            print("Çekmek istediğiniz tutar bakiyenizin üzerindedir.")
            continue
        Balance += Change
        print("Yeni bakiyeniz {} TL'dir.".format(Balance))

    elif Operation_Code == 9 :
        print("İsleminiz sonlandırılmıştır. İyi günler dileriz")
        break
    else :
        print("Geçerli olmayan bir işlem kodu girdiniz lütfen tekrar deneyiniz.")