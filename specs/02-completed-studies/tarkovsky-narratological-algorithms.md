# Andrei Tarkovsky's Narratological Algorithms

> Systematic distillation of Andrei Tarkovsky's "Sculpting in Time" methodology into formal, implementable principles for narrative and cinematic construction. Derived from *Sculpting in Time* (1986), *Time Within Time: The Diaries 1970-1986*, and collected interviews (ed. John Gianvito).

---

## Table of Contents

0. [Meta-Principles (Axioms)](#0-meta-principles-axioms)
1. [Structural Hierarchy](#1-structural-hierarchy)
2. [Temporal Dilation / Sculpting in Time](#2-temporal-dilation--sculpting-in-time)
3. [Image-as-Meditation Protocol](#3-image-as-meditation-protocol)
4. [Memory Structure Algorithm](#4-memory-structure-algorithm)
5. [Spiritual/Metaphysical Architecture](#5-spiritualmetaphysical-architecture)
6. [Elemental Vocabulary System](#6-elemental-vocabulary-system)
7. [Diagnostic Questions](#7-diagnostic-questions)
8. [Bergman Correspondence Mapping](#8-bergman-correspondence-mapping)
9. [Quick Reference Card](#9-quick-reference-card)
10. [Source Cross-Reference](#appendix-a-source-cross-reference)
11. [Research Gaps](#appendix-b-research-gaps)

---

## 0. Meta-Principles (Axioms)

| Axiom | Formulation |
|-------|-------------|
| AT-A0 | **"Time is the material of cinema."** The director sculpts time as a sculptor removes marble to reveal form. Cinema's unique artistic property is its capacity to imprint and reproduce temporal experience. |
| AT-A1 | **"Poetry is cinema's natural language; prose is its degradation."** Poetic logic (associative, emotional, non-linear) is closer to life and thought than dramatic logic. Traditional theatrical causation limits cinema's potential. |
| AT-A2 | **"The audience must be active; difficulty is respect."** The spectator must build meaning from parts. Art that explains itself patronizes; art that demands participation honors the viewer's capacity for depth. |
| AT-A3 | **"Spiritual truth cannot be stated, only shown."** The infinite cannot be made material, but an *image* of the infinite can be created. The invisible is depicted through what it touches and moves. |
| AT-A4 | **"Rhythm, not montage, is cinema's dominant force."** Time-pressure within the frame determines rhythm. Editing should match pre-existing temporal flows, not create meaning through juxtaposition (contra Eisenstein). |
| AT-A5 | **"Art prepares the soul for death."** The function of art is to "plough and harrow" the soul, rendering it capable of turning to good. Art must give hope even when depicting hopelessness. |

### Source Quotes

> "For the first time in the history of the arts, in the history of culture, man found the means to take an impression of time. And simultaneously the possibility of reproducing that time on screen as often as he wanted, to repeat it and go back to it. He acquired a matrix for actual time."
> —*Sculpting in Time*

> "The dominant, all-powerful factor of the film image is rhythm, expressing the course of time within the frame."
> —*Sculpting in Time*

> "In my view poetic reasoning is closer to the laws by which thought develops, and thus to life itself, than is the logic of traditional drama."
> —*Sculpting in Time*

> "The aim of art is to prepare a person for death, to plough and harrow his soul, rendering it capable of turning to good."
> —*Time Within Time*

> "The artistic image is always a metonym, where one thing is substituted for another, the smaller for the greater. To tell of what is living, the artist uses something dead; to speak of the infinite, he shows the finite."
> —*Sculpting in Time*

---

## 1. Structural Hierarchy

```
TEMPORAL_UNITY (the complete work)
  └── RHYTHM_WAVE (macro temporal movement)
        └── SEQUENCE (sustained temporal flow)
              └── SHOT (atomic unit: contains inherent time-pressure)
                    └── FRAME (instant: time frozen yet pregnant)
```

### Definition Table

| Unit | Definition | Constraint |
|------|------------|------------|
| **TEMPORAL_UNITY** | The complete film as a "mosaic of time" | Must create unified temporal experience; viewer goes for "time lost or spent or not yet had" |
| **RHYTHM_WAVE** | Large-scale temporal movement (act-equivalent) | Governed by accumulating time-pressure, not plot points |
| **SEQUENCE** | Sustained flow of connected shots | United by internal rhythm, not by narrative causation |
| **SHOT** | The atomic unit containing inherent time-pressure | Rhythm determined by pressure of time passing *within* it, not by length |
| **FRAME** | Single instant of frozen time | Carries potential meaning; image exists "as it is" (haiku principle) |

### Tarkovsky vs. Eisenstein: Structural Contrast

| Eisenstein | Tarkovsky |
|------------|-----------|
| Meaning created *between* shots (collision) | Meaning exists *within* shots (time-pressure) |
| Editing is generative ("montage of attractions") | Editing is subtractive (sculpting away excess) |
| Intellectual cinema | Poetic cinema |
| Concept dictates cut | Rhythm dictates cut |

---

## 2. Temporal Dilation / Sculpting in Time

### 2.1 Core Concept

```
SCULPTING_IN_TIME:
├── INPUT: "lump of time" (raw footage/experience)
├── PROCESS: Remove everything not essential to temporal truth
├── OUTPUT: Distilled time-pressure creating viewer immersion
└── METAPHOR: As sculptor removes marble to reveal form within
```

### 2.2 Time-Pressure Algorithm

```python
def calculate_time_pressure(shot):
    """
    Time-pressure increases with shot duration but is not
    determined by duration alone. It is the felt weight of
    time passing within the frame.
    """
    internal_rhythm = analyze_movement_within_frame(shot)
    duration = shot.length
    content_density = shot.visual_complexity + shot.emotional_weight

    # Pressure accumulates non-linearly
    time_pressure = internal_rhythm * log(duration) * content_density

    return time_pressure

def determine_cut_point(shot_sequence):
    """
    Tarkovsky cuts at peak time-pressure, not at plot points.
    The cut must match temporal flows between shots.
    """
    for i, shot in enumerate(shot_sequence):
        current_pressure = calculate_time_pressure(shot)
        next_rhythm = shot_sequence[i+1].internal_rhythm if i+1 < len(shot_sequence) else None

        if current_pressure >= PEAK_THRESHOLD:
            if rhythm_compatible(shot.internal_rhythm, next_rhythm):
                return CUT_VALID
            else:
                return EXTEND_OR_ADJUST

    return CONTINUE_SHOT
```

### 2.3 Temporal Dilation Decision Table

| Condition | Action | Effect |
|-----------|--------|--------|
| Scene requires contemplation | EXTEND shot duration | Time-pressure builds; viewer enters meditative state |
| Emotional weight is high | SLOW motion subtly | Time becomes viscous, dreamlike |
| Narrative urgency present | RESIST cutting faster | Maintain temporal integrity; refuse manipulation |
| Transition between states | MATCH rhythm across cut | Preserve continuous temporal experience |
| Peak pressure reached | CUT to compatible rhythm | Release/transfer accumulated energy |

### 2.4 Long Take Principle

```
LONG_TAKE_FUNCTION:
  PURPOSE: Build atmosphere; immerse viewer in temporal flow
  MECHANISM:
    - Duration forces attention to details
    - Viewer becomes aware of time passing
    - Pressure creates "lean-forward" experience
  CONSTRAINT:
    - Never extend arbitrarily
    - Internal activity must justify duration
    - Cut when rhythm demands, not when "enough" time passes
```

> "The distortion of time can be a means of giving it rhythmical expression."
> —*Sculpting in Time*

---

## 3. Image-as-Meditation Protocol

### 3.1 Poetic Logic vs. Dramatic Logic

```
LOGIC_CLASSIFICATION:
├── DRAMATIC_LOGIC (rejected as limiting)
│     ├── Linear causation
│     ├── Plot-driven connections
│     ├── Explanation precedes experience
│     └── Meaning is stated
│
└── POETIC_LOGIC (embraced as essential)
      ├── Associative linkage
      ├── Emotional resonance
      ├── Experience precedes understanding
      └── Meaning emerges from contemplation
```

### 3.2 Haiku Principle

Tarkovsky explicitly connects his image philosophy to Japanese haiku:

```
HAIKU_IMAGE_PROTOCOL:
  INPUT: Object/scene to be depicted

  PROCESS:
    1. Present image "as it is" — instantaneously, without interpretation
    2. Meaning is pre-existing in the image itself, not constructed through technique
    3. Juxtaposition of disparate elements creates whole larger than parts
    4. No symbolic encoding — the image IS, it does not REPRESENT

  OUTPUT: Direct perception unmediated by explanation

  ANTI-PATTERN:
    ✗ Building poetic image through conventional European methods
    ✗ Linguistic mediation as primary meaning-bearer
    ✗ Explanation of significance
```

> "Haiku creates images in such a way that they mean nothing beyond themselves."
> —Tarkovsky on Zen/haiku influence

### 3.3 Observation Algorithm

```python
def create_contemplative_image(subject):
    """
    Tarkovsky's method for achieving meditative image quality.
    The camera observes rather than dramatizes.
    """
    # Step 1: Naturalism of image and sound
    image = capture_without_stylization(subject)
    sound = record_ambient_reality(subject.environment)

    # Step 2: Allow subject to exist in time
    duration = calculate_contemplation_duration(subject.complexity)

    # Step 3: Build associative links (not causal)
    associations = []
    for element in image.components:
        associations.extend(find_emotional_resonances(element))

    # Step 4: Quote from non-cinematic realities
    if enhances_meaning:
        incorporate_painting(relevant_artwork)
        incorporate_music(pre_existing_composition)
        incorporate_poetry(relevant_verse)

    # Step 5: Refuse to interpret
    NEVER: add_explanatory_voiceover()
    NEVER: use_conventional_symbolism()

    return MeditativeImage(
        image=image,
        sound=sound,
        duration=duration,
        associations=associations,
        interpretation=None  # Viewer's task
    )
```

### 3.4 Active Spectator Requirement

```
SPECTATOR_ACTIVATION:
  PRINCIPLE: Viewer must build separate parts into whole

  MECHANISM:
    - Poetic linkages require intuition to perceive
    - Film meaning is co-created, not transmitted
    - "A book read by 1000 people is 1000 books"

  IMPLEMENTATION:
    - Refuse standard symbolism (prevents personal interpretation)
    - Allow multiple valid readings
    - Trust viewer's capacity for depth

  TEST:
    IF viewer can fully explain meaning on first viewing:
      THEN film has failed (too explicit)
    IF viewer returns to discover new meanings:
      THEN film succeeds (inexhaustible)
```

> "Through poetic connections feeling is heightened and the spectator is made more active."
> —*Sculpting in Time*

---

## 4. Memory Structure Algorithm

### 4.1 Non-Linear Chronology as Psychological Realism

```
MEMORY_STRUCTURE_PRINCIPLE:
  ASSERTION: Memory does not function chronologically
  IMPLICATION: Linear narrative is psychologically false
  METHOD: Structure film as memory actually operates
```

### 4.2 Memory Linkage Protocol

```python
def structure_as_memory(narrative_elements):
    """
    Connect scenes not by time or place, but by emotional/associative logic.
    Derived from Mirror's construction principles.
    """
    connections = []

    for element in narrative_elements:
        # Connections based on:
        link_by_individual = find_shared_persons(element, all_elements)
        link_by_motif = find_recurring_images(element, all_elements)
        link_by_emotion = find_emotional_resonance(element, all_elements)
        link_by_serendipity = find_chance_associations(element, all_elements)

        # NOT connected by:
        # - Chronological sequence
        # - Causal necessity
        # - Plot logic

        connections.extend([link_by_individual, link_by_motif,
                           link_by_emotion, link_by_serendipity])

    return arrange_by_poetic_logic(connections)
```

### 4.3 Temporal Fluidity in Mirror

```
MIRROR_STRUCTURE (exemplar):
├── Three timeframes (prewar ~1935, WWII 1940s, postwar 1960s-70s)
├── Freely switches between frames without transition markers
├── Same actress plays mother AND wife (identity blur)
├── Same actor plays protagonist as child AND protagonist's son
├── Newsreel footage integrates with personal memory
├── Dreams indistinguishable from memory
└── Result: Time exists "concurrently" — past is not gone but present

STRUCTURAL_PRINCIPLE:
  "Concerning its structure, Mirror for me is, in general, the most
  complicated of my films — as a structure, not as a fragment considered
  separately but precisely as a construction; its dramaturgy is
  extraordinarily complex, convoluted. Just like the structure of
  dreams or reminiscences."
  —Tarkovsky on Mirror
```

### 4.4 Memory-Truth Algorithm

```
MEMORY_TRUTH_TEST:
  FOR each scene in film:
    ASK: Does this feel like how memory actually operates?

    VALID if:
      - Transitions feel intuitive rather than explained
      - Time boundaries are permeable
      - Identity remains fluid across time
      - Emotional logic supersedes causal logic
      - Some elements remain unexplained (as in actual memory)

    INVALID if:
      - Flashback is clearly marked/framed
      - Past is "complete" and separate from present
      - All connections are logically explicable
      - Memory serves only plot function
```

---

## 5. Spiritual/Metaphysical Architecture

### 5.1 Faith as Narrative Engine

```
SPIRITUAL_CINEMA_DEFINITION:
  NOT: "Religious films" (depicting religion's role in life)
  IS: Interior terrain where person is one with oneself

  CHARACTERISTICS:
    - Faith as waiting for miracle, not declaring belief
    - Miracle occurs on borders of invisible realms
    - Felt rather than logically deciphered
    - Language of spirit through poetry of image
```

### 5.2 Depicting the Invisible

```python
def depict_transcendent(spiritual_content):
    """
    Tarkovsky's method for showing what cannot be shown.
    After Robert Bresson: "translate the invisible wind by the
    water it sculpts in passing."
    """
    # The infinite cannot be made material
    NEVER: represent_god_directly()
    NEVER: state_spiritual_truth_explicitly()

    # But the IMAGE of the infinite can be created
    visible_effects = find_material_manifestations(spiritual_content)

    # Depict the invisible through what it touches and moves
    for effect in visible_effects:
        show_effect_on_material_world(effect)
        # Wind shown through moving grass
        # Spirit shown through human transformation
        # Faith shown through inexplicable persistence

    return Image(
        content=visible_effects,
        meaning=spiritual_content,  # Present but not stated
        access="felt, not explained"
    )
```

### 5.3 Spiritual Protagonist Pattern

```
TARKOVSKY_PROTAGONIST:
├── Physically frail or emotionally unstable (external weakness)
├── Spiritually persistent (internal strength)
├── Does not conquer external world
├── Endures internal journey
├── Broken/fragmented but still believes
└── Suffering as path to transformation

EXEMPLAR (Stalker):
  - Guides others to "The Zone"
  - Physically weak, socially marginal
  - Only one who believes in transformative power
  - Embodies faith despite (because of?) evidence against it
```

### 5.4 Metaphysical Silence vs. Bergman's Silence

```
SILENCE_TYPOLOGY:
├── BERGMAN: Silence as emptiness/absence
│     God does not respond → void
│     Minimalist soundscape → Godless despair
│
└── TARKOVSKY: Silence as presence/manifestation
      "Silence" depicted through complex sound layers
      Ambient sound as metaphysical presence
      Silence affirms rather than denies the spiritual
```

### 5.5 Art as Prayer Protocol

```
ART_AS_PRAYER:
  ASSERTION: "Art is a form of prayer. Man only lives through prayer."

  IMPLEMENTATION:
    - Creative act as spiritual practice
    - Film-viewing as contemplative experience
    - Director's work is sacrificial/priestly

  FUNCTION:
    - Make "infinity tangible"
    - Make "the inexpressible, expressible"
    - "Art must give man hope and faith"

  PARADOX:
    "The more hopeless the world in the artist's version,
     the more clearly perhaps must we see the ideal that
     stands in opposition — otherwise life becomes impossible!"
```

---

## 6. Elemental Vocabulary System

### 6.1 Overview

Tarkovsky employs recurring natural elements as a systematic visual vocabulary. However, he explicitly rejected symbolic interpretation, insisting these elements should be understood as metaphors for "everyday life" rather than coded meanings.

### 6.2 Elemental Classification

```
ELEMENTAL_VOCABULARY:
├── WATER (most frequent element)
│     ├── Rain: Isolation, cleansing, temporal marker
│     ├── River/stream: Flow of time, boundary crossing
│     ├── Standing water: Reflection, memory, threshold
│     ├── Ocean (Solaris): Consciousness, the infinite
│     └── Pool (Nostalghia): Testing ground, ritual space
│
├── FIRE
│     ├── Candle: Life's fragility, hope persistence
│     ├── Burning house: Destruction as transformation
│     ├── Hearth: Domesticity, warmth, center
│     └── Often appears WITH water (Mirror, Nostalghia)
│
├── EARTH
│     ├── Mud/soil: Material reality, embodiment
│     ├── Ruin: Time's passage, decay as beauty
│     ├── Grass/vegetation: Natural rhythm, growth
│     └── Stone/masonry: Permanence, human craft
│
└── WIND/AIR
      ├── Breeze through grass: Invisible made visible
      ├── Moving curtains: Threshold, presence
      ├── Snow: Temporal suspension, purity
      └── Breath: Life force, spirit (Latin: spiritus)
```

### 6.3 Tarkovsky on His Elemental Use

> "There is always water in my films... I love the Japanese attitude to nature. They concentrate on a confined space reflecting the infinite. Water is a mysterious element — because of its structure. And it is very cinegenic; it transmits movement, depth, changes. Nothing is more beautiful than water."
> —Tarkovsky interview

> "Rain, snow, and water... a symbol of faith."
> —As noted in *The Films of Andrei Tarkovsky: A Visual Fugue* (Johnson)

### 6.4 Anti-Symbolic Reading Protocol

```
ELEMENTAL_INTERPRETATION:
  CAUTION: Tarkovsky detested fixed symbolism

  DO:
    - Read elements as metaphors for life itself
    - Allow personal/subjective interpretation
    - Observe naturalistic function (rain IS rain)
    - Notice rhythmic function (elemental time-signature)

  DO NOT:
    - Assign fixed symbolic meanings
    - Create allegorical decoder rings
    - Reduce image to concept

  PARADOX:
    Elements carry meaning (water = faith per Tarkovsky)
    BUT meaning is not fixed (viewer creates their own)

  RESOLUTION:
    "A book read by 1000 different people is 1000 different books"
```

### 6.5 Elemental Rhythm Algorithm

```python
def apply_elemental_rhythm(scene, element_type):
    """
    Natural elements provide their own temporal signature.
    The director works with (not against) these inherent rhythms.
    """
    natural_rhythms = {
        'rain': 'continuous, variable intensity, ambient sound',
        'fire': 'flickering, consuming, hypnotic center',
        'water_flow': 'perpetual, directional, meditative',
        'wind': 'intermittent, invisible force made visible',
        'snow': 'suspended, silent, covering'
    }

    element_rhythm = natural_rhythms[element_type]

    # Match scene rhythm to elemental rhythm
    scene.pacing = align_with(element_rhythm)
    scene.duration = determined_by(element_rhythm)
    scene.sound = incorporate(element_rhythm.audio_signature)

    # Elements provide respite from emotional pain
    if character.experiencing_grief_or_loss:
        surround_with(natural_element)
        allow_contemplation_of(element)

    return scene
```

---

## 7. Diagnostic Questions

Answer YES/NO for structural validation of Tarkovskian work:

### Temporal Integrity

1. Does the rhythm arise from time-pressure within shots rather than editing pace?
2. Are cuts made at points of rhythmic compatibility between shots?
3. Does duration serve contemplation rather than narrative efficiency?
4. Is temporal manipulation (slow motion, etc.) rhythmically justified?
5. Does the viewer experience time as material rather than as conveyor of plot?

### Poetic Logic

6. Are scenes connected by associative/emotional logic rather than causal necessity?
7. Does the work resist explaining its images?
8. Must the viewer actively construct meaning from parts?
9. Are there multiple valid interpretations available?
10. Does the image exist "as it is" (haiku principle) rather than representing something else?

### Memory Structure

11. Does chronology serve psychological truth rather than narrative clarity?
12. Are temporal boundaries permeable (past/present/future interpenetrating)?
13. Do identities blur across time (same actor as different ages/people)?
14. Is some material left unexplained, as in actual memory?

### Spiritual Architecture

15. Is spiritual content shown rather than stated?
16. Does the invisible become perceptible through its effects on the material?
17. Is there hope even in depictions of hopelessness?
18. Does the protagonist embody spiritual persistence despite weakness?

### Elemental Vocabulary

19. Are natural elements present with their inherent rhythms?
20. Do elements function as metaphor rather than symbol?
21. Is the viewer allowed personal interpretation of elemental meaning?

**Scoring:**
- 17-21 YES: Fully Tarkovskian
- 12-16 YES: Strong alignment
- 7-11 YES: Partial integration
- <7 YES: Fundamental revision needed

---

## 8. Bergman Correspondence Mapping

### 8.1 Mutual Recognition

| Director | Quote About the Other |
|----------|----------------------|
| Bergman on Tarkovsky | "Tarkovsky for me is the greatest of them all, the one who invented a new language, true to the nature of film, as it captures life as a reflection, life as a dream." |
| Tarkovsky on Bergman | "I am only interested in the views of two people: one is called Bresson and one called Bergman." |

### 8.2 Fundamental Contrast: Interiority Approaches

| Dimension | Tarkovsky | Bergman |
|-----------|-----------|---------|
| **Primary Visual Unit** | Landscape/environment | Face/close-up |
| **Interiority Access** | Through space (feeling-toned frames) | Through physiognomy (facial landscape) |
| **Subject-World Relation** | Person related to whole world | Person related to inner self |
| **Dramatic Mode** | Image-first; drama oblique | Drama-first; image serves |
| **Theatrical Influence** | Minimal; purely cinematic | Significant; stage-screen hybrid |
| **Human Figure** | Placed within environment | Environment secondary to face |

### 8.3 Spiritual/Religious Contrast

| Dimension | Tarkovsky (Orthodox tradition) | Bergman (Protestant tradition) |
|-----------|-------------------------------|-------------------------------|
| **God's Silence** | Silence as presence (affirms faith) | Silence as absence (denies comfort) |
| **Soundscape** | Complex layers = metaphysical presence | Minimal sound = Godless void |
| **Faith Stance** | Mystical sense of supernatural power | Despair of life without God |
| **Religious Institution** | Little regard; personal spirituality | Wrestling with institutional doubt |
| **Transcendence** | Possible through art and faith | Questioned, longed for, uncertain |

### 8.4 Visual Technique Contrast

| Technique | Tarkovsky | Bergman |
|-----------|-----------|---------|
| **Close-up** | Rare; face as part of environment | Frequent; face as primary subject |
| **Long take** | Essential; builds time-pressure | Used but not defining |
| **Camera movement** | Slow, lateral, tracking | Varied; serves drama |
| **Lighting** | Natural, diffused | High contrast, theatrical |
| **Sound** | Ambient, layered, atmospheric | Selective, often silent |

### 8.5 Shared Territory

Despite differences, both directors share:

```
SHARED_PRINCIPLES:
├── Metaphysical seriousness
├── Rejection of entertainment cinema
├── Spiritual/existential crisis as subject
├── Psychological depth over action
├── Art as ethical/spiritual endeavor
├── Personal vision over commercial appeal
└── Contempt for "the logic of traditional drama"
```

### 8.6 Correspondence Table for Bergman Study

| Tarkovsky Concept | Bergman Equivalent (to verify) | Investigation Point |
|-------------------|-------------------------------|---------------------|
| Time-pressure | ? (Bergman's temporal approach) | How does Bergman structure time? |
| Poetic logic | Psychological logic? | Is Bergman's connection system similar? |
| The Zone | The chamber (Persona, Cries)? | Enclosed space as spiritual crucible? |
| Elemental vocabulary | Facial vocabulary? | Does Bergman have equivalent system? |
| Memory structure | Dream structure? | Compare non-linearity approaches |
| Spiritual silence | Existential silence | Already mapped above |

---

## 9. Quick Reference Card

### The Sculpting Formula

```
LUMP_OF_TIME → [REMOVE_INESSENTIAL] → DISTILLED_RHYTHM → TEMPORAL_EXPERIENCE
```

### Time-Pressure Test

```
IF shot.internal_rhythm + duration = PEAK_PRESSURE:
  CUT to compatible rhythm
ELSE:
  EXTEND shot
```

### Poetic vs. Dramatic

```
POETIC: A → B (associative) ← life's logic
DRAMATIC: A → B (causal) ← theatrical logic

✓ Connect by feeling
✗ Connect by plot
```

### Image Protocol

```
HAIKU PRINCIPLE:
  Present image AS IT IS
  Meaning pre-exists; don't construct it
  ✓ Observation
  ✗ Explanation
```

### Memory Structure

```
VALID: Emotional/associative connection
INVALID: Chronological/causal connection

Time is permeable. Identity is fluid. Some things remain unexplained.
```

### Spiritual Architecture

```
SHOW the invisible through its effects
NEVER state spiritual truth directly
HOPE must be visible even in hopelessness
```

### Elemental Palette

```
WATER = faith, mystery, reflection, time-flow
FIRE = fragility, transformation, hope
WIND = invisible presence, spirit, breath
EARTH = material reality, decay, permanence

BUT: Allow personal interpretation. No fixed symbols.
```

### The Five Laws

```
1. TIME is the material
2. RHYTHM, not montage, is dominant
3. POETRY, not prose, is the language
4. The VIEWER must work
5. The SPIRITUAL can only be shown
```

---

## Appendix A: Source Cross-Reference

| Source | Key Principles Extracted |
|--------|-------------------------|
| *Sculpting in Time* (1986) | AT-A0 through AT-A5; Time-pressure theory; Poetic logic; Haiku principle; Anti-Eisenstein position |
| *Time Within Time: Diaries* (1970-1986) | Art as preparation for death; Faith struggle; Personal methodology; Stalker genesis |
| *Tarkovsky: Interviews* (ed. Gianvito) | Elemental vocabulary explanations; Reluctance re: symbolism; Bergman admiration |
| Mirror production notes | Memory structure; Non-linear chronology; Identity fluidity |
| Stalker production documents | Zone as non-symbol; Spiritual alienation theme; Film as metaphysical journey |
| Nostalghia production context | Candle scene methodology; Exile and longing themes |

---

## Appendix B: Research Gaps

### Primary Source Access Required

1. **Full text of *Sculpting in Time*** - Specific page references needed for all quotes; chapter structure for complete doctrine extraction
2. **Complete *Time Within Time*** - Additional diary entries on methodology; personal spiritual reflections
3. **John Gianvito collection** - Full interview texts; production-specific methodology details
4. **Production diaries for Stalker, Mirror, Nostalghia** - Detailed shooting decisions; temporal construction process

### Verification Needed

1. **AT-A2 axiom** - "Audience must work; difficulty is respect" - sourced from general philosophy; need direct quote
2. **Haiku passage** - Full context in *Sculpting in Time* required
3. **Water as "symbol of faith"** - Confirm exact source and context (Johnson book or direct interview?)
4. **Bergman collaboration details** - Sacrifice production specifics with Nykvist

### For Bergman Study Preparation

1. Bergman's writings on Tarkovsky (beyond the famous quote)
2. Bergman's own temporal theory (if extant)
3. *Persona* and *Cries and Whispers* as potential Zone-equivalents
4. Bergman's facial close-up methodology texts
5. Protestant vs. Orthodox aesthetic theology comparison

---

*Document generated from web-accessible excerpts of Tarkovsky's writings, interviews, and scholarly analysis. All principles extracted and formalized for practical narrative construction. Primary source verification recommended for production use.*

---

## Research Methodology Note

This study follows the narratological-algorithms skill protocol:
- **Source Classification**: Practitioner (Tarkovsky's own articulated methodology)
- **Primary Source Priority**: *Sculpting in Time* and *Time Within Time* over secondary analysis
- **Extraction Method**: Direct quotes where available; inference marked where principles are derived
- **Formalization Patterns**: Conceptual statements → constraint rules; processes → pseudocode; comparisons → decision tables

**Sequence B Status**: This document serves as foundation for the Bergman interiority study that follows. Correspondence mapping in Section 8 identifies investigation points for the comparative analysis.
