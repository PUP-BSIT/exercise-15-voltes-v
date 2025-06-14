import sys
import voltesv.gulles
import voltesv.morales
import voltesv.caculitan
import voltesv.pineda
import voltesv.corpus

choice = 0
while choice != 6:
    print("-------------------------------------------")
    print("            Voltes V Main Menu             ")
    print("-------------------------------------------")
    print("1. John Cris Caculitan ")
    print("2. Precious Hannah Corpus ")
    print("3. Althea Shane Gulles ")
    print("4. Woman Daphne Morales ")
    print("5. Dyanna May Pineda ")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    print("-------------------------------------------")

    match choice:
        case 1:
            voltesv.caculitan.Caculitan().menu()
        case 2:
            voltesv.corpus.Corpus().menu()
        case 3:
            voltesv.gulles.Gulles().menu()
        case 4:
            voltesv.morales.Morales().menu()
        case 5:
            voltesv.pineda.Pineda().menu()
        case 6:
            print("Exiting program. Goodbye!")
            sys.exit()
        case _:
            print("Invalid choice. Please select a number from 1 to 6.")