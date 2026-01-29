# Bharata Muni's Narratological Algorithms: Extended Protocols

Tertiary document completing the algorithmic distillation of the *Natyasastra*. Covers performance-integrated narrative systems: musical cues, spatial grammar, movement algorithms, special representations, and structural prohibitions.

---

## 19. Dhruva: Musical-Narrative Cue System

### 19.1 Core Principle

Dhruvas are songs that function as structural punctuation in dramatic narrative. They signal entrances, exits, emotional transitions, and scene changesâ€”serving as the audio architecture of plot progression.

```
AXIOM: Music is not decorative but STRUCTURAL.
       Dhruvas mark narrative beats as reliably as
       chapter breaks mark textual divisions.
```

### 19.2 The Five Dhruva Types

```python
DHRUVA_TYPES = {
    'prÄveÅ›ikÄ«': {
        'function': 'ENTRANCE',
        'trigger': 'Character entering stage',
        'narrative_signal': 'New agent enters the action',
        'placement': 'Begins as curtain draws, continues until character established'
    },
    'Äká¹£epikÄ«': {
        'function': 'CASUAL/INCIDENTAL',
        'trigger': 'Transitional moments, minor actions',
        'narrative_signal': 'Subordinate action or emotional coloring',
        'placement': 'During transitional business'
    },
    'niá¹£krÄmikÄ«': {
        'function': 'EXIT',
        'trigger': 'Character leaving stage',
        'narrative_signal': 'Agent withdraws from current action',
        'placement': 'Accompanies departure movement'
    },
    'prÄsÄdikÄ«': {
        'function': 'PLEASING/PACIFYING',
        'trigger': 'Resolution moments, reconciliation',
        'narrative_signal': 'Tension release, harmony restored',
        'placement': 'During emotional resolution sequences'
    },
    'ÄntarÄ': {
        'function': 'INTERMEDIATE/INTERVAL',
        'trigger': 'Between major segments',
        'narrative_signal': 'Structural pause, scene division',
        'placement': 'Bridging distinct dramatic units'
    }
}
```

### 19.3 Dhruva-Narrative Synchronization Algorithm

```python
def select_dhruva(narrative_event):
    """
    Match the appropriate dhruva type to narrative moment.
    """
    if narrative_event.type == 'character_entrance':
        return DhruvaType.PRAVESIKI
    elif narrative_event.type == 'character_exit':
        return DhruvaType.NISKRAMIKI
    elif narrative_event.type == 'emotional_resolution':
        return DhruvaType.PRASADIKI
    elif narrative_event.type == 'scene_transition':
        return DhruvaType.ANTARA
    else:
        return DhruvaType.AKSEPIKI  # Default for incidental moments

def synchronize_dhruva_to_action(dhruva, stage_action):
    """
    Dhruva must align precisely with stage movement.
    """
    # Entrance dhruva begins with curtain movement
    if dhruva.type == 'pravesiki':
        dhruva.start_on('curtain_draw')
        dhruva.end_on('character_established_in_space')
    
    # Exit dhruva accompanies departure
    elif dhruva.type == 'niskramiki':
        dhruva.start_on('departure_intention_shown')
        dhruva.end_on('character_exits_view')
    
    return dhruva
```

### 19.4 Dhruva-Rasa Correspondence

```python
DHRUVA_RASA_MAPPING = {
    # Each rasa has characteristic musical qualities for its dhruvas
    'Åšá¹›á¹…gÄra': {
        'tempo': 'medium',
        'quality': 'sweet, graceful',
        'entrance_style': 'languid, anticipatory'
    },
    'VÄ«ra': {
        'tempo': 'quick',
        'quality': 'bold, energetic',
        'entrance_style': 'martial, decisive'
    },
    'Karuá¹‡a': {
        'tempo': 'slow',
        'quality': 'plaintive, heavy',
        'entrance_style': 'weighted, sorrowful'
    },
    'Raudra': {
        'tempo': 'quick',
        'quality': 'harsh, intense',
        'entrance_style': 'aggressive, turbulent'
    },
    'HÄsya': {
        'tempo': 'varied',
        'quality': 'light, playful',
        'entrance_style': 'bouncing, comic'
    },
    'BhayÄnaka': {
        'tempo': 'irregular',
        'quality': 'ominous, tense',
        'entrance_style': 'creeping, unsettling'
    },
    'BÄ«bhatsa': {
        'tempo': 'slow',
        'quality': 'discordant, heavy',
        'entrance_style': 'reluctant, repulsed'
    },
    'Adbhuta': {
        'tempo': 'building',
        'quality': 'expansive, surprising',
        'entrance_style': 'revelatory, ascending'
    }
}
```

