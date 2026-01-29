"""LLM prompt templates for report generation.

Provides structured prompts for each report type and analyst role,
ensuring consistent and high-quality analysis output.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from narratological.models.analysis import Script


# =============================================================================
# System Prompts
# =============================================================================

COVERAGE_SYSTEM_PROMPT = """You are an expert script analyst providing studio coverage.

Your role is to evaluate scripts for:
- Commercial viability and marketability
- Structural integrity and pacing
- Character depth and development
- Dialogue quality and authenticity
- Originality and freshness
- Overall storytelling craft

Provide honest, actionable assessments. Be specific in your praise and criticism.
Your coverage will inform production decisions, so accuracy is essential."""

BEAT_MAP_SYSTEM_PROMPT = """You are a dramaturgical analyst creating a detailed beat map.

Your role is to:
- Identify the function of each scene (SETUP, INCITE, COMPLICATE, etc.)
- Classify connectors between scenes (BUT, THEREFORE, AND THEN, MEANWHILE)
- Assess tension levels (1-10 scale)
- Note key characters and dramatic beats

Be precise and consistent in your classifications. Use the 15 beat function codes:
SETUP, INCITE, COMPLICATE, ESCALATE, REVEAL, CRISIS, CLIMAX, RESOLVE,
TRANSITION, BREATHE, PLANT, PAYOFF, MIRROR, SUBPLOT, CODA."""

STRUCTURAL_SYSTEM_PROMPT = """You are a structural analyst mapping dramatic architecture.

Your role is to:
- Identify act boundaries and structure type
- Locate key structural points (inciting incident, midpoint, climax, etc.)
- Assess pacing and proportion balance
- Identify structural issues and opportunities

Apply frameworks from classical dramaturgy (Aristotle, Field, McKee, Snyder).
Be specific about where structural elements occur and how they function."""

CHARACTER_ATLAS_SYSTEM_PROMPT = """You are a character analyst mapping the dramatic persona.

Your role is to:
- Identify each character's Want (conscious goal) and Need (unconscious need)
- Identify the Lie they believe and the Truth they must learn
- Classify their arc (positive, negative, flat, corrupted, redeemed)
- Map relationships and character dynamics

Focus on psychological depth and transformation. Characters drive story;
analyze them as the engines of dramatic action."""

DIAGNOSTIC_SYSTEM_PROMPT = """You are a script diagnostician identifying structural issues.

Your role is to:
- Test causal binding (BUT/THEREFORE vs AND THEN)
- Assess scene necessity and reorderability
- Evaluate information economy and exposition efficiency
- Identify specific problems with recommended solutions

Be thorough but prioritize: focus on issues that most impact the narrative.
Provide severity levels (critical, warning, info, suggestion) for each issue."""


# =============================================================================
# Analysis Prompts
# =============================================================================

def build_coverage_prompt(script: Script) -> str:
    """Build the analysis prompt for coverage report generation.

    Args:
        script: The script being analyzed.

    Returns:
        Formatted prompt string.
    """
    scenes_summary = _format_scenes_summary(script)
    characters_summary = _format_characters_summary(script)

    return f"""Analyze this script and provide studio coverage.

SCRIPT INFORMATION:
Title: {script.title}
Format: {script.format}
Genre: {script.primary_genre or 'Not specified'}
Tone: {script.tone or 'Not specified'}
Logline: {script.logline or 'Not provided'}
Page Count: {script.page_count or 'Unknown'}
Scene Count: {script.scene_count or len(script.scenes)}

SCENES OVERVIEW:
{scenes_summary}

CHARACTERS:
{characters_summary}

Provide your coverage as a JSON object with these fields:
- logline: Your one-line summary (if not provided or to improve it)
- synopsis: Brief plot synopsis (1-2 paragraphs)
- recommendation: CONSIDER, PASS, DEVELOP, or URGENT
- premise_rating: 1-10 score for premise strength
- structure_rating: 1-10 score for structural integrity
- character_rating: 1-10 score for character depth
- dialogue_rating: 1-10 score for dialogue quality
- originality_rating: 1-10 score for originality
- marketability_rating: 1-10 score for commercial potential
- strengths: Array of key strengths
- weaknesses: Array of key weaknesses
- opportunities: Array of improvement opportunities
- comparables: Array of similar films/shows for reference"""


def build_beat_map_prompt(script: Script) -> str:
    """Build the analysis prompt for beat map generation.

    Args:
        script: The script being analyzed.

    Returns:
        Formatted prompt string.
    """
    scenes_detail = _format_scenes_detail(script)

    return f"""Create a detailed beat map for this script.

