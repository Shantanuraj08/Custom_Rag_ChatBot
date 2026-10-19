from custom_assistant.pipeline import ask , build_custom_agent


def main():
   
    print("Building the HR policy assistant...")
    agent = build_custom_agent()
    print("Assistant ready!\n")

    demo_questions = [
        "How many paid annual leave days do I get?",
        "What is the notice period during probation?",
        "Can I work from home every day?",
    ]

    for question in demo_questions:
        print("=" * 60)
        print("QUESTION:", question)
        print("-" * 60)
        answer = ask(agent, question)
        print("ANSWER:", answer)
        print("=" * 60)
        print()
        
       


if __name__ == "__main__":
 main()