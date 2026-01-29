# DAVID LYNCH: NARRATOLOGICAL ALGORITHMS
## A Formal System for Dream Logic and Dual-Reality Narrative

---

## I. ARTIST PROFILE

**David Keith Lynch** (1946-2025)
American filmmaker, painter, musician, and meditation advocate

### Primary Works Analyzed
- *Eraserhead* (1977)
- *The Elephant Man* (1980)
- *Blue Velvet* (1986)
- *Twin Peaks* (1990-1991, 2017)
- *Wild at Heart* (1990)
- *Lost Highway* (1997)
- *Mulholland Drive* (2001)
- *Inland Empire* (2006)

### Key Source Texts
- **"Lynch on Lynch"** (Chris Rodley, 1997/2005) - Extended interviews
- **"Catching the Big Fish"** (2006) - Lynch's book on creativity and TM
- **"Room to Dream"** (2018) - Memoir with Kristine McKenna
- **"The Art Life"** (2016) - Documentary on Lynch's early years

---

## II. FOUNDATIONAL AXIOMS

### DL-A0: The Incoherence Principle
> "I don't know why people expect art to make sense. They accept the fact that life doesn't make sense."
> *— Los Angeles Times interview, 1989*

**Formalization:**
```
IF life.structure == INCOHERENT
AND art.function == REFLECT(life)
THEN art.coherence_requirement == FALSE
```

**Corollary:** Narrative logic need not map to waking-life causality. The demand for "sense" is itself a category error imposed on art.

---

### DL-A1: Ideas as Autonomous Entities
> "Ideas are like fish. If you want to catch little fish, you can stay in the shallow water. But if you want to catch the big fish, you've got to go deeper."
> *— Catching the Big Fish*

> "The idea is the whole thing. If you stay true to the idea, it tells you everything you need to know."

**Formalization:**
```
DEFINE idea AS external_entity {
    origin: NOT(mind) BUT ether/unified_field
    property: arrives_complete
    requirement: fidelity_to_original_form
}

FUNCTION creative_process(artist):
    idea = catch_from_depth(meditation_practice)
    WHILE building_work:
        IF deviation_from(idea.original_feeling):
            REJECT current_direction
        MAINTAIN feeling_match(idea)
    RETURN work_that_feels_like_idea_felt
```

**Key Insight:** The artist's role is reception and faithful transmission, not construction or invention.

---

### DL-A2: Mood Primacy Over Plot
> "My approach to film stems from my art background, as I go beyond the story to the sub-conscious mood created by sound and images."

> "The beginning dictates the direction and you never know where you're going to go...the mood is what you're looking for, and somehow we always find it."

**Formalization:**
```
NARRATIVE_HIERARCHY = {
    1: mood/atmosphere,
    2: feeling/intuition,
    3: image/sound,
    4: character,
    5: plot/causality
}

FUNCTION evaluate_scene(scene):
    IF scene.mood == TARGET_MOOD:
        ACCEPT scene
        // Plot coherence is secondary concern
    ELSE:
        REJECT scene
        // Even if plot-logical
```

---

### DL-A3: The Power of Secrets
> "The magic of the discovery is ruined and the film experience, the secret, is killed."
> *— On refusing to explain his films*

> "The more unknowable the mystery, the more beautiful it is."

**Formalization:**
```
DEFINE secret AS {
    holder: [audience, artist, character]
    revelation_status: WITHHELD
    power: INVERSELY_PROPORTIONAL(explanation)
}

FUNCTION preserve_mystery(narrative):
    explanation_density = LOW
    interpretation_space = MAXIMUM
    // Secrets kept from self enhance power
    artist_understanding = PARTIAL
    RETURN narrative.mystery_intact
```

---

## III. CORE ALGORITHMS

### ALGORITHM 1: DREAM LOGIC ARCHITECTURE

Lynch's dream logic is not random surrealism but follows specific operational principles drawn from actual dream mechanics.

