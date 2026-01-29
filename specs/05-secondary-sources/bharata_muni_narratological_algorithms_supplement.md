# Bharata Muni's Narratological Algorithms: Supplement

Extended algorithms for advanced dramatic construction, covering topics not addressed in the primary document. Based on the Manomohan Ghosh translation of the *Natyasastra*.

---

## 12. GhÄá¹­a: The Theory of Blemishes (Failure Modes)

### 12.1 Core Principle

Dramatic success (siddhi) has an inverse: ghÄá¹­a (blemish/failure). Understanding failure modes enables proactive prevention. Bharata categorizes failures by source, severity, and remediability.

### 12.2 Taxonomy of Blemishes

```
GHÄ€á¹¬A (Blemishes) = 4 categories

â”œâ”€â”€ DAIVIKA (From Gods/Fate)
â”‚   â””â”€â”€ External accidents beyond human control
â”‚
â”œâ”€â”€ Ä€TMA-SAMUTTHA (Self-Made)
â”‚   â””â”€â”€ Errors by performers themselves
â”‚
â”œâ”€â”€ PARA (From Enemies)
â”‚   â””â”€â”€ Sabotage by rival groups
â”‚
â””â”€â”€ AUTPÄ€TIKA (From Portents)
    â””â”€â”€ Natural calamities during performance
```

### 12.3 Daivika GhÄá¹­a (Divine/Accidental Blemishes)

```python
DIVINE_BLEMISHES = [
    'strong_wind',           # Disrupts sound, movement
    'fire',                  # Emergency evacuation
    'rain',                  # Open-air performance ruined
    'elephant_fear',         # Animal intrusion
    'serpent_appearance',    # Panic in audience
    'lightning_strike',      # Dangerous interruption
    'ant_invasion',          # Distraction on stage
    'insect_swarm',          # Disrupts actors
    'wild_animal_entry'      # Ferocious beast intrusion
]

# These are UNPREVENTABLE but some are IGNORABLE
def assess_divine_blemish(blemish_type):
    """
    Not all divine blemishes require stopping performance.
    """
    IGNORABLE = ['ant_invasion', 'minor_animal_appearance']
    CATASTROPHIC = ['fire', 'lightning', 'earthquake']
    
    if blemish_type in CATASTROPHIC:
        return 'halt_immediately'
    elif blemish_type in IGNORABLE:
        return 'continue_with_adaptation'
    else:
        return 'director_discretion'
```

### 12.4 Ä€tma-Samuttha GhÄá¹­a (Self-Made Blemishes)

The most preventable categoryâ€”errors arising from the performers themselves.

```python
SELF_MADE_BLEMISHES = {
    # Acting errors
    'unnaturalness': {
        'description': 'Acting that breaks believability',
        'severity': 'high',
        'remedy': 'rehearsal, directorial correction'
    },
    'wrong_movement': {
        'description': 'Gestures inappropriate to sentiment/character',
        'severity': 'medium',
        'remedy': 'practice, memorization of abhinaya'
    },
    'role_unsuitability': {
        'description': 'Actor miscast for the part (vibhÅ«mikatva)',
        'severity': 'high',
        'remedy': 'proper casting, role reassignment'
    },
    'memory_loss': {
        'description': 'Forgetting lines or blocking',
        'severity': 'high',
        'remedy': 'prompting system, over-rehearsal'
    },
    'wrong_words': {
        'description': 'Speaking words not in the script (anyavacana)',
        'severity': 'medium',
        'remedy': 'strict memorization'
    },
    'distress_cry': {
        'description': 'Actor breaking character in pain/discomfort',
        'severity': 'high',
        'remedy': 'physical preparation, safety measures'
    },
    'poor_hand_work': {
        'description': 'Incorrect hand gestures (vihastatva)',
        'severity': 'medium',
        'remedy': 'hasta practice'
    },
    'crown_falling': {
        'description': 'Ornaments/costume pieces dropping',
        'severity': 'low-medium',
        'remedy': 'secure costume design'
    },
    'drum_defects': {
        'description': 'Poor percussion (puá¹£karadoá¹£a)',
        'severity': 'medium',
        'remedy': 'musician rehearsal, instrument maintenance'
    },
    'speech_shyness': {
        'description': 'Timid or unclear speech (vÄgbhÄ«ti)',
        'severity': 'high',
        'remedy': 'voice training, confidence building'
    },
    'excessive_laughing': {
        'description': 'Breaking character with inappropriate laughter',
        'severity': 'medium',
        'remedy': 'emotional discipline'
    },
    'excessive_crying': {
        'description': 'Overacting emotional states',
        'severity': 'medium',
        'remedy': 'emotional calibration'
    }
}

def diagnose_self_made_blemish(performance):
    """
    Identify self-made blemishes in a performance.
    """
    detected = []
    for blemish, config in SELF_MADE_BLEMISHES.items():
        if performance.exhibits(blemish):
            detected.append({
                'type': blemish,
                'severity': config['severity'],
                'remedy': config['remedy']
            })
    return sorted(detected, key=lambda x: 
        {'high': 0, 'medium': 1, 'low': 2}[x['severity']])
```

