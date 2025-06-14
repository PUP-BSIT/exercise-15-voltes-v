class Morales:
    def __init__(self):
        self.name = "Woman Daphne Morales"
        self.age = 22
        self.dream = "to have an eight-hour sleep"

    def greet(self):
        print(f"\nHello, I'm {self.name}!")

    def display_age(self):
        print(f"\nMy age is {self.age}")

    def display_dream(self):
        print(f"\nMy dream is {self.dream}.")

    def hobby(self):
        print(f"\nI enjoy sleeping.")

    def favorite_food(self):
        print(f"\nMy favorite food is mochi.")

    def menu(self):
        while True:
            print("\n--- Morales's Menu ---")
            print("1. Greet")
            print("2. Age")
            print("3. Dream")
            print("4. Hobby")
            print("5. Favorite Food")
            print("6. Back to VoltesV Main Menu")
            print("----------------------------")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.greet()
            elif choice == "2":
                self.display_age()
            elif choice == "3":
                self.display_dream()
            elif choice == "4":
                self.hobby()
            elif choice == "5":
                self.favorite_food()
            elif choice == "6":
                print("Returning to Voltes V Main Menu...")
                break
            else:
                print("Invalid choice. Try again.")