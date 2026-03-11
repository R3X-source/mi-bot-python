import discord
from discord.ext import commands
import os, random, asyncio, time
from flask import Flask
from threading import Thread

# --- SERVER PARA EVITAR QUE RAILWAY/RENDER SE DUERMA ---
app = Flask('')
@app.get('/')
def home(): return "🛡️ LEGION V36.2 PYTHON - FULL POWER 🛡️"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- CONFIGURACIÓN DE OBJETIVOS Y CANALES ---
OBJETIVOS = ["1457144912561832182", "1479748142722191514", "1479755930483691610", "1457984414121459856", "1447142638326120458"]
CANALES_AUTO = [1369174476574687243, 1369174478596345897, 1379141308131835914, 1369174479825145856, 1369180836582133820, 1369181058490175488]
CANALES_LIBRES = [1240012616328544419, 1266542890767876229, 1270239207071420450, 1239719951435304960]

def generar_bypass():
    syms = "ΓΔΘΛΞΠΣΦΨΩ"
    emos = ["🤣🤣", "🫵🫵", "😈😈😈", "💀", "🔥"]
    hex_val = hex(random.getrandbits(24))[2:].upper()
    return f"{random.choice(emos)} \n\u200b [{random.choice(syms)}-{hex_val}] #{str(time.time())[-4:]}"

# --- LISTA DE MENSAJES LARGOS (COPIA EXACTA) ---
MSJ_LARGO = ".t cputiñapack \n<@1425209744603218020> <@1195495311045558272> <@1369070242684473485> <@984956970014486528> <@1072352198836621385> CULOMBIANO ARGENCHANGAS <@1435003733393281055> <@1400251089361567885> <@1429177016703516764> DANIELA <@1438314463970328578> <@1384045898958508085> <@1446586105553227807> <@1452154841676775567> <@957014429822750771> <@1423439348430405722> <@1455444386421674007> <@765971830442819674> <@1394021604127936772> @everyone spam MAMITAS <@1452533908699611236> <@1438662990021922869> <@1459077041637953651> <@1468117706099396816> <@1467397075204309034> <@1466878653932634195> <@1458314974794616902> <@1403986874153832550> <@1470913175401533543> <@1464354934785839155> <@1394023020896714762> <@1399500980889976902> <@1470230646529069086> <@1462897561894649876> @everyone DANIELA <@1386330375952793723> <@1399500980889976902> <@1466878653932634195> \nhttps://files.catbox.moe/d0wcx2.mp4"