---

## 20. Kaká¹£yÄvibhÄga: Stage Zone Grammar

### 20.1 Core Principle

The stage is not neutral space but a semantic field. Location on stage signifies narrative location in the story world. Movement across the stage represents travel through dramatic geography.

```
AXIOM: Space is symbolic. A few steps on stage can
       represent miles in the story world. The actor's
       position MEANS something.
```

### 20.2 Zone Signification System

```python
STAGE_ZONES = {
    'front_center': {
        'signifies': 'immediate_presence',
        'narrative_proximity': 'closest_to_audience',
        'typical_use': 'direct_address, key_revelations'
    },
    'rear': {
        'signifies': 'distance, elsewhere',
        'narrative_proximity': 'removed_from_main_action',
        'typical_use': 'arrivals_from_afar, watching'
    },
    'stage_right': {
        'signifies': 'auspicious_direction',
        'traditional_association': 'entrance_of_noble_characters',
        'typical_use': 'heroes, divine_figures'
    },
    'stage_left': {
        'signifies': 'varied_by_context',
        'traditional_association': 'entrance_of_others',
        'typical_use': 'supporting_characters, servants'
    }
}
```

### 20.3 The Walking-Distance Convention

```python
class DistanceRepresentation:
    """
    Physical walking distance on stage maps to narrative distance.
    """
    
    DISTANCE_MAPPING = {
        'short_walk': {
            'steps': 'few',
            'signifies': 'nearby_location',
            'example': 'moving_to_adjacent_room'
        },
        'medium_walk': {
            'steps': 'moderate',
            'signifies': 'medium_distance',
            'example': 'going_to_another_part_of_city'
        },
        'long_walk': {
            'steps': 'extended_circuit',
            'signifies': 'great_distance',
            'example': 'journey_to_another_kingdom'
        }
    }
    
    def represent_travel(self, narrative_distance):
        """
        A few steps can represent any distanceâ€”
        the QUALITY of movement signals the scale.
        """
        if narrative_distance == 'nearby':
            return self.short_walk()
        elif narrative_distance == 'medium':
            return self.medium_walk_with_scene_indication()
        elif narrative_distance == 'far':
            return self.extended_walk_with_travel_markers()
```

### 20.4 Zone Change Protocol

```python
def change_zone(actor, from_location, to_location, narrative_distance):
    """
    Zone change = location change in story world.
    The walk itself represents the journey.
    """
    # Start from current position
    actor.mark_departure(from_location)
    
    # Walk represents travel
    if narrative_distance == 'nearby':
        actor.walk(steps='few', tempo='normal')
    elif narrative_distance == 'medium':
        actor.walk(steps='moderate', tempo='measured')
        # May include travel indicators (wiping brow, adjusting garments)
    elif narrative_distance == 'far':
        actor.walk(steps='extended')
        actor.show_fatigue_markers()
        # Walking around stage represents long journey
    
    # Arrival at new location
    actor.establish_in_new_zone(to_location)
    
    return actor.current_zone
```

### 20.5 Symbolic Token Convention

```python
CONVEYANCE_TOKENS = {
    # Physical objects that signify vehicles without requiring them
    'elephant': 'goad (aá¹…kuÅ›a)',
    'horse': 'bit or bridle',
    'chariot': 'whip',
    'boat': 'oar gesture',
    'celestial_vehicle': 'upward gaze + floating movement'
}

# The Natyasastra asks rhetorically:
# "Will the actors have to die when the character
#  is said to be dead?" â€” signification replaces literalism
```

