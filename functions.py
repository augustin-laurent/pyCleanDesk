from datetime import datetime
from pathlib import Path
from shutil import move

def rename_duplicate_files(source_path: Path, destination_path: Path) -> Path:
    """
    Renames a file if a file with the same name already exists in the destination path.

    Args:
        source_path (Path): The path of the source file.
        destination_path (Path): The path of the destination directory.

    Returns:
        Path: The new path of the file after renaming.

    """
    if not destination_path.exists():
        return destination_path / source_path.name

    index = 1
    while True:
        new_file_name = f"{source_path.stem}_{index}{source_path.suffix}"
        new_file_path = destination_path / new_file_name
        if not new_file_path.exists():
            return new_file_path
        index += 1

def add_date_to_path(source_path: Path) -> Path:
    """
    Adds the current date to the path of the source file.

    Args:
        source_path (Path): The path of the source file.

    Returns:
        Path: The updated path with the current date added.
    """
    path_dated = source_path.parent / f"{datetime.now().strftime('%Y-%m-%d')}_{source_path.name}"
    path_dated.mkdir(parents=True, exist_ok=True)
    return path_dated