def obtener_msj_corto(t):
    msgs = [
        f".t cputiñagachatuber <@{t}> \nQUIERES PENE SHAM4? NALGARERA GAMAMITA PUTA DE FRANKITA BY NEG4 SHE",
        f".t cejotiñaandgamami <@{t}> \nbrazos más lonjudos mejichanga nalga moncloveña soy tu masho",
        f".t cejotiñagolpeada <@{t}> \nMALDITA Q QUIERE EDITAR SUS NALG4S DESDE GROK CUANDO SU BRAZO LONJUDO ANDA FILTRADO POR LA MALDITA DE ERRE ELA EN IG Y HAY CAPS Q TENGO YO Q SON IRREFUTABLES DE ESTO🤣🤣🤣 DILE MACHA A DANIELA PUT4 IDIOTA JAJAJA",
        f".t cjotorra <@{t}> \nmamele más mejichanga q a simias como a tu las deben de llevar al matadero por mejicanas güey",
        f".t lorda <@{t}> \ny mientras tanto cjotorra viendo todo con su cara de india mejicana...",
        f".t frijolera <@{t}> \nFRIJOLERA DILE DOMADORA A TU M4CH4 Q TE TIENE DE PUTITA...",
        f".t joan <@{t}> \nmach4 g4m4mita diría la putita marrona...",
        f".t chichuda <@{t}> \nvengan mejichangas denle tet4 a su machete jsjajaja",
        f".t cjotangaandgamami <@{t}> \nCEJOTORRA Y GAMAMITA SON TAXISTAS Y ENCIMA TIENEN 20-18 AÑOS...",
        f".t cejuda2 <@{t}> \nPINCHE PERRA CJOTIÑA SOS UN KAGU3 DE RISA SHE NI QUIEN TE TOME ENSERIÓ PENDEJITA SI DESDE Q ESTAS TRAICIONADA TODOS TE HAN VENIDO TOMANDO LA COLA PARA TRAICIONARTE Y OLERTE EL PEDORRO CHE, SI HASTA AJENAS A LA CJ TE QUIEREN OLER EL QLO, HASTA LA MULTICUENTRA TRAVESTI DE HADESA Q ES REDBLACKA TE JODE LAS NALGAS🤣🤣🤣, YA NI HABLAR Q LESBERY TE ARDIÓ EL CULETE POR MICHOACANA",
        f".t nito <@{t}> \nPERRA TIENES Q ENTENDER Q SOS MEXINDIA DE MICHOACAN Y DE VERACRUZ Y ESO NADIE TE LO VA A QUITAR PUT4 ESTUPIDH4 Q SE TRAGA MI NITO JDKDJJSJSKSLDKS Y SE FUE TRAICIONADA HASTA POR PABLA",
        f".t india <@{t}> \nLA MEJINDIA DE VERACRUZ TRAICIONADA POR PABLA OTRA VEZ JDKDJJSJS",
        f".t insana <@{t}> \nTE ARDIÓ LAS NALGAS INSANA LA MISMA ARJENCHANGA Q FILTRO A LORDA y CEJOTIÑA JAJAJA, MIRA CEJOTIÑA Q DECIR DE TI LA VERDAD, SI NADIE SE TOMA ENSERIÓ TUS NALGORRAS ES PORQUE CUALQUIERA TE TIENE DE PERRA CHE, RECUERDO Q HASTA UNA PROSTITUTA TE CALLO LAS NALGAS Y ASI TE QUIERES PONER DELANTE DE TUS MACHOS MAYORES (TIPO WARSZLA) Q CLARAMENTE TE PARAN ABUSANDO, NI Q DECIR Q ERES LA MAMÁ DEL MANJUNTER/JS/SPIDERMAN TE DESPLOMA EL CULO🤣🤣🤣🤣🤣🤣, NO PERRA TU SI ESTAS BIEN JODIDA CHE, TENES 20 AÑOS, ESTAS DESEMPLEADA, SE PUEDE DECIR Q ERES UN PEDON BISEXUAL Y TRAVESTI Q LE ENCANTA FINGIR SER MUJER Y SE ENAMORO DE GD Y FUE LLENADA DE MECOS DE LA WARSZLIZA Y Q LE LLEVA CASI 6 AÑOS A MANHUTER PERRA PEDOFILA!!! MALDIT4 PEDOFILA CHE, ESTAS BIEN JODID4 Y ACABADA CJOTORRONGA 🤣🤣🤣🤣"
    ]
    return random.choice(msgs)

# --- CLASE DEL BOT ---
class LegionBot(commands.Bot):
    def __init__(self, token):
        super().__init__(command_prefix="!", self_bot=True, check_update=False)
        self.token = token

    async def on_ready(self):
        print(f'✅ [PYTHON UNIT] Conectado: {self.user.name}')
        while True:
            if random.random() < 0.75:
                canal_id = random.choice(CANALES_AUTO + CANALES_LIBRES)
                target = random.choice(OBJETIVOS)
                channel = self.get_channel(canal_id)
                
                if channel:
                    try:
                        async with channel.typing():
                            # Simulación de escritura humana
                            await asyncio.sleep(random.uniform(2.0, 4.5))
                            
                            msj = obtener_msj_corto(target) if canal_id in CANALES_AUTO else MSJ_LARGO
                            await channel.send(f"{msj} {generar_bypass()}")
                            print(f"🔥 {self.user.name} atacó {channel.name}")
                    except Exception as e:
                        print(f"❌ Error en {self.user.name}: {e}")
            
            # Pausa Gaussiana (8-12 seg promedio)
            await asyncio.sleep(max(6, random.gauss(10, 3)))

# --- LANZADOR ---
async def start_all():
    Thread(target=run, daemon=True).start()
    # Busca tokens del 1 al 4 en las variables de entorno
    tokens = [os.getenv(f'TOKEN_{i}') for i in range(1, 5) if os.getenv(f'TOKEN_{i}')]
    if not tokens:
        print("❌ No se encontraron TOKENS en las variables de entorno.")
        return
    
    bots = [LegionBot(t) for t in tokens]
    await asyncio.gather(*[bot.start(bot.token) for bot in bots])

if __name__ == "__main__":
    try:
        asyncio.run(start_all())
    except KeyboardInterrupt:
        pass
