import os

def find_pids_by_name(process_name):
    """İşlem adına göre sistemdeki tüm eşleşen PID'leri bulur."""
    pids = []
    # /proc dizinindeki tüm sayısal klasörleri tara
    try:
        for pid in [d for d in os.listdir('/proc') if d.isdigit()]:
            try:
                with open(os.path.join('/proc', pid, 'comm'), 'r') as f:
                    if process_name in f.read().strip():
                        pids.append(int(pid))
            except (FileNotFoundError, ProcessLookupError, PermissionError):
                continue
    except PermissionError:
        print("[-] Hata: /proc dizini okunamadı. Root yetkisi gerekebilir.")
    return pids