---

## 21. Gati: The Gait Algorithm System

### 21.1 Core Principle

Gait (gati) is not merely walking but characterization through movement. Character type, emotional state, and narrative situation all manifest in how a figure moves across the stage.

```
AXIOM: Movement reveals character. Before a word is spoken,
       the audience should know who approaches by HOW
       they approach.
```

### 21.2 Character-Type Gait Parameters

```python
GAIT_BY_CHARACTER_TYPE = {
    'superior': {
        'step_width': '4 tÄlas',
        'step_duration': '4 kalÄs',
        'posture': 'Vaiá¹£á¹‡ava sthÄna',
        'qualities': ['dignified', 'measured', 'unhurried'],
        'includes': ['gods', 'kings', 'sages']
    },
    'middling': {
        'step_width': '2 tÄlas',
        'step_duration': '2 kalÄs',
        'posture': 'natural',
        'qualities': ['balanced', 'purposeful'],
        'includes': ['ministers', 'merchants', 'citizens']
    },
    'inferior': {
        'step_width': '1 tÄla',
        'step_duration': '1 kalÄ',
        'posture': 'varied',
        'qualities': ['quick', 'practical'],
        'includes': ['servants', 'common people']
    },
    'women': {
        'step_width': '1 tÄla',
        'step_duration': 'graceful timing',
        'posture': 'Ä€yata or Avahittha',
        'qualities': ['delicate', 'graceful', 'lalita'],
        'movement': 'hands follow feet gently'
    }
}

def calculate_gait(character):
    """
    Determine base gait parameters from character type.
    """
    type_params = GAIT_BY_CHARACTER_TYPE[character.type]
    
    return Gait(
        step_width=type_params['step_width'],
        step_duration=type_params['step_duration'],
        posture=type_params['posture'],
        qualities=type_params['qualities']
    )
```

### 21.3 Emotional State Gait Modifiers

```python
GAIT_BY_EMOTIONAL_STATE = {
    # States that SLOW the gait (more than 4 kalÄs)
    'slow_states': {
        'fever': {'tempo': 'very_slow', 'qualities': ['weak', 'unsteady']},
        'hunger': {'tempo': 'slow', 'qualities': ['depleted', 'trembling']},
        'fatigue': {'tempo': 'slow', 'qualities': ['heavy', 'dragging']},
        'sorrow': {'tempo': 'slow', 'qualities': ['drooping', 'weighted']},
        'dissimulation': {'tempo': 'slow', 'qualities': ['cautious', 'measured']},
        'love_in_separation': {'tempo': 'slow', 'qualities': ['languid', 'distracted']}
    },
    
    # States that QUICKEN the gait (2 kalÄs or less)
    'quick_states': {
        'anxiety': {'tempo': 'quick', 'qualities': ['nervous', 'darting']},
        'panic': {'tempo': 'very_quick', 'qualities': ['frantic', 'uncontrolled']},
        'joy': {'tempo': 'quick', 'qualities': ['bouncing', 'energetic']},
        'anger': {'tempo': 'quick', 'qualities': ['forceful', 'aggressive']},
        'pursuit': {'tempo': 'very_quick', 'qualities': ['focused', 'relentless']},
        'concealed_love': {'tempo': 'quick', 'qualities': ['furtive', 'eager']}
    }
}

def modify_gait_for_state(base_gait, emotional_state):
    """
    Emotional state modifies the base character gait.
    """
    if emotional_state in GAIT_BY_EMOTIONAL_STATE['slow_states']:
        modifier = GAIT_BY_EMOTIONAL_STATE['slow_states'][emotional_state]
        base_gait.tempo = modifier['tempo']
        base_gait.add_qualities(modifier['qualities'])
        base_gait.duration *= 1.5  # Extend step duration
        
    elif emotional_state in GAIT_BY_EMOTIONAL_STATE['quick_states']:
        modifier = GAIT_BY_EMOTIONAL_STATE['quick_states'][emotional_state]
        base_gait.tempo = modifier['tempo']
        base_gait.add_qualities(modifier['qualities'])
        base_gait.duration *= 0.5  # Shorten step duration
    
    return base_gait
```

