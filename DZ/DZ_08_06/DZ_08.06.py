from parser import SimpleGameParser


def main():

    pars = SimpleGameParser(f"https://www.igromania.ru/news/", "game_news.txt")
    pars.run()


if __name__ == "__main__":
    main()
