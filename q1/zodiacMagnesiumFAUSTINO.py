byear = int(input("Enter your birth year: "))
baseline_year = 1900

if byear < baseline_year:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]  

    index = (byear - baseline_year) % 12
    print(f"Your Chinese Zodiac Sign is: {zodiac[index]}")