### 21.4 Sentiment-Specific Gait Algorithms

```python
GAIT_BY_RASA = {
    'Åšá¹›á¹…gÄra': {
        'ordinary_love': {
            'cÄrÄ«': 'AtikrÄnta',
            'qualities': ['graceful', 'adorned', 'measured'],
            'hands': 'follow feet smoothly'
        },
        'concealed_love': {
            'movement': 'dismisses servants, walks alone',
            'qualities': ['cautious', 'eager', 'looking around']
        }
    },
    'VÄ«ra': {
        'gait': 'bold, martial',
        'qualities': ['forceful steps', 'chest raised', 'arms active'],
        'cÄrÄ«': 'varies with weapon'
    },
    'Raudra': {
        'gait': 'aggressive',
        'qualities': ['stamping', 'quick', 'threatening'],
        'tempo': 'quick to very quick'
    },
    'Karuá¹‡a': {
        'gait': 'slow tempo',
        'qualities': ['eyes tearful', 'limbs drooping', 'arms thrown up and down'],
        'special': 'feet not raised high, body bent in dejection'
    },
    'BhayÄnaka': {
        'gait': 'Eá¸akakrÄ«á¸ita CÄrÄ«',
        'qualities': ['trembling', 'eyes wide and moving', 'quick steps'],
        'special': 'feet sometimes close, sometimes distant, hands follow'
    },
    'HÄsya': {
        'gait': 'swift short steps',
        'qualities': ['bouncing', 'varied direction'],
        'character_types': 'middling and inferior primarily'
    },
    'Adbhuta': {
        'gait': 'swift short steps in all directions',
        'qualities': ['sudden changes', 'expansive gestures']
    }
}
```

### 21.5 Special Condition Gaits

```python
SPECIAL_GAITS = {
    'darkness_or_blindness': {
        'feet': 'drawn over ground (not lifted)',
        'hands': 'groping for the way',
        'quality': 'tentative, searching'
    },
    'riding_chariot': {
        'posture': 'SamapÄda SthÄna',
        'hands': 'one holds bow, other holds pole',
        'quality': 'mimicry of being carried',
        'entry': 'quick simple steps'
    },
    'riding_horse': {
        'posture': 'VaiÅ›Äkha SthÄna',
        'steps': 'simple, various kinds',
        'token': 'holding bit/bridle'
    },
    'swimming': {
        'shallow_water': 'tucking up clothes',
        'deep_water': 'throwing out hands, body bent forward',
        'carried_by_current': 'arms stretch alternately, mouth fills'
    },
    'intoxication_light': {
        'quality': 'reeling',
        'feet': 'sometimes going backwards'
    },
    'intoxication_heavy': {
        'quality': 'staggering',
        'feet': 'unsteady',
        'body': 'reeling'
    },
    'lunacy': {
        'steps': 'irregular',
        'quality': 'imitates various types of men',
        'behavior': 'talks without reason, sings, laughs, dances randomly'
    },
    'old_age': {
        'body': 'trembling',
        'feet': 'raised slowly',
        'breathing': 'takes breath with each step'
    },
    'corpulence': {
        'feet': 'raised slowly',
        'quality': 'drags body with effort'
    }
}
```

---

## 22. ViÅ›eá¹£Äbhinaya: Special Representation Protocols

### 22.1 Core Principle

Certain narrative elements cannot be shown literally and require conventional representation. These protocols allow the staging of weather, time, death, dreams, and other phenomena through codified physical and vocal techniques.

### 22.2 Season Representation Algorithm

