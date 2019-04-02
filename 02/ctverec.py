#program počítá obvod a obsah čtverce

strana = float(input("Zadej cislo"))
cislo_je_spravne = strana > 0
print(cislo_je_spravne)


if cislo_je_spravne:
    print("Obvod ctverce se stranou", strana, "cm je ", 4 * strana , "cm")
    print("Obsah čtverce se stranou", strana, "cm je ", strana * strana , "cm2")
else:
    print("Zadej kladné číslo.")

print("Dekuji za pouziti kalkulacky")