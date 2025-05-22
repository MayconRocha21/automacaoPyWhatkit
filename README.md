# PyWhatKit Automation Script

Script Python para automação de tarefas utilizando a biblioteca PyWhatKit, incluindo envio de mensagens WhatsApp, pesquisas, YouTube e mais.

## 📋 Pré-requisitos

- Python 3.6+
- Biblioteca PyWhatKit instalada:
  ```bash
  pip install pywhatkit
  ```

## 🚀 Funcionalidades

### 1. Envio de Mensagens WhatsApp
```python
# Mensagem agendada
kit.sendwhatmsg("+NUMERO", "Mensagem", hora, minuto)

# Mensagem instantânea  
kit.sendwhatmsg_instantly(
    phone_no="+NUMERO",
    message="Mensagem",
    tab_close=True,
    close_time=3,
    wait_time=10)
```

### 2. Pesquisa no Google
```python
kit.search("termo de busca")
```

### 3. Reprodução de Vídeos no YouTube
```python
kit.playonyt("termo de busca")
```

### 4. Conversão para Caligrafia
```python
kit.text_to_handwriting("Texto", save_to="arquivo.png")
```

### 5. Consulta na Wikipedia
```python
info = kit.info("termo", lines=3)
print(info)
```

## ⚠️ Considerações Importantes

- Para uso do WhatsApp, é necessário ter o WhatsApp Web aberto no navegador
- O número deve estar no formato internacional (+5511999999999)
- Algumas funções requerem conexão com a internet
- O tempo de espera (wait_time) deve ser suficiente para carregar a página

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
