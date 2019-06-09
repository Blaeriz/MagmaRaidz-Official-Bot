# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import time

# -*- coding: utf-8 -*-

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
    print("bot is ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="For commands with the prefix !"))

@client.event
async def on_message_delete(message):
    logChannel = message.guild.get_channel(586709281873854464)
    authorURL = message.author.avatar_url

    delMessage = discord.Embed(title = "**Deleted Message**", description = f"**Message by** : {message.author.mention}\n\n **Message** : {message.content}", color = 0xf901e0)
    delMessage.set_thumbnail(url = authorURL)

    await logChannel.send(embed = delMessage)

@client.event
async def on_member_join(member):
    guild = member.guild
    memberCount = guild.member_count
    welcomeChannel = guild.get_channel(586709257546891294)
    ruleChannel = guild.get_channel(586709264521756692)
    hohChannel = guild.get_channel(586709260205948929)
    kitChannel = guild.get_channel(586709261183221782)
    infoChannel = guild.get_channel(586709262458159118)
    channel = guild.get_channel(586709308985704448)
    await channel.edit(name = f"Members : {memberCount}")

    joinEmbed = discord.Embed(title = "**Welcome To MagmaRaidz**", description = f"**----------------------------------------------------------------** \n \n **[ Welcome to (Server) ]** \n Welcome! {member.mention} \n \n**[ Donations ]** \n If you are interested in donating, feel free to do so! \n **Paypal**: Blaeriz123@gmail.com \n \n **[ Remember ]** \n Do not tag any staff above Sr. Admin unless it is really important. Thank you for the cooperation. \n \n**----------------------------------------------------------------**", color = 0x02f90e, video = "https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif")
    joinEmbed.add_field(name = "Rules", value = f"{ruleChannel.mention}", inline = True)
    joinEmbed.add_field(name = "Hide Or Hunt", value = f"{hohChannel.mention}", inline = True)
    joinEmbed.add_field(name = "Kit", value = f"{kitChannel.mention}", inline = True)
    joinEmbed.add_field(name = "Information", value = f"{infoChannel.mention}", inline = True)
    joinEmbed.set_thumbnail(url = "https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif")

    await welcomeChannel.send(embed = joinEmbed)


    memberRole = guild.get_role(586709242988462103)
    defaultRole = guild.get_role(586709236986413067)
    await member.add_roles(memberRole, atomic = True)
    await member.add_roles(defaultRole, atomic = True)





@client.event
async def on_member_remove(member):
    guild = member.guild
    memberCount = guild.member_count
    welcomeChannel = guild.get_channel(586709257546891294)
    channel = guild.get_channel(586709308985704448)
    await channel.edit(name = f"Members : {memberCount}")

    leaveEmbed = discord.Embed(title = "**Member Left The Server**", description = f"**--------------------------------------------------** \n \n [ Goodbye ] \n User, {member.mention} has just left our server! \n \n **--------------------------------------------------**", video = "https://media.giphy.com/media/l2YWx2VxQ5iDlJI5i/giphy.gif", color = 0xf91601)
    leaveEmbed.set_thumbnail(url = "https://media.giphy.com/media/l2YWx2VxQ5iDlJI5i/giphy.gif")
    await welcomeChannel.send(embed = leaveEmbed)

@client.command()
async def clear(ctx, amount = 1):
    if ctx.author.guild_permissions.manage_messages == True:
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)

        clearEmbed = discord.Embed(title = "**Successfully Deleted Messages**", description = f"**Deleted By** : {ctx.author.mention} \n \n **No. Of Messages Deleted** : {amount}", color = 0xd200ea)
        await ctx.send(embed = clearEmbed, delete_after = 5)


    else:
        return




