import socket, os, re, concurrent.futures, time, sys, random, base64
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
from pyfiglet import Figlet

console = Console()

class WassimGhostUltimate:
    def __init__(self):
        self.banner_text = "WASSIM GHOST"

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # --- 1. محرك الفحص الخارق ---
    def scan_single_port(self, target, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((target, port)) == 0:
                    return port
        except:
            return None

    def nmap_module(self):
        self.clear()
        console.print(Panel("[bold cyan]WASSIM ULTRA SCANNER (1 - 65535 Ports)[/bold cyan]"))
        target = console.input("[?] Target IP: ")
        p_range = console.input("[?] Range (e.g 1-1000): ")
        try:
            start, end = map(int, p_range.split('-'))
            table = Table(title=f"Open Ports on {target}", show_lines=True)
            table.add_column("PORT", style="bold green", justify="center")
            table.add_column("SERVICE", style="white", justify="center")
            
            open_ports = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
                ports = range(start, end + 1)
                results = list(track(executor.map(lambda p: self.scan_single_port(target, p), ports), total=len(ports), description="Scanning..."))
            
            for p in results:
                if p:
                    open_ports.append(p)
                    table.add_row(str(p), "OPEN SERVICE")
            
            if not open_ports:
                console.print("[red][!] No open ports found.[/red]")
            else:
                console.print(table)
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")

    # --- 2. محرك فحص الثغرات المطور ---
    def code_vulnerability_auditor(self):
        self.clear()
        console.print(Panel("[bold red]🔥 WASSIM GHOST - DEEP ZERO-DAY INTELLIGENCE ENGINE 🔥[/bold red]"))
        path = console.input("[?] Enter Path to Audit ( . ): ")

        zero_day_logic = {
            "CRITICAL: Remote Command Execution": r"(system|exec|popen|spawn|shell_exec|passthru|eval|run|os\.system|subprocess)\s*\(",
            "HIGH: Potential Buffer Overflow": r"(strcpy|strcat|gets|sprintf|scanf|memcpy)\s*\(",
            "CRITICAL: Injection Logic": r"(\.query|\.execute|db\.run|sql)\s*\(.*[\+\$].*|SELECT.*WHERE.*=.*",
            "CRITICAL: Unsafe Deserialization": r"(pickle\.load|yaml\.load|unserialize|JSON\.parse|Marshal\.load)\s*\(",
            "MEDIUM: Hardcoded Secret": r"(password|api_key|token|secret|db_pass|access_key)\s*[:=]\s*['\"].*['\"]",
            "HIGH: Path Traversal Risk": r"(fs\.readFile|open|read_file|send_file)\s*\(.*req\..*",
        }

        table = Table(title="[ WASSIM GHOST - AUDIT REPORT ]", show_lines=True)
        table.add_column("SEVERITY", style="bold red", justify="center")
        table.add_column("LOCATION (FILE:LINE)", style="cyan")
        table.add_column("VULNERABILITY TYPE", style="white")

        found_count = 0
        # دعم فحص ملف مفرد أو مجلد
        targets = []
        if os.path.isfile(path):
            targets.append((os.path.dirname(path), [], [os.path.basename(path)]))
        else:
            targets = os.walk(path)

        for root, _, files in targets:
            for file in files:
                if file.endswith(('.py', '.js', '.php', '.c', '.cpp', '.java', '.go', '.rb', '.sh')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', errors='ignore') as f:
                            content = f.read()
                            for name, pattern in zero_day_logic.items():
                                matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
                                for match in matches:
                                    line_num = content.count('\n', 0, match.start()) + 1
                                    severity = "CRITICAL" if "CRITICAL" in name else "HIGH"
                                    table.add_row(severity, f"{file}:{line_num}", name)
                                    found_count += 1
                    except: continue

        if found_count > 0:
            console.print(table)
            console.print(f"[bold green][+] Total Issues Spotted: {found_count}[/bold green]")
        else:
            console.print(Panel("[yellow][!] No obvious Zero-Day patterns matched.[/yellow]"))

    # --- 3. محرك الصيد ---
    def phisher_module(self):
        self.clear()
        console.print(Panel("[bold yellow]🔥 WASSIM PHISH PRO v7.0 🔥[/bold yellow]"))
        target = console.input("\n[WassimPhish@Admin]# Target Site Name: ")
        folder = f"WassimPhish_{target.lower()}"
        if not os.path.exists(folder): os.makedirs(folder)
        
        secret = f"<h2>Login Required</h2><form action='post.php' method='post'><input name='u' placeholder='ID'><br><input type='password' name='p' placeholder='Key'><br><input type='submit' value='Verify'></form>"
        encoded = base64.b64encode(secret.encode()).decode()
        html = f"<html><body style='text-align:center;padding-top:100px;font-family:sans-serif;'><div id='x'></div><script>document.getElementById('x').innerHTML=atob('{encoded}');</script></body></html>"
        
        with open(f"{folder}/index.html", "w", encoding="utf-8") as f: f.write(html)
        console.print(Panel(f"SUCCESS! Folder Created: {folder}", style="bold green"))

    def main_loop(self):
        while True:
            self.clear()
            f = Figlet(font='slant')
            console.print(f.renderText(self.banner_text), style="bold red")
            menu_table = Table.grid(expand=True)
            menu_table.add_row("[bold cyan]1.[/bold cyan] NMAP PRO (Scan Ports)")
            menu_table.add_row("[bold red]2.[/bold red] CODE AUDITOR (Zero-Day Scan)")
            menu_table.add_row("[bold yellow]3.[/bold yellow] WASSIMPHISH (Templates)")
            menu_table.add_row("[bold white]4.[/bold white] EXIT SYSTEM")
            console.print(Panel(menu_table, title="[ Main Menu ]", border_style="blue", padding=(1, 2)))
            
            cmd = console.input("\n[Wassim-Ghost@System]# ")
            if cmd == "1": self.nmap_module()
            elif cmd == "2": self.code_vulnerability_auditor()
            elif cmd == "3": self.phisher_module()
            elif cmd == "4": sys.exit()
            console.input("\n[System] Press Enter to return...")

if __name__ == "__main__":
    ghost = WassimGhostUltimate()
    ghost.main_loop()
