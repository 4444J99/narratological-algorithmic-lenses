"""CLI commands for running diagnostic tests."""

from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

app = typer.Typer(help="Run diagnostic tests on narratives")
console = Console()


@app.command("causal")
def diagnose_causal_binding(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to analyzed script or beat map JSON"),
    ],
    target: Annotated[
        float,
        typer.Option("--target", "-t", help="Target causal binding ratio"),
    ] = 0.80,
) -> None:
    """Test causal binding (BUT/THEREFORE vs AND THEN).

    Strong narratives have >80% causal connectors (BUT/THEREFORE).
    Weak episodic structures rely on AND THEN connections.
    """
    console.print(Panel(
        f"[bold]Target:[/bold] {target:.0%} causal binding\n"
        "[bold]Method:[/bold] BUT/THEREFORE vs AND THEN analysis",
        title="Causal Binding Diagnostic",
    ))

    console.print("\n[bold]Causal Binding Analysis[/bold]")
    console.print("The 'Therefore Rule' (South Park writers):")
    console.print("  - [green]BUT[/green] - Contradiction/obstacle that changes direction")
    console.print("  - [green]THEREFORE[/green] - Direct consequence of previous action")
    console.print("  - [red]AND THEN[/red] - Sequential but not causally connected")
    console.print("  - [yellow]MEANWHILE[/yellow] - Parallel action (valid for subplots)")

    console.print("\n[yellow]Note:[/yellow] Full causal analysis requires beat map data.")
    console.print("Run 'narratological analyze script' first to generate beat map.")


@app.command("reorder")
def diagnose_reorderability(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to analyzed script"),
    ],
) -> None:
    """Test scene reorderability.

    Identifies scenes that could be reordered without affecting
    the narrative - a sign of weak causal structure.
    """
    console.print(Panel(
        "[bold]Test:[/bold] Can scenes be reordered without breaking the narrative?",
        title="Reorderability Diagnostic",
    ))

    console.print("\n[bold]Reorderability Test[/bold]")
    console.print("Strong narratives have scenes that MUST be in order.")
    console.print("If scenes can be shuffled, causal binding is weak.")

    console.print("\n[yellow]Note:[/yellow] Requires analyzed script data.")


@app.command("necessity")
def diagnose_necessity(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to analyzed script"),
    ],
) -> None:
    """Test scene necessity.

    Identifies scenes that could be removed without affecting
    the narrative - violates information economy.
    """
    console.print(Panel(
        "[bold]Test:[/bold] Can any scene be removed without loss?",
        title="Necessity Diagnostic",
    ))

    console.print("\n[bold]Necessity Test[/bold]")
    console.print("Every scene should advance plot, character, or theme.")
    console.print("Scenes serving only one function should serve it irreplaceably.")

    console.print("\n[yellow]Note:[/yellow] Requires analyzed script data.")


@app.command("framework")
def diagnose_with_framework(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to analyzed script"),
    ],
    study_id: Annotated[
        str,
        typer.Argument(help="Study/framework to use for diagnosis"),
    ],
) -> None:
    """Run diagnostic questions from a specific study.

    Uses the diagnostic questions defined in a narratological study
    to evaluate the script.
    """
    from narratological.loader import load_study

    try:
        study = load_study(study_id)
    except KeyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)

    console.print(Panel(
        f"[bold]Framework:[/bold] {study.creator} - {study.work}",
        title=f"Diagnostic: {study_id}",
    ))

    console.print(f"\n[bold]Diagnostic Questions ({len(study.diagnostic_questions)}):[/bold]")

    table = Table()
    table.add_column("ID", style="cyan")
    table.add_column("Question")
    table.add_column("Valid If")

    for q in study.diagnostic_questions:
        table.add_row(
            q.id,
            q.question[:60] + "..." if len(q.question) > 60 else q.question,
            q.valid_if[:50] + "..." if len(q.valid_if) > 50 else q.valid_if,
        )

    console.print(table)

    console.print("\n[yellow]Note:[/yellow] Full diagnostic requires analyzed script data.")
    console.print("Run 'narratological analyze script' first.")


@app.command("all")
def diagnose_all(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to analyzed script"),
    ],
    output: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Output path for diagnostic report"),
    ] = None,
) -> None:
    """Run full diagnostic battery.

    Runs all diagnostic tests and generates a comprehensive
    diagnostic report with prioritized recommendations.
    """
    console.print(Panel(
        "[bold]Tests:[/bold] Causal Binding, Reorderability, Necessity, Information Economy",
        title="Full Diagnostic Battery",
    ))

    console.print("\n[bold]Diagnostic Tests:[/bold]")
    console.print("  1. Causal Binding Ratio (target >80%)")
    console.print("  2. Scene Reorderability (lower is better)")
    console.print("  3. Scene Necessity (higher is better)")
    console.print("  4. Information Economy (efficiency of delivery)")

    console.print("\n[bold]Framework Diagnostics:[/bold]")
    console.print("  - Bergman Chamber Drama constraints")
    console.print("  - Pixar Empathy Engineering checklist")
    console.print("  - Zelda Discovery Pacing metrics")
    console.print("  - McKee Value Charge analysis")

    console.print("\n[yellow]Note:[/yellow] Full diagnostic requires analyzed script data.")
