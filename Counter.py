import json

TRIGGER = 4
PAYLOAD = "[=*v*=]"

def get_state():
    # Assumes: state = {"count": int}
    with open("state.json", "r", encoding="utf-8") as f:
        state = json.load(f)
        return state

def save_state(new_state):
    state = get_state()
    state.update(new_state)
    with open("state.json", "w", encoding="utf-8") as f:
        json.dump(state, f)

def count_to_trigger(count):
    if count == TRIGGER:
        print(PAYLOAD)
        count = 0
        return count
    elif count < TRIGGER:
        count += 1
        return count
    
def save_memory_on_turn():
    # This function was a test for implementation in another project
    state = get_state()
    turn = state.get("count", 0)
    print(turn)
    if turn == TRIGGER:
        save_state({"memory": "Test"})
        save_state({"count": 0})
    elif turn < TRIGGER:
        save_state({"count": turn+1})
        
if __name__ == "__main__":
    while True:
        input()
        count = get_state().get("count", 0)
        print(f"Starting count: {count}")
        count = count_to_trigger(count)
        save_state({"count": count})
        print(f"Ending count: {count}\n")
        # save_memory_on_turn()