### 12.5 Para GhÄá¹­a (Enemy-Created Blemishes)

Sabotage by rival theatrical groups or hostile audience members.

```python
ENEMY_BLEMISHES = {
    'screaming': 'Deliberate noise to drown performance',
    'buzzing': 'Coordinated distracting sounds (visphoá¹­ita)',
    'noisy_clapping': 'Disruptive applause at wrong moments',
    'throwing_cowdung': 'Physical disruption with projectiles',
    'throwing_clods': 'Earth/mud thrown at performers',
    'throwing_grass': 'Debris thrown onto stage',
    'throwing_stones': 'Dangerous projectile attacks'
}

ENEMY_MOTIVATIONS = [
    'jealousy',           # Rival troupe's envy
    'hostility',          # Personal grudge
    'partisanship',       # Loyalty to rival group
    'bribery'             # Paid sabotage (arthabheda)
]

# NOTE: The Natyasastra observes that such tactics
# "sometimes occur also now-a-days in meetings supporting
# candidates from rival political parties. Human psychology
# has not much changed..."
```

### 12.6 Blemish Severity Grades

```python
SEVERITY_GRADES = {
    'minor': {
        'examples': ['crown_falling', 'minor_animal_appearance'],
        'action': 'ignore_and_continue',
        'impact_on_siddhi': 'reduces_applause'
    },
    'moderate': {
        'examples': ['speech_shyness', 'drum_defects'],
        'action': 'adapt_and_continue',
        'impact_on_siddhi': 'spoils_success_wholly'
    },
    'severe': {
        'examples': ['fire', 'earthquake', 'actor_injury'],
        'action': 'halt_performance',
        'impact_on_siddhi': 'complete_failure'
    }
}

def grade_blemish(blemish):
    """
    Determine appropriate response to a blemish.
    """
    if blemish in ['fire', 'earthquake', 'lightning']:
        return 'severe'
    elif blemish in ['speech_shyness', 'drum_defects', 'memory_loss']:
        return 'moderate'
    else:
        return 'minor'
```

---

## 13. Temporal Constraints: Time Rules for Dramatic Composition

### 13.1 The Single-Day Rule for Acts

```
AXIOM: Each Act must contain only incidents that could occur
       within the course of a SINGLE DAY.

COROLLARY: Nothing in an Act may interrupt routine duties
           such as prayers or meals (these imply day-passage).
```

### 13.2 Inter-Act Duration Limits

