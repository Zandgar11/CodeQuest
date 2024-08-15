import subprocess

def challenge_code(game, challenge_text, solution_file):
    print("\nDéfi de Programmation :")
    print(challenge_text)
    print("Tu dois écrire le code correct dans une nouvelle fenêtre de terminal.")
    print("Lorsque tu es prêt, entre 'y' pour ouvrir la fenêtre et commencer à coder.")

    start_challenge = input("Commencer le défi ? (y/n) : ").lower()

    if start_challenge == 'y':
        subprocess.run(["python", solution_file])
    else:
        print("Défi annulé. Reviens lorsque tu seras prêt.")
