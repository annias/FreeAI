from aigc.main import ask

while True:
  prompt = input("You: ")
  response = ask(prompt)
  print(f"GPT: {response}")
