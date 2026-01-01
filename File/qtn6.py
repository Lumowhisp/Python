def count_letter_digits(str):
    with open("imp.txt","a+")as f:
        countDigit=0
        countAlpha=0
        for ch in str:
            if ch.isdigit():
                countDigit+=1
            if ch.isalpha():
                countAlpha+=1
        f.write(f"Number of Digits :{countDigit}")
        f.write(f"Number of Letter :{countAlpha}")
count_letter_digits("I am Adi 89078")
            