SCRIPT: {script.title}

SCENES:
{scenes_detail}

For each scene, provide:
- function: Primary beat function (SETUP, INCITE, COMPLICATE, ESCALATE, REVEAL, CRISIS, CLIMAX, RESOLVE, TRANSITION, BREATHE, PLANT, PAYOFF, MIRROR, SUBPLOT, CODA)
- secondary_function: Secondary function if applicable (or null)
- connector: How this scene connects to the next (BUT, THEREFORE, AND_THEN, MEANWHILE)
- tension: Tension level 1-10

Respond with a JSON object containing:
- entries: Array of beat map entries, one per scene
- function_distribution: Count of each function type
- connector_distribution: Count of each connector type
- average_tension: Average tension level"""


def build_structural_prompt(script: Script, structure_type: str = "Three-Act") -> str:
    """Build the analysis prompt for structural report generation.

    Args:
        script: The script being analyzed.
        structure_type: The structural framework to apply.

    Returns:
        Formatted prompt string.
    """
    scenes_summary = _format_scenes_summary(script)

    return f"""Analyze the dramatic structure of this script using {structure_type} framework.

SCRIPT: {script.title}
TOTAL SCENES: {len(script.scenes)}
TOTAL PAGES: {script.page_count or 'Unknown'}

SCENES:
{scenes_summary}

Identify:
1. Act boundaries (which scene numbers end each act)
2. Key structural points:
   - Opening image
   - Inciting incident
   - First act break
   - Midpoint
   - All is lost moment
   - Second act break
   - Climax
   - Resolution
   - Closing image

Respond with a JSON object containing:
- structure_type: "{structure_type}"
- act_count: Number of acts
- acts: Array of act analyses with:
  - number: Act number
  - start_scene: Starting scene
  - end_scene: Ending scene
  - percentage: Percentage of total script
  - summary: Act summary
  - key_events: Array of key events
- opening_image: Scene number (or null)
- inciting_incident: Scene number (or null)
- first_act_break: Scene number (or null)
- midpoint: Scene number (or null)
- all_is_lost: Scene number (or null)
- second_act_break: Scene number (or null)
- climax: Scene number (or null)
- resolution: Scene number (or null)
- closing_image: Scene number (or null)
- act_proportions: Array of proportions for each act
- pacing_notes: Notes on pacing
- structural_issues: Array of identified issues"""


def build_character_atlas_prompt(script: Script) -> str:
    """Build the analysis prompt for character atlas generation.

    Args:
        script: The script being analyzed.

    Returns:
        Formatted prompt string.
    """
    characters_detail = _format_characters_detail(script)
    scenes_summary = _format_scenes_summary(script)

    return f"""Create a character atlas for this script.

SCRIPT: {script.title}

CHARACTERS:
{characters_detail}

SCENES (for context):
{scenes_summary}

For each significant character, identify:
- Want: Their conscious, external goal
- Need: Their unconscious, internal need
- Lie: The false belief they hold
- Truth: What they must learn/accept
- Arc type: positive, negative, flat, corrupted, or redeemed
- Key scenes: Important scenes for their arc

Respond with a JSON object containing:
- total_characters: Total named characters
- principal_count: Number of principal characters
- entries: Array of character entries with:
  - name: Character name
  - role: Narrative role (protagonist, antagonist, ally, etc.)
  - screen_time: Percentage of scenes they appear in (0.0-1.0)
  - first_appearance: First scene number
  - want: Conscious goal (or null)
  - need: Unconscious need (or null)
  - lie: False belief (or null)
  - truth: Truth to learn (or null)
  - arc_type: positive, negative, flat, corrupted, or redeemed
  - arc_description: Summary of their arc
  - key_scenes: Array of key scene numbers
- protagonist: Main protagonist name
- antagonist: Main antagonist name (or null)
- ensemble_balance: Notes on ensemble balance
- missing_archetypes: Array of missing archetypal roles"""


def build_diagnostic_prompt(script: Script) -> str:
    """Build the analysis prompt for diagnostic report generation.

    Args:
        script: The script being analyzed.

    Returns:
        Formatted prompt string.
    """
    scenes_detail = _format_scenes_detail(script)

    return f"""Perform a structural diagnostic on this script.

SCRIPT: {script.title}

SCENES:
{scenes_detail}

Run these diagnostic tests:
1. CAUSAL BINDING: Check if scenes connect with BUT/THEREFORE (good) or AND THEN (weak)
2. REORDERABILITY: Identify scenes that could be moved without affecting the story
3. NECESSITY: Identify scenes that could be cut without losing essential information
4. INFORMATION ECONOMY: Check for redundant exposition or missing setup

