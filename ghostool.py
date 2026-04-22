import socket, os, concurrent.futures, sys, time
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

    def scan_single_port(self, target, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.6)
                if s.connect_ex((target, port)) == 0:
                    return port
        except:
            return None

    def nmap_module(self):
        self.clear()
        console.print(Panel("[bold red]⚡ WASSIM ULTRA PENETRATION SCANNER ⚡[/bold red]"))
        target = console.input("[bold white][?] Target IP/Host: [/bold white]")
        port_range = console.input("[bold white][?] Range (1-10000): [/bold white]")

        try:
            start_p, end_p = map(int, port_range.split('-'))
            if end_p - start_p > 10000: end_p = start_p + 10000
        except:
            console.print("[bold red][!] Invalid Range.[/bold red]"); return

        console.print("[bold yellow][*] Bypassing Firewalls & IDS...[/bold yellow]")
        time.sleep(1)

        table = Table(title=f"RECON: {target}", show_lines=True)
        table.add_column("PORT", style="bold green", justify="center")
        table.add_column("STATE", style="bold cyan")
        table.add_column("SERVICE", style="bold white")

        ports = range(start_p, end_p + 1)
        open_ports = []

        # تقليل الـ workers لـ 50 يضمن استقراراً كاملاً في Termux الضعيف والقوي
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            results = list(track(executor.map(lambda p: self.scan_single_port(target, p), ports), 
                                total=len(ports), description="[bold red]Infiltrating...[/bold red]"))
        
        for p in results:
            if p:
                open_ports.append(p)
                try: service = socket.getservbyport(p).upper()
                except: service = "UNKNOWN"
                table.add_row(str(p), "OPEN", service)

        self.clear()
        if not open_ports:
            console.print(Panel(f"[red]No vulnerabilities in {port_range}[/red]"))
        else:
            console.print(table)
            console.print(f"\n[bold green][+] Found: {len(open_ports)} Active Ports.[/bold green]")

    def main_loop(self):
        while True:
            self.clear()
            console.print(Figlet(font='slant').renderText(self.banner_text), style="bold red")
            menu = Table.grid(expand=True)
            menu.add_row("[bold red]1.[/bold red] ADVANCED PORT DISCOVERY")
            menu.add_row("[bold red]2.[/bold red] EXIT SYSTEM")
            console.print(Panel(menu, title="[ GHOST HUB ]", border_style="red"))
            
            cmd = console.input("\n[Wassim@Root]# ")
            if cmd == "1": self.nmap_module(); console.input("\n[Enter] to return...")
            elif cmd == "2": sys.exit()

if __name__ == "__main__":
    WassimGhostUltimate().main_loop()
