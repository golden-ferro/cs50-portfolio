import customtkinter as ctk

# ======================================================
# =============== TIMER + TASK APPLICATION =============
# ======================================================

def create_app():
    """
    Creates the complete application, but does NOT run mainloop().

    """
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.title("Task Timer Manager")
    app.geometry("900x900")

    # ======================================================
    # ================ MAIN + BONUS TIMERS =================
    # ======================================================

    app.main_time_left = 0        # countdown for current task (seconds)
    app.main_running = False
    app.main_counting_down = False

    app.bonus_time = 0            # accumulated bonus time (seconds)
    app.bonus_running = False

    app.active_task = None        # tuple (task_frame, entry_name, entry_minutes)


    # ================= TIME FORMATTER =====================

    def format_time(s):
        h = s // 3600
        m = (s % 3600) // 60
        s = s % 60
        return f"{h:02d}:{m:02d}:{s:02d}"


    # Allow access in tests if needed
    app.format_time = format_time


    # ======================================================
    # ================= TOP TIMER BAR ======================
    # ======================================================

    top_frame = ctk.CTkFrame(app, fg_color="transparent")
    top_frame.pack(pady=20, fill="x")

    app.main_label = ctk.CTkLabel(
        top_frame,
        text="00:00:00",
        font=("Helvetica", 110),
        text_color="red"
    )
    app.main_label.pack(side="left", padx=40)

    app.bonus_label = ctk.CTkLabel(
        top_frame,
        text="Bonus: 00:00:00",
        font=("Helvetica", 40),
        text_color="green"
    )
    app.bonus_label.pack(side="right", padx=40)


    def update_bonus_label():
        app.bonus_label.configure(text=f"Bonus: {format_time(app.bonus_time)}")


    # ======================================================
    # =================== UPDATE TIMERS ====================
    # ======================================================

    def update_timers():

        # ---- MAIN TIMER ----
        if app.main_running:
            if app.main_counting_down and app.main_time_left > 0:
                app.main_time_left -= 1
                app.main_label.configure(text=format_time(app.main_time_left))

                if app.main_time_left == 0:
                    app.main_running = False
                    app.main_counting_down = False

                    if app.active_task is not None:
                        task_frame, _, _ = app.active_task
                        task_frame.configure(fg_color="#882222")
                        app.active_task = None

                    app.main_label.configure(text="00:00:00")

        # ---- BONUS TIMER ----
        if app.bonus_running:
            app.bonus_time -= 1
            update_bonus_label()

        app.after(1000, update_timers)

    update_timers()


    # ======================================================
    # ================= BUTTON CONTROLS ====================
    # ======================================================

    def start_main():
        app.main_running = True

    def pause_main():
        app.main_running = False

    def start_bonus():
        app.bonus_running = True

    def pause_bonus():
        app.bonus_running = False


    # ======================================================
    # ============= MAIN + BONUS BUTTONS AREA ==============
    # ======================================================

    buttons_area = ctk.CTkFrame(app)
    buttons_area.pack(pady=15)

    # ----------------- First Row -----------------
    row1 = ctk.CTkFrame(buttons_area)
    row1.pack(pady=5, fill="x")

    btn_start_main = ctk.CTkButton(
        row1, text="Start Main", width=120,
        fg_color="#2a4cb2", hover_color="#3f69ca",
        command=start_main
    )
    btn_start_main.pack(side="left", padx=40)

    btn_start_bonus = ctk.CTkButton(
        row1, text="Start Bonus", width=120,
        fg_color="#2a4cb2", hover_color="#3f69ca",
        command=start_bonus
    )
    btn_start_bonus.pack(side="right", padx=40)

    # ----------------- Second Row -----------------
    row2 = ctk.CTkFrame(buttons_area)
    row2.pack(pady=5, fill="x")

    btn_pause_main = ctk.CTkButton(
        row2, text="Pause Main", width=120,
        fg_color="#2a4cb2", hover_color="#3f69ca",
        command=pause_main
    )
    btn_pause_main.pack(side="left", padx=40)

    btn_pause_bonus = ctk.CTkButton(
        row2, text="Pause Bonus", width=120,
        fg_color="#2a4cb2", hover_color="#3f69ca",
        command=pause_bonus
    )
    btn_pause_bonus.pack(side="right", padx=40)


    # ======================================================
    # ===================== TASK SYSTEM ====================
    # ======================================================

    tasks_frame = ctk.CTkScrollableFrame(app, width=850, height=500)
    tasks_frame.pack(pady=20)

    app.tasks = []   # list of (task_frame, entry_name, entry_minutes)


    def remove_task(task_frame):
        for t in app.tasks:
            if t[0] == task_frame:
                app.tasks.remove(t)
                break
        task_frame.destroy()


    def complete_task(task_frame, entry_minutes):
        if app.active_task and app.active_task[0] == task_frame and app.main_counting_down:
            leftover = max(app.main_time_left, 0)

            if leftover > 0:
                app.bonus_time += leftover
                update_bonus_label()

            app.main_running = False
            app.main_counting_down = False
            app.main_time_left = 0
            app.main_label.configure(text="00:00:00")
            app.active_task = None

        task_frame.configure(fg_color="#224422")


    def start_task(entry_name, entry_minutes, task_frame):
        name = entry_name.get().strip()
        mins = entry_minutes.get().strip()

        if not mins.isdigit():
            print("ERROR: Minutes must be a number.")
            return

        seconds = int(mins) * 60

        app.active_task = (task_frame, entry_name, entry_minutes)

        app.main_time_left = seconds
        app.main_running = True
        app.main_counting_down = True

        app.main_label.configure(text=format_time(seconds))

        task_frame.configure(fg_color="#444422")


    def add_task():
        task_frame = ctk.CTkFrame(tasks_frame)
        task_frame.pack(fill="x", pady=5, padx=5)

        entry_name = ctk.CTkEntry(task_frame, placeholder_text="Task name...")
        entry_name.pack(side="left", fill="x", expand=True, padx=5)

        entry_minutes = ctk.CTkEntry(task_frame, placeholder_text="min", width=60)
        entry_minutes.pack(side="left", padx=5)

        start_btn = ctk.CTkButton(
            task_frame, text="Start", width=70,
            fg_color="#2a4cb2", hover_color="#3f69ca",
            command=lambda: start_task(entry_name, entry_minutes, task_frame)
        )
        start_btn.pack(side="left", padx=5)

        done_btn = ctk.CTkButton(
            task_frame, text="✓", width=40,
            fg_color="#33aa33", hover_color="#44cc44",
            command=lambda: complete_task(task_frame, entry_minutes)
        )
        done_btn.pack(side="left", padx=5)

        remove_btn = ctk.CTkButton(
            task_frame, text="X", width=40,
            fg_color="#aa3333", hover_color="#cc4444",
            command=lambda: remove_task(task_frame)
        )
        remove_btn.pack(side="right", padx=5)

        app.tasks.append((task_frame, entry_name, entry_minutes))


    ctk.CTkButton(
        app, text="Add Task", fg_color="#2a4cb2",
        hover_color="#3f69ca", command=add_task
    ).pack(pady=10)

    return app


# ======================================================
# ======================== MAIN ========================
# ======================================================

def main():
    app = create_app()
    app.mainloop()


if __name__ == "__main__":
    main()
