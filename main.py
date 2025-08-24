from pathlib import Path
import shutil
from datetime import datetime
import logging
import json

# Log file for undo operations
log_file = "undo_log.json"


def log_move(source, destination):
    """Record a file move operation to JSON log (for undo)."""
    if Path(log_file).exists():
        with open(log_file, 'r') as f:
            try:
                history = json.load(f)
            except Exception as e:
                print(f"Error loading log file: {e}")
                history = []
    else:
        history = []

    history.append({"source": str(source), "destination": str(destination)})

    with open(log_file, 'w') as f:
        json.dump(history, f, indent=4)


def undo_moves():
    """Undo all moves recorded in JSON log."""
    if not Path(log_file).exists():
        print("No undo log found. Nothing to undo.")
        return

    with open(log_file, "r") as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            print("Undo log corrupted. Cannot undo.")
            return

    # Reverse order: undo the latest moves first
    for record in reversed(history):
        source = Path(record["source"])
        destination = Path(record["destination"])

        if destination.exists():
            try:
                shutil.move(str(destination), str(source))
                print(f"Restored {destination.name} → {source}")
            except Exception as e:
                print(f"Failed to restore {destination.name}: {e}")
        else:
            print(f"File {destination} missing. Skipping.")

    # Clear log after undo
    with open(log_file, "w") as f:
        json.dump([], f)
    print("Undo completed. Log cleared.")


# Setup logging for file operations
logging.basicConfig(
    filename="file_manager.log",
    filemode="a",
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)


# --- Sorting Functions ---

def sort_by_extension(folder_dir_path_obj: Path):
    """Sort files into subfolders based on file extension."""
    print("You chose to sort by extension")

    for components in folder_dir_path_obj.iterdir():
        if components.is_file():
            ext_name = components.suffix.lstrip(".") or "no_extension"
            target_folder = folder_dir_path_obj / "Organized_Files" / ext_name

            # Create folder if it doesn’t exist
            target_folder.mkdir(parents=True, exist_ok=True)
            logging.info(f"Folder created: {target_folder}")

            # Move file
            destination = target_folder / components.name
            try:
                shutil.move(str(components), str(destination))
                log_move(components, destination)
                logging.info(f"File {components.name} moved to {destination}")
            except Exception as e:
                logging.error(f"Failed to move {components.name} → {destination}\nError: {e}")


def sort_by_time(folder_dir_path_obj: Path):
    """Sort files into subfolders by year/month (based on last modified time)."""
    print("You chose to sort by Date & Time")

    for components in folder_dir_path_obj.iterdir():
        if components.is_file():
            file_name = components.name.strip()

            # Get last modified time
            file_meta_data = components.stat()
            last_modified = datetime.fromtimestamp(file_meta_data.st_mtime)

            # Build year/month hierarchy
            year_folder = last_modified.strftime("%Y")
            month_folder = last_modified.strftime("%m-%b")  # Ex: "08-Aug"

            target_folder = folder_dir_path_obj / "Organized_Files" / year_folder / month_folder

            target_folder.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created folder: {target_folder}")

            # Move file
            destination = target_folder / components.name
            try:
                shutil.move(str(components), str(destination))
                log_move(components, destination)
                logging.info(f"File {file_name} moved to {destination}")
            except Exception as e:
                logging.error(f"Unable to move {file_name} → {destination}\nError: {e}")


# --- Main Execution ---

if __name__ == "__main__":
    folder_dir = input("Please enter the folder to be cleaned: ")
    folder_dir_path_obj = Path(folder_dir)

    if folder_dir_path_obj.exists():
        print("✅ Folder Found!")

        sort_method = input(
            "Choose sorting method:\n"
            "  e ---> Sort by extension\n"
            "  t ---> Sort by time\n"
            "  u ---> Undo last operation\n"
            "Your choice: "
        ).lower()

        if sort_method == 'e':
            sort_by_extension(folder_dir_path_obj)
        elif sort_method == 't':
            sort_by_time(folder_dir_path_obj)
        elif sort_method == 'u':
            undo_moves()
        else:
            print("❌ Invalid input. Please try again.")

    else:
        print("❌ No such folder exists.")
        exit()
