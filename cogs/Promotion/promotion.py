import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option
from cogs.Promotion.db_handler_promotion import db_handler_promote

db_handler = db_handler_promote("./../../database.db")


def setup(bot):
    bot.add_cog(promotion(bot))


class promotion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="promotion", guild_ids=[998628148616904894], description="Promeut un chat", options=[
        create_option(name="membre", description="Le nom de la personne à promouvoir", option_type=6, required=True),
        create_option(name="grade", description="Le grade auquel le chat et promeut", option_type=3, required=True,
                      choices=[create_choice(name="Meneur", value="Meneur"),
                               create_choice(name="Lieutenant", value="Lieutenant"),
                               create_choice(name="Soigneur", value="Soigneur"),
                               create_choice(name="Apprenti soigneur", value="Apprenti soigneur"),
                               create_choice(name="Chasseur", value="Chasseur"),
                               create_choice(name="Combattant", value="Combattant"),
                               create_choice(name="Défenseur", value="Défenseur"),
                               create_choice(name="Apprenti chasseur", value="Apprenti chasseur"),
                               create_choice(name="Apprenti combatant", value="Apprenti combatant"),
                               create_choice(name="Apprenti défenseur", value="Apprenti défenseur"),
                               create_choice(name="Reine", value="Reine"),
                               create_choice(name="Ancien", value="Ancien"),
                               create_choice(name="Chaton", value="Chaton")])])
    async def promotion(self, ctx, membre, grade):
        member_name = str(membre)
        member_id = int(membre.id)
        db_handler.promote(grade, member_name, member_id)
        await ctx.send(f"{membre.mention} a été promu au rang de {grade}")
