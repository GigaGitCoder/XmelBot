from g4f.client import Client as G4FClient
from colorama import Fore
import re

def AI_answer(text: str, prompt: str = '', request_theme: str = "", deb: str = "0", model: str = 'gpt-4o', limit: int = 3, timeout: int = 100) -> str | None:
    if deb == "1":
        def send_request():
            try:
                client = G4FClient()
                print(Fore.GREEN + f"Отправка запроса к модели {model}...")
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": f"{prompt}\n{text}"}]
                )
                return response.choices[0].message.content
            except Exception as e:
                print(Fore.RED + f"Ошибка при отправке запроса: {e}")
                return None

        print(Fore.CYAN + "\n" + "=" * 15 + f"{request_theme}" + "=" * 15)

        for attempt in range(15):
            response = send_request()
            if response:
                clear_text = re.sub(r"[A-Za-z0-9]", "", response)
                clear_text = re.sub(r'\s+', ' ', clear_text.strip())
                if len(clear_text) > limit:
                    print(Fore.GREEN + f"Ответ подходит, возвращаем результат.")
                    print(Fore.CYAN + "=" * 15 + "="*len(request_theme) + "=" * 15)
                    return response.strip()
            print(Fore.RED + f"Процесс прерван после {attempt+1} попытки.")
            print(Fore.CYAN + "=" * 15 + "="*len(request_theme) + "=" * 15 + "\n")

        return None
    


    else:
        def send_request():
            try:
                client = G4FClient()
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": f"{prompt}\n{text}"}]
                )
                return response.choices[0].message.content
            except Exception as e:
                return None

        for attempt in range(15):
            response = send_request()
            if response:
                clear_text = re.sub(r"[A-Za-z0-9]", "", response)
                clear_text = re.sub(r'\s+', ' ', clear_text.strip())
                if len(clear_text) > limit:
                    return response.strip()

        return None

def escape_formating(text):
    return text.replace('_', '\\_').replace('.', '\\.').replace(':', '\\:').replace('#', '\\#').replace('-', '\\-').replace('(', '\\(').replace(')', '\\)').replace('!', '\\!').replace('**', '*').replace('=', '\\=').replace('<', '\\<').replace('>', '\\>').replace('+', '\\+')
