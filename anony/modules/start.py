@app.on_message(filters.command(["start"]) & filters.private)
async def f_start(_, m: types.Message):
    await app.send_photo(
        chat_id=m.chat.id,
        photo=Translation.PHOTO_URL,
        caption=Translation.START_TXT.format(m.from_user.first_name),
        reply_markup=buttons.start_key(),
        parse_mode=enums.ParseMode.HTML
    )
    await db.add_user(m.from_user.id)