```python
INTER_ACT_TIME_RULES = {
    'minimum': 'immediate_continuation',  # Same day possible
    'maximum': 'one_year',                # Never more than a year
    'indication_method': 'praveÅ›aka',     # Introductory Scene
    
    'RULE': """
        The lapse of time between two Acts, which might be
        a month or a year (but never more than a year) is
        to be indicated by an Introductory Scene (praveÅ›aka)
        preceding the last one.
    """
}

def validate_temporal_structure(drama):
    """
    Check temporal constraints across all acts.
    """
    for i, act in enumerate(drama.acts):
        # Check single-day rule
        if act.implied_duration > ONE_DAY:
            raise TemporalViolation(
                f"Act {i+1} exceeds single-day limit"
            )
        
        # Check inter-act gap
        if i > 0:
            gap = drama.time_between(act, drama.acts[i-1])
            if gap > ONE_YEAR:
                raise TemporalViolation(
                    f"Gap between Acts {i} and {i+1} exceeds one year"
                )
            if gap > ONE_DAY and not act.has_pravesaka:
                raise TemporalViolation(
                    f"Act {i+1} needs Introductory Scene for time gap"
                )
    
    return True
```

### 13.3 Single-Act Drama Types

Some dramatic forms are constrained to one act:

```python
SINGLE_ACT_FORMS = {
    'VyÄyoga': {
        'duration': 'events_of_single_day',
        'content': ['battle', 'personal_combat', 'challenge', 'angry_conflict'],
        'hero': 'well_known_character'
    },
    'Utsá¹›á¹£á¹­ikÄá¹…ka': {
        'duration': 'single_day',
        'content': ['pathetic_sentiment', 'women_lament'],
        'hero': 'human'
    },
    'Prahasana': {
        'duration': 'single_day',
        'content': ['comic_sentiment', 'farce', 'satire'],
        'hero': 'varied'
    },
    'BhÄá¹‡a': {
        'duration': 'single_day',
        'content': ['monologue', 'rogue_adventure'],
        'hero': 'single_actor'
    },
    'VÄ«thÄ«': {
        'duration': 'single_day',
        'content': ['short_dramatic_sketch'],
        'hero': 'one_or_two_actors'
    }
}
```

---

## 14. PÅ«rvaraá¹…ga: The Preliminaries Protocol

### 14.1 Core Principle

Every performance begins with PÅ«rvaraá¹…ga (Preliminaries)â€”a structured ritual sequence that consecrates the performance space, invokes divine blessing, and prepares the audience for aesthetic experience.

### 14.2 The Nineteen Components

```python
PURVARANGA_SEQUENCE = [
    # Phase 1: Musical Preparation
    ('pratyÄhÄra', 'Musical tuning and preparation'),
    ('avatÄraá¹‡a', 'Descent/entry of performers'),
    ('Ärambha', 'Beginning of instrumental music'),
    ('ÄÅ›ravaá¹‡a', 'Making audience attentive through sound'),
    ('vaktrapÄá¹‡i', 'Hand gestures indicating time-beat'),
    ('parighaá¹­á¹­ana', 'Striking drums in specific pattern'),
    ('saá¹ƒghoá¹­ana', 'Rehearsing hand poses for time-beat'),
    ('mÄrgÄsÄrita', 'Harmonious playing of drums and strings'),
    ('ÄsÄrita', 'Practicing time-fraction beats'),
    
    # Phase 2: Vocal/Ritual
    ('gÄ«tavidhi', 'Application of songs praising gods'),
    ('utthÄpana', 'Raising ceremonyâ€”starts performance proper'),
    ('parivartana', 'Walking-round praising guardian deities'),
    ('nandÄ«', 'Benediction invoking gods, Brahmins, kings'),
    ('Å›uá¹£kÄvaká¹›á¹£á¹­a', 'Dhruva with meaningless sounds for Jarjara'),
    
    # Phase 3: Dramatic Introduction
    ('raá¹…gadvÄra', 'Gateway to performanceâ€”words and gestures begin'),
    ('cÄrÄ«', 'Movements depicting Erotic Sentiment'),
    ('mahÄcÄrÄ«', 'Movements depicting Furious Sentiment'),
    ('trigata', 'Three Men\'s Talkâ€”Director, Assistant, Jester'),
    ('prarocanÄ', 'Laudationâ€”suggesting the play\'s denouement')
]

def execute_purvaranga(performance):
    """
    Execute the Preliminaries in proper sequence.
    """
    for component, description in PURVARANGA_SEQUENCE:
        perform_component(component)
        # Each component must complete before next begins
    
    # After Preliminaries, main play may commence
    return 'ready_for_main_performance'
```

