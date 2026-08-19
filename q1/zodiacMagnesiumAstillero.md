# Chinese Zodiac Output

## Requirements
a. Ask the user to enter a year of birth.  The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.



## Code
``` Python
zodiac_year = int(input("Please input a year of birth: "))
zodiacs = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū"]

if zodiac_year > 1899:
    index_of_the_zodiac = (zodiac_year - 1900) % 12
    print(" ")
    print(f"Congrats! Your Chinese Zodiac Sign is {zodiacs[index_of_the_zodiac]}!")
    print("Thank you for your time!")
else:
    print("Unfortunatly, we only accept birth years that are in the 1900s onward. Please try again!")
```
## Documentation

![Zodiac_Ouput_Screenshot](image.png)
