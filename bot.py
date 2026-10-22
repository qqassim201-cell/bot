from openai import OpenAI
from telethon import TelegramClient, events

api_id = 31968687
api_hash = "e0fb7e00acafd5c2e587b5e9b29ce561"
openai_key = "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"

client = TelegramClient("userbot", api_id, api_hash)
ai = OpenAI(api_key=openai_key)

@client.on(events.NewMessage(incoming=True, outgoing=False))
async def main(event):
    if event.is_private:
        res = ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a normal guy chatting on Telegram. Always reply in casual, everyday English (street slang, relaxed tone, lowercase, natural abbreviations like 'u', 'r', 'gonna', 'wanna', 'lol'). Do NOT sound like an AI, a bot, or a formal assistant. Keep responses short and conversational, just like a real person texting a friend."
                },
                {"role": "user", "content": event.raw_text}
            ]
        )
        await event.reply(res.choices[0].message.content)

client.start()
client.run_until_disconnected()
