import random
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from filters.chat_filters import ChatTypeFilter
from common.functions import get_random_dog, get_random_picture

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

# List of random greetings
greetings = [
    "Hello there!", 
    "Hi! How's it going?", 
    "Hey! Nice to see you!", 
    "Greetings!", 
    "Hiya! What’s up?"
]

# List of random farewells
farewells = [
    "Goodbye! Take care!", 
    "See you later!", 
    "Bye-bye!", 
    "Catch you later!", 
    "Farewell!"
]

# Random greeting handler
@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(random.choice(greetings))

# Random farewell handler
@user_private_router.message(F.text.in_(['bye', 'goodbye', 'see you', 'Bye', 'GoodBye', 'See you']))
async def farewell_handler(message: Message):
    await message.answer(random.choice(farewells))

# Help command
@user_private_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("I'm a simple bot")

# Random dog picture command
@user_private_router.message(Command('dog'))
async def cmd_dog(message: Message):
    await message.answer_photo(get_random_dog()) 

# Random picture command
@user_private_router.message(Command('random'))
async def cmd_random(message: Message):
    await message.reply("Here's your random picture: ")
    res = message.text
    await message.answer_photo(get_random_picture(res)) 

# Handle incoming photos
@user_private_router.message(F.photo)
async def get_photo(message: Message):
    await message.reply("This is a photo, but I need some text to help you")

# Simple hello handler
@user_private_router.message(F.text.in_(['Hello', 'Hi', 'Hey', 'hello', 'hi', 'hey', 'sup', 'Sup']))
async def answer_hello(message: Message):
    await message.answer(random.choice(greetings))
