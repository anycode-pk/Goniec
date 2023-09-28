from discord.ext import commands
import settings

logger = settings.logging.getLogger("bot")

class CommandManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=['i'],
        help="Provide info about AnyCode organization",
        description="",
        brief="Info about AnyCode"
    )
    async def info(self, ctx):
        """Info about AnyCode"""
        logger.info("Executting command $info...")
        await ctx.send("We are student science club \'AnyCode\' at the Koszalin University of Technology")

    @commands.command(
        aliases=['his'],
        help="History of AnyCode",
        description="",
        brief="History of AnyCode"
    )
    async def history(self, ctx):
        """Provide history of AnyCode"""
        logger.info("Executting command $history...")
        await ctx.send("Our organization has a rich history...")

    @commands.command(
        aliases=['m'],
        help="Members of AnyCode",
        description="",
        brief="Members of AnyCode"
    )
    async def members(self, ctx):
        """Provide information about AnyCode members"""
        await ctx.send("Our organization is comprised of a diverse group of members...")

def setup(bot):
    bot.add_cog(CommandManager(bot))