#### 1.1 The Dream Grammar

```
DREAM_LOGIC_SYSTEM {

    // Core Principle: Feeling-Based Causality
    CONNECTION_TYPE: emotional_resonance NOT logical_sequence

    // Lynch: "I hardly ever get ideas from dreams, but I love dream logic."

    RULES {

        RULE temporal_collapse:
            // Past, present, future exist simultaneously
            time_sequence = NON_LINEAR
            memory = PRESENT_TENSE
            prophecy = ALREADY_OCCURRED

        RULE identity_fluidity:
            // One actor, multiple characters
            // One character, multiple actors
            character_boundaries = PERMEABLE
            self = MULTIPLE_SIMULTANEOUS_VERSIONS

        RULE spatial_dislocation:
            // Spaces connect by feeling, not geography
            location_transition = EMOTIONAL_LOGIC
            // The Red Room connects to everywhere
            threshold_spaces = PORTAL_FUNCTION

        RULE symbolic_literalization:
            // Metaphors become actual
            "eaten by guilt" = LITERAL_CONSUMPTION
            "split self" = PHYSICAL_DOUBLING

        RULE non_sequitur_as_meaning:
            // Seeming randomness carries emotional truth
            disconnection = DEEPER_CONNECTION
            absurdity = REVELATION
    }
}
```

#### 1.2 Dream Logic Implementation

```
ALGORITHM apply_dream_logic(narrative_element):

    // Step 1: Disconnect from Waking Causality
    narrative_element.causal_chain = SEVER

    // Step 2: Establish Emotional Truth
    core_feeling = extract_emotional_content(narrative_element)

    // Step 3: Allow Transformation
    transformed = dream_transform(narrative_element) {
        apply(temporal_collapse)
        apply(identity_fluidity)
        apply(symbolic_literalization)
        MAINTAIN(core_feeling)  // This is the constant
    }

    // Step 4: Test Against Feeling
    IF transformed.emotional_resonance == core_feeling:
        ACCEPT transformed
    ELSE:
        RETRY transformation

    RETURN transformed
```

#### 1.3 The Waiting Room / Threshold Space

```
THRESHOLD_SPACE_PATTERN {

    // The Red Room as paradigm

    PROPERTIES {
        location: BETWEEN_WORLDS
        time: SUSPENDED / NONLINEAR
        communication: CRYPTIC / REVERSED / RIDDLED
        inhabitants: SPIRIT_ENTITIES / DOPPELGANGERS
        floor_pattern: CHEVRON (zigzag = spiritual_portal)
        curtains: RED_VELVET (boundary between known/unknown)
    }

    FUNCTION operate_threshold(protagonist):
        // Entry through dream, near-death, or crisis
        protagonist.state = LIMINAL

        // Information delivered in riddles
        message = ENCODE(truth, cryptic_layer)

        // Time operates differently
        25_years_later = NOW

        // Identity becomes unstable
        protagonist.self = ENCOUNTER(doppelganger)

        RETURN transformed_protagonist OR trapped_protagonist
}
```

---

### ALGORITHM 2: DUALITY / DOUBLING SYSTEMS

Lynch's use of doubles is systematic and follows identifiable patterns.

#### 2.1 The Doubling Taxonomy