### 14.3 The Benediction (NandÄ«) Algorithm

```python
def compose_nandi():
    """
    The Benediction must include blessings for three entities.
    """
    REQUIRED_BLESSINGS = ['gods', 'brahmins', 'kings']
    
    nandi = Benediction()
    
    for entity in REQUIRED_BLESSINGS:
        nandi.add_blessing(
            target=entity,
            words='holy_auspicious_terms',
            metre='appropriate_to_sentiment'
        )
    
    # The Nandi sets the tone for the entire performance
    # Wrong Benediction is classified as a Blemish
    return nandi
```

### 14.4 The Three Men's Talk (Trigata)

```python
class Trigata:
    """
    Conversational introduction involving three characters.
    """
    
    PARTICIPANTS = {
        'sÅ«tradhÄra': 'Directorâ€”leads the conversation',
        'pÄripÄrÅ›vika': 'Assistantâ€”responds and queries',
        'vidÅ«á¹£aka': 'Jesterâ€”provides comic relief and transitions'
    }
    
    def execute(self, play):
        """
        The Trigata introduces the play through dialogue.
        """
        # Director enters and establishes context
        self.sutradhara.establish_setting()
        
        # Assistant queries about the play
        self.pariparsvika.ask_about_play()
        
        # Director reveals playwright, plot summary
        self.sutradhara.reveal_play_details(
            playwright=play.author,
            title=play.name,
            subject=play.subject_summary
        )
        
        # Jester provides transition to action
        self.vidusaka.comic_transition()
        
        # Exit Preliminaries, enter main play
        return 'commence_main_action'
```

### 14.5 Preliminaries Types

```python
PRELIMINARIES_TYPES = {
    'Å›uddha': {
        'name': 'Pure Preliminaries',
        'characteristics': 'Full 19-component sequence',
        'use': 'Major dramatic productions'
    },
    'tryasra': {
        'name': 'Triangular Preliminaries',
        'characteristics': 'Abbreviated sequence',
        'use': 'Shorter dramatic forms'
    },
    'miÅ›ra': {
        'name': 'Mixed Preliminaries',
        'characteristics': 'Combined elements from both',
        'use': 'Context-dependent adaptation'
    }
}
```

---

## 15. Rasa Combination Rules

### 15.1 Primary-Derivative Relationships

```python
RASA_DERIVATION = {
    # PRIMARY â†’ DERIVATIVE (with mechanism)
    'Åšá¹›á¹…gÄra': ('HÄsya', 'mimicry'),      # Erotic â†’ Comic
    'Raudra': ('Karuá¹‡a', 'result'),        # Furious â†’ Pathetic
    'VÄ«ra': ('Adbhuta', 'result'),         # Heroic â†’ Marvellous
    'BÄ«bhatsa': ('BhayÄnaka', 'consequence')  # Odious â†’ Terrible
}

# The four PRIMARY rasas generate the four DERIVATIVE rasas
PRIMARY_RASAS = {'Åšá¹›á¹…gÄra', 'Raudra', 'VÄ«ra', 'BÄ«bhatsa'}
DERIVATIVE_RASAS = {'HÄsya', 'Karuá¹‡a', 'Adbhuta', 'BhayÄnaka'}
```

### 15.2 Dominant Rasa Principle

```python
def establish_dominant_rasa(drama):
    """
    Every drama must have ONE dominant sentiment that
    governs the work, though others may appear.
    """
    # The dominant rasa determines:
    # - Overall tone and style (vá¹›tti)
    # - Hero's primary emotional journey
    # - Resolution type
    
    dominant = drama.select_primary_sentiment()
    
    # All other rasas must SERVE the dominant
    for scene in drama.scenes:
        if scene.rasa != dominant:
            assert serves_dominant(scene.rasa, dominant), \
                f"{scene.rasa} must support {dominant}"
    
    return dominant
```

