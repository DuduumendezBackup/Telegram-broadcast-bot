import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import time

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your bot token
BOT_TOKEN = "7339742375:AAHq490Hnpe6EqSCNWgdPcp7wNxJcRBb7gU"

# Replace with your group/channel ID (e.g., @channelusername or -1001234567890 for groups)
CHAT_ID = "@duduu_mendez_bots_store"

# Define multiple messages
MESSAGES = [
    {
        "text": (
            "🚀 *Good Morning!* 🌞\n\n"
            "Start your day by joining our community:\n\n"
            "👉 Join our **Telegram Channel** for daily updates.\n"
            "👉 Subscribe to our **YouTube Channel** for awesome videos.\n"
            "👉 Join our **WhatsApp Group** for real-time discussions.\n\n"
            "Click the buttons below to join now!"
        ),
        "buttons": [
            [
                InlineKeyboardButton("Join Our Telegram Channel", url="https://t.me/duduu_mendez_store")
            ],
            [
                InlineKeyboardButton("Subscribe Our YouTube Channel", url="https://youtube.com/@duduu_mendez?si=U2J-NcS4ho25wpyY")
            ],
            [
                InlineKeyboardButton("Join Our WhatsApp Group", url="https://whatsapp.com/channel/0029VacgCaPKmCPGmTmrnT04")
            ]
        ],
        "time": time(hour=9, minute=0)  # 9:00 AM
    },
    {
        "text": (
            "🚀 *HOW TO DEPLOY 𝐌𝐄𝐍𝐃𝐄𝐙 V4.1 BUG BOT USING PANEL* 🚀\n\n"
            "Video link:\n"
            "https://youtu.be/tKhJctST6Wc?si=9M7C84kdrfYHDcM6\n\n"
            "Bot link:\n"
            "https://t.me/duduu_mendez_store/178\n\n"
            "Panel link:\n"
            "https://dashboard.katabump.com/auth/login#440069\n\n"
            "Replit App:\n"
            "https://play.google.com/store/apps/details?id=com.replit.app\n\n"
            "Get Creds.json (link with WhatsApp):\n"
            "https://replit.com/@nicksoniaudax5/MENDEZ-4-Pairing?s=app\n\n"
            "NB:\n"
            "IF LINK OF GETTING CREDS.JSON FAILED USE VPN especially TANZANIANS 🇹🇿\n\n"
            "ENJOY BUGING FOR 😁 😂\n\n"
            "#Duduumendez\n"
            "#Duduu_mendez\n"
            "#Duduu_mendez_backup\n\n"
            "`MENDEZ💀💀›`"
        ),
        "buttons": [],
        "time": time(hour=12, minute=0)  # 12:00 PM
    },
    {
        "text": (
            "🐞 *BUG BOT* 🐞\n\n"
            "Nini maana ya Bug Bot?\n"
            "Hizi bot za WhatsApp ambazo zina features za kipekee sana tofauti na bot nyingine, hii bot ina view status kama bot nyingine, Hii bot ina uwezo wa kuhack mtu na inazalisha virus kitu ambacho BOT nyingine hazina.\n\n"
            "Hii feature ya kuwa na uwezo wa kuhack mtu au group la WhatsApp kwa mda mfupi, ndo inazifanya BUG BOT ziwe za kipekee sana.\n\n"
            "BUG BOT zina kitu kinaitwa bugs, hizi ni kama virus ambazo ukimtumia mtu au ukatuma kwenye group zitatafuna hilo group na kupelekea kuliharibu hilo group. Kama umemtumia mtu, zitatafuna simu yake na kupelekea kiharib simu yake na kumfanya mtu asiwahi kutumia tena WhatsApp mpaka adownload upya WhatsApp.\n\n"
            "BUG BOT ZINAZOTOLEWA NA DUDUU_MENDEZ COMMUNITY:\n"
            "1. MENDEZ-𝐕4\n"
            "Angalia namna ya kutengeneza GUSA HAPA MENDEZ-𝐕4\n\n"
            "2. Shoyu+V1\n"
            "Angalia namna ya kutengeneza GUSA HAPA Shoyu+V1\n\n"
            "KAMA UNATAKA TUKUTENGENEZEE BOT, unaweza kuja na kununua BOT kwetu. Wasiliana nasi kupitia @DUDUU_MENDEZ_BOT.\n\n"
            "#Duduumendez\n"
            "#Duduu_mendez\n"
            "#Duduu_mendez_backup\n"
            "#Dml_Tech"
        ),
        "buttons": [],
        "time": time(hour=15, minute=0)  # 3:00 PM
    },
    {
        "text": (
            "📱 *HUDUMA YA WHATSAPP BOT KUTOKA DUDUU_MENDEZ COMMUNITY* 📱\n\n"
            "**NORMAL WHATSAPP BOT**\n"
            "Bei == 3000/=\n"
            "Mda mwezi mmoja na wiki 2\n\n"
            "**MENDEZ-𝐕4 BUG**\n"
            "Hii inafanya kazi kama hizo normal bot ila ina nyongeza ya commands za bugs. Hii unaweza kuitumia kuhack WhatsApp account na group.\n\n"
            "Bei == 5000/=\n"
            "Mda miezi 2\n\n"
            "**BUG VIA TELEGRAM**\n"
            "Hii ndo bot yenyewe, kazi yake ni moja ni kutuma bugs (kuhack account ya mlengwa wako). Hii kwenye suala la kuhack ina nguvu kubwa sana. Ukimhack mtu, hataweza kutumia WhatsApp kamwe mpaka afute data zake na aanze upya. Hii ni kwa matapeli na maadui.\n\n"
            "**Premium Service**\n"
            "1 week == 2000/=\n"
            "1 month == 4000/=\n"
            "1 day == 500/=\n"
            "Unlimited == 10,000/=\n\n"
            "KUPATA MAELEZO ZAIDI YA BOT, TEMBELEA HII WEBSITE:\n"
            "https://mendez-website.vercel.app/botDeployment.html\n\n"
            "Wasiliana nasi kama unataka huduma @DUDUU_MENDEZ_BOT\n\n"
            "Hii ni kwa wale ambao wamesha deploy bot ya MENDEZ-𝐕4 ila hawana access ya kutuma bugs. Cha kufanya, andika hii command kwenye WhatsApp:\n"
            "`.owner`\n"
            "Kisha text hio namba inayokuja hapo ili upate huduma.\n\n"
            "#Duduu_mendez\n"
            "#Dml_Tech"
        ),
        "buttons": [],
        "time": time(hour=18, minute=0)  # 6:00 PM
    }
]

# Function to send a custom message with buttons
async def send_custom_message(chat_id, context, message_data):
    keyboard = message_data["buttons"]
    reply_markup = InlineKeyboardMarkup(keyboard) if keyboard else None
    await context.bot.send_message(
        chat_id=chat_id,
        text=message_data["text"],
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running! Use /broadcast to send a test message.")

# Command to manually trigger a broadcast
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await send_custom_message(CHAT_ID, context, MESSAGES[0])  # Send the first message as a test
        await update.message.reply_text("Broadcast message sent successfully!")
    except Exception as e:
        logger.error(f"Error broadcasting message: {e}")
        await update.message.reply_text("Failed to send broadcast message.")

# Scheduled broadcast function
async def scheduled_broadcast(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    message_data = job.data
    try:
        await send_custom_message(CHAT_ID, context, message_data)
        logger.info(f"Scheduled message sent: {message_data['text']}")
    except Exception as e:
        logger.error(f"Error in scheduled broadcast: {e}")

def main():
    # Create the Application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("broadcast", broadcast))

    # Schedule multiple messages
    job_queue = application.job_queue
    for message in MESSAGES:
        job_queue.run_daily(
            scheduled_broadcast,
            time=message["time"],
            data=message  # Pass the message data to the job
        )

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()