import json
import os

SAVE_FILE = "progress.json"


DAYS = [
    "Day 1  - Number guessing game",
    "Day 2  - Dictionaries + scoreboard",
    "Day 3  - File reading and writing",
    "Day 4  - Functions deep dive",
    "Day 5  - Lists and loops",
    "Day 6  - Error handling",
    "Day 7  - Week 1 review project",
    "Day 8  - Ollama API basics",
    "Day 9  - Chat with Qwen in Python",
    "Day 10 - System prompts and personas",
    "Day 11 - Streaming responses",
    "Day 12 - Prompt engineering",
    "Day 13 - Build an AI summarizer",
    "Day 14 - Week 2 review project",
    "Day 15 - What are embeddings",
    "Day 16 - nomic-embed-text setup",
    "Day 17 - ChromaDB basics",
    "Day 18 - Semantic search",
    "Day 19 - Build a RAG pipeline",
    "Day 20 - Chat with your notes",
    "Day 21 - Week 3 review project",
    "Day 22 - JSON mode and structured output",
    "Day 23 - Function calling",
    "Day 24 - Pydantic validation",
    "Day 25 - Build a task extractor",
    "Day 26 - Agent loop concept",
    "Day 27 - Build a simple agent",
    "Day 28 - Week 4 review project",
    "Day 29 - FastAPI basics",
    "Day 30 - Build an AI web app",
    "Day 31 - Polish and push to GitHub",
]

def load():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {}

def save(progress):
    with open(SAVE_FILE, "w") as f:
        json.dump(progress, f)

def show(progress):
    os.system("clear")
    done = sum(1 for v in progress.values() if v)
    print("=" * 45)
    print(f"  Python + AI Roadmap — {done}/31 days done")
    filled = int((done /31) * 20)
    bar = "[" + "#" * filled + "-" * (20 - filled) + "]"
    print(f" {bar} {done}/31")
    print("=" * 45)
    for i, day in enumerate(DAYS):
        status = "x" if progress.get(str(i)) else " "
        print(f"  [{status}] {i+1:2}. {day}")
    print("=" * 45)
    print("  Type a day number to toggle it done")
    print("  Type 'q' to quit")
    print("=" * 45)

def main():
    progress = load()
    while True:
        show(progress)
        choice = input("\n  > ").strip().lower()
        if choice == "q":
            print("See you tomorrow.")
            break
        try:
            num = int(choice) - 1
            if 0 <= num < len(DAYS):
                key = str(num)
                progress[key] = not progress.get(key, False)
                save(progress)
            else:
                input("  Invalid number. Press Enter.")
        except ValueError:
            input("  Type a number or q. Press Enter.")

main()