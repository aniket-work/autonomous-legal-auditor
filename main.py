import time
import sys
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.layout import Layout
from auditor.analyzer import ContractAnalyzer

def main():
    console = Console()
    analyzer = ContractAnalyzer()

    # Title
    console.print(Panel.fit("[bold cyan]Autonomous Legal Contract Auditor[/bold cyan]\n[italic]Compliance & Risk Intelligence Engine[/italic]", border_style="cyan"))
    console.print()

    # Mock Contract Input
    contract_sample = """
    SERVICE AGREEMENT
    ...
    Payment Terms: Net 60.
    Governing Law: Laws of the State of New York.
    Liability: [SILENT]
    ...
    """

    console.print("[bold white]Loading Contract:[/bold white] [green]vendor_service_agreement_v1.pdf[/green]")
    time.sleep(0.8)

    # Analysis Animation
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task1 = progress.add_task("Parsing natural language...", total=100)
        while not progress.finished:
            progress.update(task1, advance=2)
            time.sleep(0.02)
        
        task2 = progress.add_task("Cross-referencing corporate policies...", total=100)
        while not progress.finished:
            progress.update(task2, advance=3)
            time.sleep(0.03)

        task3 = progress.add_task("Generating risk assessment...", total=100)
        while not progress.finished:
            progress.update(task3, advance=5)
            time.sleep(0.02)

    # Perform Analysis
    results = analyzer.analyze_contract(contract_sample)

    # Display Results
    console.print("\n[bold]Audit Results:[/bold]")
    
    table = Table(title="Compliance Findings", border_style="blue")
    table.add_column("Rule ID", style="cyan", no_wrap=True)
    table.add_column("Severity", style="magenta")
    table.add_column("Status", justify="center")
    table.add_column("Details", style="white")

    for finding in results["findings"]:
        status_style = "green" if finding["status"] == "PASS" else "red"
        status_icon = "✔" if finding["status"] == "PASS" else "✘"
        table.add_row(
            finding["rule_id"],
            finding["severity"],
            f"[{status_style}]{status_icon} {finding['status']}[/{status_style}]",
            finding["detail"]
        )

    console.print(table)
    console.print()

    # Final Score Panel
    score = results['score']
    color = "green" if score >= 80 else "yellow" if score >= 50 else "red"
    console.print(Panel(f"[bold {color}]Compliance Score: {score}/100[/bold {color}]", title="Final Assessment", expand=False))

if __name__ == "__main__":
    main()
