import os
import sys
import argparse

def check_root():
    """Programın root yetkisiyle çalışıp çalışmadığını kontrol eder."""
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

    if not args.pid and not args.name:
        parser.print_help()
        sys.exit(0)

    print("[+] Process-Ghost başlatıldı...")
    # Sonraki adımlar buraya gelecek

if __name__ == "__main__":
    main()
