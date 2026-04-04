import os
import sys
import argparse
from utils import find_pids_by_name, hide_process, reveal_process

def check_root():
    """Programın root yetkisiyle çalışıp çalışmadığını kontrol eder."""
    if os.geteuid() != 0:
        print("[-] Hata: Bu işlem için root (sudo) yetkisi gereklidir!")
        sys.exit(1)

def main():
    check_root()
    
    parser = argparse.ArgumentParser(description="Process-Ghost: Linux Process Hiding Tool")
    parser.add_argument("-p", "--pid", type=int, help="Hedef işlemin PID numarası")
    parser.add_argument("-n", "--name", type=str, help="Hedef işlemin adı")
    parser.add_argument("--reveal", action="store_true", help="İşlemi tekrar görünür yap")

    args = parser.parse_args()

    target_pids = []

    if args.pid:
        target_pids.append(args.pid)
    elif args.name:
        # Görünür yaparken /proc altında bulamayacağımız için 
        # reveal modunda isimle arama yapamayabiliriz, bu yüzden PID önerilir.
        target_pids = find_pids_by_name(args.name)
        if not target_pids and not args.reveal:
            print(f"[-] Hata: '{args.name}' adında bir işlem bulunamadı.")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(0)

    for pid in target_pids:
        if not args.reveal:
            print(f"[+] Hedef PID belirlendi: {pid}")
            if hide_process(pid):
                print(f"[!] BAŞARILI: PID {pid} gizlendi.")
        else:
            if reveal_process(pid):
                print(f"[+] BAŞARILI: PID {pid} tekrar görünür yapıldı.")

if __name__ == "__main__":
    main()
