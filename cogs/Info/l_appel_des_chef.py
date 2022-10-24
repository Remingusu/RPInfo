import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


def setup(bot):
    bot.add_cog(appel_chef(bot))


class appel_chef(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="chef_call", guild_ids=[998628148616904894], description="Donne les phrases des différents clan pour appeler les chats de ce clan",
                       options=[create_option(name="clan", description="Le nom du clan", option_type=3, required=True,
                                              choices=[create_choice(name="Mousses", value="tmo"),
                                                       create_choice(name="Brises", value="tbr"),
                                                       create_choice(name="Ruisseaux", value="tru"),
                                                       create_choice(name="Rochers", value="tro")])])
    async def chef_call(self, ctx, clan):
        # --------------------------------------------------------------------------------------------------------------------------------------------
        roembed = discord.Embed(title="Appel du chef du clan des *Rochers*", color=0x999999)
        roembed.set_thumbnail(url="https://i.ibb.co/bNPWVyd/appel-des-chef.png")
        roembed.add_field(name="Appel", value="Que tous ceux qui sont en âge de parcourir le sentier des cailloux "
                                              "tranchants s'approche de l'estrade pour une assemblée de Clan .")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        ruembed = discord.Embed(title="Appel du chef du clan des *Ruisseaux*", color=0x00D5DC)
        ruembed.set_thumbnail(url="https://i.ibb.co/bNPWVyd/appel-des-chef.png")
        ruembed.add_field(name="Appel", value="Que tous ceux qui sont en âge de traverser le torrent glaciale "
                                              "s'approche du saule pour une assemblée de Clan.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        bembed = discord.Embed(title="Appel du chef du clan des *Brises*", color=0xE8FEFF)
        bembed.set_thumbnail(url="https://i.ibb.co/bNPWVyd/appel-des-chef.png")
        bembed.add_field(name="Appel", value="Que tous ceux qui sont en âge de s'aventurer dans les champs de blés "
                                             "s'approche de la corniche pour une assemblée de Clan.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        membed = discord.Embed(title="Appel du chef du clan des *Mousses*", color=0x1B8D25)
        membed.set_thumbnail(url="https://i.ibb.co/bNPWVyd/appel-des-chef.png")
        membed.add_field(name="Appel", value="Que tous ceux qui sont en âge d'escalader le vieux chêne "
                                             "s'approche de l'arbre pour une assemblée de Clan.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        dico = {"tro": roembed,
                "tru": ruembed,
                "tbr": bembed,
                "tmo": membed}
        choix = dico[clan]
        await ctx.send(embed=choix)
