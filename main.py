from game import Game
from profiles import load_profile, save_profile

def main():
    player_name = input("Entrez votre nom de joueur : ")
    profile = load_profile(player_name)

    game = Game(profile)
    game.start()

    # Sauvegarder le profil à la fin du jeu
    save_profile(profile)

if __name__ == "__main__":
    main()
