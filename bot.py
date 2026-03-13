import asyncio
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# API Tokenlar
TOKEN = "7678836579:AAEGPLXN-Pw5FNPKXlcIm7Q8Fv961Ug7IY0"
GEMINI_API_KEY = "AIzaSyDpOF9awDgH93YS_nmLUVAQi27uQslrblY"

# Bot va AI sozlamalari
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Gemini AI sozlash
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # TO'G'RI MODEL NOMI

@dp.message(Command("start"))
async def welcome(message: Message):
    await message.answer("👋 Salom! Men Google AI botman. Menga savol bering!")

# /help komandasi
@dp.message(Command('help'))
async def help_command(message: Message):
    await message.answer("✉️ Telegram orqali bog‘lanish uchun: @zuPREDATOR")

# /info komandasi
@dp.message(Command('info'))
async def info_command(message: Message):
    await message.answer("ℹ️ Botning ma'lumotlari:\n📅 Ishlab chiqarilgan sana: 2025.03.27\n🔢 Versiya: Gemeni AI 1.5 pro")    

@dp.message()
async def gemini_reply(message: Message):
    try:
        response = model.generate_content(message.text)  # Foydalanuvchi matniga javob olish
        await message.answer(response.text)  # Javobni yuborish
    except Exception as e:
        await message.answer("Haddan tashqari ko‘p so‘rov yuborildi. Biroz kuting va qayta urinib ko‘ring.")
        await asyncio.sleep(60)  # 1 daqiqa kutish
        print(f"Xato: {e}")  # Terminalda xatolikni chiqarish
     

# Asinxron botni ishga tushirish
async def main():
    try:
        print("Bot ishga tushdi...")
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Polling bekor qilindi!")
    except KeyboardInterrupt:
        print("Bot to‘xtatildi!")
    finally:
        print("Bot yopildi.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur majburan to‘xtatildi!")