```
DOUBLING_TYPES {

    TYPE_1: SPLIT_SELF {
        // One character becomes two
        // Fred Madison -> Pete Dayton (Lost Highway)
        // Betty/Diane (Mulholland Drive)

        trigger: TRAUMA / UNBEARABLE_REALITY
        mechanism: PSYCHOGENIC_FUGUE
        relationship: WISH_FULFILLMENT vs REALITY
        structure: MOBIUS_STRIP (endless loop)
    }

    TYPE_2: MIRROR_DOUBLE {
        // Same actor, explicitly two characters
        // Renee/Alice (Lost Highway)
        // Rita/Camilla (Mulholland Drive)

        relationship: OBJECT_OF_DESIRE_SPLIT
        one_version: ATTAINABLE / SAFE
        other_version: DANGEROUS / TRUE
    }

    TYPE_3: SHADOW_POSSESSION {
        // External evil inhabiting host
        // Leland/BOB (Twin Peaks)

        mechanism: POSSESSION_NOT_SPLITTING
        relationship: HOST_UNAWARE or COMPLICIT
        evil_source: EXTERNAL_ENTITY
    }

    TYPE_4: SUPERNATURAL_DOUBLE {
        // Lodge doppelgangers
        // Evil Cooper (Twin Peaks: The Return)

        origin: OTHER_DIMENSION
        purpose: REPLACE_ORIGINAL
        marker: WRONG_EYES / WRONG_BEHAVIOR
    }
}
```

#### 2.2 The Doubling Algorithm

```
ALGORITHM create_double(character, narrative_purpose):

    // Determine doubling type based on narrative need
    IF narrative_purpose == ESCAPE_TRAUMA:
        double_type = SPLIT_SELF
        structure = BEFORE_AFTER_REVERSAL

    ELIF narrative_purpose == EXPLORE_DESIRE:
        double_type = MIRROR_DOUBLE
        structure = PARALLEL_VERSIONS

    ELIF narrative_purpose == EXTERNALIZE_EVIL:
        double_type = SHADOW_POSSESSION
        structure = HIDDEN_WITHIN

    // Implementation
    double = CREATE {
        same_actor: TRUE (usually)
        different_name: TRUE
        inverted_characteristics: SELECTIVE
        shared_memories: FRAGMENTED / BLEEDING_THROUGH
    }

    // The Photograph Test (from Lost Highway)
    // If both versions appear in same photo, reality breaks
    IF photograph.contains(both_versions):
        protagonist.sanity = CRUMBLES
        narrative.reality = FRACTURES

    RETURN double
```

#### 2.3 The Mobius Strip Narrative

```
MOBIUS_NARRATIVE_PATTERN {

    // Both Lost Highway and Mulholland Drive use this

    STRUCTURE {
        opening_line = closing_line  // "Dick Laurent is dead"
        ending = return_to_beginning
        loop = INFINITE
        escape = IMPOSSIBLE
    }

    FUNCTION construct_mobius(narrative):

        SEGMENT_1 (Fantasy/Wish):
            protagonist = idealized_version
            relationships = as_desired
            threat = external_only

        TRANSITION (The Blue Box / The Cabin):
            reality_fracture_point
            switch_trigger = KEY_OBJECT

        SEGMENT_2 (Reality/Nightmare):
            protagonist = damaged_version
            relationships = failed/betrayed
            threat = protagonist_is_source

        RECURSIVE_RETURN:
            ending_loops_to_opening
            cycle = INESCAPABLE

        // The two segments are same story, opposite valence
        S1 = INVERSE(S2)
        S1 + S2 = complete_truth

    RETURN mobius_narrative
}
```

---

### ALGORITHM 3: TONAL RUPTURE SYSTEM

Lynch's signature juxtaposition of incompatible tones.

#### 3.1 Tonal Collision Mechanics

```
TONAL_RUPTURE_SYSTEM {

    // Lynch creates meaning through impossible juxtapositions
    // Not ironic distance but sincere occupation of both

    PRIMARY_COLLISIONS {

        horror + comedy:
            // "Just You" song in Twin Peaks
            // Dancing dwarf in Red Room
            EFFECT: uncanny, destabilizing, true

        violence + beauty:
            // Dorothy's bruised face + blue velvet
            // Murder + Badalamenti score
            EFFECT: aesthetic violence, seductive horror

        innocence + corruption:
            // Small town America + absolute evil
            // White picket fence + severed ear
            EFFECT: paradise_revealed_as_hell

        sincerity + absurdity:
            // Cooper's genuine enthusiasm
            // Log Lady's absolute seriousness
            NOT_IRONIC: Lynch means it
    }

    // J. Hoberman's formulation:
    // "troubling juxtapositions, outlandish non sequiturs,
    //  and eroticized derangement of the commonplace"
}
```

