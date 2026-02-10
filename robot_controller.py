import tkinter as tk

x = 20
y = 120
speed = 5
game_over = False

# --- BUZZER ---

def buzzer(times=5):
    if times > 0:
        root.bell()
        root.after(150, lambda: buzzer(times-1))

# --- COLLISION FUNCTIONS ---

def hit_wall(nx, ny):
    return (
        nx+40 > 200 and nx < 240 and
        ny+40 > 100 and ny < 160
    )

def hit_door(nx):
    return nx+40 >= 260

def hit_person(nx, ny):
    # person area
    return (
        nx+40 > 150 and nx < 190 and
        ny+40 > 60 and ny < 120
    )

# --- DRAW ---

def draw_scene():
    canvas.delete("all")

    # Robot
    canvas.create_rectangle(x, y, x+40, y+40, fill="gray")

    # Person
    canvas.create_oval(150, 60, 190, 120, fill="peachpuff")
    canvas.create_text(170, 130, text="Person")

    # Wall
    canvas.create_rectangle(200, 100, 240, 160, fill="brown")
    canvas.create_text(220, 170, text="Wall")

    # Door
    canvas.create_rectangle(260, 100, 295, 170, fill="darkred")
    canvas.create_text(278, 180, text="Door")

# --- AUTO MOVE ---

def auto_move():
    global x, game_over

    if game_over:
        return

    nx = x + speed

    if hit_person(nx, y):
        game_over = True
        status.set("Hit person! GAME OVER")
        buzzer()
        draw_scene()
        return

    if hit_door(nx):
        game_over = True
        status.set("Door reached! GAME OVER")
        buzzer()
        draw_scene()
        return

    if hit_wall(nx, y):
        status.set("Wall ahead! Choose direction")
        buzzer(2)
        draw_scene()
        return

    x = nx
    status.set("Moving...")
    draw_scene()
    root.after(80, auto_move)

# --- BUTTON MOVES ---

def avoid_up():
    global y
    ny = max(0, y-30)
    if not hit_wall(x, ny):
        y = ny
    draw_scene()

def avoid_down():
    global y
    ny = min(180, y+30)
    if not hit_wall(x, ny):
        y = ny
    draw_scene()

def avoid_back():
    global x
    nx = max(10, x-40)
    if not hit_wall(nx, y):
        x = nx
    draw_scene()

# --- UI ---

root = tk.Tk()
root.title("Robot Simulator")
root.geometry("400x320")

canvas = tk.Canvas(root, width=300, height=220, bg="lightblue")
canvas.pack()

status = tk.StringVar()
tk.Label(root, textvariable=status).pack()

tk.Button(root, text="Start", command=auto_move).pack(pady=5)

buttons = tk.Frame(root)
buttons.pack()
tk.Button(buttons, text="Up", command=avoid_up).pack(side="left")
tk.Button(buttons, text="Down", command=avoid_down).pack(side="left")
tk.Button(buttons, text="Back", command=avoid_back).pack(side="left")

draw_scene()
root.mainloop()
