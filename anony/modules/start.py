from pyrogram import filters, types
from anony import app, buttons, db

PHOTO_URL = "https://o.uguu.se/buNPcLrC.jpg"

@app.on_message(filters.command(["start"]) & filters.private)
async def f_start(_, m: types.Message):
    await m.reply_photo(
        photo=PHOTO_URL,
        caption=f"Hey {m.from_user.first_name},\n\nThis is {app.mention},\nAn open source session generator bot.",
        reply_markup=buttons.start_key(),
    )
    await db.add_user(m.from_user.id)
