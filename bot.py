import google.genai as genai
from telethon import TelegramClient, events

api_id = 31968687
api_hash = "e0fb7e00acafd5c2e587b5e9b29ce561"
gemini_key = "AQ.Ab8RN6I8vU4YaTQcwuxtKyKESOz0ZJqM3kA5suPusGaDjXaIgg"

client = TelegramClient("userbot", api_id, api_hash)
ai_client = genai.Client(api_key=gemini_key)

system_instruction = (
    "You are a normal guy chatting on Telegram. Always reply in casual,"
    " everyday English (street slang, relaxed tone, lowercase, natural"
    " abbreviations like 'u', 'r', 'gonna', 'wanna', 'lol'). Do NOT sound like"
    " an AI, a bot, or a formal assistant. Keep responses short and"
    " conversational, just like a real person texting a friend."
)


@client.on(events.NewMessage(incoming=True, outgoing=False))
async def main(event):
  if event.is_private:
    response = ai_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=event.raw_text,
        config={"system_instruction": system_instruction},
    )
    await event.reply(response.text)


client.start()
client.run_until_disconnected()
