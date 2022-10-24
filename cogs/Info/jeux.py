import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


def setup(bot):
    bot.add_cog(jeux(bot))


class jeux(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="jeux", guild_ids=[998628148616904894], description="Donne les jeux des différents clans",
                       options=[create_option(name="clan", description="Le nom du clan", option_type=3, required=True,
                                              choices=[create_choice(name="Mousses", value="tmo"),
                                                       create_choice(name="Brises", value="tbr"),
                                                       create_choice(name="Ruisseaux", value="tru"),
                                                       create_choice(name="Rochers", value="tro")])])
    async def jeux(self, ctx, clan):
        # --------------------------------------------------------------------------------------------------------------------------------------------
        membed = discord.Embed(title="Jeux", color=0x476DCB)
        membed.set_thumbnail(url="https://i.ibb.co/ncQ6t0p/game.png")
        membed.add_field(name="**Clan des Mousses**", value="Le **Clan des mousses** joue à "
                                                            "\"*Acro-chat*\"\n\n"
                                                            "\"*Acro-chat*\", règles du jeu: \n\n"
                                                            "Le jeu est très simple. "
                                                            "L'objectif est de faire le plus de tour du camp,"
                                                            " en passant par les quatre arbres qui l'entoure, "
                                                            "sans toucher le sol, le plus rapidement possible.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        bembed = discord.Embed(title="Jeux", color=0x476DCB)
        bembed.set_thumbnail(url="https://i.ibb.co/ncQ6t0p/game.png")
        bembed.add_field(name="**Clan des Brises**", value="Le **Clan des brises** joue à "
                                                           "\"*Offrande*\"\n\n"
                                                           "\"*Offrande*\", règles du jeu: \n\n"
                                                           "Imaginons, que Nuage de couleuvre, Nuage brulée, "
                                                           "Nuage tempétueuse, Etoile du Lynx et Ombre "
                                                           "rousse joue ensemble. Lynx est le chef de jeu. "
                                                           "Il attribue à chaque joueur un objet qu'il va "
                                                           "ensuite cacher. Le premier joueur qui trouve son objet et "
                                                           "l'apporte à Lynx a gagné !")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        ruembed = discord.Embed(title="Jeux", color=0x476DCB)
        ruembed.set_thumbnail(url="https://i.ibb.co/ncQ6t0p/game.png")
        ruembed.add_field(name="**Clan des Ruisseaux**", value="Le **Clan des ruisseaux** joue à "
                                                               "\"*Chasse-Cache*\"\n\n"
                                                               "\"*Chasse-Cache*\", règles du jeu: \n\n"
                                                               "Imaginons que Nuage de saule, Nuage de reflet, "
                                                               "Etoile des cieux et Doux nénuphars jouent ensemble. "
                                                               "Les deux apprentis attendent 20 secondes pour laisser "
                                                               "le temps à leurs parents de se cacher. "
                                                               "Si Saule et Reflet trouvent les parents, ceux-ci "
                                                               "doivent s'enfuir. Dès que les parents sont attraper, "
                                                               "Saule et Reflet on gagné !")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        roembed = discord.Embed(title="Jeux", color=0x476DCB)
        roembed.set_thumbnail(url="https://i.ibb.co/ncQ6t0p/game.png")
        roembed.add_field(name="**Clan des Rochers**", value="Le **Clan des rochers** joue à "
                                                             "\"*Comme une pierre*\"\n\n"
                                                             "\"*Comme une pierre*\", règles du jeu: \n\n"
                                                             "Imaginons que Petite forêt, Feuille de trèfle et "
                                                             "Masque de blaireau joue ensemble. Masque de blaireau, "
                                                             "va compter jusqu'à cinq avant de se retourner. "
                                                             "Pendant ce temps, Feuille de trèfle et Petite forêt "
                                                             "doivent atteindre Masque de blaireau. "
                                                             "Lorsque Masque de blaireau se retourne, les participants "
                                                             "ne doivent pas être visible. Si Masque de blaireau "
                                                             "découvre un participant, celui-ci est éliminé. "
                                                             "\"Comme un pierre\" est utiliser comme entraînement et "
                                                             "peut être composé de parcours !")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        dico = {"tro": roembed,
                "tru": ruembed,
                "tbr": bembed,
                "tmo": membed}
        choix = dico[clan]
        await ctx.send(embed=choix)
