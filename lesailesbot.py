import aiogram
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia, WebAppInfo, message
import asyncio
from random import randint

from pyexpat.errors import messages

from funtions import *

from russian import handle_text_r

TOKEN = "7702041998:AAGYq7SjeufGnJQ4OFAr2zrzqVP7VyD6nCM"

bot = Bot(token=TOKEN)
dp = Dispatcher()
user_data = {}


@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start":
        await start(message)
    elif "holat" not in user_data[user_id]:
        await shaxarlar(message)
    elif "shaxar" not in user_data[user_id]:
        await menu(message)
    elif message.text == "/boshmenu":
        await menu(message)
    elif message.text == "🛍 Buyurtma berish" or message.text == "↙️ Ortga":
        await order(message)
    elif message.text == "🔥 Aksiya":
        await sale(message)
    elif message.text == "🙋🏻‍♂️ Jamoamizga qo'shiling":
        await team(message)
    elif message.text == "☎️ Les Ailes bilan aloqa":
        await call(message)
    elif message.text == "⬅️ Ortga":
        await menu(message)
    elif message.text == "📖 Buyurtmalar tarixi":
        await history(message)
    elif message.text == "💬 Biz bilan aloqaga chiqing":
        await bizbilanaloqa(message)
    elif message.text == "✍️ Fikr bildirish":
        await fikr(message)
    elif message.text == "◀️ Ortga":
        await call(message)
    elif message.text == "⚙️Sozlash ℹ️ Ma'lumotlar":
        await sozlamalar(message)
    elif message.text == "Isimni o'zgartirish":
        await ism(message)
    elif message.text == "🔽 Ortga" or message.text == "⤵️ Ortga":
        await sozlamalar(message)
    elif "ismlarr" in user_data[user_id]:
        await checkname(message)
        await sozlamalar(message)
    # elif message.contact is not None or "+998" in message.text:
    #     await ask_phone(message)
    elif "ver_code" in user_data[user_id]:
        await check_code(message)
    elif message.text == "📱 Raqamni o'zgartirish":
        await history(message)
    elif message.text == "🏃 Olib ketish" or message.text == "▶️ Ortga":
        await olibketish(message)
    elif message.text == "🌐 Bu yerda buyurtma berish":
        await website(message)
    elif message.text == "Filialni tanlang" or message.text == "↩️ Ortga":
        await filialnitanlash(message)
    elif message.text == "🚙 Yetkazib berish":
        await yetkazibberish(message)
    elif message.text == "🗺 Mening manzillarim":
        await manzil(message)
    elif message.text in lists:
        await asosiymenu(message)
    elif message.text == "↪️ Ortga":
        await asosiymenu(message)
    elif message.text in main_menu:
        await menu_tekshiruv(message)
    elif message.text == "↖️ Ortga":
        if user_data[user_id]['tanlov'] == 'Setlar':
            await taomlar(message)
        elif user_data[user_id]['tanlov'] == 'Ichimliklar':
            await ichimlik(message)
        elif user_data[user_id]['tanlov'] == 'Tovuq':
            await tovuqlar(message)
        elif user_data[user_id]['tanlov'] == 'Sneklar':
            await snek(message)
        elif user_data[user_id]['tanlov'] == 'Lesterlar':
            await lester(message)
        elif user_data[user_id]['tanlov'] == 'Burgerlar':
            await burger(message)
        elif user_data[user_id]['tanlov'] == 'Longerlar/Hot-dog':
            await longer_hotdog(message)
        elif user_data[user_id]['tanlov'] == 'Salatlar':
            await salat(message)
        elif user_data[user_id]['tanlov'] == 'Ponchiklar':
            await ponchik(message)
        elif user_data[user_id]['tanlov'] == 'Bolajonlarga':
            await bolalarga(message)
        elif user_data[user_id]['tanlov'] == 'Souslar':
            await sous(message)
    elif message.text in taom:
        await savat(message)
    elif message.text in tovuq_dict:
        await tovuqlarr(message)
    elif message.text in button_values_snek:
        await sneklarr(message)
    elif message.text in button_values_lester:
        await lestrlarr(message)
    elif message.text in burger_dict:
        await burgerlarr(message)
    elif message.text in ichimliklar:
        await ichimlik_zakaz(message)
    elif message.text == "📥 Savat":
        await show_cart(message)
    elif message.text == "Savatni to'ldirdim ✅":
        await tolovgqismi(message)
    elif message.text == "Iloji boricha tezroq✅":
        await onlinepayment(message)
    elif message.text == "📍 Eng yaqin fillialni tanlang":
        await engyaqinfilial(message)
    elif "locationkeldi" in user_data[user_id]:
        await check_location(message)







@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
         types.KeyboardButton(text="🇺🇸 English")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n\n"
        "Здравствуйте! Добро пожаловать в службу доставки Les Ailes.\n\n"
        "Hello! Welcome to Les Ailes delivery service.",
        reply_markup=keyboard)
    print(1, user_data)


