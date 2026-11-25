import os

JOKE = "I invited my burnout to a recurring meeting and it declined \u2014 already fully booked."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
