🖥️ Shutdown Timer - Windows Utility
A simple GUI tool to schedule automatic shutdown of your Windows computer based on a countdown timer. Built with Python and Tkinter.

🔧 Features
⏱️ Schedule a shutdown after a custom number of minutes.

❌ Cancel a scheduled shutdown with a click.

🧠 Input validation for safety (only positive numbers allowed).

🪟 Lightweight and intuitive interface.

📦 How to Use
Open the application (run the ShutDownTimer.exe file).

In the field "Time on minutes", enter how many minutes until shutdown.

Click the "Shut Down" button.

A confirmation will appear.

Windows will shut down after the entered time.

To cancel the shutdown, click "Cancel Action" at any time.

⚠️ Notes
Only works on Windows systems.

The .exe must be run with appropriate permissions (admin recommended for shutdown commands).

If shutdown is scheduled and the PC is restarted manually, the timer will be cleared.

🛠️ Build it Yourself (Optional)
If you have Python installed and want to build the .exe:

Install pyinstaller

bash
Copy
Edit
pip install pyinstaller
Build the executable:

bash
Copy
Edit
pyinstaller --onefile --noconsole your_script.py
🧙 Author
Made by Ludwind Rotstein

FEEL FREE TO USE IT
