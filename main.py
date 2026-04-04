import os
import sys
import argparse
from utils import find_pids_by_name

def check_root():
    if os.geteuid() != 0:
        print("[-] Hata: Bu işlem için root (sudo) yetkisi gereklidir!")
        sys.exit(1)

def main():
    check_root()
    
    parser = argparse.ArgumentParser(description="Process-Ghost: Linux Process Hiding Tool")
    parser.add_argument("-p", "--pid", type=int, help="Gizlenecek işlemin PID numarası")
    parser.add_argument("-n", "--name", type=str, help="Gizlenecek işlemin adı")
    parser.add_argument("--reveal", action="store_true", help="İşlemi tekrar görünür yap")

    args = parser.parse_args()

    target_pids = []

    if args.pid:
        target_pids.append(args.pid)
    elif args.name:
        target_pids = find_pids_by_name(args.name)
        if not target_pids:
            print(f"[-] Hata: '{args.name}' adında bir işlem bulunamadı.")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(0)

    for pid in target_pids:
        print(f"[+] Hedef PID belirlendi: {pid}")

if __name__ == "__main__":
    main()
