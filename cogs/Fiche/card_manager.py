import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option
from cogs.Fiche.database_handler_fiche import db_handler_fiche

db_handler = db_handler_fiche("./../../database.db")


def setup(bot):
    bot.add_cog(card(bot))


class card(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="enregistrer", guild_ids=[998628148616904894], description="Créé et enregistre une fiche",
                       options=[create_option(name="membre", description="nom du membre", option_type=6, required=True),
                                create_option(name="nom", description="Nom du chat", option_type=3, required=True),
                                create_option(name="lunes", description="Nombre de lunes", option_type=4, required=True),
                                create_option(name="grade", description="Grade du chat", option_type=3, required=True,
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
                                                       create_choice(name="Chaton", value="Chaton"),
                                                       create_choice(name="Solitaire", value="Solitaire"),
                                                       create_choice(name="Domestique", value="Domestique")]),
                                create_option(name="fourrure", description="Description de la fourrure", option_type=3, required=True),
                                create_option(name="yeux", description="Description des yeux", option_type=3, required=True),
                                create_option(name="carrure", description="Description de la carrure", option_type=3, required=True),
                                create_option(name="aime", description="Choses aimée(s)", option_type=3, required=True),
                                create_option(name="deteste", description="Choses détestée(s)", option_type=3, required=True),
                                create_option(name="qualite", description="Qualité(s) du chat", option_type=3, required=True),
                                create_option(name="defaut", description="Défaut(s) du chat", option_type=3, required=True),
                                create_option(name="image_credit", description="Image-Crédits de la fiche", option_type=3, required=True),
                                create_option(name="pere", description="Nom du père (Mention si membre)", option_type=3, required=False),
                                create_option(name="mere", description="Nom de la mère (Mention si membre)", option_type=3, required=False),
                                create_option(name="frere", description="Nom(s) du/des frère(s) (Mention(s) si membre(s)", option_type=3, required=False),
                                create_option(name="soeur", description="Nom(s) du/des soeur(s) (Mention(s) si membre(s)", option_type=3, required=False),
                                create_option(name="partenaire", description="Nom du partenaire (Mention si membre)", option_type=3, required=False),
                                create_option(name="chaton", description="Nom(s) du/des chaton(s) (Mention(s) si membre(s)", option_type=3, required=False),
                                create_option(name="histoire", description="Passer du chat", option_type=3, required=False),
                                create_option(name="clan", description="Nom du clan", option_type=3, required=False,
                                              choices=[create_choice(name="Mousses", value="Mousses"),
                                                       create_choice(name="Ruisseaux", value="Ruisseaux"),
                                                       create_choice(name="Brises", value="Brises"),
                                                       create_choice(name="Rochers", value="Rochers")])])
    async def enregister(self, ctx, membre, nom, lunes, grade, fourrure, yeux, carrure, aime,
                         deteste, qualite, defaut , image_credit, pere=None, mere=None, frere=None,
                         soeur=None, partenaire=None, chaton=None, histoire=None, clan=None):
        member_name = str(membre)
        member_id = int(membre.id)
        nbr_lunes = lunes
        soeurs = soeur
        chatons = chaton
        qualites = qualite
        defauts = defaut
        db_handler.create(member_name, member_id, nom, nbr_lunes, clan, grade,
                          pere, mere, frere, soeurs, partenaire, chatons,
                          fourrure, yeux, carrure, aime, deteste, qualites, defauts, histoire, image_credit)
        await ctx.send("Fiche enregistrée")
