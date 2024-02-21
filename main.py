import sys
from subprocess import check_output
from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from event_handle import Event_Handle

def main():
    """
    Main function that sets up the file monitoring and cleaning process based on the operating system.

    The function checks the operating system and sets the source and destination paths accordingly.
    It creates an event handler object and an observer object to monitor file events in the source path.
    The observer is started and runs indefinitely until interrupted by the user.
    During the monitoring process, any file events in the source path trigger the event handler to clean and move the files to the destination path.
    """

    if sys.platform == "darwin": 
        source_path = Path.home() / "Desktop"
        destination_path = Path.home() / "Desktop" / "pyCleanDesk"
        event_handler = Event_Handle(source_path, destination_path)
        observer = Observer()
        observer.schedule(event_handler, f"{source_path}", recursive=True)
        observer.start()

        try:
            while True:
                sleep(60)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    elif sys.platform.startswith("linux"): 
        # Need to recover the desktop name folder, XDG_USER_DIR might change users folder depending on the language
        desktop_path = Path(check_output(["xdg-user-dir", "DESKTOP"]).decode("utf-8").strip().split("/")[-1])
        source_path = Path.home() / desktop_path
        destination_path = Path.home() / desktop_path / "pyCleanDesk"
        event_handler = Event_Handle(source_path, destination_path)
        observer = Observer()
        observer.schedule(event_handler, f"{source_path}", recursive=True)
        observer.start()

        try:
            while True:
                sleep(60)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    elif sys.platform == "win32": 
        source_path = Path.home() / "Desktop"
        destination_path = Path.home() / "Desktop" / "pyCleanDesk"
        event_handler = Event_Handle(source_path, destination_path)
        observer = Observer()
        observer.schedule(event_handler, f"{source_path}", recursive=True)
        observer.start()

        try:
            while True:
                sleep(60)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    main()
