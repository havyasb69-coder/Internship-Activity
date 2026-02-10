import tkinter as tk
import random

x = 20
y = 120
speed = 5
mode = "move"
target_x = 260
countdown_time = 0

def beep():
    root.bell()

def draw_scene():
    canvas.delete("all")

    # Robot
    canvas.create_rectangle(x, y, x+40, y+40, fill="gray")
    canvas.create_oval(x+5, y-15, x+15, y, fill="white")
    canvas.create_oval(x+25, y-15, x+35, y, fill="white")

    # Wall
    if mode == "wall":
        canvas.create_rectangle(200, 100, 240, 160, fill="brown")
        canvas.create_text(220, 170, text="Wall")

    # Person
    if mode == "person":
        canvas.create_oval(205, 80, 235, 110, fill="peachpuff")
        canvas.create_line(220, 110, 220, 150, width=3)
        canvas.create_line(220, 120, 200, 135, width=3)
        canvas.create_line(220, 120, 240, 135, width=3)
        canvas.create_line(220, 150, 200, 180, width=3)
        canvas.create_line(220, 150, 240, 180, width=3)
        canvas.create_text(220, 195, text="Person")

def auto_move():
    global x, mode

    if mode != "move":
        return

    event = random.choice(["none", "wall", "person"])

    # --- WALL COLLISION ---
    if event == "wall" and x > 120:
        mode = "wall"
        beep()
        status.set("Wall touched! Choose direction!")
        draw_scene()
        buttons.pack()
        return

    # --- PERSON COLLISION ---
    if event == "person" and x > 120:
        mode = "person"
        beep()
        status.set("Person ahead! Stopping...")
        draw_scene()
        start_countdown(5)
        return

    # Normal movement
    if x < target_x:
        x += speed
        status.set("Moving forward...")
        draw_scene()
        root.after(80, auto_move)
    else:
        status.set("Target reached!")

# --- User direction buttons ---

def avoid_up():
    global y, mode
    y -= 20
    if y < 40:
        y = 40
    continue_forward()

def avoid_down():
    global y, mode
    y += 20
    if y > 160:
        y = 160
    continue_forward()

def avoid_back():
    global x, mode
    x -= 30
    if x < 10:
        x = 10
    continue_forward()

def continue_forward():
    global mode
    buttons.pack_forget()
    mode = "move"
    status.set("Obstacle avoided → moving forward")
    draw_scene()
    root.after(200, auto_move)

# --- Person countdown ---

def start_countdown(sec):
    global countdown_time
    countdown_time = sec
    countdown()

def countdown():
    global countdown_time, mode

    if countdown_time > 0:
        status.set(f"Waiting {countdown_time}s")
        countdown_time -= 1
        root.after(1000, countdown)
    else:
        mode = "move"
        status.set("Path clear!")
        auto_move()

# --- UI ---

root = tk.Tk()
root.title("Robot Wall Avoidance Simulator")
root.geometry("400x320")

canvas = tk.Canvas(root, width=300, height=220, bg="lightblue")
canvas.pack()

status = tk.StringVar()
tk.Label(root, textvariable=status).pack()

tk.Button(root, text="Start", command=auto_move).pack(pady=5)

buttons = tk.Frame(root)
tk.Button(buttons, text="Up", command=avoid_up).pack(side="left")
tk.Button(buttons, text="Down", command=avoid_down).pack(side="left")
tk.Button(buttons, text="Back", command=avoid_back).pack(side="left")

draw_scene()
root.mainloop()