### 15.3 Transitory State Compatibility

```python
# Not all vyabhicÄris work with all rasas
VYABHICARI_EXCLUSIONS = {
    'erotic_union': {
        'exclude': ['fear', 'indolence', 'cruelty', 'disgust'],
        'reason': 'These destroy the mood of love-in-union'
    },
    'comic': {
        'compatible': ['indolence', 'dissimulation', 'drowsiness', 
                      'sleep', 'dreaming', 'insomnia', 'envy'],
        'reason': 'Comic requires specific coloring states'
    }
}

def validate_vyabhicari_selection(rasa, vyabhicaris):
    """
    Check that transitory states are compatible with sentiment.
    """
    if rasa in VYABHICARI_EXCLUSIONS:
        exclusions = VYABHICARI_EXCLUSIONS[rasa].get('exclude', [])
        for v in vyabhicaris:
            if v in exclusions:
                raise IncompatibilityError(
                    f"{v} incompatible with {rasa}"
                )
    return True
```

### 15.4 Scene-Level Rasa Shifts

```python
def manage_rasa_transitions(drama):
    """
    Rasas may shift between scenes but must transition smoothly.
    """
    for i, scene in enumerate(drama.scenes[1:], 1):
        prev_rasa = drama.scenes[i-1].rasa
        curr_rasa = scene.rasa
        
        if prev_rasa != curr_rasa:
            # Transition must be motivated
            assert scene.has_transition_trigger(), \
                "Rasa shift requires narrative motivation"
            
            # Some transitions are more natural than others
            if is_related_rasa(prev_rasa, curr_rasa):
                # Primary â†’ Derivative is smooth
                continue
            else:
                # Unrelated rasas need stronger bridging
                assert scene.has_strong_bridge(), \
                    f"Transition from {prev_rasa} to {curr_rasa} needs bridging"
```

---

## 16. Unity Principles: Structural Coherence Mechanisms

### 16.1 The BÄ«ja (Germ) Continuity Rule

```python
BIJA_RULE = """
The Germ (bÄ«ja) of the play as well as its Prominent Point (bindu)
must relate to EVERY Act of the play. The Hero must either appear
in every Act or be mentioned there.
"""

def validate_bija_continuity(drama):
    """
    The seed planted in Act 1 must connect to all subsequent acts.
    """
    bija = drama.acts[0].germ  # Planted in Opening (Mukha)
    
    for act in drama.acts:
        # Bija must be referenced or advanced
        assert act.references_or_advances(bija), \
            f"Act {act.number} loses connection to the Germ"
        
        # Hero must appear or be mentioned
        assert act.hero_present or act.hero_mentioned, \
            f"Act {act.number} must include Hero presence/reference"
    
    return True
```

### 16.2 The Bindu (Point) Maintenance Rule

```python
class Bindu:
    """
    The Bindu maintains continuity when action seems interrupted.
    It's a narrative device that keeps the thread alive during
    apparent diversions.
    """
    
    def apply(self, scene_sequence):
        """
        Insert bindu elements where continuity might break.
        """
        for i, scene in enumerate(scene_sequence):
            if scene.diverges_from_main_plot():
                # Insert a binduâ€”a reference back to main action
                scene.add_bindu(
                    reference=self.main_plot_element,
                    method='dialogue_mention' or 'visual_callback'
                )
        return scene_sequence
```

### 16.3 Incident Density Control

```python
INCIDENT_DENSITY_RULE = """
An Act must not present TOO MANY incidents.
Subsidiary events that might affect unity of impression
should be REPORTED (in Introductory Scenes) rather than
directly presented.
"""

def control_incident_density(act):
    """
    Ensure act doesn't overload with incidents.
    """
    MAX_MAIN_INCIDENTS = 3  # Guideline, not strict rule
    
    main_incidents = [i for i in act.incidents if i.is_main]
    subsidiary = [i for i in act.incidents if not i.is_main]
    
    if len(main_incidents) > MAX_MAIN_INCIDENTS:
        # Too manyâ€”consider redistribution
        return 'redistribute_to_other_acts'
    
    for sub in subsidiary:
        if sub.would_break_unity():
            # Move to Introductory Scene as report
            sub.convert_to_pravesaka_report()
    
    return act
```

