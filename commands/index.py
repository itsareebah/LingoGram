# import discord
# from discord.ext import commands
# from dotenv import load_dotenv
# import linguaCommand

# load_dotenv()

# intents = discord.Intents(guilds=True)
# client = commands.Bot(command_prefix="!", intents=intents)

# @client.event
# async def on_ready():
#     print(f"Ready! Logged in as {client.user}")

# @client.event
# async def on_interaction(interaction):
#     if not isinstance(interaction, discord.Interaction):
#         return
    
#     if not interaction.is_command():
#         return
    
#     if interaction.data["name"] != "lingua":
#         print("Unknown command")
#         return

#     try:
#         await linguaCommand.execute(interaction)
#     except Exception as error:
#         print(error)
#         if interaction.response.is_done():
#             await interaction.response.send_message("There was an error while executing this command!", ephemeral=True)
#         else:
#             await interaction.response.send_message("There was an error while executing this command!", ephemeral=True)

# client.run(os.getenv("DISCORD_BOT_TOKEN"))