```python
SEASON_REPRESENTATION = {
    'Å›arad_autumn': {
        'behavioral': 'composure of all senses, tranquility',
        'visual': 'view of different flowers',
        'quality': 'serene, balanced'
    },
    'hemanta_early_winter': {
        'superior_middling': 'narrowing limbs, seeking sun/fire/warm clothing',
        'inferior': 'groaning, clicking, trembling head/lips, chattering teeth'
    },
    'Å›iÅ›ira_winter': {
        'behavioral': 'smelling flowers, drinking wine',
        'environmental': 'pleasant wind indicated'
    },
    'vasanta_spring': {
        'behavioral': 'acts of rejoicing, enjoyments, festivities',
        'visual': 'display of various flowers'
    },
    'grÄ«á¹£ma_summer': {
        'behavioral': 'fans, wiping sweat',
        'environmental': 'heat of earth, hot wind indicated'
    },
    'vará¹£Ä_rainy_season': {
        'visual': 'Kadamba, Nimba, Kutaja flowers; green grass; Indragopa insects',
        'grouping': 'peacocks gathering'
    },
    'rainy_night': {
        'auditory': 'loud sound of clouds',
        'visual': 'falling showers, lightning',
        'environmental': 'thunder indicated'
    }
}

def represent_season(season, character_type):
    """
    Season representation varies by character status.
    """
    season_protocol = SEASON_REPRESENTATION[season]
    
    # Superior characters may indicate discomfort more subtly
    if character_type == 'superior' and 'superior_middling' in season_protocol:
        return season_protocol['superior_middling']
    elif character_type == 'inferior' and 'inferior' in season_protocol:
        return season_protocol['inferior']
    else:
        return season_protocol.get('behavioral', season_protocol)
```

### 22.3 Death Representation Algorithm

```python
DEATH_REPRESENTATION = {
    'general_principle': """
        Death from different conditions requires different representation.
        Sometimes throwing out all hands and feet,
        sometimes paralysis of all limbs.
    """,
    
    'death_from_disease': {
        'vocal': 'hiccough, hard breathing',
        'physical': 'imperceptible movement, relaxed limbs'
    },
    
    'death_from_poison': {
        'physical': 'throwing out hands, feet, limbs',
        'progression': 'quivering action through body parts',
        'eight_stages': [
            ('glÄni', 'general weaknessâ€”sunken eyes, depressed cheeks/lips/belly/shoulder, feeble arms'),
            ('vepathu', 'tremorâ€”shaking head, hands, feet simultaneously or separately'),
            ('dÄha', 'burning sensation'),
            ('hikkÄ', 'hiccough'),
            ('phena', 'froth in mouth'),
            ('grÄ«vÄbhaá¹…ga', 'breaking/bending of neck'),
            ('stambha', 'paralysis/rigidity'),
            ('maraá¹‡a', 'death')
        ]
    },
    
    'dying_speech': {
        'voice': 'indistinct (kala)',
        'speech_organs': 'relaxed and heavy',
        'quality': 'faltering, like sound of small bells',
        'accompaniments': 'hiccough, hard breathing, phlegm action'
    },
    
    'swoon_resembling_death': {
        'indicators': 'hiccough and hard breathing',
        'speech': 'contains repetition'
    }
}

def represent_death(cause, character):
    """
    Select appropriate death representation protocol.
    """
    if cause == 'disease':
        return execute_disease_death(character)
    elif cause == 'poison':
        return execute_poison_death_stages(character)
    elif cause == 'weapon':
        return execute_violent_death(character)
    elif cause == 'grief':
        return execute_grief_death(character)
```

### 22.4 Speech Mode Protocols

