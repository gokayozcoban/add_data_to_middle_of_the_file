
file = open("Ek yapılan dosya.txt","w")
file.write("""Bu satırın altına ek yapılsın.
Üst satıra ek yapıldı.
""")
file.close()

with open("Ek yapılan dosya.txt","r+") as file:
    ek_veri = file.readlines()
    ek_veri.insert(1,"BU SATIR SONRADAN EKLENDİ.\n")
    file.seek(0)
    file.writelines(ek_veri)



