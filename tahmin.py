import random

def main():
    min_sayi = 1
    max_sayi = 100
    hedef_sayi = random.randint(min_sayi, max_sayi)
    can_sayisi = int(input("Kaç hakkınız olsun? (1-10): "))
    
    while can_sayisi > 0:
        tahmin = int(input(f"Lütfen {min_sayi}-{max_sayi} arasında bir sayı tahmin edin: "))
        
        if tahmin < min_sayi or tahmin > max_sayi:
            print("Geçersiz tahmin! Lütfen verilen aralıkta bir sayı girin.")
            continue
        
        if tahmin == hedef_sayi:
            print("Tebrikler, doğru tahmin ettiniz!")
            break
        elif tahmin < hedef_sayi:
            print("Daha büyük bir sayı girin.")
        else:
            print("Daha küçük bir sayı girin.")
        
        can_sayisi -= 1
    
    if can_sayisi == 0:
        print(f"Üzgünüm, hakkınız bitti. Hedef sayı {hedef_sayi} idi.")
    
    puan = can_sayisi * 20
    print(f"Puanınız: {puan}/100")

if __name__ == "__main__":
    main()
