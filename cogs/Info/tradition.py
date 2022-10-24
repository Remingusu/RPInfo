import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


def setup(bot):
    bot.add_cog(tradition(bot))


class tradition(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="traditions", guild_ids=[998628148616904894], description="Donne les traditions des Clans",
                       options=[create_option(name="clan", description="Le nom du clan", option_type=3, required=True,
                                              choices=[create_choice(name="Mousses", value="tmo"),
                                                       create_choice(name="Brises", value="tbr"),
                                                       create_choice(name="Ruisseaux", value="tru"),
                                                       create_choice(name="Rochers", value="tro")])])
    async def traditions(self, ctx, clan):
        # --------------------------------------------------------------------------------------------------------------------------------------------
        troembed = discord.Embed(title="Traditions", color=0xF60086)
        troembed.set_thumbnail(url="https://i.ibb.co/hBmk3Zg/tradition.png")
        troembed.add_field(name="**Clan des rochers**", value="Les membres du Clan de rochers croient, "
                                                              "comme tout les autres Clans, au Clan ancestral. "
                                                              "Pour leur rendre hommage, "
                                                              "ils accrochent des pierres précieuses de "
                                                              "différentes couleur. "
                                                              "Chaque couleur a sa signification:\n"
                                                              "- Le bleu pour la pureté,\n"
                                                              "- Le violet pour la force vital, physique et mental,\n"
                                                              "- Le rouge pour l'amour,\n"
                                                              "- Le vert pour l'espoir,\n"
                                                              "- Le jaune pour une bonne chasse,\n"
                                                              "- Le blanc pour une longue vie.\n "
                                                              "Chaque couleur correspond à une pierre précieuse:\n"
                                                              "- Le bleue correspond au saphir,\n"
                                                              "- Le violet correspond à l'améthyste,\n"
                                                              "- Le rouge correspond au rubis,\n"
                                                              "- Le vert correspond à l'émeraude,\n"
                                                              "- Le jaune correspond à l'ambre,\n"
                                                              "- La blanc correspond au diamant."
                                                              "Toutes ces pierres précieuses sont accrochées au dessus "
                                                              "de l'entrée des tanières pour que chaque chat qui passe "
                                                              "en dessous de la guirlande soit bénie par leur ancêtres."
                                                              " Le meneur doit porter autour de son cou un diamant "
                                                              "lorsqu'il se rend à l'assemblée des 4 Clans.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        truembed = discord.Embed(title="Traditions", color=0xF60086)
        truembed.set_thumbnail(url="https://i.ibb.co/hBmk3Zg/tradition.png")
        truembed.add_field(name="**Clan des ruisseaux**", value="Pour rendre hommage au Clan ancestral, "
                                                              "le Clan des ruisseaux fait des couronnes de roseaux "
                                                              "pour leurs ancêtres.\n"
                                                              "Chaque couronne est composer de 5 éléments:\n"
                                                              "- Principalement, du roseaux,\n"
                                                              "- Une tige de lierre,\n"
                                                              "- 3 fleurs bleues,\n"
                                                              "- 2 feuilles de lierres,\n"
                                                              "- 10 tige d'herbe.\n"
                                                              "Ces couronnes sont déposées devant l'entrée "
                                                              "des tanières sur des pierres plates."
                                                              "Pour se rendre a une assemblée, le meneur doit porté "
                                                              "autour de son cou un collier de roseaux.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        tbrembed = discord.Embed(title="Traditions", color=0xF60086)
        tbrembed.set_thumbnail(url="https://i.ibb.co/hBmk3Zg/tradition.png")
        tbrembed.add_field(name="**Clan des Brises**", value="En hommage à leurs ascendants, les chats du "
                                                             "Clan des brises font des tours d'oreilles composés:"
                                                             "- De blé (épis + tige),\n"
                                                             "- De bruyère,\n"
                                                             "- De pissenlit,\n"
                                                             "- De coquelicot,\n"
                                                             "- De marguerite.\n"
                                                             "Après avoir confectionné leur tour d'oreille, les membres"
                                                             " du Clan accroche leur tour d'oreille sur "
                                                             "les branches de l'arbre situé dans leur camp. "
                                                             "Le meneur du Clan des brises doit porter, "
                                                             "lors des assemblées, un collier de blé, "
                                                             "de bruyère et de coquelicot.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        tmoembed = discord.Embed(title="Traditions", color=0xF60086)
        tmoembed.set_thumbnail(url="https://i.ibb.co/hBmk3Zg/tradition.png")
        tmoembed.add_field(name="**Clan des Mousses**", value="Les félins du Clan des mousses rendent hommage "
                                                              "au Clan ancestral en confectionnant "
                                                              "des bracelets fait avec:\n"
                                                              "- De la mousse,\n"
                                                              "- Du lierre,\n"
                                                              "- De l'herbe,\n"
                                                              "-Des feuilles,\n"
                                                              "-Des fleurs.\n"
                                                              "Après avoir créés ces bracelets, "
                                                              "ils les déposent sur l'arbre de la tanière de leur chef."
                                                              "Le guide du Clan des mousses doit porté à son cou "
                                                              "un collier de lierre, d'herbe et de fleurs pour "
                                                              "se rendre au assemblées.")
        # --------------------------------------------------------------------------------------------------------------------------------------------
        dico = {"tro": troembed,
                "tru": truembed,
                "tbr": tbrembed,
                "tmo": tmoembed}
        choix = dico[clan]
        await ctx.send(embed=choix)