```python
SPEECH_MODES = {
    'ÄkÄÅ›abhÄá¹£ita': {
        'name': 'Speaking to the Sky',
        'function': 'Address to invisible/absent person',
        'technique': 'Eyes directed upward/outward, no physical addressee',
        'narrative_use': 'Prayers, appeals to fate, addressing departed'
    },
    'janÄntika': {
        'name': 'Private Personal Address',
        'function': 'Confidential speech heard only by intended recipient',
        'technique': 'Words spoken in ear, preceded by "so, so"',
        'narrative_use': 'Secrets, conspiracies, intimate communication'
    },
    'Ätmagata': {
        'name': 'Speaking Aside',
        'function': 'Thoughts spoken aloud, unheard by other characters',
        'technique': 'Relates to something within oneself, deliberation and feeling',
        'narrative_use': 'Interior monologue, audience-directed commentary'
    },
    'apavÄritaka': {
        'name': 'Concealed Speaking',
        'function': 'Speech deliberately hidden from some characters',
        'technique': 'TripatÄka hand covering the speaker',
        'narrative_use': 'Plotting, private reactions, dramatic irony'
    }
}

def execute_speech_mode(mode, content, visible_to, hidden_from):
    """
    Apply appropriate speech convention.
    """
    protocol = SPEECH_MODES[mode]
    
    speech = Speech(content=content)
    speech.apply_technique(protocol['technique'])
    speech.visible_to = visible_to
    speech.hidden_from = hidden_from
    
    return speech
```

### 22.5 Sleep and Dream Representation

```python
SLEEP_REPRESENTATION = {
    'somnolent_state': {
        'gesture_rule': 'States NOT represented by hand movement',
        'method': 'Through speech (meaning of words) only',
        'rationale': 'Sleeping body does not gesture'
    },
    
    'speech_in_sleep': {
        'voice': 'slow',
        'words': 'sometimes distinct, sometimes indistinct',
        'content': 'senses repeated twice',
        'quality': 'depends on recollection of past events'
    },
    
    'dream_content': {
        'representation': 'Through sleep-speech describing visions',
        'narrative_function': 'Prophecy, memory, desire revelation'
    }
}
```

### 22.6 Word Repetition Protocol

```python
WORD_REPETITION_RULES = {
    'triggers': ['fright', 'calamity', 'anger', 'intense_sorrow'],
    
    'words_to_repeat': [
        'tell', 'well done', 'ah', 'alas', 
        'go away', 'what', 'let me go', 'no', 'speak'
    ],
    
    'repetition_count': 'twice or thrice',
    
    'function': 'Indicates emotional intensity beyond normal speech'
}
```

---

## 23. Niá¹£edha: On-Stage Prohibitions (Expanded)

### 23.1 Core Principle

Certain events must NEVER be directly shown on stage. They are reported, implied, or represented through conventional signs. This is not prudishness but dramatic wisdomâ€”some things gain power by remaining unseen.

### 23.2 Comprehensive Prohibition List

```python
STAGE_PROHIBITIONS = {
    'absolute_prohibitions': {
        # These must NEVER be shown directly
        'death_of_hero': {
            'reason': 'Hero must survive for narrative completion',
            'alternative': 'Report in PraveÅ›aka or show recovery'
        },
        'killing_on_stage': {
            'reason': 'Violence distances audience from rasa',
            'alternative': 'Sounds off-stage, character reports'
        },
        'battle': {
            'reason': 'Cannot be adequately represented',
            'alternative': 'Messengers report, sounds indicate'
        },
        'eating_on_stage': {
            'reason': 'Interrupts dramatic time',
            'alternative': 'Character exits, time passes'
        },
        'bathing': {
            'reason': 'Practical and decorum concerns',
            'alternative': 'Character enters freshly bathed'
        },
        'sexual_union': {
            'reason': 'Inappropriate for public performance',
            'alternative': 'Suggestion, time-skip, poetic description'
        },
        'sleeping': {
            'reason': 'Stops dramatic action',
            'alternative': 'Brief doze shown, full sleep off-stage'
        }
    },
    
    'contextual_prohibitions': {
        # These depend on dramatic form and context
        'siege_operations': {
            'forms': 'most nÄá¹­akas',
            'exception': 'Some single-act forms (VyÄyoga)'
        },
        'loss_of_kingdom': {
            'reason': 'Major event requires fuller treatment',
            'alternative': 'Report or show aftermath'
        },
        'journey': {
            'reason': 'Cannot show actual travel',
            'alternative': 'Walking convention represents distance'
        }
    }
}
```

### 23.3 The Report-vs-Show Decision Algorithm