async def shaxarlar(message: types.Message):
    user_id = message.from_user.id
    language = message.text
    if message.text == '🇷🇺 Русский':
        await handle_text_r(message, user_data)
    else:
        user_data[user_id]["holat"] = language
        button = [
            [types.KeyboardButton(text="Toshkent"), types.KeyboardButton(text="Andijon")],
            [types.KeyboardButton(text="Samarqand"), types.KeyboardButton(text="Farg'ona")],
            [types.KeyboardButton(text="Buxoro"), types.KeyboardButton(text="Marg'ilon")],
            [types.KeyboardButton(text="Nukus"), types.KeyboardButton(text="Xorazm")],
            [types.KeyboardButton(text="Chirchiq"), types.KeyboardButton(text="Qo'qon")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer("Qaysi shaharda yashaysiz? \nIltimos, shaharni tanlang:", reply_markup=keyboard)
        print(2, user_data)

city = [
    "Toshkent", "Andijon",
    "Samarqand", "Farg'ona",
    "Buxoro", "Marg'ilon",
    "Nukus", "Xorazm",
    "Chirchiq", "Qo'qon"
]

async def menu(message: types.Message):
    user_id = message.from_user.id
    if message.text in city:
        boshmenu = message.text
        user_data[user_id]["shaxar"] = boshmenu
    else:
        user_data[user_id]["shaxar01"] = message.text
    button = [
        [types.KeyboardButton(text="🛍 Buyurtma berish")],
        [types.KeyboardButton(text="📖 Buyurtmalar tarixi")],
        [types.KeyboardButton(text="⚙️Sozlash ℹ️ Ma'lumotlar"), types.KeyboardButton(text="🔥 Aksiya")],
        [types.KeyboardButton(text="🙋🏻‍♂️ Jamoamizga qo'shiling"),
         types.KeyboardButton(text="☎️ Les Ailes bilan aloqa")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Bosh menyu", reply_markup=keyboard)
    print(3, user_data)


async def order(message: types.Message):
    user_id = message.from_user.id
    buyurtma = message.text
    user_data[user_id]["holat"] = buyurtma
    button = [
        [types.KeyboardButton(text="🏃 Olib ketish"), types.KeyboardButton(text="🚙 Yetkazib berish")],
        [types.KeyboardButton(text="⬅️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Buyurtmani o'zingiz 🙋‍♂️ olib keting yoki Yetkazib berishni 🚙 tanlang", reply_markup=keyboard)
    print(3, user_data)


async def sale(message: types.Message):
    user_id = message.from_user.id
    aksiya = message.text
    user_data[user_id]["holat"] = "aksiya"
    await message.answer("Shahringizda hali aksiyalar mavjud emas")
    print(4, user_data)


async def team(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "team"
    buttons = [
        [types.InlineKeyboardButton(text="O'tish", url="https://t.me/@HavoqandJamoa_Bot")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer(
        "Ahil jamoamizda ishlashga taklif qilamiz! \nTelegramdan chiqmay, shu yerning o'zida anketani \nto'ldirish uchun quyidagi tugmani bosing.",
        reply_markup=keyboard)


async def call(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "call"
    button = [
        [types.KeyboardButton(text="💬 Biz bilan aloqaga chiqing"), types.KeyboardButton(text="✍️ Fikr bildirish")],
        [types.KeyboardButton(text="⬅️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Agar siz bizga yozsangiz yoki sharh qoldirmoqchi bo'lsangiz, xursand bo'lamiz.",
                         reply_markup=keyboard)
    print(5, user_data)


async def bizbilanaloqa(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "bizbilanaloqa"
    buttons = [
        [types.InlineKeyboardButton(text="💬 Biz bilan aloqaga chiqing", url="https://t.me/@lesaileshelpbot")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer("Agar biron-bir savol yoki taklif bo'lsa, bizga aloqaga chiqing.", reply_markup=keyboard)
    print(6, user_data)


async def history(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "history"
    button = [
        [types.KeyboardButton(text="📞 Mening raqamim", request_contact=True),types.KeyboardButton(text="⬅️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Avval ro'yxatdan o'ting.")
    await message.answer("Ro'yxatdan o'tish uchun telefon raqamingizni kiriting!\nMisol uchun, +998xx xxx xx xx",reply_markup=keyboard)


async def ask_phone(message: types.Message):
    user_id = message.from_user.id
    i = '+1234567890'
    ok = True
    if message.contact is not None:
        phone_c = message.contact.phone_number
        user_data[user_id]['phone'] = phone_c
        ver_code = randint(100000, 999999)
        user_data[user_id]['ver_code'] = ver_code
        await message.answer(f"Nomeringizga tasdiqlash kodi yuborildi \nIltimos kodni kiriting: {ver_code}")
    elif len(message.text) == 13 and message.text[0:4] == '+998':
        for symbol in message.text:
            if symbol not in i:
                await message.answer('Hato nomer kiritildi')
                ok = False
                break
        if ok == True:
            phone = message.text
            user_data[user_id]['phone'] = phone
            ver_code = randint(100000, 999999)
            user_data[user_id]['ver_code'] = ver_code
            await message.answer(f"Nomeringizga tasdiqlash kodi yuborildi \nIltimos kodni kiriting: {ver_code}")

    else:
        await message.answer('Hato nomer kiritildi')
        print(user_data)

    print(7, user_data)

async def check_code(message: types.Message):
    user_id = message.from_user.id
    code = message.text
    ver_code = user_data[user_id]["ver_code"]
    if str(ver_code) == code:
        user_data[user_id]["status"] = "verified"
        await message.answer("Nomeringiz tasdiqlandi")
        await menu(message)
    else:
        await message.answer("Kod xato terildi. Yana urinib ko'ring")
    del user_data[user_id]['ver_code']
    print(user_data)


async def sozlamalar(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "sozlamalar"
    button = [
        [types.KeyboardButton(text="Isimni o'zgartirish"), types.KeyboardButton(text="📱 Raqamni o'zgartirish")],
        [types.KeyboardButton(text="🏙 Shaharni o'zgartirish"), types.KeyboardButton(text="🇺🇿 Tilni o'zgartirish")],
        [types.KeyboardButton(text="ℹ️ Filallar haqida ma'lumot"), types.KeyboardButton(text="📄 Ommaviy taklif")],
        [types.KeyboardButton(text="⬅️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Harakatni tanlang:", reply_markup=keyboard)
    print(8, user_data)


async def ism(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]['ismlarr'] = "ism"
    # user_data[user_id]['name'] = "change name"
    button = [
        [types.KeyboardButton(text="🔽 Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Iltimos, ismingiz va familiyangizni kiriting.", reply_markup=keyboard)
    print(9, user_data)


async def checkname(message: types.Message):
    user_id = message.from_user.id
    checkname = message.text
    user_data[user_id]["name"] = checkname
    await message.answer("✅ Tayyor")
    del user_data[user_id]['ismlarr']



async def fikr(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = fikr
    button = [
        [types.KeyboardButton(text="◀️ Ortga"), types.KeyboardButton(text="✅ Tasdiqlash")],
    ]
    buttons = [
        [types.InlineKeyboardButton(text="Mahsulot", callback_data="mahsulot")],
        [types.InlineKeyboardButton(text="1😣", callback_data="sticker"),
         types.InlineKeyboardButton(text="2☹️", callback_data="sticker"),
         types.InlineKeyboardButton(text="3😐", callback_data="sticker"),
         types.InlineKeyboardButton(text="4😑", callback_data="sticker"),
         types.InlineKeyboardButton(text="5😍", callback_data="sticker"), ],
        [types.InlineKeyboardButton(text="Xizmat", callback_data="xizmat")],
        [types.InlineKeyboardButton(text="1👊🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="2👎🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="3👌🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="4🤙🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="5👍🏻", callback_data="sticker"), ],
        [types.InlineKeyboardButton(text="Yetkazib berish", callback_data="yetkazib berish")],
        [types.InlineKeyboardButton(text="1🐌", callback_data="sticker"),
         types.InlineKeyboardButton(text="2🐢", callback_data="sticker"),
         types.InlineKeyboardButton(text="3🛺", callback_data="sticker"),
         types.InlineKeyboardButton(text="4🏎", callback_data="sticker"),
         types.InlineKeyboardButton(text="5🚀", callback_data="sticker"), ],
    ]
    keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("✅ Les Ailes xizmati sharhi.", reply_markup=keyboards)
    await message.answer("Tanlovingiz uchun rahmat va biz ishimizni 5 balli tizimda baholashingizdan mamnun bo'lamiz.",
                         reply_markup=keyboard)
    print(8, user_data)



async def olibketish(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "olibketish"
    button = [
        [types.KeyboardButton(text="↙️ Ortga"),types.KeyboardButton(text="📍 Eng yaqin fillialni tanlang")],
        [types.KeyboardButton(text="🌐 Bu yerda buyurtma berish"), types.KeyboardButton(text="Filialni tanlang")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Qayerdasiz 👀? Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni aniqlaymiz",reply_markup=keyboard)



async def website(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "website"

    # Tugmalarni aniqlash
    button = [
        [types.InlineKeyboardButton(text="O'tish", url="https://lesailes.uz/")],
    ]
    keyboards = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)

    # Rasm yuborish va matn bilan havolani qo'shish
    file_path = "images/images.png"
    caption_text = (
        "O'z joylashuvingiz bilan buyurtma bering -\n"
        "[https://lesailes.uz/](https://lesailes.uz/)"
    )

    await message.reply_photo(
        caption=caption_text,
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",  # Markdown formatida matnni formatlash
        reply_markup=keyboards  # Tugmalarni rasm bilan yuborish
    )


async def engyaqinfilial(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["engyaqinfilial"] = "engyaqinfilial"
    button = [
        [types.KeyboardButton(text="Lokatsiyani jo'natish",request_location=True)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)
    await message.answer("Lokatsiyangizni jo'nating",reply_markup=keyboard)
    print(user_data)
    user_data[user_id]["locationkeldi"] = "locationkeldi"


location = {}

from geopy.geocoders import Nominatim

async def check_location(message: types.Message):
    user_id = message.from_user.id
    geolocator = Nominatim(user_agent="geo_bot")

    if message.location is not None:
        latitude = message.location.latitude
        longitude = message.location.longitude

        # # Koordinatalarni manzil nomiga o‘girish
        # location_info = geolocator.reverse((latitude, longitude), exactly_one=True)
        # address = location_info.address if location_info else "Manzil topilmadi"

        address_info = geolocator.reverse((latitude, longitude), exactly_one=True)

        if address_info:
            address = address_info.address
        else:
            address = "Manzil topilmadi"

        location = {
            "latitude": latitude,
            "longitude": longitude,
            "address": address
        }
    else:
        location = message.text

    user_data[user_id]["location"] = location
    button = [
        [types.KeyboardButton(text="▶️ Ortga"), types.KeyboardButton(text="✅ Tasdiqlash")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)

    await message.reply(f"Sizning manzilingiz:📍{address}\n\nJoylashuvni tasdiqlang yoki qayta yuboring",
                        reply_markup=keyboard)
    print(user_data)
    print(location)


async def filialnitanlash(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "filialnitanlash"
    button = [
        [types.KeyboardButton(text="Yunusobod"),types.KeyboardButton(text="S.Rahimova")],
        [types.KeyboardButton(text="Atlas"),types.KeyboardButton(text="M-5")],
        [types.KeyboardButton(text="Asia Nukus"),types.KeyboardButton(text="Farhod")],
        [types.KeyboardButton(text="Ko‘kcha"),types.KeyboardButton(text="Oybek")],
        [types.KeyboardButton(text="Parus"),types.KeyboardButton(text="Samarqand Darvoza")],
        [types.KeyboardButton(text="Chilonzor"),types.KeyboardButton(text="Next")],
        [types.KeyboardButton(text="Zenit"),types.KeyboardButton(text="Atlas")],
        [types.KeyboardButton(text="Buyuk ipak yo'li"),types.KeyboardButton(text="Sergili")],
        [types.KeyboardButton(text="↙️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Qaysi filialdan olib ketishni tanlang",reply_markup=keyboard)






async def asosiymenu(message: types.Message):
    user_id = message.from_user.id
    location = message.text
    if location == '↖️ Ortga' or location == '↪️ Ortga':
        loc = 'salom'
    else:
        loc = lists[location]
        await message.answer(f"{loc}")
        await bot.send_location(chat_id=message.from_user.id,
                                longitude=69.338328,
                                latitude=41.344346)
    user_data[user_id]["holat"] = "asosiymenu"
    button = [
        [types.KeyboardButton(text="↩️ Ortga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="🍱 Setlar"), types.KeyboardButton(text="🍗 Tovuq")],
        [types.KeyboardButton(text="🍟 Sneklar"), types.KeyboardButton(text="🌯 Lesterlar")],
        [types.KeyboardButton(text="🍔 Burgerlar"), types.KeyboardButton(text="🌭 Longerlar/Hot-dog")],
        [types.KeyboardButton(text="🥤 Ichimliklar"), types.KeyboardButton(text="🥗 Salatlar")],
        [types.KeyboardButton(text="🍩 Ponchiklar"), types.KeyboardButton(text="👶 Bolajonlarga")],
        [types.KeyboardButton(text="🍅 Souslar")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Nimadan boshlaymiz?", reply_markup=keyboard)




async def yetkazibberish(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "yetkazibberish"
    button = [
        [types.KeyboardButton(text="📍 Eng yaqin fillialni tanlang")],
        [types.KeyboardButton(text="↙️ Ortga"),types.KeyboardButton(text="🗺 Mening manzillarim")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Buyurtmangizni qayerga yetkazib berish "
                         "kerak 🚙?\nAgar lokatsiyangizni📍 yuborsangiz, sizga "
                         "eng yaqin filialni va yetkazib berish xarajatlarini aniqlaymiz 💵",reply_markup=keyboard)



async def yopiqmanzil(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "yopiqmanzil"
    await message.answer("Afsuski, bu filial yopiq. 😔\n"
                             "Buyurtmani ish soatlarida berishga ishonch hosil qiling.\n"
                             "Les Ailes yetkazib berish xizmatini tanlaganingiz uchun tashakkur.")


async def manzil(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "manzil"
    await message.answer("Sizda saqlangan manzillar yo'q")


lists = {"Yunusobod":"Yunusobod \nA. Donish ko‘chasi, 80",
         "S.Rahimova":"S.Rahimov\nмахалля Яккабог, Чиланзарский район, Ташкент",
         "M-5":"M-5\nSh. Rashidov shox k. 16A",
         "Asia Nukus":"Asia Nukus\nMKAD, 19",
         "Farhod":"Farhod\nUchtepa t. G9A, 21/2",
         "Ko‘kcha":"Ko‘kcha\nShayxontohur t.\nKo‘kcha darvoza 3A",
         "Oybek":"Oybek\nShahrisabz ko‘chasi, 10b",
         "Samarqand Darvoza savdo markazi":"Samarqand Darvoza savdo markazi\nToshkent shahar, Qoratosh ko'chasi, 5A",
         "Chilonzor":"Chilonzor\n2-blok, 2-uy",
         "Next":"Next\nBobur ko‘chasi, 6-uy",
         "Zenit":"Zenit\n7-й квартал, 49, массив Юнусабад, Юнусабадский район, Ташкент",
         "Sergeli":"Sergeli\nGolden life KSM",
         }


taom = [
    'Kombo set', '1+1 Sezar burger',"Qiyqiriq set",
    'Klassik set', "Do'stlar 1x", "Lester set",
    "Snek set", "Do'stlar 2x, achchiq", "4 Friends Klassik burger",
    "4 Friends Lester chiz", "Do'stlar 4x, achchiq", "1+1 Barbekyu burger", "Yangi set",
    "Skulll set", "Do'stlar 1x, achchiq", "Longer rings set", "Big set",
    "4 Friends Hot-dog", "4 Friends Longer chiz", "Do'stlar 4x"
]

ichimliklar = {
    'Montella 0.33': 15000,
    "Qora choy": 16000,
    "Ko'k choy": 17000,
    "Limonli qora choy": 18000,
    "Limonli ko'k choy": 19000,
    'Espresso': 20000,
    'Coca-cola 0.5': 21000,
    "Fanta 0.5": 22000,
    "Sprite 0.5": 23000,
    "Les tea!": 24000,
    "Frutea Berry mix": 25000,
    'Frutea Orange': 26000,
    'Frutea Strawberry': 27000,
    "Americano": 28000,
    "Ays kofe": 29000,
    "Aysti": 30000,
    "Cappuccino": 31000,
    'Latte': 32000,
    "Ays kofe milk": 33000,
    "New Moxito": 34000,
    "Berry Moxito": 35000
}

# tovuq_dict = {
#     'Chiken korn': 15000,
#     "Qanot, 3 dona": 18000,
#     'Achchiq qanot, 3 dona': 20000,
#     "Strips, 3 dona": 22000,
#     "Achchiq strips, 3 dona": 25000,
#     "Chizi chiken korn": 27000,
#     "Qanot, 7 dona": 30000,
#     "Achchiq qanot, 7 dona": 32000,
#     "Strips, 7 dona": 35000,
#     "Achchiq strips, 7 dona": 37000,
#     "Qanot, 17 dona": 40000,
#     'Achchiq qanot, 17 dona': 42000,
#     'Strips, 17 dona': 45000,
#     "Achchiq strips, 17 dona": 50000
# }

button_values_snek = {
    'Tovuq nagetsi, 3 dona': 15000,
    "Chiken stiks, 3 dona": 17000,
    'Fri kartoshkasi': 20000,
    "Pishloqli tovuq sharchalari, 3 dona": 22000,
    "Pishloqli kartoshka sharchalari, 7 dona": 25000,
    "Jaydari kartoshka": 27000,
    "Tovuq nagetsi, 5 dona": 30000,
    "Chiken stiks, 5 dona": 32000,
    "Pishloqli tovuq sharchalari, 5 dona": 35000,
    "Pishloqli kartoshka sharchalari, 11 dona": 37000,
    "Fri basket": 40000
}

button_values_lester = {
    'Lester sezar': 15000,
    "Amerikan lester": 18000,
    'Lester toster': 20000,
    "Barbekyu lester": 22000,
    "Lester chili": 25000,
    "Lester xalapenyo": 27000,
    "Lester chiz": 30000,
    "Big boks": 35000
}

button_values_burger = {
    'Klassik': 15000,
    "1+1 Barbekyu burger": 18000,
    '1+1 Sezar burger': 20000,
    "Singer": 22000,
    "Chiken chiz": 25000,
    "Xalapenyo burger": 27000,
    "Biger": 30000,
    "Dabl chiken chiz": 35000
}

button_values_longer_hotdog = {
    'Hot-dog': 15000,
    "Longer": 18000,
    'Longer rings': 20000,
    "Longer chiz": 22000
}

button_values_salat = {
    'Koulslou': 15000,
    "Sezam": 18000,
    'Les Barbekyu': 20000,
    "Sezar": 22000,
    'Grekcha': 25000
}

button_values_ponchik = {
    'Blueberry donut': 15000,
    "Caramel": 18000,
    'Cinnamon': 20000,
    "Cookies": 22000,
    "Nutty cream": 25000,
    'Panna cotta': 27000,
    'Strawberry': 30000
}

button_values_bolalarga = {
    "Kids box longer O'": 15000,
    "Kids box longer Q": 18000,
    "Kids box lester O'": 20000,
    "Kids box lester Q": 22000
}

button_values_sous = {
    'Ketchup': 15000,
    "Chili": 18000,
    'Sezar': 20000,
    "Chizi": 22000,
    'Mayonez': 25000
}



main_menu = [
    "🍱 Setlar", "🍗 Tovuq", "🍟 Sneklar", "🌯 Lesterlar",
    "🍔 Burgerlar", "🌭 Longerlar/Hot-dog", "🥤 Ichimliklar","🥗 Salatlar","🍩 Ponchiklar",
    "👶 Bolajonlarga", "🍅 Souslar",
]


async def menu_tekshiruv(message: types.Message):
    user_id = message.from_user.id
    choice = message.text
    if choice == '🍱 Setlar':
        await taomlar(message)
        user_data[user_id]['tanlov'] = 'Setlar'
    elif choice == '🥤 Ichimliklar':
        await ichimlik(message)
        user_data[user_id]['tanlov'] = 'Ichimliklar'
    # elif choice == '↖️ Ortga':
    #     await asosiymenu(message)
    elif choice == '🍗 Tovuq':
        await tovuqlar(message)
        user_data[user_id]['tanlov'] = 'Tovuq'
    elif choice == '🍟 Sneklar':
        await snek(message)
        user_data[user_id]['tanlov'] = 'Sneklar'
    elif choice == '🌯 Lesterlar':
        await lester(message)
        user_data[user_id]['tanlov'] = 'Lesterlar'
    elif choice == "🍔 Burgerlar":
        await burger(message)
        user_data[user_id]['tanlov'] = 'Burgerlar'
    elif choice == "🌭 Longerlar/Hot-dog":
        await longer_hotdog(message)
        user_data[user_id]['tanlov'] = 'Longerlar/Hot-dog'
    elif choice == "🥗 Salatlar":
        await salat(message)
        user_data[user_id]['tanlov'] = 'Salatlar'
    elif choice == "🍩 Ponchiklar":
        await ponchik(message)
        user_data[user_id]['tanlov'] = 'Ponchiklar'
    elif choice == "👶 Bolajonlarga":
        await bolalarga(message)
        user_data[user_id]['tanlov'] = 'Bolajonlarga'
    elif choice == "🍅 Souslar":
        await sous(message)
        user_data[user_id]['tanlov'] = 'Souslar'




async def ichimlik(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "ichimlik"
    button = [
        [types.KeyboardButton(text="↪️ Ortga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text='Montella 0.33'), types.KeyboardButton(text='Qora choy')],
        [types.KeyboardButton(text="Ko'k choy"), types.KeyboardButton(text='Limonli qora choy')],
        [types.KeyboardButton(text="Ko'k limonli choy"), types.KeyboardButton(text="Espresso")],
        [types.KeyboardButton(text="Coca-cola 0.5"), types.KeyboardButton(text="Fanta 0.5")],
        [types.KeyboardButton(text="Sprite 0.5"), types.KeyboardButton(text="Les tea!")],
        [types.KeyboardButton(text="Frutea Berry mix"), types.KeyboardButton(text="Frutea Orange")],
        [types.KeyboardButton(text="Frutea Strawberry"), types.KeyboardButton(text="Americano")],
        [types.KeyboardButton(text="Ayse kofe"), types.KeyboardButton(text="Aysti")],
        [types.KeyboardButton(text="Cappuccino"), types.KeyboardButton(text="Latte")],
        [types.KeyboardButton(text="Ayse kofe milk"), types.KeyboardButton(text="New moxito")],
        [types.KeyboardButton(text="Berry moxito")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Nimadan boshlaymiz?", reply_markup=keyboard)
    print(user_data)


async def ichimlik_zakaz(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "ichimlik_zakaz"
    item = message.text
    price = ichimliklar[item]
    name = item
    buttons = [
        [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
    ]
    keyboards = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    button = [
        [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}"),],
        [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)

    # Rasm yuborish va matn bilan havolani qo'shish
    file_path_cola = "images/cola.jpg"
    caption_text_cola = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_koklimon = "images/Limonliko'kchoy.jpg"
    caption_text_koklimon = (
        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_limonqora = "images/Limonliqorachoy.jpg"
    caption_text_limonqora = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_kok = "images/Ko'k-choy.jpg"
    caption_text_kok = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_qora = "images/Qora-choy.jpg"
    caption_text_qora = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_montella = "images/montelaa-033.jpg"
    caption_text_montella = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_fanta = "images/fanta.jpg"
    caption_text_fanta = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_sprite = "images/sprite.jpg"
    caption_text_sprite = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_lestea = "images/Lestea!.jpg"
    caption_text_lestea = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_frutberry = "images/FruteaBerry.jpg"
    caption_text_frutberry = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_frutfanta = "images/FruteaOrange.jpg"
    caption_text_frutfanta = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_frutstrbyy = "images/FruteaStrawberry.jpg"
    caption_text_frutstrbyy = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )


    await message.answer("Miqdorni belgilang",reply_markup=keyboards)
    if message.text == 'Montella 0.33':
        await message.reply_photo(
            caption=caption_text_montella,
            photo=types.FSInputFile(path=file_path_montella),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Qora choy':
        await message.reply_photo(
            caption=caption_text_qora,
            photo=types.FSInputFile(path=file_path_qora),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Ko'k choy":
        await message.reply_photo(
            caption=caption_text_kok,
            photo=types.FSInputFile(path=file_path_kok),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Limonli qora choy':
        await message.reply_photo(
            caption=caption_text_limonqora,
            photo=types.FSInputFile(path=file_path_limonqora),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Ko'k limonli choy":
        await message.reply_photo(
            caption=caption_text_koklimon,
            photo=types.FSInputFile(path=file_path_koklimon),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Coca-cola 0.5":
        await message.reply_photo(
            caption=caption_text_cola,
            photo=types.FSInputFile(path=file_path_cola),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Fanta 0.5":
        await message.reply_photo(
            caption=caption_text_fanta,
            photo=types.FSInputFile(path=file_path_fanta),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Sprite 0.5":
        await message.reply_photo(
            caption=caption_text_sprite,
            photo=types.FSInputFile(path=file_path_sprite),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Les tea!":
        await message.reply_photo(
            caption=caption_text_lestea,
            photo=types.FSInputFile(path=file_path_lestea),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Frutea Berry mix":
        await message.reply_photo(
            caption=caption_text_frutberry,
            photo=types.FSInputFile(path=file_path_frutberry),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Frutea Orange":
        await message.reply_photo(
            caption=caption_text_frutfanta,
            photo=types.FSInputFile(path=file_path_frutfanta),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Frutea Strawberry":
        await message.reply_photo(
            caption=caption_text_frutstrbyy,
            photo=types.FSInputFile(path=file_path_frutstrbyy),
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    else:
        await message.answer("Hi")

async def taomlar(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "taomlar"
    button = [
        [types.KeyboardButton(text="↪️ Ortga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Kombo set"), types.KeyboardButton(text="1+1 Barbekyu burger")],
        [types.KeyboardButton(text="1+1 Sezar burger"), types.KeyboardButton(text="Yangi set")],
        [types.KeyboardButton(text="Klassik set"), types.KeyboardButton(text="Skulll set")],
        [types.KeyboardButton(text="Do'stlar 1x"), types.KeyboardButton(text="Do'stlar 1x, achchiq")],
        [types.KeyboardButton(text="Qiyqiriq set"), types.KeyboardButton(text="Longer rings set")],
        [types.KeyboardButton(text="Lester set"), types.KeyboardButton(text="Big set")],
        [types.KeyboardButton(text="Snek set"), types.KeyboardButton(text="Do'stlar 2x")],
        [types.KeyboardButton(text="Do'stlar 2x, achchiq"), types.KeyboardButton(text="4 Friends Hot-dog")],
        [types.KeyboardButton(text="4 Friends Klassik burger"), types.KeyboardButton(text="4 Friends Longer chiz")],
        [types.KeyboardButton(text="4 Friends Lester chiz"), types.KeyboardButton(text="Do'stlar 4x")],
        [types.KeyboardButton(text="Do'stlar 4x, achchiq")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Nimadan boshlaymiz?", reply_markup=keyboard)
    print(user_data)





async def savat(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "savat"
    item = message.text
    price = 22000
    name = item
    buttons = [
        [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
    ]
    keyboards = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    button = [
        [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}"),],
        [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)

    # Rasm yuborish va matn bilan havolani qo'shish
    file_path_c = "images/1+1.jpg"
    caption_text_c = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    # Rasm yuborish va matn bilan havolani qo'shish 2
    file_path_s = "images/cezar.jpg"
    caption_text_s = (
        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_a = "images/klassic.jpg"
    caption_text_a = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_z = "images/yangiset.jpg"
    caption_text_z = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_x = "images/school.jpg"
    caption_text_x = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path = "images/komboset.jpg"
    caption_text = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_d = "images/Do’stlar-1х.jpg"
    caption_text_d = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_ach = "images/Do’stlar-1х-achchiq.jpg"
    caption_text_ach = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_qiyqiriq = "images/Qiyqiriq-set.jpg"
    caption_text_qiyqiriq = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_long = "images/Longer-rings-set.jpg"
    caption_text_long = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_lest = "images/Lester-set.jpg"
    caption_text_lest = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_big = "images/Big-set.jpg"
    caption_text_big = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_snek = "images/Snek-set.jpg"
    caption_text_snek = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_dost = "images/Do’stlar-2х.jpg"
    caption_text_dost = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_achiq = "images/Do’stlar-2х-achchiq.jpg"
    caption_text_achiq = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_4dost = "images/4 Friends-Hot-dog.jpg"
    caption_text_4dost = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_4dostb = "images/4-Friends-Klassik burger.jpg"
    caption_text_4dostb = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_4dostbl = "images/4-Friends-Longer-chiz.jpg"
    caption_text_4dostbl = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_4doslch = "images/4-Friends-Lester-chiz.jpg"
    caption_text_4doslch = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_dost4 = "images/Do’stlar-4х.jpg"
    caption_text_dost4 = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_dost4ach = "images/Do’stlar-4х.jpg"
    caption_text_dost4ach = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )


    await message.answer("Miqdorni belgilang",reply_markup=keyboards)
    if message.text == 'Kombo set':
        await message.reply_photo(
            caption=caption_text,
            photo=types.FSInputFile(path=file_path),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == '1+1 Barbekyu burger':
        await message.reply_photo(
            caption=caption_text_c,
            photo=types.FSInputFile(path=file_path_c),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == '1+1 Sezar burger':
        await message.reply_photo(
            caption=caption_text_a,
            photo=types.FSInputFile(path=file_path_a),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == 'Klassik set':
        await message.reply_photo(
            caption=caption_text_s,
            photo=types.FSInputFile(path=file_path_s),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == 'Skulll set':
        await message.reply_photo(
            caption=caption_text_x,
            photo=types.FSInputFile(path=file_path_x),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == 'Yangi set':
        await message.reply_photo(
            caption=caption_text_z,
            photo=types.FSInputFile(path=file_path_z),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == "Do'stlar 1x":
        await message.reply_photo(
            caption=caption_text_d,
            photo=types.FSInputFile(path=file_path_d),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == "Do'stlar 1x, achchiq":
        await message.reply_photo(
            caption=caption_text_ach,
            photo=types.FSInputFile(path=file_path_ach),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Qiyqiriq set":
        await message.reply_photo(
            caption=caption_text_qiyqiriq,
            photo=types.FSInputFile(path=file_path_qiyqiriq),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Longer rings set":
        await message.reply_photo(
            caption=caption_text_long,
            photo=types.FSInputFile(path=file_path_long),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Lester set":
        await message.reply_photo(
            caption=caption_text_lest,
            photo=types.FSInputFile(path=file_path_lest),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Big set":
        await message.reply_photo(
            caption=caption_text_big,
            photo=types.FSInputFile(path=file_path_big),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Snek set":
        await message.reply_photo(
            caption=caption_text_snek,
            photo=types.FSInputFile(path=file_path_snek),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Do'stlar 2x":
        await message.reply_photo(
            caption=caption_text_dost,
            photo=types.FSInputFile(path=file_path_dost),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Do'stlar 2x, achchiq":
        await message.reply_photo(
            caption=caption_text_achiq,
            photo=types.FSInputFile(path=file_path_achiq),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "4 Friends Hot-dog":
        await message.reply_photo(
            caption=caption_text_4dost,
            photo=types.FSInputFile(path=file_path_4dost),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "4 Friends Klassik burger":
        await message.reply_photo(
            caption=caption_text_4dostb,
            photo=types.FSInputFile(path=file_path_4dostb),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "4 Friends Longer chiz":
        await message.reply_photo(
            caption=caption_text_4dostbl,
            photo=types.FSInputFile(path=file_path_4dostbl),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "4 Friends Lester chiz":
        await message.reply_photo(
            caption=caption_text_4doslch,
            photo=types.FSInputFile(path=file_path_4doslch),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Do'stlar 4x":
        await message.reply_photo(
            caption=caption_text_dost4,
            photo=types.FSInputFile(path=file_path_dost4),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == "Do'stlar 4x, achchiq":
        await message.reply_photo(
            caption=caption_text_dost4ach,
            photo=types.FSInputFile(path=file_path_dost4ach),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    else:
        await message.answer("Hi")


# Mahsulotlar haqidagi ma'lumotlarni bitta lug'atda jamlaymiz:
tovuq_dict = {
    'Chiken korn': {
        'narx': 15000,
        'rasm': "images/chickencorn.jpg"
    },
    "Qanot, 3 dona": {
        'narx': 18000,
        'rasm': "images/qanot-3dona.jpg"
    },
    'Achchiq qanot, 3 dona': {
        'narx': 20000,
        'rasm': "images/achchiqqanot3dona.jpg"
    },
    "Strips, 3 dona": {
        'narx': 22000,
        'rasm': "images/strips3dona.jpg"
    },
    "Achchiq strips, 3 dona": {
        'narx': 25000,
        'rasm': "images/achchiqstrips.jpg"
    },
    "Chizi chiken korn": {
        'narx': 27000,
        'rasm': "images/chizchicken.jpg"
    },
    "Qanot, 7 dona": {
        'narx': 30000,
        'rasm': "images/qanot7.jpg"
    },
    "Achchiq qanot, 7 dona": {
        'narx': 32000,
        'rasm': "images/achchiqqanot7.jpg"
    },
    "Strips, 7 dona": {
        'narx': 35000,
        'rasm': "images/strips7.jpg"
    },
    "Achchiq strips, 7 dona": {
        'narx': 37000,
        'rasm': "images/achchiqstrips7.jpg"
    },
    "Qanot, 17 dona": {
        'narx': 40000,
        'rasm': "images/qanot17.jpg"
    },
    "Achchiq qanot, 17 dona": {
        'narx': 42000,
        'rasm': "images/achchiqqanot17.jpg"
    },
    "Strips, 17 dona": {
        'narx': 45000,
        'rasm': "images/strips17.jpg"
    },
    "Achchiq strips, 17 dona": {
        'narx': 50000,
        'rasm': "images/achchiqstrips17.jpg"
    }
}


async def tovuqlarr(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "tovuqlarr"
    item = message.text

    # Agar mahsulot lug'atda bo'lsa
    if item in tovuq_dict:
        info = tovuq_dict[item]
        narx = info['narx']
        rasm_manzi = info['rasm']

        # Klaviatura tugmalari
        asosiy_tugmalar = [
            [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
        ]
        reply_keyboard = types.ReplyKeyboardMarkup(keyboard=asosiy_tugmalar, resize_keyboard=True)

        inline_tugmalar = [
            [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
             types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
             types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}")],
            [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}")],
        ]
        inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=inline_tugmalar, resize_keyboard=True)

        # Caption yaratamiz (oddiy qilib)
        caption_text = f"Nomi: {item}\nNarxi: {narx} so'm"

        await message.answer("Miqdorni belgilang", reply_markup=reply_keyboard)
        await message.reply_photo(
            caption=caption_text,
            photo=types.FSInputFile(path=rasm_manzi),
            parse_mode="Markdown",
            reply_markup=inline_keyboard
        )
    else:
        await message.answer("Bunday mahsulot topilmadi!")


burger_dict = {
    'Klassik': {
        'narx': 15000,
        'rasm': "images/classic.jpg"
    },
    "1+1 Barbekyu burger": {
        'narx': 18000,
        'rasm': "images/1+1barbekyu.jpg"
    },
    '1+1 Sezar burger': {
        'narx': 20000,
        'rasm': "images/1+1Sezarburger.jpg"
    },
    "Singer": {
        'narx': 22000,
        'rasm': "images/singer.jpg"
    },
    "Chiken chiz": {
        'narx': 25000,
        'rasm': "images/chickenchiz.jpg"
    },
    "Xalapenyo burger": {
        'narx': 27000,
        'rasm': "images/xalapenyo.jpg"
    },
    "Biger": {
        'narx': 30000,
        'rasm': "images/bigger.jpg"
    },
    "Dabl chiken chiz": {
        'narx': 32000,
        'rasm': "images/doublechickenchiz.jpg"
    }
}


async def burgerlarr(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "burgerlar"
    item = message.text

    # Agar mahsulot lug'atda bo'lsa
    if item in burger_dict:
        info = burger_dict[item]
        narx = info['narx']
        rasm_manzi = info['rasm']

        # Klaviatura tugmalari
        asosiy_tugmalar = [
            [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
        ]
        reply_keyboard = types.ReplyKeyboardMarkup(keyboard=asosiy_tugmalar, resize_keyboard=True)

        inline_tugmalar = [
            [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
             types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
             types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}")],
            [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}")],
        ]
        inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=inline_tugmalar, resize_keyboard=True)

        # Caption yaratamiz (oddiy qilib)
        caption_text = f"Nomi: {item}\nNarxi: {narx} so'm"

        await message.answer("Miqdorni belgilang", reply_markup=reply_keyboard)
        await message.reply_photo(
            caption=caption_text,
            photo=types.FSInputFile(path=rasm_manzi),
            parse_mode="Markdown",
            reply_markup=inline_keyboard
        )
    else:
        await message.answer("Bunday mahsulot topilmadi!")





async def sneklarr(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "sneklar"
    item = message.text
    price = 22000
    name = item
    buttons = [
        [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
    ]
    keyboards = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    button = [
        [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}"), ],
        [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)

    file_path_tn = "images/tovuqnagets.jpg"
    print("rasm yuborildi")
    caption_text_tn = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_chst = "images/chickenstiks.jpg"
    caption_text_chst = (
        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_free = "images/free.jpg"
    caption_text_free = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_pshk = "images/pishloqlikartoshka.jpg"
    caption_text_pshk = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_cheest = "images/cheestovuq5.jpg"
    caption_text_cheest = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_jaydari = "images/jaydarikartoshka.jpg"
    caption_text_jaydari = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_tn5 = "images/tovuqnagets.jpg"
    caption_text_tn5 = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_chs5 = "images/chickensticks.jpg"
    caption_text_chs5 = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_ptsh5 = "images/tovuqsharchalari.jpg"
    caption_text_ptsh5 = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_ptsh11 = "images/pishloqlikartoshka.jpg"
    caption_text_ptsh11 = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_freebasket = "images/freebasket.jpg"
    caption_text_freebasket = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )

    await message.answer("Miqdorni belgilang", reply_markup=keyboards)
    if message.text == 'Tovuq nagetsi, 3 dona':
        await message.reply_photo(
            caption=caption_text_tn,
            photo=types.FSInputFile(path=file_path_tn),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Chiken stiks, 3 dona':
        await message.reply_photo(
            caption=caption_text_chst,
            photo=types.FSInputFile(path=file_path_chst),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Fri kartoshkasi':
        await message.reply_photo(
            caption=caption_text_free,
            photo=types.FSInputFile(path=file_path_free),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Pishloqli tovuq sharchalari, 3 dona':
        await message.reply_photo(
            caption=caption_text_pshk,
            photo=types.FSInputFile(path=file_path_pshk),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Pishloqli kartoshka sharchalari, 7 dona':
        await message.reply_photo(
            caption=caption_text_cheest,
            photo=types.FSInputFile(path=file_path_cheest),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Jaydari kartoshka':
        await message.reply_photo(
            caption=caption_text_jaydari,
            photo=types.FSInputFile(path=file_path_jaydari),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Tovuq nagetsi, 5 dona':
        await message.reply_photo(
            caption=caption_text_tn5,
            photo=types.FSInputFile(path=file_path_tn5),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Chiken stiks, 5 dona':
        await message.reply_photo(
            caption=caption_text_chs5,
            photo=types.FSInputFile(path=file_path_chs5),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Pishloqli tovuq sharchalari, 5 dona':
        await message.reply_photo(
            caption=caption_text_ptsh5,
            photo=types.FSInputFile(path=file_path_ptsh5),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Pishloqli kartoshka sharchalari, 11 dona':
        await message.reply_photo(
            caption=caption_text_ptsh11,
            photo=types.FSInputFile(path=file_path_ptsh11),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Fri basket':
        await message.reply_photo(
            caption=caption_text_freebasket,
            photo=types.FSInputFile(path=file_path_freebasket),
            parse_mode="Markdown",
            reply_markup=keyboard
        )

    else:
        await message.answer("Hi")




async def lestrlarr(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "lestrlarr"
    item = message.text
    price = 22000
    name = item
    buttons = [
        [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
    ]
    keyboards = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    button = [
        [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}"),],
        [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)

    file_path_ls = "images/lestersezar.jpg"
    print("rasm yuborildi")
    caption_text_ls = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_al = "images/americanlester.jpg"
    caption_text_al = (
        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_lt = "images/lestartoster.jpg"
    caption_text_lt = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_bl = "images/barbekyulestar.jpg"
    caption_text_bl = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_lch = "images/lestarchili.jpg"
    caption_text_lch = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_lx = "images/lestarxalapenyo.jpg"
    caption_text_lx = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_lchiz = "images/lestarchiq.jpg"
    caption_text_lchiz = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_bb = "images/bigbox.jpg"
    caption_text_bb = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )


    await message.answer("Miqdorni belgilang",reply_markup=keyboards)
    if message.text == 'Lester sezar':
        await message.reply_photo(
            caption=caption_text_ls,
            photo=types.FSInputFile(path=file_path_ls),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Amerikan lester':
        await message.reply_photo(
            caption=caption_text_al,
            photo=types.FSInputFile(path=file_path_al),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Lester toster':
        await message.reply_photo(
            caption=caption_text_lt,
            photo=types.FSInputFile(path=file_path_lt),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Barbekyu lester':
        await message.reply_photo(
            caption=caption_text_bl,
            photo=types.FSInputFile(path=file_path_bl),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Lester chili':
        await message.reply_photo(
            caption=caption_text_lch,
            photo=types.FSInputFile(path=file_path_lch),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Lester xalapenyo':
        await message.reply_photo(
            caption=caption_text_lx,
            photo=types.FSInputFile(path=file_path_lx),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Lester chiz':
        await message.reply_photo(
            caption=caption_text_lchiz,
            photo=types.FSInputFile(path=file_path_lchiz),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif message.text == 'Big boks':
        await message.reply_photo(
            caption=caption_text_bb,
            photo=types.FSInputFile(path=file_path_bb),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    else:
        await message.answer("Hi")






count = 1
@dp.callback_query(lambda c: c.data.startswith(('plus', 'minus', 'add')))
async def checkcallback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    narx = callback.data
    price = 10
    name = "Fri kartoshkasiCoca-cola 0.5\n"
    command, item = callback.data.split('_')
    global count

    if command == 'plus':
        count += 1
    elif command == 'minus':
        if count > 1:
            count -= 1
    elif command == 'add':
        if 'basket' not in user_data[user_id]:
            user_data[user_id]['basket'] = {item: count}
        else:
            if item in user_data[user_id]['basket']:
                user_data[user_id]['basket'][item] += count
            else:
                user_data[user_id]['basket'][item] = count

        count = 1  # Reset count after adding item to the basket
        await callback.message.answer(f"Mahsulot: {name} savatga muvaffaqiyatli qo'shildi ✅\n"
                                    "Davom etamizmi?")

    print(f"Count:{count}")
    button = [
        [types.InlineKeyboardButton(text=f"-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text=f"{count}", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text=f"+", callback_data=f"plus_{item}"), ],
        [types.InlineKeyboardButton(text=f"📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    price = price * count  # Update the price based on count
    try:
        print(user_data)
        await callback.message.edit_caption(
            caption="Kombo set\n\n"
                    f"Nomi: {name}\n"
                    f"Narxi: {price} so'm",
            reply_markup=keyboard
        )
    except aiogram.exceptions.TelegramBadRequest as e:
        if "message is not modified" in str(e):
            print("Xabar o'zgarmaganligi sababli yangilash o'tkazib yuborildi.")
        else:
            print(f"Xato yuz berdi: {e}")


async def show_cart(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or not user_data[user_id].get("basket"):
        button = [
            [types.KeyboardButton(text="⬅️ Ortga"), types.KeyboardButton(text="Savatni to'ldirdim ✅")],
            [types.KeyboardButton(text="🔄 tozalash")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer("🛒 Sizning savatingiz bo'sh", reply_markup=keyboard )
        return
    cart_items = user_data[user_id]["basket"]
    total_price = 0
    cart_text = "🛒 Sizning savatingiz:\n\n"
    for idx, (item_name, item_count) in enumerate(cart_items.items(), start=1):
        item_price = 10  # This is the price for each item
        total_price += item_price * item_count  # Multiply price by the count
        cart_text += f"{idx}. {item_name} x{item_count} — {item_price * item_count} so'm\n"
    cart_text += f"\n💵 Jami: {total_price} so'm"
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text="Savatni to'ldirdim ✅")],
        [types.KeyboardButton(text="🔄 tozalash")],
    ]
    button_in = [
        [types.InlineKeyboardButton(text=f"❌bekor qilish", callback_data=f"item_name")],
        [types.InlineKeyboardButton(text="-", callback_data=f"minus"),
         types.InlineKeyboardButton(text="1", callback_data=f"miqdor"),
         types.InlineKeyboardButton(text="+", callback_data=f"plus"),],
    ]
    keyboards = types.InlineKeyboardMarkup(inline_keyboard=button_in, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f'"❌ Mahsulot nomi" - savatdan ochirish\n\n'
                         f'" - и +" - mahsulot sonini kamaytirish yoki qoshish\n\n'
                         f'"🔄 Tozalash" - savatni butunlay boshatish',reply_markup=keyboard)
    await message.answer(cart_text,reply_markup=keyboards)
    print(3, user_data)


async def tolovgqismi(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "final"
    button = [
        [types.KeyboardButton(text="🕙 Keyinroq"),types.KeyboardButton(text="Iloji boricha tezroq✅")],
        [types.KeyboardButton(text="ortgaaaa"),]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("📥 Savat:\n\n"
                         "Bu yerda tovarlarning nomi yozilishi kerak\n\n"
                         "Umumiy narxi:")
    await message.answer("Buyurtmani qabul qilish uchun o'zingizga qulay vaqtni tanlang:",reply_markup=keyboard)


async def onlinepayment(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "onlinepayment"
    button = [
        [types.KeyboardButton(text="💵 Naqd pul ")],
        [types.KeyboardButton(text="💳 Payme"),types.KeyboardButton(text="💳 Click"),],
        [types.KeyboardButton(text="ortgaaaaa")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("To'lov turini tanlang:",reply_markup=keyboard)

async def tovuqlar(message: types.Message):
    user_id = message.from_user.id
    tovuq = message.text
    user_data[user_id]['tovuq'] = tovuq
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Chiken korn'), types.KeyboardButton(text="Qanot, 3 dona")],
        [types.KeyboardButton(text='Achchiq qanot, 3 dona'), types.KeyboardButton(text="Strips, 3 dona")],
        [types.KeyboardButton(text="Achchiq strips, 3 dona"), types.KeyboardButton(text='Chizi chiken korn')],
        [types.KeyboardButton(text='Qanot, 7 dona'), types.KeyboardButton(text="Achchiq qanot, 7 dona")],
        [types.KeyboardButton(text="Strips, 7 dona"), types.KeyboardButton(text="Achchiq strips, 7 dona")],
        [types.KeyboardButton(text="Qanot, 17 dona"), types.KeyboardButton(text='Achchiq qanot, 17 dona')],
        [types.KeyboardButton(text='Strips, 17 dona'), types.KeyboardButton(text="Achchiq strips, 17 dona")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)


async def snek(message: types.Message):
    user_id = message.from_user.id
    snek = message.text
    user_data[user_id]['snek'] = snek
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Tovuq nagetsi, 3 dona'), types.KeyboardButton(text="Chiken stiks, 3 dona")],
        [types.KeyboardButton(text='Fri kartoshkasi'), types.KeyboardButton(text="Pishloqli tovuq sharchalari, 3 dona")],
        [types.KeyboardButton(text="Pishloqli kartoshka sharchalari, 7 dona"), types.KeyboardButton(text='Jaydari kartoshka')],
        [types.KeyboardButton(text='Tovuq nagetsi, 5 dona'), types.KeyboardButton(text="Chiken stiks, 5 dona")],
        [types.KeyboardButton(text="Pishloqli tovuq sharchalari, 5 dona"), types.KeyboardButton(text="Pishloqli kartoshka sharchalari, 11 dona")],
        [types.KeyboardButton(text="Fri basket")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)


async def lester(message: types.Message):
    user_id = message.from_user.id
    lester = message.text
    user_data[user_id]['lester'] = lester
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Lester sezar'), types.KeyboardButton(text="Amerikan lester")],
        [types.KeyboardButton(text='Lester toster'), types.KeyboardButton(text="Barbekyu lester")],
        [types.KeyboardButton(text="Lester chili"), types.KeyboardButton(text='Lester xalapenyo')],
        [types.KeyboardButton(text='Lester chiz'), types.KeyboardButton(text="Big boks")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)


async def burger(message: types.Message):
    user_id = message.from_user.id
    burger = message.text
    user_data[user_id]['burger'] = burger
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Klassik'), types.KeyboardButton(text="1+1 Barbekyu burger")],
        [types.KeyboardButton(text='1+1 Sezar burger'), types.KeyboardButton(text="Singer")],
        [types.KeyboardButton(text="Chiken chiz"), types.KeyboardButton(text='Xalapenyo burger')],
        [types.KeyboardButton(text='Biger'), types.KeyboardButton(text="Dabl chiken chiz")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)


async def longer_hotdog(message: types.Message):
    user_id = message.from_user.id
    longer_hotdog = message.text
    user_data[user_id]['longer_hotdog'] = longer_hotdog
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Hot-dog'), types.KeyboardButton(text="Longer")],
        [types.KeyboardButton(text='Longer rings'), types.KeyboardButton(text="Longer chiz")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)



async def salat(message: types.Message):
    user_id = message.from_user.id
    salat = message.text
    user_data[user_id]['salat'] = salat
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Koulslou'), types.KeyboardButton(text="Sezam")],
        [types.KeyboardButton(text='Les Barbekyu'), types.KeyboardButton(text="Sezar")],
        [types.KeyboardButton(text='Grekcha')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)


async def ponchik(message: types.Message):
    user_id = message.from_user.id
    ponchik = message.text
    user_data[user_id]['ponchik'] = ponchik
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Blueberry donut'), types.KeyboardButton(text="Caramel")],
        [types.KeyboardButton(text='Cinnamon'), types.KeyboardButton(text="Cookies")],
        [types.KeyboardButton(text="Nutty cream"), types.KeyboardButton(text='Panna cotta')],
        [types.KeyboardButton(text='Strawberry')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)



async def bolalarga(message: types.Message):
    user_id = message.from_user.id
    bolalarga = message.text
    user_data[user_id]['bolalarga'] = bolalarga
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text="Kids box longer O'"), types.KeyboardButton(text="Kids box longer Q")],
        [types.KeyboardButton(text="Kids box lester O'"), types.KeyboardButton(text="Kids box lester Q")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)

async def sous(message: types.Message):
    user_id = message.from_user.id
    sous = message.text
    user_data[user_id]['sous'] = sous
    button = [
        [types.KeyboardButton(text='↪️ Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Ketchup'), types.KeyboardButton(text="Chili")],
        [types.KeyboardButton(text='Sezar'), types.KeyboardButton(text="Chizi")],
        [types.KeyboardButton(text='Mayonez')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)








async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())

