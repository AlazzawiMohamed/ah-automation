import anthropic
import os

# قراءة الأوامر من prompt.txt
with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(message.content[0].text)

# حفظ النتائج
with open("audit-results.txt", "w", encoding="utf-8") as f:
    f.write(message.content[0].text)