@client.command()
async def report(ctx, against : discord.Member, *, complaint = None):

    reportChannel = ctx.guild.get_channel(586709287318061056)
    thumbnail = against.avatar_url

    if complaint == None:
        incompEmbed = discord.Embed(title = "**Report Could Not Be Sent**", description = "Write a report first", color = 0x01f915)
        await ctx.send(embed = incompEmbed, delete_after = 5)
        await ctx.message.delete()

    else:
        confirmEmbed = discord.Embed(title = "**Report Sent**", description = "Your report will be reviewed soon.\n Make sure it is not a false report. \nIf it is, Contact staff immediately and inform them.", color = 0x01f915)
        await ctx.send(embed = confirmEmbed, delete_after = 5)
        await ctx.message.delete()

        reportEmbed = discord.Embed(title = "**Report**", description = f"**Reported By** : {ctx.author}\n **Reported Against** : {against.mention}\n **Issue**: {complaint}")
        reportEmbed.set_thumbnail(url = thumbnail)
        await reportChannel.send(embed = reportEmbed)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    if ctx.author.guild_permissions.kick_members == True:
        await member.kick(reason = reason)
        await ctx.message.delete()


        KickEmbed = discord.Embed(title = "**Player Has Been Kicked**",  description = f"\n **Kicked By** : {ctx.author.mention} \n\n  **Player Kicked : ** {member.mention}", color = 0xea7900)
        await ctx.send(embed = KickEmbed, delete_after = 5)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    if ctx.author.guild_permissions.ban_members == True:
        await member.ban(reason = reason)

        BanEmbed = discord.Embed(title = "**Player Has Been banned**",  description = f"**Banned By** : @{ctx.author.mention} \n \n **Member banned** : {member.mention}\n \n **Reason** : {reason}" , color = 0xdd0000)
        await ctx.send(embed = BanEmbed, delete_after = 5)



@client.command()
async def unban(ctx, *, member):
    if ctx.author.guild_permissions.administrator == True:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                unBanEmbed = discord.Embed(title = "**Player Has Been Unbanned**",  description = f"\n **Un Banned By** : {ctx.author} \n\n  **Player Unbanned : ** @{member_name}{member_discriminator}", color = 0x24dd00)
                await ctx.send(embed = unBanEmbed, delete_after = 5)

@client.command()
async def mute(ctx, user : discord.Member):
    if ctx.author.guild_permissions.kick_members == True:
        muteRole = ctx.guild.get_role(586709243357429771)
        await user.add_roles(muteRole, atomic = True)
        muteEmbed = discord.Embed(title = "**Player Muted**", description = f"**Muted By** : {ctx.author.mention}\n **Muted** : {user.mention}", color = 0xf91601)
        await ctx.send(embed = muteEmbed)

@client.command()
async def unmute(ctx, user : discord.Member):
    if ctx.author.guild_permissions.kick_members == True:
        muteRole = ctx.guild.get_role(586709243357429771)
        await user.remove_roles(muteRole, atomic = True)
        unMuteEmbed = discord.Embed(title = "**Player Un muted**", description = f"**Un muted By** : {ctx.author.mention}\n **Un Muted** : {user.mention}", color = 0x02f90e )
        await ctx.send(embed = unMuteEmbed)

@client.command()
async def nick(ctx,nick = None):
    if nick == None:
        incompEmbed = discord.Embed(title = "**Nickname Not found**", description = "**Usage** : !nick (name)", color = 0x01f915)
        await ctx.send(embed = incompEmbed)

    else:
        nickEmbed = discord.Embed(title = "**Nickname Changed**", description = f"**Nick name Successfully changed to {nick}**")
        await ctx.author.edit(reason = None, nick = nick)




@client.command()
async def Help(ctx):
    helpEmbed = discord.Embed(title = "**Commands**", description = "---**Commands For Members**---\n**Note:** ""!"" is the prefix.\n\n**1)** report\n**2)** nick\n**3)** Help\n\n---**Commands For Staff**---\n**1)** ban\n**2)** clear\n**3)** kick\n**4)** mute", color = 0x00d7db)
    await ctx.send(embed = helpEmbed)


client.run("NTc3MjIyOTI1MzIxNTAyNzQw.XPkofg.BWSggWSg_9SG7rPdFkfNAtaJYn4")
