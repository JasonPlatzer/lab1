name = str(input("what is your name: "))
month = str(input("what month were you born in: "))
print(f'Hello {name}')
print(f'there are {len(name)} letters in your name')
check_month = month.lower()
if month == check_month:
    print(f'You were born in august')