```python
def should_show_or_report(event):
    """
    Determine whether an event should be staged or reported.
    """
    # Check absolute prohibitions first
    if event.type in STAGE_PROHIBITIONS['absolute_prohibitions']:
        return 'REPORT'
    
    # Check if event is too complex for staging
    if event.complexity > STAGING_THRESHOLD:
        return 'REPORT_IN_PRAVESAKA'
    
    # Check if event would break unity of impression
    if event.would_fragment_audience_attention():
        return 'REPORT'
    
    # Check if event can be adequately represented
    if not event.has_adequate_convention():
        return 'REPORT'
    
    # Default: show if possible
    return 'SHOW_WITH_CONVENTION'
```

---

## 24. Integration: The Complete Performance Algorithm

### 24.1 Scene Construction with All Systems

```python
def construct_scene(scene_data):
    """
    Integrate all systems into coherent scene construction.
    """
    scene = Scene()
    
    # 1. Establish dominant rasa
    scene.rasa = scene_data.primary_sentiment
    
    # 2. Select appropriate dhruva for entrance
    for character in scene_data.entering_characters:
        entrance_dhruva = select_dhruva_for_entrance(
            character=character,
            rasa=scene.rasa
        )
        scene.add_musical_cue(entrance_dhruva)
        
        # 3. Calculate character gait
        gait = calculate_gait(character)
        gait = modify_gait_for_state(gait, character.emotional_state)
        gait = adjust_gait_for_rasa(gait, scene.rasa)
        character.set_gait(gait)
        
        # 4. Establish zone position
        character.enter_from_zone(
            determine_entrance_zone(character.type)
        )
    
    # 5. Handle special representations
    for element in scene_data.special_elements:
        if element.type == 'season':
            apply_season_representation(element, scene)
        elif element.type == 'time_of_day':
            apply_time_representation(element, scene)
        elif element.type == 'aside':
            apply_speech_mode(element, 'Ätmagata')
    
    # 6. Validate against prohibitions
    for event in scene_data.events:
        if event.type in STAGE_PROHIBITIONS:
            event.convert_to_report()
    
    # 7. Add exit dhruvas
    for character in scene_data.exiting_characters:
        exit_dhruva = select_dhruva_for_exit(character, scene.rasa)
        scene.add_musical_cue(exit_dhruva)
    
    return scene
```

---

## 25. Extended Diagnostic Questions

### 25.1 Dhruva Integration Checklist

| Question | Purpose |
|----------|---------|
| "Does every entrance have an accompanying dhruva?" | Verify musical-narrative integration |
| "Does the dhruva tempo match the rasa?" | Check music-sentiment alignment |
| "Are exits musically marked?" | Verify structural punctuation |

### 25.2 Spatial Grammar Checklist

| Question | Purpose |
|----------|---------|
| "Is character position meaningful?" | Verify zone significance |
| "Do walking patterns indicate distance appropriately?" | Check distance convention |
| "Are conveyances represented by tokens?" | Verify symbolic staging |

### 25.3 Gait Consistency Checklist

| Question | Purpose |
|----------|---------|
| "Does gait match character type?" | Verify base parameters |
| "Does emotional state modify gait appropriately?" | Check state modifiers |
| "Is gait consistent with dominant rasa?" | Verify sentiment alignment |

### 25.4 Special Representation Checklist

| Question | Purpose |
|----------|---------|
| "Are seasons indicated through behavioral/visual signs?" | Verify environmental representation |
| "Are speech modes correctly applied (aside, sky-speech, etc.)?" | Check vocal conventions |
| "Are prohibited events reported rather than shown?" | Verify staging boundaries |

---

## Appendix G: Complete Numerical Reference (All Documents)