### 16.4 The Pravesaka (Introductory Scene) Device

```python
class Pravesaka:
    """
    Introductory Scene placed before an Act to:
    1. Indicate time passage between acts
    2. Report subsidiary events that can't be shown
    3. Clarify complex plot points
    4. Maintain unity by summarizing rather than showing
    """
    
    FUNCTIONS = [
        'time_passage_indication',   # "A year has passed..."
        'off_stage_event_report',    # "Meanwhile, the battle occurred..."
        'clarification',             # "What the hero meant was..."
        'subsidiary_plot_summary'    # "While we follow X, Y has been..."
    ]
    
    def compose(self, preceding_act, following_act, events_to_report):
        """
        Create an Introductory Scene bridging two acts.
        """
        pravesaka = Scene(type='introductory')
        
        # Indicate time gap if any
        time_gap = following_act.time - preceding_act.time
        if time_gap > ONE_DAY:
            pravesaka.add_time_indication(time_gap)
        
        # Report events that shouldn't be staged
        for event in events_to_report:
            if event in PROHIBITED_REPRESENTATIONS:
                pravesaka.add_report(event)
        
        return pravesaka
```

---

## 17. Language and Dialect Rules

### 17.1 Character-Language Mapping

```python
LANGUAGE_RULES = {
    'sanskrit': {
        'speakers': ['kings', 'brahmins', 'sages', 'gods', 'ministers'],
        'register': 'elevated',
        'context': 'formal_discourse, philosophical_discussion'
    },
    'prakrit': {
        'speakers': ['women', 'children', 'common_people'],
        'variants': {
            'Å›aurasenÄ«': 'women_of_rank',
            'mÄgadhÄ«': 'servants',
            'ardhamÄgadhÄ«': 'merchants',
            'avantÄ«': 'rogues_and_gamblers'
        },
        'register': 'colloquial'
    }
}

def assign_language(character):
    """
    Determine appropriate language for a character.
    """
    if character.type in ['king', 'brahmin', 'sage', 'god', 'minister']:
        return 'sanskrit'
    elif character.type == 'woman':
        if character.rank == 'high':
            return ('prakrit', 'Å›aurasenÄ«')
        else:
            return ('prakrit', 'general')
    elif character.type == 'servant':
        return ('prakrit', 'mÄgadhÄ«')
    # ... and so on
```

### 17.2 Diction Quality Marks

```python
DICTION_QUALITIES = {
    # Positive marks (guá¹‡a)
    'clarity': 'Words must be intelligible',
    'euphony': 'Sounds must be agreeable and soft',
    'appropriateness': 'Language matches character status',
    'accessibility': 'Intelligible to country people',
    'recitability': 'Feminine speech uses words women can recite',
    
    # Negative marks (doá¹£a)
    'circumlocution': 'Unnecessary wordiness',
    'superfluous_expression': 'Redundant phrasing',
    'want_of_significance': 'Empty words',
    'logical_defect': 'Internal contradiction',
    'metrical_defect': 'Verse that doesn\'t scan',
    'hiatus': 'Unpleasant vowel collision',
    'slang': 'Inappropriate colloquialism for context'
}
```

---

## 18. Supplementary Diagnostic Questions

### 18.1 Blemish Prevention Checklist

| Question | Purpose |
|----------|---------|
| "Are all actors properly cast for their roles?" | Prevent vibhÅ«mikatva |
| "Have actors memorized completely?" | Prevent memory loss errors |
| "Are costumes/props secured?" | Prevent physical blemishes |
| "Have musicians rehearsed adequately?" | Prevent puá¹£karadoá¹£a |
| "Is the performance space protected from intrusion?" | Prevent divine/enemy blemishes |

### 18.2 Temporal Structure Checklist