#### 3.2 The Sincere Uncanny

```
ALGORITHM create_sincere_uncanny(scene):

    // Lynch is NOT being ironic about the 1950s wholesomeness
    // He genuinely loves it AND sees the horror beneath

    surface_tone = WARMTH / NOSTALGIA / BEAUTY
    subsurface_tone = DREAD / VIOLENCE / CORRUPTION

    // Both are true simultaneously
    final_tone = HOLD_BOTH(surface_tone, subsurface_tone)

    // Key: Lynch believes in the light
    light_value = SINCERE (not parodic)
    dark_value = SINCERE (not exploitation)

    // The horror makes the beauty more precious
    // The beauty makes the horror more terrible
    relationship = MUTUAL_INTENSIFICATION

    RETURN scene.uncanny_sincere
```

---

### ALGORITHM 4: MOOD/ATMOSPHERE AS NARRATIVE

```
MOOD_PRIMACY_SYSTEM {

    // Narrative exists to deliver mood
    // Not: mood enhances narrative
    // But: narrative serves mood

    FUNCTION construct_sequence(target_mood):

        // Start with desired feeling
        feeling = DEFINE(target_mood)

        // Sound design first (Lynch's method)
        sound = CREATE_SOUNDSCAPE(feeling) {
            industrial_drone: IF feeling.includes(dread)
            badalamenti_jazz: IF feeling.includes(mystery)
            fifties_pop: IF feeling.includes(nostalgia_danger)
            silence: IF feeling.includes(sacred_horror)
        }

        // Image second
        image = CREATE_VISUAL(feeling) {
            lighting: chiaroscuro / noir
            movement: slow_track OR static_hold
            color: saturated OR drained
            texture: velvet / industrial / suburban
        }

        // Narrative events third (almost incidental)
        events = WHATEVER_MAINTAINS(feeling)

        // Lynch to Badalamenti: never "happy" or "sad"
        // Always: specific moods, atmospheres, story fragments

    RETURN sequence.delivers(target_mood)
}
```

---

### ALGORITHM 5: SYMBOLIC RECURRENCE

Lynch's motifs function as a consistent symbolic vocabulary across works.

```
LYNCH_SYMBOL_LEXICON {

    RED_CURTAINS {
        meaning: boundary_between_worlds
        function: conceals_horror / marks_threshold
        deployment: Red Room, Club Silencio, stage performances
        // "Humans are filled with dread when it comes to the unseen"
    }

    ELECTRICITY {
        meaning: supernatural_intrusion
        markers: flickering_lights, power_surges, static
        function: "medium through which lodge spirits enter mundane world"
        // Lynch: "Scientists don't understand it...there's a certain point
        //         where they say, 'We don't know why that happens.'"
    }

    FIRE {
        meaning: transformation / destruction / spiritual_power
        function: FWWM = "Fire Walk With Me" (invocation)
        deployment: burning cabin, match strikes, industrial flames
    }

    COFFEE {
        meaning: grounding / ritual / surface_innocence
        function: connection_to_normal_world
        deployment: "damn fine coffee" as incantation of normalcy
        // Ritual against darkness
    }

    CHEVRON_FLOOR {
        meaning: spiritual_portal / altered_space
        origin: Jean Cocteau's Orphee (underworld passage)
        deployment: Red Room, Henry's apartment (Eraserhead)
    }

    INDUSTRIAL_MACHINERY {
        meaning: unconscious_forces / body_horror / generation
        deployment: Eraserhead factory, radiator, mechanisms
        // Lynch: "I like thirties and forties electricity...smokestack
        //         industry...fire...smoke...the noise"
    }

    DINER / ROADHOUSE {
        meaning: threshold_between_worlds
        function: ordinary_space_as_portal
        deployment: Double R, Winkie's (MD), Roadhouse (TP)
    }
}

ALGORITHM deploy_symbol(symbol, context):

    meaning = SYMBOL_LEXICON[symbol].meaning

    // Symbols accrue meaning across works
    IF viewer.previous_lynch_exposure:
        resonance = AMPLIFIED
        meaning = meaning + accumulated_associations

    // Symbols operate subconsciously
    viewer.conscious_understanding = NOT_REQUIRED
    viewer.felt_meaning = TRUE

    RETURN symbol.deployed_with(meaning)
```

