###
# Copyright 2021 tomGER, git@tomger.eu
#
# Licensed under the EUPL, Version 1.2 or – as soon they will be approved by the European Commission - subsequent versions of the EUPL (the "Licence");
# You may not use this work except in compliance with theLicence.
#
# You may obtain a copy of the Licence at: https://joinup.ec.europa.eu/software/page/eupl
#
# Unless required by applicable law or agreed to in writing, software distributed under the Licence is distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and limitations under the Licence.
###

import discord
import dislash

import config

from discord.ext import commands
from dislash import InteractionClient, Option, OptionType

bot = commands.Bot(command_prefix="!")
inter_client = InteractionClient(bot, test_guilds=[config.guild])

channel_option = Option("channel", "Specify the channel", OptionType.CHANNEL, required=True)
text_option = Option("text", "Text that should be added", OptionType.STRING, required=True)

@dislash.has_role(config.admin_role_id)
@inter_client.slash_command(description = "Link to the source code of the bot")
async def note(ctx):
    pass # Base for subcommands

@say.sub_command(description = "Link to the source code of the bot",
    options = [
        channel_option,
        text_option
    ])
async def add(ctx, channel, text: str):
    if not isinstance(channel, discord.TextChannel):
        ctx.send("Invalid Channel")
    if text == "":
        ctx.send("Invalid Text")

    pass # @TODO

@inter_client.slash_command(description = "Link to the source code of the bot")
async def source(ctx):
    await ctx.send("The Source Code can be found at: @TODO: Don't forget to fill this")

bot.run(config.token)