| Category | Count | Location |
|----------|-------|----------|
| Meta-Principles | 7 | Primary Â§0 |
| Rasas | 8 | Primary Â§1 |
| Bhavas | 49 (8+33+8) | Primary Â§2 |
| Abhinaya Modes | 4 | Primary Â§3 |
| DharmÄ«s | 2 | Primary Â§4 |
| Vá¹›ttis | 4 | Primary Â§5 |
| Plot Stages | 5 | Primary Â§6 |
| Plot Elements | 5 | Primary Â§6 |
| Sandhis | 5 | Primary Â§6 |
| Dramatic Forms | 10 | Primary Â§7 |
| Hero Types | 4 | Primary Â§8 |
| Heroine Types | 8 | Primary Â§8 |
| Siddhi Types | 2 | Primary Â§9 |
| Blemish Categories | 4 | Supplement Â§12 |
| Self-Made Blemishes | 12+ | Supplement Â§12 |
| PÅ«rvaraá¹…ga Components | 19 | Supplement Â§14 |
| Dhruva Types | 5 | Extended Â§19 |
| Stage Zones | 4+ | Extended Â§20 |
| Gait Parameters | 3 types | Extended Â§21 |
| Season Representations | 7 | Extended Â§22 |
| Speech Modes | 4 | Extended Â§22 |
| Poison Death Stages | 8 | Extended Â§22 |
| Absolute Prohibitions | 7 | Extended Â§23 |

---

## Appendix H: Extended Glossary (All Documents)

| Term | Sanskrit | Meaning |
|------|----------|---------|
| Dhruva | à¤§à¥à¤°à¥à¤µ | Fixed song; musical cue marking narrative beat |
| PrÄveÅ›ikÄ« | à¤ªà¥à¤°à¤¾à¤µà¥‡à¤¶à¤¿à¤•à¥€ | Entrance dhruva |
| Niá¹£krÄmikÄ« | à¤¨à¤¿à¤·à¥à¤•à¥à¤°à¤¾à¤®à¤¿à¤•à¥€ | Exit dhruva |
| Ä€ká¹£epikÄ« | à¤†à¤•à¥à¤·à¥‡à¤ªà¤¿à¤•à¥€ | Incidental/casual dhruva |
| PrÄsÄdikÄ« | à¤ªà¥à¤°à¤¾à¤¸à¤¾à¤¦à¤¿à¤•à¥€ | Pleasing/resolution dhruva |
| Ä€ntarÄ | à¤†à¤¨à¥à¤¤à¤°à¤¾ | Intermediate/interval dhruva |
| Kaká¹£yÄ | à¤•à¤•à¥à¤·à¥à¤¯à¤¾ | Stage zone, spatial division |
| Gati | à¤—à¤¤à¤¿ | Gait, manner of walking |
| TÄla | à¤¤à¤¾à¤² | Unit of spatial measure (for steps) |
| KalÄ | à¤•à¤²à¤¾ | Unit of temporal measure (for step duration) |
| ViÅ›eá¹£Äbhinaya | à¤µà¤¿à¤¶à¥‡à¤·à¤¾à¤­à¤¿à¤¨à¤¯ | Special representation |
| Ä€kÄÅ›abhÄá¹£ita | à¤†à¤•à¤¾à¤¶à¤­à¤¾à¤·à¤¿à¤¤ | Speaking to the sky (addressing invisible) |
| JanÄntika | à¤œà¤¨à¤¾à¤¨à¥à¤¤à¤¿à¤• | Private personal address |
| Ä€tmagata | à¤†à¤¤à¥à¤®à¤—à¤¤ | Speaking aside |
| ApavÄritaka | à¤…à¤ªà¤µà¤¾à¤°à¤¿à¤¤à¤• | Concealed speaking |
| Niá¹£edha | à¤¨à¤¿à¤·à¥‡à¤§ | Prohibition, what must not be shown |

---

*This extended document completes the algorithmic distillation of Bharata Muni's Natyasastra. Together with the primary document (Â§0-11) and supplement (Â§12-18), it provides comprehensive coverage of narratologically significant principles.*

*Compiled from Bharata Muni. Natyasastra: A Treatise on Hindu Dramaturgy and Histrionics. Translated by Manomohan Ghosh. Calcutta: Asiatic Society of Bengal, 1950.*