---

## IV. THEORETICAL CORRESPONDENCES

### 4.1 TARKOVSKY MAPPING: DREAM AND MEMORY

Both Lynch and Tarkovsky explore dream/memory space, but with distinct approaches.

```
LYNCH_TARKOVSKY_CORRESPONDENCE {

    SHARED_PRINCIPLES {

        dream_as_valid_reality:
            TARKOVSKY: dreams/memories as alternative spatio-temporal patterns
            LYNCH: dream logic as narrative grammar
            SHARED: dreams are not "less real"

        non_linear_time:
            TARKOVSKY: past-present-future simultaneous
            LYNCH: 25 years later = now (Red Room)
            SHARED: temporal collapse as meaning-structure

        actor_multiplicity:
            TARKOVSKY: same actor for mother and wife (Mirror)
            LYNCH: same actor for split selves (MD, LH)
            FUNCTION: tap into subjectivity of dream/memory

        image_as_thought:
            TARKOVSKY: "the image we see is no longer just a barn on fire—
                        we see instead a reflection of our own dream images"
            LYNCH: films as "moving portraits captured on celluloid"
            SHARED: cinema as thought-externalization
    }

    DIVERGENCES {

        TARKOVSKY_EMPHASIS: memory_and_time
            // Personal/historical memory
            // Time as sculptural medium
            // Nostalgia, childhood, Russia
            // Spiritual/religious overtones

        LYNCH_EMPHASIS: dream_and_unconscious
            // Collective/personal unconscious
            // Nightmare as valid as dream
            // American mythology/suburbia
            // Surrealist/Freudian overtones

        TEMPO:
            TARKOVSKY: prolonged_gaze, contemplative_stillness
            LYNCH: juxtaposition, rhythm, rupture

        MOOD:
            TARKOVSKY: melancholy, elegy, spiritual_yearning
            LYNCH: dread, uncanny, beauty_in_horror
    }
}

SYNTHESIS_FUNCTION compare_approaches():

    // Both create "living reality" that involves viewer
    // Both use cinema to access subtler consciousness realms
    // Both reject conventional narrative logic

    TARKOVSKY: time_sculpting_approach {
        method: hold_shot_until_image_transforms
        viewer_state: contemplation -> hypnosis -> revelation
        memory: personal/collective merge
    }

    LYNCH: dream_architecture_approach {
        method: juxtapose_until_meaning_emerges
        viewer_state: disorientation -> feeling -> understanding
        dream: personal/collective merge
    }

    CONVERGENCE_POINT:
        "Their cinematic artworks...are the living reality that involves
         the viewer in itself. It is the reality that comes from the
         dreamscape, a subtler and deeper and wider reality which is
         impregnated with awareness."
```

### 4.2 SURREALIST CINEMA TRADITION

