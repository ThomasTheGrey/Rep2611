from lib2to3.pytree import convert

name ="Thomas"
ausbildung="Pending"
zitat="wtf?"

print(f"{name}\t{ausbildung}\n\"{zitat}\"")


name = input("Bitte geben Sie ihren namen ein:")
alter = input("Bitte geben sie ihr Alter ein:")
beruf = input("Bitte geben sie ihren Beuf ein:")


print(f"Hallo {name}, schön das ein {alter}-jähriger {beruf} hier ist!")

zahl = input("\nBitte geben sie jetzt eine Zahl ein:")

if (zahl.isdigit):
    print("\nDas ist wirklich eine Zahl, herzlichen Glückwunsch!")
else:
    print("\nEs wäre gut zu wissen, was eine Zahl ist..")

GanzeZahl = 2
GleitkommaZahl = 1.2
Text = "Text!!"
Wahrheitswert = True

print(f"Gleitkommazahl ist ein {type(GleitkommaZahl)}")
print(f"GanzeZahl ist ein {type(GanzeZahl)}")
print(f"Text ist ein {type(Text)}")
print(f"Wahrheitswert ist ein {type(Wahrheitswert)} und gleich {Wahrheitswert}")



GZfloat = float(GanzeZahl)
GZstring = str(GanzeZahl)

print(f"{GanzeZahl}\n{GZfloat}\n{GZstring}")

