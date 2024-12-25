"""დაწერეთ შემთხვევითი რიცხვების გენერატორი Python- ში. მან უნდა გამოიყენოს ზოგიერთი ფიზიკური ელემენტი.
მის განსახორციელებლად შეგიძლიათ გამოიყენოთ ხმა, მაუსის მოძრაობა, პროცესორის სიჩქარე ან ნებისმიერი სხვა ფიზიკური სტრუქტურა.
შემთხვევითი რიცხვის სიგრძე უნდა იყოს 16 ბიტი. გამოიყენეთ საჭირო ბიბლიოთეკები.
"""
import time
from pynput import mouse
import random

# ეტაპი 1: სიის ინიციალიზაცია მაუსის კოორდინატების შესანახად
mouse_data = []


def on_move(x, y):
    """მაუსის მოძრაობის დაფიქსირება."""
    global mouse_data
    # კოორდინატების დამატება სიაში
    mouse_data.append((x, y))
    print(f"მაუსის კოორდინატები: X={x}, Y={y}")  # კოორდინატების დაბეჭდვა

    # მონაცემების საკმარისი რაოდენობის შემდეგ შევაჩეროთ ლისტენერი
    if len(mouse_data) >= 16:  # მინიმუმ 16 კოორდინატის შეგროვება
        print("მონაცემები საკმარისია. ვწყვეტთ მაუსის დაფიქსირებას.")
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('↓↓↓')
        return False  # ლისტენერის გაჩერება


def generate_random_number(data):
    """მაუსის მონაცემებიდან 16-ბიტიანი რანდომული რიცხვის გენერაცია."""
    # კოორდინატების გაერთიანება ერთ რიცხვში
    combined = sum(int(x) ^ int(y) for x, y in data)  # XOR
    print(f"კომბინირებული მნიშვნელობა: {combined}")  # კომბინირებული მონაცემების დაბეჭდვა

    random.seed(combined)
    random_number = random.getrandbits(16)  # 16-ბიტიანი რიცხვის მიღება
    return random_number


# ეტაპი 2: მაუსის მოძრაობების დაფიქსირება
print("გადაადგილეთ მაუსი, რათა შეგროვდეს მონაცემები...")
with mouse.Listener(on_move=on_move) as listener:
    listener.join()

# ეტაპი 3: რანდომული რიცხვის გენერაცია
if len(mouse_data) >= 16:
    print(f"შეგროვდა {len(mouse_data)} მონაცემთა წერტილი.")
    random_number = generate_random_number(mouse_data)
    print(f"გენერირებული 16-ბიტიანი რანდომული რიცხვი: {random_number}")
else:
    print("მონაცემები არასაკმარისია.")