```
SURREALIST_LINEAGE {

    HISTORICAL_CONTEXT {
        // Lynch hosted 1987 BBC Arena on surrealist cinema
        // Called it "automatic cinema" or "cinepoetry"

        ORIGIN: Breton, Dali, Bunuel (1920s-30s)
        PRINCIPLE: access_unconscious, reject_rationality
        METHOD: automatic_creation, dream_transcription
    }

    BUNUEL_LYNCH_CORRESPONDENCE {

        // Un Chien Andalou (1929) -> Blue Velvet (1986)
        // Hand spawning ants -> severed ear with ants
        DIRECT_INFLUENCE: acknowledged

        SHARED_METHODS:
            - symbolic_literalization (eye-slicing / ear-cutting)
            - dream_logic_narrative
            - bourgeois_critique_through_surreality
            - sexuality_and_violence_fused

        DIVERGENCE:
            BUNUEL: intellectual_provocation, political_militancy
            LYNCH: intuitive_exploration, spiritual_quest
    }

    LYNCH_AS_SURREALIST_EVOLUTION {

        // Lynch accesses unconscious through TM, not automatic writing
        // Same destination, different vehicle

        CLASSIC_SURREALIST_METHOD:
            technique: automatic_writing, dream_journals
            goal: bypass_conscious_control

        LYNCH_METHOD:
            technique: transcendental_meditation
            goal: "dive deep" to "catch ideas"

        BOTH_ACHIEVE:
            access_to_unconscious_material
            rejection_of_rational_narrative
            symbolic_density
            dream_as_structure
    }
}
```

---

## V. IMPLEMENTATION PROTOCOLS

### 5.1 Creating a Lynchian Narrative

```
PROTOCOL lynch_narrative_construction():

    STEP_1: Catch the Idea
        // Meditative practice or equivalent
        // Wait for idea to arrive complete
        // Note the FEELING of the idea
        target_feeling = capture(idea.feeling)

    STEP_2: Build Mood Architecture
        // Before plot, establish atmosphere
        soundscape = design_for(target_feeling)
        visual_palette = design_for(target_feeling)

    STEP_3: Allow Dream Logic
        // Disable conventional causality
        causality_type = EMOTIONAL not LOGICAL
        time_structure = NON_LINEAR

    STEP_4: Introduce Doubles
        IF trauma OR desire_split:
            create_double(protagonist, SPLIT_SELF)
        IF obsession_object:
            create_double(object, MIRROR_DOUBLE)

    STEP_5: Deploy Symbolic Vocabulary
        symbols = SELECT_FROM(LYNCH_SYMBOL_LEXICON)
        recurrence_pattern = ESTABLISH(symbols)

    STEP_6: Create Tonal Ruptures
        juxtapose(horror, beauty)
        juxtapose(innocence, corruption)
        MAINTAIN(sincerity) in both

    STEP_7: Preserve Mystery
        explanation_level = MINIMAL
        interpretation_space = MAXIMAL
        // Keep secrets even from yourself

    STEP_8: Test Against Original Feeling
        IF narrative.feeling == target_feeling:
            ACCEPT
        ELSE:
            REVISE until match

    RETURN completed_narrative
```

### 5.2 The Feel-Think Navigation

```
ALGORITHM feel_think_navigation(creative_decision):

    // Lynch: "It's an intuition: You feel-think your way through"

    FOR each decision_point:

        options = generate_possibilities()

        FOR each option IN options:
            feeling = EVALUATE_INTUITIVELY(option)

            IF feeling == "correct":
                // Not logical proof, felt rightness
                SELECT option
                BREAK

        // If nothing feels right, wait
        IF nothing_selected:
            WAIT for right_feeling
            DO_NOT force_decision

    // The idea is always talking
    // Listen for what it wants

    RETURN navigated_path
```

---

## VI. SIGNATURE PATTERNS

### The Lynch Pattern Library

