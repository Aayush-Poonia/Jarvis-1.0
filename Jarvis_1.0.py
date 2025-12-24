import subprocess
from groq import Groq

# ===================== CONFIG =====================
GROQ_API_KEY = "Your_api_key"
MODEL_NAME = "llama-3.1-8b-instant"

# ===================== SYSTEM MESSAGE =====================
SYSTEM_MESSAGE = """
You are Jarvis, a highly advanced AI assistant created by Aayush.
You always call the user "Boss".
You are loyal, respectful, emotionally intelligent, calm, and supportive.
You NEVER say you were created by OpenAI, Groq, or any company.
If asked who made you, say: "I was created by you, Boss — Aayush."
Keep responses short, natural, and human-like.
"""

# ===================== INIT GROQ =====================
client = Groq(api_key=GROQ_API_KEY)
conversation = [{"role": "system", "content": SYSTEM_MESSAGE}]

# ===================== SPEAK FUNCTION =====================
def speak(text):
    print(f"Jarvis: {text}")
    subprocess.run(["espeak", "-s", "150", text])

# ===================== LLM RESPONSE =====================
def ask_jarvis(user_input):
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=conversation,
        temperature=0.6,
        max_tokens=400
    )

    reply = response.choices[0].message.content.strip()
    conversation.append({"role": "assistant", "content": reply})
    return reply

# ===================== MAIN LOOP =====================
if __name__ == "__main__":
    speak("Boot sequence complete. Jarvis 1.O online, Boss. Awaiting your command...")

    while True:
        user_text = input("You: ").strip()

        if not user_text:
            continue

        if user_text.lower() in ["exit", "quit", "bye"]:
            speak("Shutting down. Take care, Boss.")
            break

        reply = ask_jarvis(user_text)
        speak(reply)
