# Chinese Zodiac Activity
## Requirements:
The requirements are to create a Python file that asks the user to enter their year of birth, using 1900 as the baseline year. The program must validate the input and display a message if the entered year is earlier than 1900, then stop the program. If the year is valid, the program must determine the user's Chinese zodiac sign based on their given birth year. The Chinese zodiac signs must begin with Rat and follow the given order of Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, and Pig, repeating the cycle every 12 years.

___
## Code:
```python
    byear = int(input("Enter your birth year: "))
    baseline_year = 1900

  if byear < baseline_year:
      print("Invalid Year, it should not be earlier than 1900")
  else:
      zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)",   "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]  

      index = (byear - baseline_year) % 12
      print(f"Your Chinese Zodiac Sign is: {zodiac[index]}")
```
___
## Documentation (Output):
<img width="1798" height="204" alt="image" src="https://github.com/user-attachments/assets/a377f7cf-983a-46f4-b6e2-91e9646b3956" />
