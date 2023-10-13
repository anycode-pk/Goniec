import asyncio
from discord.ext import commands
import settings
import discord


logger = settings.logging.getLogger("bot")
PURPLE_COLOR = discord.Color.purple()


class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Tools commands"

    @commands.command(
    aliases=['f'],
    help="Encourages members to anonymously provide feedback or suggestions to help improve the organization's activities and services",
    description="Usage: $feedback\n\nEncourages members to anonymously provide feedback or suggestions to help improve the organization's activities and services",
    brief="Encourage members to anonymously provide feedback and suggestions."
    )
    async def feedback(self, ctx, *, feedback_message: str = None):
        """
        Usage: $feedback or $f

        Encourages members to anonymously provide feedback or suggestions to help improve the organization's activities and services.
        """
        if feedback_message:
            feedback_message = feedback_message.strip()
        else:
            await ctx.send("Provide feedback message like this: `$feedback 'Your feedback message'`")
            return
        for guild in self.bot.guilds:
            for text_channel in guild.text_channels:
                if text_channel.name.lower() == 'feedback':
                   feedback_channel = text_channel

        await ctx.message.delete()
        if feedback_channel:            
            await feedback_channel.send(f"Feedback from '{ctx.author.display_name}' user:\n\n{feedback_message}")
            

        await ctx.send("Thank you for your feedback! It has been forwarded to our team for review.")

    @commands.command(
    aliases=['sc'],
    help="Share code snippets with the community in nice embed style.",
    description="Usage: $sharecode or $sc\n\nShare your code snippets with the community. "
                "Provide the code snippet as the argument.",
    brief="Share code snippets."
    )
    async def sharecode(self, ctx, *, code_snippet: str = None):
        """
        Usage: $sharecode or $sc

        Share your code snippets with the community by providing the code snippet as the argument.

        Example:
        $sharecode This is my Python code:
        ```python
        print('Hello, world!')
        ```
        """
        embed = discord.Embed(
            title="Code Snippet Shared",
            description=f"Code snippet shared by {ctx.author.mention}:\n\n```{code_snippet}```",
            color=PURPLE_COLOR
        )

        if code_snippet:
            code_snippet = code_snippet
        else:
            await ctx.send("Missing parameter, use it like this: `$sc 'your code'`")
            return
        for guild in self.bot.guilds:
            for text_channel in guild.text_channels:
                if text_channel.name.lower() == 'code-snipets':
                   code_snippet_channel = text_channel

        if code_snippet_channel:
            await ctx.message.delete()
            logger.info("Code snippet shared successfully!")
            await ctx.send(embed=embed)
        else:
            logger.warn("Something went not yes...")
            await ctx.send("Something went not yes...")

    @commands.command(
    aliases=['nm'],
    help="Notify members about important news in nice discord embeded style.",
    description="Usage: $nm or $notify_members\n\nNotify members about important news in nice discord embeded style. "
                "Provide the code snippet as the argument.",
    brief="Notify members about important news in nice discord embeded style."
    )
    @commands.has_role("Admin")
    async def notify_members(self, ctx, *, important_message: str = None):
        """
        Send importnat message to a #chat in internal category.

        Parameters:
        - `message` (str): The content of the message to be sent.

        Usage:
        $send_message 'message'

        Example:
        $send_message '@Member Hello, everyone! This is an admin message.'

        Note:
        - This command can only be used by users with the 'Admin', 'Ceo' or 'Deputy of Ceo' role.
        """

        if important_message:
            important_message = important_message
        else: 
            logger.warn("Provide message as a parameter. Use command again...")
            return

        for guild in self.bot.guilds:
            for text_channel in guild.text_channels:
                if text_channel.name.lower() == 'chat':
                   chat_internal = text_channel

        embed = discord.Embed(
            title=f"Important Message by {ctx.message.author.display_name}!",
            description=important_message,
            color=PURPLE_COLOR
        )

        if chat_internal:
            await ctx.message.delete()
            await chat_internal.send(embed=embed)
            logger.info(f"important message send by {ctx.message.author.display_name} to chat '#chat' in internal category")
        else:
            logger.warn(f"'#chat' not found. Message not send.")

def setup(bot):
    bot.add_cog(Tools(bot))