import os
from userbot import CMD_LIST, ALIVE_NAME, CMD_HELP, CMD_HNDLR
from userbot.utils import admin_cmd
from userbot.manager.utils import edit_or_reply
from userbot.UniborgConfig import config
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Tamilbot"

CUSTM_HLP_EMOJ = os.environ.get("CUSTM_HLP_EMOJ", "✯")

CMD_HNDLR = config.CMD_HNDLR

if CMD_HNDLR is None:
    CMD_HNDLR = "."
 #@command(pattern="^.help ?(.*)")
@borg.on(admin_cmd(pattern=r"help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += CUSTM_HLP_EMOJ + " " + i + " " + CUSTM_HLP_EMOJ + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "cmd.txt"
                    await bot.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="**COMMANDS**",
                        reply_to=reply_to_id
                    )
                    await event.delete()
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = f"""Bot σƒ {DEFAULTUSER}
           
              ⚙️•𝚃𝚊𝚖𝚒𝚕𝙱𝚘𝚝 𝙼𝚎𝚗𝚞•⚙️ """
            try:
                results = await bot.inline_query(  # pylint:disable=E0602
                    tgbotusername,
                    help_string
                )
                await results[0].click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True
                )
                await event.delete()
            except BaseException:
                await event.edit(
                    f"This bot has inline disabled. Please enable it to use `{CMD_HNDLR}help`.\nGet help from [here](t.me/TamilSupport)"
                )

@borg.on(admin_cmd(outgoing=True, pattern="info ?(.*)"))
async def info(event):
    """ For .info command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_or_reply(event, "Please specify a valid plugin name.")
    else:
        string = "**Please specify which plugin do you want help for !!**\
            \n**Usage:** `.info` <plugin name>\n\n"
        for i in sorted(CMD_HELP):
            string += "🔹`" + str(i)
            string += "`   "
        await edit_or_reply(event, string)
