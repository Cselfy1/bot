from aiogram.types import BotCommand

listOfCommands = [
    BotCommand(command="start", description="This command starts bot"),
    BotCommand(command="help", description="This command helps user to make a choice"),
    BotCommand(command="menu", description="This command calls the menu"),
    BotCommand(command="dog", description="This command shows a dog"),
    BotCommand(command="random", description="This command shows random picture"),
]