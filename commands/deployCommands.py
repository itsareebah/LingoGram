# import discord
# from discord.ext import commands
# from dotenv import load_dotenv
# import commands.commandsList as commandsList

# import os

# load_dotenv()

# async def deploy_commands():
#     commands = commandsList.commands_list()
#     token = os.getenv("DISCORD_BOT_TOKEN")
#     client_id = os.getenv("CLIENT_ID")
#     guild_id = os.getenv("GUILD_ID")
    
#     rest = discord.http.RouteBuilder(
#         discord.http.RouteType.APPLICATION_COMMAND,
#         "/applications/{application_id}/guilds/{guild_id}/commands",
#         application_id=client_id,
#         guild_id=guild_id
#     )
    
#     print(f"Starting to redeploy with commands: {commands}")

#     try:
#         print("Starting to redeploy")
#         async with discord.http.HTTPClient() as http:
#             data = await http.put(
#                 rest.build(),
#                 json=commands
#             )
#         print("Successfully redeployed")
#     except Exception as error:
#         print(f"Error during deployment: {error}")

# async def main():
#     await deploy_commands()
#     await client.close()

# client.run(os.getenv("DISCORD_BOT_TOKEN"))
