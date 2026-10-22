from openai import OpenAI
from telethon import TelegramClient, events

api_id = 3196867
api_hash = "e0fb700acafd5c2e587b5e9b29ce561"
openai_key = (
    "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"
)

client = TelegramClient("userbot", api_id, api_hash)
ai = OpenAI(api_key=openai_key)


@client.on(events.NewMessage(incoming=True, outgoing=False))
async def main(event):
  if event.is_private:
    res = ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": event.raw_text}],
    )
    await event.reply(res.choices[0].message.content)


client.start()
client.run_until_disconnected()
