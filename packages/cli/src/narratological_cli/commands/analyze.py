"""CLI commands for analyzing scripts and stories."""

from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

app = typer.Typer(help="Analyze scripts and stories")
console = Console()


@app.command("script")
def analyze_script(
    script_path: Annotated[
        Path,
        typer.Argument(help="Path to script file (txt, pdf, fdx)"),
    ],
    framework: Annotated[
        Optional[str],
        typer.Option("--framework", "-f", help="Primary framework/study to apply"),
    ] = None,
    output: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Output directory for reports"),
    ] = None,
    reports: Annotated[
        str,
        typer.Option("--reports", "-r", help="Reports to generate: all, coverage, beatmap, structural, character, diagnostic"),
    ] = "coverage",
) -> None:
    """Analyze a script using narratological algorithms.

    This command ingests a script and generates analysis reports
    based on the selected framework(s).
    """
    if not script_path.exists():
        console.print(f"[red]Script file not found: {script_path}[/red]")
        raise typer.Exit(1)

    console.print(Panel(
        f"[bold]Analyzing:[/bold] {script_path.name}\n"
        f"[bold]Framework:[/bold] {framework or 'auto-detect'}\n"
        f"[bold]Reports:[/bold] {reports}",
        title="Script Analysis",
    ))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Reading script...", total=None)

        # Placeholder for actual analysis implementation
        # In a full implementation, this would:
        # 1. Parse the script file (txt, pdf, fdx)
        # 2. Run the analysis pipeline
        # 3. Generate requested reports

        progress.update(task, description="Parsing structure...")
        progress.update(task, description="Identifying beats...")
        progress.update(task, description="Analyzing characters...")
        progress.update(task, description="Running diagnostics...")
        progress.update(task, description="Generating reports...")

    console.print("\n[yellow]Note:[/yellow] Full script analysis requires LLM integration.")
    console.print("Install with: [cyan]pip install narratological[llm][/cyan]")
    console.print("\n[green]Analysis pipeline ready.[/green]")


@app.command("scene")
def analyze_scene(
    scene_text: Annotated[
        str,
        typer.Argument(help="Scene text to analyze (or path to file)"),
    ],
    framework: Annotated[
        Optional[str],
        typer.Option("--framework", "-f", help="Framework to apply"),
    ] = None,
) -> None:
    """Analyze a single scene using narratological algorithms.

    Provides quick analysis of beat function, tension, and structure.
    """
    # Check if it's a file path
    scene_path = Path(scene_text)
    if scene_path.exists():
        text = scene_path.read_text()
    else:
        text = scene_text

    console.print(Panel(
        f"[dim]{text[:500]}{'...' if len(text) > 500 else ''}[/dim]",
        title="Scene Text",
    ))

    console.print("\n[yellow]Note:[/yellow] Scene analysis requires LLM integration.")
    console.print("This would identify:")
    console.print("  - Beat function (SETUP, INCITE, ESCALATE, etc.)")
    console.print("  - Tension level (1-10)")
    console.print("  - Character dynamics")
    console.print("  - Connector to next scene (BUT/THEREFORE/AND THEN)")


@app.command("compare")
def compare_scripts(
    script_a: Annotated[Path, typer.Argument(help="First script")],
    script_b: Annotated[Path, typer.Argument(help="Second script")],
) -> None:
    """Compare two scripts structurally.

    Analyzes structural similarities and differences between scripts.
    """
    if not script_a.exists() or not script_b.exists():
        console.print("[red]One or both script files not found[/red]")
        raise typer.Exit(1)

    console.print(f"Comparing: [cyan]{script_a.name}[/cyan] vs [cyan]{script_b.name}[/cyan]")
    console.print("\n[yellow]Note:[/yellow] Script comparison requires full analysis.")


@app.command("batch")
def batch_analyze(
    directory: Annotated[
        Path,
        typer.Argument(help="Directory containing scripts"),
    ],
    pattern: Annotated[
        str,
        typer.Option("--pattern", "-p", help="File pattern to match"),
    ] = "*.txt",
    output: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Output directory"),
    ] = None,
) -> None:
    """Batch analyze multiple scripts.

    Process all matching scripts in a directory.
    """
    if not directory.exists():
        console.print(f"[red]Directory not found: {directory}[/red]")
        raise typer.Exit(1)

    scripts = list(directory.glob(pattern))
    console.print(f"Found [cyan]{len(scripts)}[/cyan] scripts matching '{pattern}'")

    for script in scripts:
        console.print(f"  - {script.name}")

    console.print("\n[yellow]Note:[/yellow] Batch analysis requires LLM integration.")