Respond with a JSON object containing:
- frameworks_applied: Array of frameworks used
- issues: Array of issues with:
  - id: Unique identifier (e.g., "CB-001")
  - severity: critical, warning, info, or suggestion
  - category: structure, character, pacing, dialogue, etc.
  - description: What the issue is
  - location: Where in the script (scene number, act, etc.)
  - recommendation: How to fix it
  - framework_source: Which framework identified this
- causal_binding_ratio: Float 0.0-1.0 (target >0.80)
- reorderability_score: Float 0.0-1.0 (lower is better)
- necessity_score: Float 0.0-1.0 (higher is better)
- information_economy_score: Float 0.0-1.0 (higher is better)
- critical_count: Number of critical issues
- warning_count: Number of warnings
- overall_health: Assessment string (Excellent, Good, Fair, Poor, Critical)
- priority_fixes: Array of top priority fixes in order"""


# =============================================================================
# Role-Specific Prompts
# =============================================================================

def build_role_analysis_prompt(role: str, script: Script) -> str:
    """Build an analysis prompt for a specific analyst role.

    Args:
        role: The analyst role (aesthete, dramaturgist, etc.).
        script: The script being analyzed.

    Returns:
        Formatted prompt string.
    """
    role_prompts = {
        "aesthete": _build_aesthete_prompt,
        "dramaturgist": _build_dramaturgist_prompt,
        "narratologist": _build_narratologist_prompt,
        "art_historian": _build_art_historian_prompt,
        "cinephile": _build_cinephile_prompt,
        "rhetorician": _build_rhetorician_prompt,
        "producer": _build_producer_prompt,
        "academic": _build_academic_prompt,
        "first_reader": _build_first_reader_prompt,
    }

    builder = role_prompts.get(role.lower())
    if builder is None:
        raise ValueError(f"Unknown analyst role: {role}")

    return builder(script)


def _build_aesthete_prompt(script: Script) -> str:
    """Build prompt for the Aesthete role."""
    return f"""As the AESTHETE, analyze this script's form and style.

SCRIPT: {script.title}

Focus on:
- Visual and sensory patterns
- Tonal consistency and register
- Stylistic distinctiveness
- Formal elegance or innovation
- Beauty in structure and language

Provide observations about what makes this script aesthetically distinctive
or where its aesthetic identity could be strengthened."""


def _build_dramaturgist_prompt(script: Script) -> str:
    """Build prompt for the Dramaturgist role."""
    return f"""As the DRAMATURGIST, analyze this script's structure and rhythm.

SCRIPT: {script.title}

Focus on:
- Dramatic tension and release
- Pacing and rhythm patterns
- Act structure effectiveness
- Scene transitions and flow
- Theatrical dynamics

Identify what works structurally and what needs dramaturgical attention."""


def _build_narratologist_prompt(script: Script) -> str:
    """Build prompt for the Narratologist role."""
    return f"""As the NARRATOLOGIST, analyze this script's narrative mechanisms.

SCRIPT: {script.title}

Focus on:
- Causal chains and plot logic
- Information management (setup/payoff)
- Point of view and narrative distance
- Temporal structure (flashbacks, parallel timelines)
- Story vs discourse separation

Identify the narrative engines driving this story and their effectiveness."""


def _build_art_historian_prompt(script: Script) -> str:
    """Build prompt for the Art Historian role."""
    return f"""As the ART HISTORIAN, analyze this script's context and influences.

SCRIPT: {script.title}
GENRE: {script.primary_genre or 'Not specified'}

Focus on:
- Genre traditions and conventions
- Historical and cultural context
- Influences and lineages
- How it relates to its artistic moment
- Tradition vs innovation balance

Situate this work in its artistic context and identify its influences."""


def _build_cinephile_prompt(script: Script) -> str:
    """Build prompt for the Cinephile role."""
    return f"""As the CINEPHILE, identify comparable works for this script.

SCRIPT: {script.title}
GENRE: {script.primary_genre or 'Not specified'}
TONE: {script.tone or 'Not specified'}

Focus on:
- Similar films/shows in genre, tone, or theme
- Reference points for marketing/positioning
- Both obvious and unexpected comparisons
- What audiences this would appeal to

Provide 5-7 comparable works with brief explanations of the connection."""


def _build_rhetorician_prompt(script: Script) -> str:
    """Build prompt for the Rhetorician role."""
    return f"""As the RHETORICIAN, analyze this script's language and dialogue.

SCRIPT: {script.title}

