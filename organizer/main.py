import os
from organizer.mover import move_file

DOWNLOADS = os.path.expanduser("~/Downloads")

def run():
    for file_name in os.listdir(DOWNLOADS):
        file_path = os.path.join(DOWNLOADS, file_name)

        if os.path.isfile(file_path):
            result = move_file(file_path, DOWNLOADS)
            print(result)

if __name__ == "__main__":
    run()
