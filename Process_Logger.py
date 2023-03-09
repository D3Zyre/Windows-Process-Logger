import psutil
import win32process
import win32gui
import time


def get_active_window_process() -> list:
    """
    returns [process_id, name_of_process, create_time(s)]
    for the process that is in focus by the user, or None
    """
    pid = None
    window = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(window)[1]
    if pid is not None:
        try:
            process = psutil.Process(pid)
            status = process.status()
            if status == "running":
                name = process.name()
                create_time = process.create_time()
                return [pid, name, create_time]
            else:
                return None
        except psutil.NoSuchProcess:
            pass
    else:
        return None


def get_active_processes() -> list:
    """
    gets all running processes and returns
    a list of lists, where each element is
    [process_id, name_of_process, create_time(s)]
    """
    # Get a list of process IDs
    pids = psutil.pids()
    output = list()

    # Print the list of process IDs
    for pid in pids:
        try:
            process = psutil.Process(pid)
            status = process.status()
            if status == "running":
                name = process.name()
                create_time = process.create_time()

                output.append([pid, name, create_time])
        except psutil.NoSuchProcess:
            pass
    
    return output


def append_to_log_file(file = "process_log.csv") -> None:
    pass


def main() -> None:
    print(get_active_processes())
    print(get_active_window_process())


if __name__ == "__main__":
    main()

