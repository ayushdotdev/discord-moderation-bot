# 🌟 Moderation Bot

A powerful, easy-to-use Discord moderation bot designed to help server admins manage their communities effectively. Built with Python and SQLite, Zaro tracks warnings, kicks, bans, and mutes per user across guilds, ensuring a structured and fair moderation system.

---

## ⚡ Features
- **Warn users**: Track warnings per user.  
- **Kick members**: Kick users while logging their actions in the database.  
- **Ban members**: Temporary or permanent bans.  
- **Mute users**: Restrict users from sending messages.  
- **Moderation stats**: View a user’s total warnings, kicks, bans, and mutes.  
- **Lazy database initialization**: Only tracks users who have been moderated.  
- **Embed notifications**: Clear and styled Discord messages for moderation actions.  

---

## 🛠 Setup & Installation

1. **Clone the repository**  
```bash
git clone https://github.com/ayushdotdev/discord-moderation-bot.git
cd zaro
```

2. **Install the requirements**
```bash
pip install -r requirements.txt
```

3. **Create a .env file in your root folder**
```
DISCORD_TOKEN =
```

4. **Run the bot**
```bash
python main.py
```
