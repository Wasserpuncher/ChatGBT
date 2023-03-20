import random

# Spiel 1: Zahlenraten
def zahlenraten():
  print("Willkommen zu Zahlenraten! Ich denke mir eine Zahl zwischen 1 und 100 aus, und du musst sie erraten.")
  zielzahl = random.randint(1, 100)
  geraten = False
  while not geraten:
    tipp = int(input("Gib eine Zahl ein: "))
    if tipp < zielzahl:
      print("Zu niedrig! Versuch es noch einmal.")
    elif tipp > zielzahl:
      print("Zu hoch! Versuch es noch einmal.")
    else:
      print("Richtig geraten! Die Zahl war", zielzahl)
      geraten = True

# Spiel 2: Hangman
def hangman():
  print("Willkommen zu Hangman! Ich denke mir ein Wort aus, und du musst es erraten.")
  wortliste = ["Python", "Java", "Ruby", "Javascript", "Cplusplus", "HTML", "CSS", "PHP"]
  wort = random.choice(wortliste).lower()
  geraten = set()
  leben = 6

  while leben > 0:
    print("Du hast noch", leben, "Leben.")
    wortanzeige = ""
    for buchstabe in wort:
      if buchstabe in geraten:
        wortanzeige += buchstabe
      else:
        wortanzeige += "-"
    print(wortanzeige)

    tipp = input("Gib einen Buchstaben ein: ").lower()
    if tipp in geraten:
      print("Den hast du schon geraten.")
    elif tipp in wort:
      print("Richtig geraten!")
      geraten.add(tipp)
    else:
      print("Falsch geraten!")
      leben -= 1

    if "-" not in wortanzeige:
      print("Du hast gewonnen! Das Wort war", wort)
      return

  print("Du hast verloren! Das Wort war", wort)

# Hauptmenü
while True:
  print("Willkommen zu meiner Spielesammlung!")
  print("1. Zahlenraten")
  print("2. Hangman")
  print("3. Beenden")
  auswahl = input("Welches Spiel möchtest du spielen? ")
  if auswahl == "1":
    zahlenraten()
  elif auswahl == "2":
    hangman()
  elif auswahl == "3":
    print("Auf Wiedersehen!")
    break
  else:
    print("Ungültige Eingabe. Versuche es noch einmal.")
