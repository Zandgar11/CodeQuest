from profiles import save_profile

class Game:
    def __init__(self, profile):
        self.profile = profile

    def start(self):
        print(f"Bienvenue, {self.profile['name']}, à CodeQuest!")
        self.play_next_chapter()

    def play_next_chapter(self):
        if self.profile['progress'] == 0:
            import chapters.chapter_1 as chapter
        elif self.profile['progress'] == 1:
            import chapters.chapter_2 as chapter  # Pour plus tard
        else:
            print("Félicitations, tu as terminé le jeu !")
            return

        chapter.play_chapter(self)
        self.profile['progress'] += 1
        save_profile(self.profile)
        self.play_next_chapter()
