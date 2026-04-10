@app.on_message(filters.command(["start"]) & filters.private)
async def f_start(_, m: types.Message):
    await app.send_photo(
        chat_id=m.chat.id,
        photo="https://files.catbox.moe/kpfuks.jpg",
        caption=f"""<b>👋 Hello {m.from_user.first_name}</b>

🤖 Welcome to Session Generator Bot

🔥 Generate Pyrogram & Telethon Session easily!

👇 Click below to start""",
        reply_markup=buttons.start_key(),
        parse_mode=enums.ParseMode.HTML
    )
    await db.add_user(m.from_user.id)
