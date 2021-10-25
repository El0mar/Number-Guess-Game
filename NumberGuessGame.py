import random

class Game():
    def NumberGuess():
        number1 = random.randint(1,10)
        lives = 5
        while True:
            try:
                userNumber = int(input("1-10 arası sayı giriniz: "))
                if userNumber > 10:
                    print("Lütfen 1-10 arası sayı giriniz.")
                elif 1<=userNumber<=10:
                    if userNumber == number1:
                        print("Tebrikler! Sayıyı buldunuz.")
                        break
                    elif userNumber<number1 or userNumber>number1:
                        lives -= 1
                        print(f"Sayıyı bulamadınız. Kalan hakkınız: {lives}")
                    if lives == 0 :
                        print(f"Kaybettiniz. Sayı: {number1}")
                        break
            except ValueError:
                print("Lütfen sayı giriniz.")

Game.NumberGuess()