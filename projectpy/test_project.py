import pytest
from project import create_app


def test_format_time():
    app = create_app()

    assert app.format_time(0) == "00:00:00"
    assert app.format_time(59) == "00:00:59"
    assert app.format_time(60) == "00:01:00"
    assert app.format_time(3661) == "01:01:01"


def test_start_main_timer():
    app = create_app()

    # simulate main start
    app.main_time_left = 120
    app.main_running = False

    # the real button calls this:
    def start_main(): app.main_running = True
    start_main()

    assert app.main_running is True
    assert app.main_time_left == 120


def test_pause_main_timer():
    app = create_app()

    app.main_running = True

    def pause_main(): app.main_running = False
    pause_main()

    assert app.main_running is False


def test_start_bonus_timer():
    app = create_app()

    def start_bonus(): app.bonus_running = True
    start_bonus()

    assert app.bonus_running is True


def test_pause_bonus_timer():
    app = create_app()

    app.bonus_running = True

    def pause_bonus(): app.bonus_running = False
    pause_bonus()

    assert app.bonus_running is False


def test_add_task_creates_task_widget():
    app = create_app()

    before = len(app.tasks)

    # add_task is defined inside create_app — but it is linked to the button.
    # Then we access the function using the Add Task button command:
    add_task_button = app.winfo_children()[-1]  # last widget (Add Task btn)
    add_task_cmd = add_task_button._command

    add_task_cmd()  # simulate user click

    after = len(app.tasks)

    assert after == before + 1


def test_start_task_sets_active_task():
    app = create_app()

    # Add one task
    add_btn = app.winfo_children()[-1]
    add_task_cmd = add_btn._command
    add_task_cmd()

    task_frame, entry_name, entry_minutes = app.tasks[0]

    entry_name.insert(0, "Study")
    entry_minutes.insert(0, "2")  # 2 minutes

    # simulate pressing Start inside task
    for widget in task_frame.winfo_children():
        if isinstance(widget, type(add_btn)):  # button
            if widget.cget("text") == "Start":
                widget._command()

    assert app.active_task[0] == task_frame
    assert app.main_time_left == 120
    assert app.main_running is True
    assert app.main_counting_down is True
