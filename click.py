import time
from pynput import mouse, keyboard

# Настройки
CLICK_INTERVAL = 0.2
STOP_KEY = keyboard.Key.ctrl_r

running = True


def on_press(key):
    global running
    if key == STOP_KEY:
        running = False
        return False


def clicker():
    mouse_controller = mouse.Controller()

    with keyboard.Listener(on_press=on_press) as listener:
        while running:
            mouse_controller.click(mouse.Button.left)
            time.sleep(CLICK_INTERVAL)
        listener.join()


if __name__ == "__main__":
    print(f"Автокликер запущен. Нажимайте {STOP_KEY} для остановки.")
    clicker()
