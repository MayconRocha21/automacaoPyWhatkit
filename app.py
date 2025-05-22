# Usando PyWhatKit com Python

import pywhatkit as kit

# 1. Enviar mensagem no WhatsApp Agendada
kit.sendwhatmsg("+", "Olá, tudo bem?", 19, 51)

# 2. Enviar mensagem instantânea
kit.sendwhatmsg_instantly(
    phone_no="+5511999999999",
    message="Olá, tudo bem?",
    tab_close=True,
    close_time=3,
    wait_time=10)

# 3. Pesquisar no Google
kit.search("Python PyWhatKit")

# 4. Tocar vídeos no YouTube
kit.playonyt("Python tutorial")

# 5. Converter texto em caligrafia
kit.text_to_handwriting("Texto para converter em caligrafia", save_to="caligrafia.png")

# 6. Obter informações da Wikipedia
info = kit.info("Python", lines=3)
print(info)
