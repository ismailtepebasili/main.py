meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
print("Merhaba! Meme'leri Anlamlandırma Programına Hoş Geldiniz!")
print("Bu program ile anlamadığınız 5 kelimenin anlamını öğrenebilirsiniz.")
print("Lütfen her kelimeyi BÜYÜK HARFLERLE yazın.")            
            
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(word, " Kelimesinin anlamı: ", meme_dict[word])
    else:
        print("Üzgünüm ", word, "kelimesinin anlamını bilmiyorum")