Focus on:
- Dialogue craft and authenticity
- Voice distinctiveness per character
- Subtext and implied meaning
- Argumentative structure (if applicable)
- Language as character/worldbuilding

Assess the linguistic and rhetorical effectiveness of the writing."""


def _build_producer_prompt(script: Script) -> str:
    """Build prompt for the Producer role."""
    return f"""As the PRODUCER, assess this script's practical viability.

SCRIPT: {script.title}
FORMAT: {script.format}
PAGE COUNT: {script.page_count or 'Unknown'}

Focus on:
- Production complexity (locations, effects, cast size)
- Budget implications
- Casting considerations
- Market positioning
- Potential issues in production

Provide a practical assessment of bringing this script to screen."""


def _build_academic_prompt(script: Script) -> str:
    """Build prompt for the Academic role."""
    return f"""As the ACADEMIC, analyze this script through theoretical frameworks.

SCRIPT: {script.title}

Apply relevant frameworks:
- Classical dramaturgy (Aristotle's Poetics)
- Hero's Journey / Monomyth (Campbell)
- Three-Act Structure (Field)
- Character-driven story (McKee)
- Save the Cat beats (Snyder)

Assess theoretical coherence and identify which frameworks best apply."""


def _build_first_reader_prompt(script: Script) -> str:
    """Build prompt for the First-Reader role."""
    return f"""As the FIRST-READER, describe your emotional response to this script.

SCRIPT: {script.title}
LOGLINE: {script.logline or 'Not provided'}

Focus on:
- Initial engagement (did it hook you?)
- Emotional journey (what did you feel?)
- Satisfaction with ending
- What stuck with you
- Overall impression

Be honest about your gut reaction as a reader/viewer."""


# =============================================================================
# Helper Functions
# =============================================================================

def _format_scenes_summary(script: Script) -> str:
    """Format a brief summary of all scenes."""
    if not script.scenes:
        return "No scenes provided."

    lines = []
    for scene in script.scenes[:50]:  # Limit for context window
        chars = ", ".join(scene.characters_present[:3]) if scene.characters_present else "N/A"
        line = f"Scene {scene.number}: {scene.slug} - {scene.summary[:80]}... [{chars}]"
        lines.append(line)

    if len(script.scenes) > 50:
        lines.append(f"... and {len(script.scenes) - 50} more scenes")

    return "\n".join(lines)


def _format_scenes_detail(script: Script) -> str:
    """Format detailed scene information."""
    if not script.scenes:
        return "No scenes provided."

    lines = []
    for scene in script.scenes[:30]:  # Limit for context window
        chars = ", ".join(scene.characters_present) if scene.characters_present else "N/A"
        page_info = f"Pages {scene.page_start}-{scene.page_end}" if scene.page_start else ""
        tension = f"Tension: {scene.tension_level}" if scene.tension_level else ""

        line = f"""Scene {scene.number}: {scene.slug}
  Summary: {scene.summary}
  Characters: {chars}
  {page_info} {tension}"""
        lines.append(line.strip())

    if len(script.scenes) > 30:
        lines.append(f"\n... and {len(script.scenes) - 30} more scenes")

    return "\n\n".join(lines)


def _format_characters_summary(script: Script) -> str:
    """Format a brief summary of all characters."""
    if not script.characters:
        return "No characters provided."

    lines = []
    for char in script.characters[:20]:
        want_need = ""
        if char.want:
            want_need = f" | Want: {char.want[:40]}..."
        if char.need:
            want_need += f" | Need: {char.need[:40]}..."

        line = f"- {char.name} ({char.role}): {char.description[:60]}...{want_need}"
        lines.append(line)

    if len(script.characters) > 20:
        lines.append(f"... and {len(script.characters) - 20} more characters")

    return "\n".join(lines)


def _format_characters_detail(script: Script) -> str:
    """Format detailed character information."""
    if not script.characters:
        return "No characters provided."

    lines = []
    for char in script.characters[:15]:
        details = f"""{char.name}
  Role: {char.role}
  Description: {char.description}"""

        if char.want:
            details += f"\n  Want: {char.want}"
        if char.need:
            details += f"\n  Need: {char.need}"
        if char.lie:
            details += f"\n  Lie: {char.lie}"
        if char.truth:
            details += f"\n  Truth: {char.truth}"
        if char.arc_classification:
            details += f"\n  Arc: {char.arc_classification.value}"

        lines.append(details)

    if len(script.characters) > 15:
        lines.append(f"\n... and {len(script.characters) - 15} more characters")

    return "\n\n".join(lines)
