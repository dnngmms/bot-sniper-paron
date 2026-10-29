import time, requests
import yfinance as yf

# --- GANTI 2 INI DOANG MET ---
BOT_TOKEN = "ISI_TOKEN_DARI_BOTFATHER"
MY_ID = "ISI_ID_DARI_USERINFOBOT"
# ------------------------------

def kirim(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": MY_ID, "text": msg, "parse_mode": "Markdown"})
    except: pass

kirim("🔔 *ALARM SNIPER PARON AKTIF*\n\nGue jagain XAUUSD buat lu met:\n- PDM 4028\n- LNDN 4032\n- ASIA 4042\n- Wick 4051/4056/4065\n\nKalo deket level, gue teriak di sini.")

last_alert = {}

def cek_harga():
    try:
        data = yf.Ticker("GC=F").history(period="1d", interval="1m")
        harga = float(data['Close'].iloc[-1])
        return harga
    except:
        return None

LEVELS = {
    4028.3: "🔥 *PDM 4028 DISAPU!* Kayak setup kemarin, siap-siap BUY 4031 SL 4027",
    4031.0: "🚀 *ENTRY 4031!* Setup RR 9.5 kemarin keulang! Cek BUY sekarang",
    4042.6: "⚠️ *ASIA LOW 4042 DISENTUH!* Hati-hati reversal",
    4051.0: "💰 *TP1 4051 KENA!* Amankan 50% dulu met!",
    4056.0: "💰💰 *TP2 4056 KENA!* Kayak SS lu kemarin!",
    4065.0: "🏆 *TP FINAL 4065!* Wick daily kesapu, FULL TP!"
}

while True:
    harga = cek_harga()
    if harga:
        print(f"Harga: {harga}")
        for level, pesan in LEVELS.items():
            # alarm kalo jarak < 1 dollar
            if abs(harga - level) < 1.0:
                if last_alert.get(level, 0) + 1800 < time.time(): # anti spam 30 menit
                    kirim(f"Harga sekarang *{harga}*\n\n{pesan}")
                    last_alert[level] = time.time()
    time.sleep(60) # cek tiap 1 menit
