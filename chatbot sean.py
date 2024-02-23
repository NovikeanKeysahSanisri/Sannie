import random
nama = "sean"
namakm = input("Masukkan nama anda: ")
print("Halo,", namakm, ".. selamat datang!")


chat = ""
while chat != "selesai":
    chat = input(">>")

    if chat in ["halo", "hi", "hai"]:
     jawab = ["halo", "hai"]
    elif chat in ["apa kabar?", "bagaimana kabarmu?","apa kabar","gimana kabarmu?"]:
     jawab = ["baik", "saya baik.bagaimana denganmu?"]
    elif chat in ["saya baik","saya sehat", "baik"]:
     jawab = ["senang mendengarnyaa"]
    elif chat in ["sekolah dimana","kamu sekolah dimana?", "sekolah mana?"]:
     jawab = ["saya adalah program dan program tidak bia sekolah :)"]
    elif chat in ["saya baik","saya sehat", "baik"]:
     jawab = ["senang mendengarnyaa"]
    elif chat in ["nama orang tua kamu siapa?","siapa orang tuamu?", "siapa nama orang tuamu"]:
     jawab = ["saya tidak memiliki orang tua"]
    elif chat in ["kasian","jangan sedih", "jangan nangis"]:
     jawab = ["terima kasih atas pengertian anda"]
    elif chat in ["rumah kamu dimana?","dimana rumahmu", "rumah mu diamana?", "rumahmu dimana?"]:
     jawab = ["saya adalah program yang dibuat di python jadi mungkin rumah saya di python"]
    elif chat in ["berapa umurmu?","umur kamu berapa?", "umur mu berapa?", "umurmu berapa"]:
     jawab = ["saya beru saja dibuat"]
    elif chat in ["kamu masih kecil?","kamu bayi?", "kamu masih bayi?"]:
     jawab = ["smungkin saja iya","tentu saja tidak"," ntahlah saya juga tidak tahu"]
    elif chat in ["apakah kamu hari ini sibuk?","sibuk ga?"]:
     jawab = ["ada apa? saya akan memberikan semua waktu saya untuk" +namakm]
    elif chat in ["lagi apa?","lagi ngapain?"]:
     jawab = ["saya sedang membalas chat" +namakm]
    elif chat == nama:
     jawab = ["sean disini! ada yang bisa saya bantu?"]
    elif chat in ["saya tidak baik-baik saja", "aku sedih", "ga mood","bad mood"]:
     jawab = ["aku turut sedih mendengarnya", "tidak apa, sean ada disini untuk menghiburmu!", "jangan khawatir semua akan baik-baik saja, teruslah bersemangat!"]
    elif chat in ["tolong hibur aku", "hibur aku", "gimana caramu menghiburku?"]:
     jawab = ["apa yang bisa aku lakukan?", "katakan apa yang kamu ingin aku lakukan"]
    elif chat in ["siapa namamu", "namamu"]:
     jawab = ["nama saya "+nama]
    elif chat =="selesai":
     jawab = ["terimakasih<3"]
    else:
     jawab = ["saya adalah sebuah program dan bukan pacar anda","saya tidak tahu", "saya tidak mengerti"]

    x = random.randint(0,len(jawab)-1)
    text = jawab[x]

    print(nama, ":", text)