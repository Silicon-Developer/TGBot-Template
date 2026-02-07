from pyrogram.client import Client
from info import API_ID, API_HASH, BOT_TOKEN, ADMINS

class Bot(Client):
    def __init__(self) -> None:
        super().__init__(
            name="Silicon",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=3,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        for i in ADMINS:
            await self.send_message(i, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
    async def stop(self, *args): 
        await super().stop()
        print("Stopped.....")


Bot().run() #