import os

TASK_FILE = 'tasks.txt'
XP_FILE = 'xp.txt'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def load_xp():
    if not os.path.exists(XP_FILE):
        return 0
    with open(XP_FILE, 'r') as f:
        return int(f.read())

def save_xp(xp):
    with open(XP_FILE, 'w') as f:
        f.write(str(xp))

def add_task(tasks):
    task = input("📝 Enter your new quest: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Quest added: {task}")
    else:
        print("⚠️ Cannot add an empty quest.")

def view_tasks(tasks):
    if not tasks:
        print("🎉 No active quests. Time to relax!")
    else:
        print("\n📜 Active Quests:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task(tasks, xp):
    view_tasks(tasks)
    if not tasks:
        return xp
    try:
        idx = int(input("🎯 Choose quest number to complete: "))
        if 1 <= idx <= len(tasks):
            completed = tasks.pop(idx - 1)
            xp += 10  # Gain XP for completing a task
            save_tasks(tasks)
            save_xp(xp)
            print(f"🏆 Quest completed: {completed} (+10 XP)")
        else:
            print("⚠️ That quest doesn't exist.")
    except ValueError:
        print("⚠️ Enter a valid number.")
    return xp

def show_status(xp):
    print(f"\n💪 Current XP: {xp} {'⭐' * (xp // 50)}")

def main():
    tasks = load_tasks()
    xp = load_xp()

    while True:
        show_status(xp)
        print("\n=== TaskMaster Menu ===")
        print("1. View Quests")
        print("2. Add New Quest")
        print("3. Complete a Quest")
        print("4. Exit")

        choice = input("Choose your action (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            xp = remove_task(tasks, xp)
        elif choice == '4':
            print("👋 Until next time, adventurer!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == '__main__':
    main()
