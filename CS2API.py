import logging
import offsets
import ctypes
import pymem
import time
from colorama import Fore, Style, init

init()

name = 'CS2API'
version = '1.0.65'
github = 'github.com/watakak/CS2API'

logging.basicConfig(filename=f'CS2API.log',
                    filemode='w',
                    format=f'%(asctime)s.%(msecs)03d | %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

def console_log(message, level="INFO", bold=False):
    colors = {
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED,
        None: Fore.RESET,
    }
    color = colors.get(level, Fore.WHITE)
    if bold:
        color = colors.get(level, Fore.WHITE) + Style.BRIGHT
    print(f"{color}{message}{Style.RESET_ALL}")

def log(message, level="INFO", bold=False):
    if level == 'INFO':
        logging.info(message)
    elif level == 'WARNING':
        logging.warning(message)
    elif level == 'ERROR':
        logging.error(message)
    elif level == 'CRITICAL':
        logging.critical(message)
    else:
        logging.info(message)
    console_log(message, level, bold=bold)

log(f'{name} {version} | {github}', None)

while True:
    try:
        pm = pymem.Pymem('cs2.exe')
        log('Counter-Strike 2 process found.', 'INFO')
        break
    except:
        try:
            log('Counter-Strike 2 is not opened. Waiting...', 'WARNING')
            time.sleep(2)
        except KeyboardInterrupt:
            log('Script stopped by user while waiting for the game.', 'CRITICAL', True)
            exit()

while True:
    try:
        client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        log('client.dll module loaded successfully.', 'INFO')
        break
    except:
        try:
            log('Counter-Strike 2 is opening. Loading...', 'WARNING')
            time.sleep(2)
        except KeyboardInterrupt:
            log('Script stopped by user while opening the game.', 'CRITICAL', True)
            exit()

def find_offset(variable, current_dict=None, base_offset_list=None):
    current_dict = current_dict or offsets.offsets
    base_offset_list = base_offset_list or []

    for key, value in current_dict.items():
        if isinstance(value, dict):
            found = find_offset(variable, value, base_offset_list + [value.get(key, 0)])
            if found:
                return found
        elif key == variable:
            return base_offset_list + [value]
    return None

def access_offset(variable):
    offsets_info = find_offset(variable)
    if offsets_info is None:
        log(f"Offset '{variable}' not found.", 'ERROR')
        return None

    base_address = client
    for offset in offsets_info[:-1]:
        base_address = pm.read_longlong(base_address + offset) if offset != 0 else base_address

    final_address = base_address + offsets_info[-1]
    return final_address

def read(variable, type=bool):
    try:
        address = access_offset(variable)
    except pymem.exception.MemoryReadError as error:
        log(f"Error while getting address for '{variable}': {error}", 'ERROR')

    read_methods = {
        int: pm.read_int,
        float: pm.read_float,
        bool: pm.read_bool,
        str: pm.read_string,
        'uint': pm.read_uint,
        'longlong': pm.read_longlong
    }

    try:
        result = read_methods[type](address)
        log(f"Value of '{variable}' is {result}", 'INFO')
        return result
    except pymem.exception.MemoryReadError as error:
        log(f"Error while reading '{variable}': {error}", 'ERROR')
        return None
    except UnboundLocalError:
        log(f"Warning while reading '{variable}', because its returns None", 'WARNING')
        return None

def write(variable, data, type=bool):
    try:
        address = access_offset(variable)
    except :
        log(f"Error while getting write address for '{variable}': {error}", 'ERROR')

    write_methods = {
        int: pm.write_int,
        float: pm.write_float,
        bool: pm.write_bool,
        str: pm.write_string,
        'uint': pm.write_uint,
        'longlong': pm.write_longlong
    }

    try:
        write_methods[type](address, data)
        log(f"Successfuly writed {data} for '{variable}'", 'INFO')
    except pymem.exception.MemoryWriteError as error:
        log(f"Error while writing to '{variable}': {error}", 'ERROR')

def key(key):
    if key == 'space':
        key = 0x20
    return ctypes.windll.user32.GetAsyncKeyState(key)

def do(variable, first_data=True, second_data=False, type=bool, interval=0.026):
    log(f"Executing 'do' function for '{variable}'", 'INFO')
    write(variable, first_data, type)
    time.sleep(interval)
    write(variable, second_data, type)
    time.sleep(interval)

def listen(callback, interval=0.0007):
    log('Listening for the events...', 'WARNING')
    try:
        while True:
            callback()
            time.sleep(interval)
    except KeyboardInterrupt:
        log('Listening were stopped by user.', 'CRITICAL', True)
        exit()
