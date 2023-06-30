import psutil
import time
import os
import colorama
from colorama import init, Fore, Style

colorama.init(autoreset=True)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_network_usage():
    net = psutil.net_io_counters()
    return net.bytes_sent, net.bytes_recv

def format_size(bytes):
    # Convert bytes to a human-readable format
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while bytes >= 1024 and index < len(suffixes) - 1:
        bytes /= 1024
        index += 1
    return f"{bytes:.2f} {suffixes[index]}"

os.system('cls')
print('====== Windows Resource Monitor ======\n')

while True:
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    bytes_sent, bytes_received = get_network_usage()

    print('\033[4A\033[2K', end='')
    print(f"-> CPU Usage: {Fore.LIGHTBLUE_EX}{cpu_usage}%")
    print(f"-> Memory Usage: {Fore.LIGHTBLUE_EX}{memory_usage}%")
    print(f"-> Disk Usage: {Fore.LIGHTBLUE_EX}{disk_usage}%")
    print(f"-> Network Usage: Sent: {Fore.LIGHTBLUE_EX}{format_size(bytes_sent)}{Style.RESET_ALL} / Received: {Fore.LIGHTBLUE_EX}{format_size(bytes_received)}")
    #print('\033[4A\033[2K', end='')

    time.sleep(.1)  # Wait for 1 second before updating the information
    
