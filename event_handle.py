from watchdog.events import FileSystemEventHandler
from pathlib import Path
from shutil import move
from dictionnary import path_based_on_extension
from functions import rename_duplicate_files, add_date_to_path

class Event_Handle(FileSystemEventHandler):
    def __init__(self, source_path: Path, destination_path: Path):
        """
        Initializes an instance of the Event_Handle class.

        Args:
            source_path (Path): The source directory path.
            destination_path (Path): The destination directory path.
        """
        self.absolute_source_path = source_path.resolve()
        self.absolute_destination_path = destination_path.resolve()

    @DeprecationWarning
    def on_modified(self, event):
        """
        Event handler method called when a file is modified in the source directory.

        Args:
            event: The event object representing the file modification event.
        """
        for file in self.absolute_source_path.iterdir():
            if file.is_file() and file.suffix[1:].lower() in path_based_on_extension.keys():
                destination = self.absolute_destination_path / path_based_on_extension[file.suffix[1:].lower()]
                destination = add_date_to_path(destination)
                destination = rename_duplicate_files(file, destination)
                move(file, destination)
                print(f"{file.name} moved to {destination}")