import settings
from jaycommands import bot


def run():
    bot.run(settings.DAT, root_logger=True)


if __name__ == "__main__":
    run()
