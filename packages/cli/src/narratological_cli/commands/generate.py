"""CLI commands for generating narrative structures."""

from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

app = typer.Typer(help="Generate narrative structures")
console = Console()


@app.command("outline")
def generate_outline(
    premise: Annotated[
        str,
        typer.Argument(help="Story premise or logline"),
    ],
    framework: Annotated[
        str,
        typer.Option("--framework", "-f", help="Framework/study to use"),
    ] = "pixar",
    acts: Annotated[
        int,
        typer.Option("--acts", "-a", help="Number of acts"),
    ] = 3,
    output: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Output file path"),
    ] = None,
) -> None:
    """Generate a story outline from a premise.

    Uses the structural hierarchy and algorithms from the selected
    framework to generate a story outline.
    """
    from narratological.loader import load_study

    try:
        study = load_study(framework)
    except KeyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)

    console.print(Panel(
        f"[bold]Premise:[/bold] {premise}\n"
        f"[bold]Framework:[/bold] {study.creator}\n"
        f"[bold]Acts:[/bold] {acts}",
        title="Outline Generation",
    ))

    console.print("\n[bold]Structural Hierarchy from Framework:[/bold]")
    tree = Tree(f"[bold]{study.id}[/bold]")
    for level in study.structural_hierarchy.levels:
        branch = tree.add(f"[cyan]Level {level.level}:[/cyan] {level.name}")
        branch.add(f"[dim]{level.description}[/dim]")
    console.print(tree)

    console.print("\n[bold]Available Algorithms:[/bold]")
    for algo in study.core_algorithms[:5]:
        console.print(f"  - [green]{algo.name}[/green]")

    console.print("\n[yellow]Note:[/yellow] Full outline generation requires LLM integration.")
    console.print("Install with: [cyan]pip install narratological[llm][/cyan]")


@app.command("beats")
def generate_beats(
    scene_description: Annotated[
        str,
        typer.Argument(help="Scene description or context"),
    ],
    function: Annotated[
        str,
        typer.Option("--function", "-f", help="Target beat function"),
    ] = "ESCALATE",
) -> None:
    """Generate beats for a scene.

    Creates micro-level beat structure for a scene based on
    the target function and dramatic context.
    """
    from narratological.models.analysis import BeatFunction

    try:
        beat_func = BeatFunction(function.upper())
    except ValueError:
        valid = ", ".join(f.value for f in BeatFunction)
        console.print(f"[red]Invalid function: {function}[/red]")
        console.print(f"Valid functions: {valid}")
        raise typer.Exit(1)

    console.print(Panel(
        f"[bold]Scene:[/bold] {scene_description[:100]}...\n"
        f"[bold]Function:[/bold] {beat_func.value}",
        title="Beat Generation",
    ))

    console.print("\n[bold]Beat Function Characteristics:[/bold]")
    characteristics = {
        "SETUP": "Establishes information, world, characters",
        "INCITE": "Disrupts equilibrium, sets story in motion",
        "COMPLICATE": "Adds obstacles, complexity",
        "ESCALATE": "Raises stakes, increases tension",
        "REVEAL": "Discloses information, changes understanding",
        "CRISIS": "Forces difficult choice",
        "CLIMAX": "Peak of action/emotion",
        "RESOLVE": "Provides resolution",
        "BREATHE": "Pacing relief, emotional reset",
        "PLANT": "Sets up future payoff",
        "PAYOFF": "Delivers on earlier setup",
    }
    console.print(f"  {beat_func.value}: {characteristics.get(beat_func.value, 'N/A')}")

    console.print("\n[yellow]Note:[/yellow] Beat generation requires LLM integration.")


@app.command("character")
def generate_character(
    role: Annotated[
        str,
        typer.Argument(help="Character role (protagonist, antagonist, etc.)"),
    ],
    genre: Annotated[
        Optional[str],
        typer.Option("--genre", "-g", help="Genre context"),
    ] = None,
    framework: Annotated[
        str,
        typer.Option("--framework", "-f", help="Framework for character design"),
    ] = "pixar",
) -> None:
    """Generate a character structure.

    Creates Want/Need/Lie/Truth structure and arc based on
    the selected framework's character principles.
    """
    console.print(Panel(
        f"[bold]Role:[/bold] {role}\n"
        f"[bold]Genre:[/bold] {genre or 'not specified'}\n"
        f"[bold]Framework:[/bold] {framework}",
        title="Character Generation",
    ))

    console.print("\n[bold]Character Structure Template:[/bold]")
    console.print("  [cyan]WANT[/cyan] - Conscious external goal")
    console.print("  [cyan]NEED[/cyan] - Unconscious internal need")
    console.print("  [cyan]LIE[/cyan] - False belief character holds")
    console.print("  [cyan]TRUTH[/cyan] - Truth character must learn")

    console.print("\n[bold]Arc Types:[/bold]")
    console.print("  - Positive: Growth toward better state")
    console.print("  - Negative: Decline toward worse state")
    console.print("  - Flat: Tests existing beliefs")

    console.print("\n[yellow]Note:[/yellow] Character generation requires LLM integration.")


@app.command("transformation")
def generate_transformation(
    subject: Annotated[
        str,
        typer.Argument(help="Subject to transform"),
    ],
    cause: Annotated[
        str,
        typer.Option("--cause", "-c", help="Cause of transformation"),
    ] = "divine intervention",
    preserve: Annotated[
        str,
        typer.Option("--preserve", "-p", help="What to preserve (mens pristina)"),
    ] = "consciousness",
) -> None:
    """Generate an Ovidian transformation sequence.

    Uses the Metamorphoses algorithm to create a transformation
    narrative with proper mens_pristina preservation.
    """
    from narratological.loader import load_study

    study = load_study("ovid-metamorphoses")

    console.print(Panel(
        f"[bold]Subject:[/bold] {subject}\n"
        f"[bold]Cause:[/bold] {cause}\n"
        f"[bold]Preserve:[/bold] {preserve}",
        title="Transformation Generation (Ovid)",
    ))

    console.print("\n[bold]Ovidian Transformation Principles:[/bold]")
    for axiom in study.axioms[:3]:
        console.print(f"  - [cyan]{axiom.name}[/cyan]")

    # Find transformation algorithm
    for algo in study.core_algorithms:
        if "transformation" in algo.name.lower() or "metamorphosis" in algo.name.lower():
            console.print(f"\n[bold]Algorithm: {algo.name}[/bold]")
            console.print(f"[dim]{algo.purpose}[/dim]")
            break

    console.print("\n[yellow]Note:[/yellow] Full transformation generation requires LLM integration.")
