class Pineda:
    def __init__(self):
        self.name = "Dyanna May Pineda"
        self.age = 20
        self.course = "BSIT"

    def greet(self):
        print(f"\nHello, I’m {self.name}!")

    def display_age(self):
        print(f"\nI’m {self.age} years old.")

    def show_course(self):
        print(f"\nMy course is {self.course}.")

    def say_hobby(self):
        print("\nI enjoy playing Uncharted.")

    def fun_fact(self):
        print("\nI love rewatching Twilight Saga's every rainy season.")

    def menu(self):
        while True:
            print("\n--- Pineda's Menu ---")
            print("1. Greet")
            print("2. Age")
            print("3. Course")
            print("4. Hobby")
            print("5. Fun-Fact")
            print("6. Back to VoltesV Main Menu")
            print("----------------------------")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.greet()
            elif choice == "2":
                self.display_age()
            elif choice == "3":
                self.show_course()
            elif choice == "4":
                self.say_hobby()
            elif choice == "5":
                self.fun_fact()
            elif choice == "6":
                print("Returning to Voltes V Main Menu...")
                break
            else:
                print("Invalid choice. Try again.")