```
PATTERN_1: The Threshold Moment
    // Ear in grass, curtain pulled back, key turned
    structure: ordinary -> discovery -> entry_to_other_world
    function: narrative_portal

PATTERN_2: The Impossible Phone Call
    // Mystery Man calling from your house
    // Dick Laurent is dead (from yourself)
    structure: communication_that_violates_spacetime
    function: reality_fracture_marker

PATTERN_3: The Performance That Tells Truth
    // Julee Cruise at Roadhouse, Rebekah Del Rio at Club Silencio
    // Lady in the Radiator
    structure: staged_performance_delivers_revelation
    function: truth_through_entertainment

PATTERN_4: The Photograph Evidence
    // Same woman in two places (LH)
    // Photos that shouldn't exist
    structure: photograph_reveals_impossible_truth
    function: reality_break_evidence

PATTERN_5: The Cryptic Warning
    // "It is happening again"
    // The owls are not what they seem
    structure: message_understood_too_late
    function: oracle_pattern

PATTERN_6: The Return That Isn't
    // Cooper emerges wrong after 25 years
    // Fred "returns" as Pete
    structure: homecoming_that_fails
    function: permanent_displacement
```

---

## VII. CONCLUSIONS AND CORE INSIGHTS

### The Lynch Paradox
Lynch creates rigorous formal systems for expressing the irrational. His work is not chaos—it is a precise grammar of dream and unconscious translated into cinema.

### Primary Takeaways

1. **Ideas are caught, not made.** The artist's job is fidelity to the original feeling, not construction from parts.

2. **Mood is structural.** Atmosphere is not decoration but the primary narrative content.

3. **Dream logic is logic.** Non-causal connection operates by consistent rules of emotional resonance.

4. **Doubling reveals truth.** Split characters expose what single identity conceals.

5. **Secrets generate power.** Unexplained mystery maintains narrative energy; explanation kills.

6. **Sincerity enables horror.** Lynch's genuine love of light makes his darkness devastating.

7. **Symbols accumulate.** Recurring motifs gain power through repetition across works.

---

## VIII. SOURCES AND REFERENCES

### Primary Sources
- Lynch, David. *Catching the Big Fish: Meditation, Consciousness, and Creativity.* Tarcher, 2006.
- Rodley, Chris. *Lynch on Lynch.* Faber & Faber, 1997/2005.
- Lynch, David and McKenna, Kristine. *Room to Dream.* Random House, 2018.

### Critical Sources
- "Dreaming and the Cinema of David Lynch" - Springer Academic
- "Enchanted by Reality: Tarkovsky and Lynch as Transpersonal Visionaries" - Academia.edu
- BFI Sight & Sound: "Motifs, themes and doubles in David Lynch's world"
- Film School Rejects: "Lynchian Doubles: Mulholland Drive and Lost Highway"
- Criterion Collection: "Lynch on Mulholland Dr."

### Key Quotations Verified

**DL-A0:** "I don't know why people expect art to make sense. They accept the fact that life doesn't make sense."
*— Los Angeles Times, 1989*

**DL-A1:** "The idea is the whole thing. If you stay true to the idea, it tells you everything you need to know."
*— Catching the Big Fish / MasterClass*

**DL-A2:** "My approach to film stems from my art background, as I go beyond the story to the sub-conscious mood created by sound and images."
*— Various interviews*

**DL-A3:** "The magic of the discovery is ruined and the film experience, the secret, is killed."
*— On refusing to explain films*

---

## IX. APPENDIX: COMPARATIVE DREAM LOGIC TABLE

| Principle | Lynch Implementation | Tarkovsky Implementation |
|-----------|---------------------|-------------------------|
| Time | Simultaneous/Looping | Flowing/Sculptural |
| Space | Portals/Thresholds | Zones/Passages |
| Identity | Splitting/Doubling | Merging/Continuity |
| Memory | Fragmented/Bleeding | Flowing/Nostalgic |
| Sound | Industrial/Uncanny | Natural/Sacred |
| Mood | Dread-Wonder | Melancholy-Transcendence |
| Structure | Mobius/Fractured | Non-linear/Poetic |

---

*Document compiled from primary and secondary sources, formalizing the narratological principles of David Lynch's cinema.*

*Generated: 2026-01-25*
