import random
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL":"Bir şakaya karşılık cevap",
            "SHEESH":"onaylamamak",
            "CREEPY":"korkunç",
            "AGGRO":"agresifleşmek/sinirlenmek"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ").upper()
if word in meme_dict.keys():
      print(meme_dict[word])
else:
   print("Bu kelime bulunmuyor.")
   
print(random.choice(meme_dict.values()))
