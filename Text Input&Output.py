
name ="Thomas"
ausbildung="Pending"
zitat="wtf?"

print(f"{name}\t{ausbildung}\n\"{zitat}\"")


name = input("Bitte geben Sie ihrenm namen ein:")
alter = input("Bitte geben sie ihr Alter ein:")
beruf = input("Bitte geben sie ihren Beuf ein:")


print(f"Hallo {name}, schön das ein {alter}-jähriger {beruf} hier ist!")

zahl = input("\nBitte geben sie jetzt eine Zahl ein:")

if (zahl.isdigit):
    print("\nDas ist wirklich eine Zahl, herzlichen Glückwunsch!")
else:
    print("\nEs wäre gut zu wissen, was eine Zahl ist..")