| Question | Purpose |
|----------|---------|
| "Does each act stay within single-day bounds?" | Validate act duration |
| "Are inter-act gaps under one year?" | Validate structural limits |
| "Are time gaps indicated by PraveÅ›aka?" | Verify continuity devices |
| "Does the hero appear or get mentioned in every act?" | Check bÄ«ja continuity |

### 18.3 Unity Verification Checklist

| Question | Purpose |
|----------|---------|
| "Does the Germ (bÄ«ja) connect all acts?" | Verify plot coherence |
| "Are subsidiary events reported rather than shown when appropriate?" | Check incident density |
| "Do all rasas serve the dominant sentiment?" | Validate emotional unity |
| "Are transitions between rasas motivated?" | Check emotional flow |

---

## Appendix E: Extended Numerical Reference

| Category | Count | Components |
|----------|-------|------------|
| Blemish Types | 4 | Divine, Self-made, Enemy, Portent |
| Self-Made Blemishes | 12+ | See Section 12.4 |
| PÅ«rvaraá¹…ga Components | 19 | See Section 14.2 |
| Preliminary Types | 3 | Pure, Triangular, Mixed |
| Primary Rasas | 4 | Åšá¹›á¹…gÄra, Raudra, VÄ«ra, BÄ«bhatsa |
| Derivative Rasas | 4 | HÄsya, Karuá¹‡a, Adbhuta, BhayÄnaka |
| Diction Qualities | 10+ | Positive and negative marks |
| Single-Act Forms | 5 | VyÄyoga, Utsá¹›á¹£á¹­ikÄá¹…ka, Prahasana, BhÄá¹‡a, VÄ«thÄ« |

---

## Appendix F: Extended Glossary

| Term | Sanskrit | Meaning |
|------|----------|---------|
| GhÄá¹­a | à¤˜à¤¾à¤Ÿ | Blemish, failure, defect in production |
| Daivika | à¤¦à¥ˆà¤µà¤¿à¤• | Divine, relating to fate/gods |
| Ä€tma-samuttha | à¤†à¤¤à¥à¤®à¤¸à¤®à¥à¤¤à¥à¤¥ | Self-arising, self-made |
| Para | à¤ªà¤° | Enemy, other, rival |
| AutpÄtika | à¤”à¤¤à¥à¤ªà¤¾à¤¤à¤¿à¤• | Relating to portents/omens |
| PÅ«rvaraá¹…ga | à¤ªà¥‚à¤°à¥à¤µà¤°à¤™à¥à¤— | Preliminaries, pre-performance ritual |
| NandÄ« | à¤¨à¤¨à¥à¤¦à¥€ | Benediction, auspicious opening |
| Trigata | à¤¤à¥à¤°à¤¿à¤—à¤¤ | Three Men's Talk |
| PrarocanÄ | à¤ªà¥à¤°à¤°à¥‹à¤šà¤¨à¤¾ | Laudation, introduction of play |
| PraveÅ›aka | à¤ªà¥à¤°à¤µà¥‡à¤¶à¤• | Introductory Scene |
| BÄ«ja | à¤¬à¥€à¤œ | Germ, seed of plot |
| Bindu | à¤¬à¤¿à¤¨à¥à¤¦à¥ | Point, continuity device |
| VibhÅ«mikatva | à¤µà¤¿à¤­à¥‚à¤®à¤¿à¤•à¤¤à¥à¤µ | Role unsuitability, miscasting |
| Puá¹£karadoá¹£a | à¤ªà¥à¤·à¥à¤•à¤°à¤¦à¥‹à¤· | Defect in drumming |
| VÄgbhÄ«ti | à¤µà¤¾à¤—à¥à¤­à¥€à¤¤à¤¿ | Speech shyness, timidity |

---

*This supplement extends the primary Bharata Muni Narratological Algorithms document. Together they provide a comprehensive algorithmic framework for classical Indian dramatic theory.*

*Compiled from Bharata Muni. Natyasastra: A Treatise on Hindu Dramaturgy and Histrionics. Translated by Manomohan Ghosh. Calcutta: Asiatic Society of Bengal, 1950.*
