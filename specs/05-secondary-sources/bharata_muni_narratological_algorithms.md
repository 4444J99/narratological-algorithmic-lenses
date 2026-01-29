# Bharata Muni's Narratological Algorithms

A systematic distillation of Bharata Muni's *Natyasastra* (~200 BCE â€“ 200 CE) into formal, implementable principles for dramatic composition and narrative affect generation. Based on the Manomohan Ghosh translation.

---

## 0. Meta-Principles (Axioms)

The *Natyasastra* operates from foundational assumptions about the nature of dramatic representation, emotional experience, and aesthetic pleasure.

| Axiom | Formulation |
|-------|-------------|
| B0 | Drama (Natya) is **mimicry** (anukarana) of the exploits of gods, Asuras, kings, and householders |
| B1 | Drama exists to provide **satisfaction** to people of differing tastes in one place |
| B2 | The **Sentiment** (rasa) is the soul of dramaâ€”no meaning proceeds without it |
| B3 | Sentiments arise from **States** (bhava), not States from Sentiments |
| B4 | Aesthetic experience is **tasted** (asvadayanti)â€”like culinary flavor from combined ingredients |
| B5 | Successful representation requires **both** realistic (lokadharmi) and conventional (natyadharmi) practices |
| B6 | The ultimate court of appeal concerning dramatic practice is **the people** |

### 0.1 The Cooking Analogy (Central Metaphor)

```
GIVEN:
  - culinary taste (rasa) results from combining spices, vegetables, and other articles
  - six distinct tastes emerge from specific ingredient combinations
  
WHEN:
  - Dominant States (sthayibhava) combine with:
    - Determinants (vibhava)
    - Consequents (anubhava)
    - Transitory States (vyabhicaribhava)
    
THEN:
  - Dominant States "attain the quality of Sentiment"
  - Spectators "taste" these Sentiments through representation
  
THEREFORE:
  rasa_production = combine(sthayibhava, vibhava, anubhava, vyabhicari)
  aesthetic_pleasure = spectator.taste(rasa)
```

### 0.2 The Universality Principle

```
CONDITION_FOR_RASA:
  States become Sentiments WHEN:
    imbued_with(quality_of_universality = True)  # samanya/siddhartha
    
RATIONALE:
  - Personal emotion (bhava) = particular, individual
  - Aesthetic emotion (rasa) = universal, shared
  
TRANSFORMATION:
  def bhava_to_rasa(state, representation):
      if representation.achieves_universality():
          return Sentiment(state)
      else:
          return state  # remains particular, not aesthetic
```

---

## 1. Rasa Theory: The Eight Sentiments

### 1.1 The Canonical Eight

| # | Rasa | English | Dominant State | Color | Presiding Deity |
|---|------|---------|----------------|-------|-----------------|
| 1 | Åšá¹›á¹…gÄra | Erotic | Love (rati) | Bright/Green | Viá¹£á¹‡u |
| 2 | HÄsya | Comic | Mirth (hÄsa) | White | Pramathas |
| 3 | Karuá¹‡a | Pathetic | Sorrow (Å›oka) | Ash-colored | Rudra |
| 4 | Raudra | Furious | Anger (krodha) | Red | Yama |
| 5 | VÄ«ra | Heroic | Energy (utsÄha) | Light orange | Indra |
| 6 | BhayÄnaka | Terrible | Fear (bhaya) | Black | KÄla |
| 7 | BÄ«bhatsa | Odious | Disgust (jugupsÄ) | Blue | Åšiva |
| 8 | Adbhuta | Marvellous | Astonishment (vismaya) | Yellow | Brahman |

### 1.2 The Four Primary â†’ Eight Derived

```
PRIMARY_SENTIMENTS = {Raudra, VÄ«ra, BÄ«bhatsa, Åšá¹›á¹…gÄra}

DERIVATION_MAP:
  Åšá¹›á¹…gÄra â†’ HÄsya     # Comic derives from Erotic (mimicry of love)
  Raudra  â†’ Karuá¹‡a    # Pathetic derives from Furious (result of anger)
  VÄ«ra    â†’ Adbhuta   # Marvellous derives from Heroic (result of heroism)
  BÄ«bhatsa â†’ BhayÄnaka # Terrible derives from Odious

MECHANISM:
  derived_rasa = transform(primary_rasa, mode)
  WHERE mode IN {mimicry, result, consequence}
```

### 1.3 Rasa Evocation Formula

```python
def evoke_rasa(target_sentiment):
    """
    The canonical formula for producing aesthetic experience.
    """
    # Step 1: Identify the Dominant State
    sthayibhava = DOMINANT_STATE_MAP[target_sentiment]
    
    # Step 2: Establish Determinants (causes/stimuli)
    vibhavas = select_determinants(target_sentiment)
    
    # Step 3: Express through Consequents (reactions/expressions)
    anubhavas = select_consequents(target_sentiment)
    
    # Step 4: Color with Transitory States
    vyabhicaris = select_compatible_transitory_states(target_sentiment)
    
    # Step 5: Combine through representation
    return combine_through_abhinaya(
        sthayibhava,
        vibhavas,
        anubhavas,
        vyabhicaris
    )
```

---

## 2. Bhava Theory: The Forty-Nine States

### 2.1 Taxonomy of States

```
STATES (Bhava) = 49 total

â”œâ”€â”€ DOMINANT STATES (SthÄyibhÄva): 8
â”‚   â””â”€â”€ Love, Mirth, Sorrow, Anger, Energy, Fear, Disgust, Astonishment
â”‚
â”œâ”€â”€ TRANSITORY STATES (VyabhicÄribhÄva): 33
â”‚   â””â”€â”€ Discouragement, Weakness, Apprehension, Envy, Intoxication,
â”‚       Weariness, Indolence, Depression, Anxiety, Distraction,
â”‚       Recollection, Contentment, Shame, Inconstancy, Joy, Agitation,
â”‚       Stupor, Arrogance, Despair, Impatience, Sleep, Epilepsy,
â”‚       Dreaming, Awakening, Indignation, Dissimulation, Cruelty,
â”‚       Assurance, Sickness, Insanity, Death, Fright, Deliberation
â”‚
â””â”€â”€ TEMPERAMENTAL STATES (SÄttvikabhÄva): 8
    â””â”€â”€ Paralysis (stambha), Perspiration (sveda), Horripilation (romÄÃ±ca),
        Change of Voice (svarabheda), Trembling (vepathu),
        Change of Colour (vaivará¹‡ya), Weeping (aÅ›ru), Fainting (pralaya)
```

### 2.2 The Hierarchy of States

```
ANALOGY: King and Attendants

JUST_AS:
  - Among persons of similar characteristics
  - Some attain KINGSHIP (due to birth, manners, learning, skill)
  - Others become ATTENDANTS (due to inferior intellect)

SO_TOO:
  DOMINANT_STATES = "kings"
    - All other states DEPEND on them
    - They alone become SENTIMENTS
    
  DETERMINANTS_AND_CONSEQUENTS = "local officers"
    - Support the Dominant States
    
  TRANSITORY_STATES = "attendants"
    - Serve the Dominant States
    - "Carry" the Sentiment through representation

RULE:
  "Just as only a king surrounded by numerous attendants 
   receives this epithet [of king] and not any other man,
   so the Dominant States only followed by Determinants,
   Consequents and Transitory States receive the name of Sentiment."
```

### 2.3 VibhÄva (Determinants) â€” Causes

```python
DETERMINANT_PATTERNS = {
    'erotic': [
        'pleasures_of_season', 'garlands', 'unguents', 'ornaments',
        'beloved_persons', 'splendid_mansions', 'gardens',
        'seeing_beloved', 'hearing_beloved_words', 'playing', 'dallying'
    ],
    'comic': [
        'unseemly_dress', 'impudence', 'greediness', 'quarrel',
        'defective_limb', 'irrelevant_words', 'mentioning_faults'
    ],
    'pathetic': [
        'affliction_under_curse', 'separation_from_dear_ones',
        'loss_of_wealth', 'death_of_beloved', 'captivity'
    ],
    'furious': [
        'anger', 'rape', 'abuse', 'insult', 'untrue_allegation',
        'threatening', 'revengefulness', 'jealousy'
    ],
    'heroic': [
        'presence_of_mind', 'perseverance', 'diplomacy', 'discipline',
        'military_strength', 'aggressiveness', 'reputation_of_might'
    ],
    'terrible': [
        'hideous_noise', 'sight_of_ghosts', 'panic', 'empty_house',
        'forest', 'death_of_dear_ones', 'owl_cry', 'jackal_cry'
    ],
    'odious': [
        'hearing_unpleasant_things', 'seeing_unpleasant_things',
        'offensive_objects', 'impure_objects', 'harmful_things'
    ],
    'marvellous': [
        'illusion', 'magic', 'extraordinary_feats',
        'great_excellence_in_painting', 'art_works'
    ]
}
```

### 2.4 AnubhÄva (Consequents) â€” Expressions

```python
CONSEQUENT_PATTERNS = {
    'erotic': [
        'clever_eye_movements', 'eyebrow_movements', 'glances',
        'soft_limb_movements', 'sweet_words'
    ],
    'comic': [
        'throbbing_lips', 'throbbing_nose', 'throbbing_cheek',
        'wide_eyes', 'contracted_eyes', 'perspiration',
        'face_colour_change', 'holding_sides'
    ],
    'pathetic': [
        'shedding_tears', 'lamentation', 'bewailing', 'change_of_colour',
        'loss_of_voice', 'loose_limbs', 'falling_on_ground',
        'crying', 'deep_breathing', 'paralysis'
    ],
    'furious': [
        'red_eyes', 'knitting_eyebrows', 'defiance', 'biting_lips',
        'cheek_movement', 'pressing_hands_together'
    ],
    'heroic': [
        'firmness', 'patience', 'heroism', 'charity', 'diplomacy'
    ],
    'terrible': [
        'trembling_hands_feet', 'horripilation', 'change_of_colour',
        'loss_of_voice', 'palpitation', 'dry_mouth'
    ],
    'odious': [
        'contracting_limbs', 'narrowing_mouth', 'vomiting',
        'spitting', 'shaking_limbs'
    ],
    'marvellous': [
        'wide_opening_eyes', 'looking_without_winking',
        'eyebrow_movement', 'horripilation', 'head_moving',
        'cry_of_well_done'
    ]
}
```

### 2.5 Compatible Transitory States

```python
TRANSITORY_COMPATIBILITY = {
    'erotic_union': EXCLUDE(['fear', 'indolence', 'cruelty', 'disgust']),
    'erotic_separation': [
        'indifference', 'langour', 'fear', 'jealousy', 'fatigue',
        'anxiety', 'yearning', 'drowsiness', 'sleep', 'dreaming',
        'awakening', 'illness', 'insanity', 'epilepsy', 'inactivity',
        'fainting', 'death'
    ],
    'comic': [
        'indolence', 'dissimulation', 'drowsiness', 'sleep',
        'dreaming', 'insomnia', 'envy'
    ],
    'furious': [
        'presence_of_mind', 'determination', 'energy', 'indignation',
        'restlessness', 'fury', 'perspiration', 'trembling',
        'horripilation', 'choking_voice'
    ],
    'heroic': [
        'contentment', 'judgement', 'pride', 'agitation', 'energy',
        'ferocity', 'indignation', 'remembrance', 'horripilation'
    ],
    'terrible': [
        'paralysis', 'perspiration', 'choking_voice', 'horripilation',
        'trembling', 'loss_of_voice', 'change_of_colour', 'fear',
        'stupefaction', 'dejection', 'agitation', 'restlessness',
        'inactivity', 'epilepsy', 'death'
    ],
    'odious': [
        'epilepsy', 'delusion', 'agitation', 'fainting',
        'sickness', 'death'
    ]
}
```

---

## 3. Abhinaya: The Four Modes of Representation

### 3.1 The Quadripartite System

```
ABHINAYA (Histrionic Representation) = {
    Ä€á¹„GIKA:   Gestures â€” physical expression through body movements
    VÄ€CIKA:   Words â€” verbal expression through speech
    Ä€HÄ€RYA:   Costumes & Make-up â€” visual expression through appearance
    SÄ€TTVIKA: Temperament â€” psychological expression through inner states
}

DISTRIBUTION:
  Each mode contributes to total dramatic effect
  All four must work in HARMONY
  Different situations emphasize different modes
```

### 3.2 Ä€á¹…gika (Gestural Representation)

```python
class AngikAbhinaya:
    """
    Physical representation through major and minor limbs.
    """
    MAJOR_LIMBS = ['head', 'hands', 'chest', 'sides', 'waist', 'feet']
    MINOR_LIMBS = ['eyes', 'eyebrows', 'nose', 'lips', 'cheeks', 'chin']
    
    def select_gesture(self, sentiment, character_type, situation):
        """
        Gestures must match sentiment, character status, and context.
        """
        base_gesture = GESTURE_LIBRARY[sentiment]
        
        # Adjust for character type
        if character_type == 'superior':
            return refine(base_gesture, subtlety='high')
        elif character_type == 'middling':
            return refine(base_gesture, subtlety='medium')
        else:
            return refine(base_gesture, subtlety='low')
```

### 3.3 VÄcika (Verbal Representation)

```python
class VacikaAbhinaya:
    """
    Verbal expression including speech, intonation, and metre.
    """
    
    def configure_speech(self, sentiment):
        """
        Speech parameters vary by sentiment.
        """
        config = {
            'erotic': {'intonation': 'madhyama', 'tempo': 'medium', 'note': 'gandhara_nisada'},
            'comic': {'intonation': 'madhyama', 'tempo': 'medium', 'note': 'gandhara_nisada'},
            'pathetic': {'intonation': 'normal', 'tempo': 'slow', 'note': 'gandhara_nisada'},
            'heroic': {'intonation': 'udatta', 'tempo': 'quick', 'note': 'sadja_rsabha'},
            'furious': {'intonation': 'udatta', 'tempo': 'quick', 'note': 'sadja_rsabha'},
            'marvellous': {'intonation': 'udatta', 'tempo': 'quick', 'note': 'sadja_rsabha'},
            'terrible': {'intonation': 'normal', 'tempo': 'quick', 'note': 'sadja_rsabha'},
            'odious': {'intonation': 'normal', 'tempo': 'quick', 'note': 'sadja_rsabha'}
        }
        return config[sentiment]
```

### 3.4 Ä€hÄrya (Visual Representation)

```
COSTUME_PRINCIPLES:
  1. APPROPRIATENESS: Match costume to character's status, region, occupation
  2. CONSISTENCY: Maintain character identity throughout
  3. SIGNIFICATION: Use conventional colors for character types
  
COLOR_CODING:
  Gods         â†’ golden/yellow
  Kings        â†’ variegated, rich
  Ascetics     â†’ matted hair, bark garments
  Raksasas     â†’ black, unkempt
  Women        â†’ appropriate to status (wife, courtesan, etc.)
  
MAKE-UP:
  Apply to enhance recognition of character type
  Use conventional features for divine vs. human vs. demonic
```

### 3.5 SÄttvika (Temperamental Representation)

```python
class SattvikaAbhinaya:
    """
    The eight involuntary psychophysical responses.
    These arise from the actor's internal state (sattva/mind).
    """
    
    SATTVIKA_BHAVAS = [
        'stambha',      # Paralysis â€” immobility from emotion
        'sveda',        # Perspiration â€” spontaneous sweating
        'romanca',      # Horripilation â€” goosebumps
        'svarabheda',   # Voice change â€” breaking/trembling voice
        'vepathu',      # Trembling â€” involuntary shaking
        'vaivarnya',    # Color change â€” pallor/flushing
        'asru',         # Tears â€” weeping
        'pralaya'       # Fainting â€” loss of consciousness
    ]
    
    def represent(self, state, intensity='natural'):
        """
        Sattvika bhavas must arise from genuine internal engagement.
        Cannot be mechanically producedâ€”require actor's psychological investment.
        """
        if intensity == 'natural':
            return full_expression(state)
        elif intensity == 'feigned':
            return milder_expression(state)
```

---

## 4. DharmÄ«: The Two Practices

### 4.1 Lokadharmi (Realistic Practice)

```
DEFINITION:
  "Reproduction of natural behaviour of men and women on the stage"
  
CHARACTERISTICS:
  - Mimics everyday life actions
  - Natural speech patterns
  - Ordinary movements and gestures
  - Familiar emotional expressions
  
APPLICATION:
  - Domestic scenes
  - Conversational exchanges
  - Common activities
  - Character establishment
```

### 4.2 NÄtyadharmÄ« (Conventional Practice)

```
DEFINITION:
  "Theatrical conventions not found in ordinary life"
  
CHARACTERISTICS:
  - Stylized movement vocabulary
  - Codified gesture system
  - Dance-like quality
  - Musical accompaniment
  - Exaggerated expression
  
EXAMPLES:
  - Characters speak in verse
  - Movements timed to rhythm
  - Conventional exits/entrances
  - Symbolic space representation
  
RATIONALE:
  "The Hindu theatre recognized very clearly that drama or the Natya 
   was different from the real life and followed its own conventions."
```

### 4.3 Practice Selection Algorithm

```python
def select_dharmi(scene_type, sentiment, characters):
    """
    Determine appropriate practice for scene.
    """
    # Emotional intensity determines base practice
    if sentiment in ['erotic', 'heroic', 'furious', 'marvellous']:
        base = 'natyadharmi'  # heightened states need stylization
    else:
        base = 'lokadharmi'  # grounded states use realism
    
    # Scene type modifies
    if scene_type == 'combat' or scene_type == 'love_making':
        return 'natyadharmi'  # always stylized
    elif scene_type == 'domestic':
        return 'lokadharmi'  # always realistic
    else:
        return blend(base, scene_requirements)
```

---

## 5. Vá¹›tti: The Four Styles

### 5.1 Style Classification

| Style | Sanskrit | Characteristics | Primary Sentiments |
|-------|----------|-----------------|-------------------|
| Verbal | BhÄratÄ« | Dialogue-dominant, Sanskrit emphasis | All (universal base) |
| Grand | SÄttvatÄ« | Noble characters, exalted speech, gestures | Heroic, Marvellous, Furious |
| Graceful | KaiÅ›ikÄ« | Charming costumes, dance, female characters | Erotic, Comic |
| Energetic | Ä€rabhaá¹­Ä« | Bold presentation, battles, conflicts | Terrible, Furious |

### 5.2 Style-Sentiment Mapping

```python
STYLE_SENTIMENT_MAP = {
    'bharati': {
        'description': 'Speech-centered, intellectual engagement',
        'sentiments': ['all'],
        'features': ['elaborate_dialogue', 'sanskrit_predominant', 'minimal_dance']
    },
    'sattvati': {
        'description': 'Grand manner for noble themes',
        'sentiments': ['heroic', 'marvellous', 'furious'],
        'features': ['exalted_characters', 'dignified_gestures', 'elevated_diction']
    },
    'kaisiki': {
        'description': 'Graceful manner for love and humor',
        'sentiments': ['erotic', 'comic'],
        'features': ['charming_costumes', 'dance_emphasis', 'female_centered', 'love_themes']
    },
    'arabhati': {
        'description': 'Energetic manner for conflict',
        'sentiments': ['terrible', 'furious'],
        'features': ['bold_presentation', 'battle_scenes', 'physical_intensity']
    }
}

def select_style(dominant_sentiment, play_type, act_number):
    """
    Styles are not mutually exclusiveâ€”blend according to scene needs.
    """
    primary_style = STYLE_SENTIMENT_MAP.get_primary(dominant_sentiment)
    
    # Different acts may emphasize different styles
    # A single play often uses multiple styles across its acts
    return blend_styles(primary_style, scene_requirements)
```

---

## 6. Vastu: Plot Structure

### 6.1 The Five Stages of Action

```
HERO'S_EXERTION = [
    1. Ä€RAMBHA (Beginning)      â€” Initial impulse toward the goal
    2. PRAYATNA (Effort)        â€” Active pursuit of the objective
    3. PRÄ€PTI-SAMBHAVA          â€” Possibility of attainment appears
       (Possibility of Attainment)
    4. NIYATÄ€PTI                â€” Certainty of attainment emerges
       (Certainty of Attainment)
    5. PHALÄ€GAMA                â€” Actual attainment of the result
       (Attainment of Result)
]
```

### 6.2 The Five Elements of Plot

```python
PLOT_ELEMENTS = {
    'bija': {
        'name': 'Germ/Seed',
        'function': 'Initial cause that generates entire action',
        'placement': 'Opening'
    },
    'bindu': {
        'name': 'Point/Drop',
        'function': 'Maintains continuity when action seems interrupted',
        'placement': 'Throughout (as needed)'
    },
    'pataka': {
        'name': 'Episode/Banner',
        'function': 'Subsidiary narrative supporting main action',
        'placement': 'Development'
    },
    'prakari': {
        'name': 'Episodical Incident',
        'function': 'Minor incident within episode',
        'placement': 'Development'
    },
    'karya': {
        'name': 'Denouement',
        'function': 'Final resolution of action',
        'placement': 'Conclusion'
    }
}
```

### 6.3 The Five Junctures (Sandhi)

```python
SANDHIS = {
    'mukha': {
        'name': 'Opening',
        'function': 'Introduces germ (bija) of the plot',
        'stage_correspondence': 'Ärambha',
        'contains': ['bija_introduction', 'hero_establishment']
    },
    'pratimukha': {
        'name': 'Progression',
        'function': 'Germ begins to sprout, action advances',
        'stage_correspondence': 'prayatna',
        'contains': ['complication_introduction', 'bindu_development']
    },
    'garbha': {
        'name': 'Development',
        'function': 'Main body of action, episodes unfold',
        'stage_correspondence': 'prapti_sambhava',
        'contains': ['pataka_episodes', 'primary_conflicts']
    },
    'vimarsa': {
        'name': 'Pause',
        'function': 'Crisis point, action seems in doubt',
        'stage_correspondence': 'niyatapti',
        'contains': ['suspense_peak', 'reversal_possibility']
    },
    'nirvahana': {
        'name': 'Conclusion',
        'function': 'Resolution, result achieved',
        'stage_correspondence': 'phalagama',
        'contains': ['denouement', 'karya_completion']
    }
}
```

### 6.4 Principal vs. Incidental Plots

```python
class PlotStructure:
    """
    Dual plot architecture in dramatic composition.
    """
    
    def __init__(self):
        self.adhikarika = None  # Principal/Primary plot
        self.prasangika = []     # Incidental/Subsidiary plots
    
    def set_principal_plot(self, hero, objective, obstacles):
        """
        The adhikarika (principal) plot is obvious from its nameâ€”
        it concerns the Hero's main action.
        """
        self.adhikarika = {
            'hero': hero,
            'objective': objective,
            'obstacles': obstacles,
            'sandhis': generate_five_junctures(hero, objective)
        }
    
    def add_incidental_plot(self, characters, their_interest, hero_benefit):
        """
        Incidental plots: characters acting in their own interest
        INCIDENTALLY further the purpose of the Hero.
        """
        self.prasangika.append({
            'characters': characters,
            'their_interest': their_interest,
            'how_it_helps_hero': hero_benefit
        })
```

---

## 7. NÄá¹­aka Typology: The Ten Dramatic Forms

### 7.1 Classification Table

| Form | Acts | Hero Type | Plot Source | Dominant Elements |
|------|------|-----------|-------------|-------------------|
| NÄá¹­aka | 5-10 | Royal/divine | Celebrated legend | All sentiments (heroic dominant) |
| Prakaraá¹‡a | 5-10 | Brahmin/merchant | Original/invented | Love (bourgeois comedy) |
| SamavakÄra | 3 | God/Asura | Mythological | Deception, excitement, love |
| ÄªhÄmá¹›ga | 4 | Divine males | Divine conflict | Love, discord, intrigue |
| á¸Œima | 4 | Exalted, well-known | Well-constructed | All except Comic & Erotic |
| VyÄyoga | 1 | Well-known | Single day events | Battle, combat, conflict |
| Utsá¹›á¹£á¹­ikÄá¹…ka | 1 | Human | Well-known | Pathetic (women's lament) |
| Prahasana | 1 | Varied | Original | Comic (farce, satire) |
| BhÄá¹‡a | 1 | Single actor | Adventure | Monologue (rogue/parasite) |
| VÄ«thÄ« | 1 | 1-2 actors | Varied | Short dramatic sketch |

### 7.2 NÄá¹­aka Construction Algorithm

```python
def construct_nataka(legendary_source, hero):
    """
    The NÄá¹­aka is the most complete dramatic form.
    """
    # Validation
    assert hero.type in ['royal', 'divine_descended', 'sage_descended']
    assert legendary_source.is_celebrated == True
    
    # Structure
    nataka = {
        'acts': range(5, 11),  # 5-10 acts
        'hero': {
            'type': 'exalted',
            'character': hero,
            'death_prohibition': True  # Hero cannot die on stage
        },
        'plot': {
            'source': legendary_source,
            'junctures': generate_five_sandhis()
        },
        'constraints': {
            'location': 'India',  # Human characters placed in India
            'time_per_act': 'one_day_maximum',
            'on_stage_prohibitions': [
                'hero_death', 'battle', 'loss_of_kingdom',
                'siege', 'eating', 'bathing', 'sexual_union',
                'natural_calamity', 'degradation'
            ]
        },
        'outcome': 'hero_triumph_or_prosperity'
    }
    return nataka
```

### 7.3 On-Stage Prohibitions

```python
PROHIBITED_REPRESENTATIONS = [
    'death_of_hero',
    'actual_battle',
    'loss_of_kingdom',
    'siege_of_town',
    'eating',
    'bathing',
    'sexual_union',
    'anointing',
    'application_of_unguents',
    'natural_calamity',
    'degradation_of_hero'
]

# These may be REPORTED in Introductory Scenes (praveÅ›aka)
# but never SHOWN directly on stage

def can_show_on_stage(event):
    return event not in PROHIBITED_REPRESENTATIONS
```

---

## 8. Character Typology

### 8.1 The Three Character Types

```python
CHARACTER_TYPES = {
    'superior': {
        'qualities': ['noble_birth', 'learning', 'skill', 'dignity'],
        'emotional_expression': 'restrained',
        'laughter_style': ['slight_smile', 'smile'],
        'sorrow_style': 'patience',
        'examples': ['kings', 'gods', 'sages']
    },
    'middling': {
        'qualities': ['moderate_status', 'education', 'refinement'],
        'emotional_expression': 'moderate',
        'laughter_style': ['gentle_laughter', 'laughter_of_ridicule'],
        'sorrow_style': 'controlled_grief',
        'examples': ['merchants', 'ministers', 'officers']
    },
    'inferior': {
        'qualities': ['common_status', 'unrefined'],
        'emotional_expression': 'unrestrained',
        'laughter_style': ['vulgar_laughter', 'excessive_laughter'],
        'sorrow_style': 'open_weeping',
        'examples': ['servants', 'rogues', 'parasites']
    }
}
```

### 8.2 The Eight Types of Heroines (NÄyikÄ)

```python
NAYIKA_TYPES = {
    'vÄsaka-sajjÄ': {
        'name': 'Dressed for Union',
        'state': 'Expectantly awaiting lover',
        'emotional_dominant': 'anticipation'
    },
    'virahotkÄá¹‡á¹­hitÄ': {
        'name': 'Distressed by Separation',
        'state': 'Pining for absent lover',
        'emotional_dominant': 'yearning'
    },
    'svÄdhÄ«na-patikÄ': {
        'name': 'Having Husband in Subjection',
        'state': 'Confident in lover\'s devotion',
        'emotional_dominant': 'contentment'
    },
    'kalahÄntaritÄ': {
        'name': 'Separated by Quarrel',
        'state': 'Estranged after argument',
        'emotional_dominant': 'regret'
    },
    'khaá¹‡á¸itÄ': {
        'name': 'Enraged',
        'state': 'Angry at lover\'s infidelity',
        'emotional_dominant': 'jealous_anger'
    },
    'vipralabdhÄ': {
        'name': 'Deceived',
        'state': 'Betrayed by lover',
        'emotional_dominant': 'disappointment'
    },
    'proá¹£ita-bhartá¹›kÄ': {
        'name': 'With Sojourning Husband',
        'state': 'Husband away on journey',
        'emotional_dominant': 'loneliness'
    },
    'abhisÄrikÄ': {
        'name': 'Moving to Lover',
        'state': 'Going to meet lover',
        'emotional_dominant': 'adventurous_love'
    }
}
```

### 8.3 Anger Expression by Relationship

```python
def express_anger(character, target_relationship):
    """
    Anger manifestation varies by social relationship.
    """
    ANGER_EXPRESSIONS = {
        'towards_enemy': [
            'knitting_eyebrows', 'fierce_look', 'bitten_lips',
            'hands_clasping', 'touching_head_and_breast'
        ],
        'towards_superior': [
            'slightly_downcast_eyes', 'wiping_slight_perspiration',
            'NO_violent_movement'  # Constrained expression
        ],
        'towards_beloved': [
            'very_slight_body_movement', 'shedding_tears',
            'knitting_eyebrows', 'sidelong_glances', 'throbbing_lips'
        ],
        'towards_servant': [
            'threat', 'rebuke', 'dilating_eyes',
            'contemptuous_looks_various_kinds'
        ],
        'feigned': [
            'mild_versions_of_above',
            'ulterior_motive_present'
        ]
    }
    return ANGER_EXPRESSIONS[target_relationship]
```

---

## 9. Siddhi: The Theory of Success

### 9.1 Dual Success Model

```python
SUCCESS_TYPES = {
    'daiviki': {
        'name': 'Divine Success',
        'source': 'Superior spectators (cultured, educated)',
        'recognition_of': 'Deeper aspects of play',
        'expression': 'Refined appreciation',
        'measure': 'quality_of_understanding'
    },
    'mÄnuá¹£Ä«': {
        'name': 'Human Success',
        'source': 'Average spectators (ordinary people)',
        'recognition_of': 'Superficial/obvious aspects',
        'expression': 'Tumultuous applause, energetic response',
        'measure': 'intensity_of_reaction'
    }
}

# Both are valid and necessary
# "The ultimate court of appeal concerning dramatic practice is THE PEOPLE"
```

### 9.2 Audience Taste Differentiation

```python
AUDIENCE_PREFERENCES = {
    'lovers': 'erotic_sentiment_presentation',
    'learned': 'religious_philosophical_doctrine',
    'wealth_seekers': 'acquisition_themes',
    'passionless': 'liberation_topics',
    'fierce_persons': 'odious_terrible_sentiments',
    'warriors': 'personal_combats_battles',
    'elderly': 'puranic_tales_virtue',
    'common_women_children_uncultured': 'comic_sentiment_remarkable_costumes'
}

# A drama must satisfy DIVERSE tastes in ONE PLACE
# This is the essence of dramatic art's social function
```

---

## 10. Compositional Methodology

### 10.1 The Integration Principle

```python
def compose_drama(source, intended_sentiment):
    """
    Systematic approach to dramatic composition.
    """
    # Step 1: Establish core rasa
    dominant_rasa = select_primary_sentiment(intended_sentiment)
    
    # Step 2: Identify sthayibhava
    dominant_state = RASA_TO_BHAVA[dominant_rasa]
    
    # Step 3: Design vibhavas (determinants/causes)
    vibhavas = create_circumstances_that_trigger(dominant_state)
    
    # Step 4: Design anubhavas (consequents/expressions)
    anubhavas = design_expression_vocabulary(dominant_state)
    
    # Step 5: Select compatible vyabhicaris
    transitory_states = filter_compatible(dominant_rasa)
    
    # Step 6: Choose appropriate style (vrtti)
    style = STYLE_SENTIMENT_MAP[dominant_rasa]
    
    # Step 7: Structure plot (vastu)
    plot = construct_five_sandhis(source, hero)
    
    # Step 8: Distribute across acts
    acts = distribute_elements(plot, dominant_rasa, style)
    
    # Step 9: Design abhinaya for each scene
    for act in acts:
        for scene in act.scenes:
            scene.angika = design_gestures(scene.sentiment)
            scene.vacika = design_dialogue(scene.sentiment)
            scene.aharya = design_costumes(scene.characters)
            scene.sattvika = design_internal_states(scene.sentiment)
    
    return Drama(acts)
```

### 10.2 Diction Guidelines

```python
DICTION_PRINCIPLES = {
    'metre_selection': {
        'heroic_furious': 'arya_metre',
        'erotic': ['malini', 'mandakranta'],  # Gentle metres
        'pathetic': ['sakkari', 'atidhriti']
    },
    'euphony': {
        'requirement': 'agreeable_and_soft_sounds',
        'accessibility': 'intelligible_to_country_people',
        'feminine_speech': 'words_recitable_by_women'
    },
    'verse_prose_balance': {
        'warning': 'Long prose passages prove tiresome to spectators',
        'recommendation': 'Emphasize verse in dialogue'
    },
    'character_names': {
        'method': 'suggestive_significant_names',
        'function': 'Names indicate character qualities'
    }
}
```

---

## 11. Diagnostic Questions

### 11.1 Rasa Verification

| Question | Purpose |
|----------|---------|
| "Which Dominant State is being evoked?" | Confirm clear sthayibhava identification |
| "What are the specific Determinants (causes)?" | Verify vibhava specificity |
| "Are the Consequents (expressions) appropriate?" | Check anubhava selection |
| "Are the Transitory States compatible?" | Validate vyabhicari choices |
| "Does the representation achieve universality?" | Test for aesthetic vs. personal emotion |

### 11.2 Structural Verification

| Question | Purpose |
|----------|---------|
| "Is the Germ (bija) planted in the Opening?" | Verify plot foundation |
| "Do the Five Junctures appear in sequence?" | Check structural completeness |
| "Does the Incidental Plot serve the Principal Plot?" | Test subplot integration |
| "Is the Hero's progression through the Five Stages clear?" | Verify dramatic arc |
| "Does the Conclusion arise from the Development?" | Check organic resolution |

### 11.3 Performance Verification

| Question | Purpose |
|----------|---------|
| "Do all four Abhinaya modes work in harmony?" | Verify integrated representation |
| "Is the practice (dharmi) appropriate to the scene?" | Check realistic/conventional balance |
| "Is the style (vrtti) matched to the sentiment?" | Validate style-sentiment correspondence |
| "Are character expressions appropriate to their type?" | Verify character consistency |

---

## Appendix A: Quick Reference Card

### The Core Formula

```
RASA = STHAYIBHAVA + VIBHAVA + ANUBHAVA + VYABHICARI
      (Sentiment)   (Dominant)  (Determinants) (Consequents) (Transitory)
                    (State)     (Causes)       (Expressions) (States)
```

### The Eight Rasas

```
Åšá¹›á¹…gÄra (Erotic)    â† Love      â†’ Comic
HÄsya (Comic)       â† Mirth
Karuá¹‡a (Pathetic)   â† Sorrow    â† Furious
Raudra (Furious)    â† Anger     â†’ Pathetic
VÄ«ra (Heroic)       â† Energy    â†’ Marvellous
BhayÄnaka (Terrible)â† Fear      â† Odious
BÄ«bhatsa (Odious)   â† Disgust   â†’ Terrible
Adbhuta (Marvellous)â† Astonishment
```

### The Four Representations

```
Ä€á¹…gika   â†’ BODY (gestures, movement)
VÄcika   â†’ WORDS (speech, intonation)
Ä€hÄrya   â†’ APPEARANCE (costume, make-up)
SÄttvika â†’ TEMPERAMENT (psychophysical states)
```

### The Five Junctures

```
1. Mukha (Opening)      â†’ Germ planted
2. Pratimukha (Progress)â†’ Germ sprouts
3. Garbha (Development) â†’ Action unfolds
4. VimarÅ›a (Pause)      â†’ Crisis point
5. Nirvahana (Conclusion)â†’ Resolution
```

---

## Appendix B: Validation Checklist

```python
def validate_drama(drama):
    checks = [
        # Rasa
        ("Clear dominant sentiment identified", rasa_clarity_test),
        ("Sthayibhava consistently evoked", dominant_state_test),
        ("Vibhavas specific and appropriate", determinant_test),
        ("Anubhavas match sentiment", consequent_test),
        ("Vyabhicaris compatible", transitory_state_test),
        ("Universal quality achieved", universality_test),
        
        # Structure
        ("Germ (bija) in Opening", germ_placement_test),
        ("Five Junctures present", sandhi_completeness_test),
        ("Principal plot clear", adhikarika_test),
        ("Incidental plots serve main", prasangika_test),
        ("Hero's Five Stages visible", hero_progression_test),
        
        # Representation
        ("Four Abhinaya modes integrated", abhinaya_integration_test),
        ("Practice (dharmi) appropriate", practice_selection_test),
        ("Style (vrtti) matches sentiment", style_sentiment_test),
        ("Character types consistent", character_consistency_test),
        ("Prohibited actions excluded", prohibition_test),
        
        # Success
        ("Appeals to diverse tastes", diversity_test),
        ("Both divine and human success possible", dual_success_test),
    ]
    
    return all(test(drama) for name, test in checks)
```

---

## Appendix C: Theoretical Correspondence Table

| Bharata Muni | Aristotle | McKee | South Park |
|--------------|-----------|-------|------------|
| Rasa (Sentiment) | Catharsis | Emotional experience | Episode impact |
| Sthayibhava (Dominant State) | Pathos | Core emotion | Emotional throughline |
| Vibhava (Determinant) | Probable cause | Inciting incident/setup | Setup |
| Anubhava (Consequent) | Recognition/expression | Payoff | Payoff |
| Vyabhicari (Transitory) | Complication | Gap complications | Complications |
| Sandhi (Juncture) | Plot structure | Act structure | Story beats |
| Natyadharmi | Poetic truth | â€” | â€” |
| Lokadharmi | Historical truth | â€” | â€” |
| Abhinaya | Spectacle/manner | â€” | â€” |

---

## Appendix D: Key Terms Glossary

| Sanskrit | Translation | Function |
|----------|-------------|----------|
| Rasa | Sentiment/Aesthetic flavor | Goal of dramatic representation |
| BhÄva | State/Emotion | Building blocks of rasa |
| SthÄyibhÄva | Dominant State | Core emotion underlying rasa |
| VibhÄva | Determinant | Causes that trigger emotional response |
| AnubhÄva | Consequent | Expressions that follow emotion |
| VyabhicÄribhÄva | Transitory State | Accompanying/coloring emotions |
| SÄttvikabhÄva | Temperamental State | Psychophysical involuntary responses |
| Abhinaya | Representation | Acting/expression technique |
| Ä€á¹…gika | Gestural | Body-based representation |
| VÄcika | Verbal | Speech-based representation |
| Ä€hÄrya | Costume/Visual | Appearance-based representation |
| SÄttvika | Temperamental | Psychology-based representation |
| DharmÄ« | Practice | Mode of representation |
| Lokadharmi | Realistic | Everyday-life imitation |
| NÄá¹­yadharmi | Conventional | Theatrical stylization |
| Vá¹›tti | Style | Manner of presentation |
| Sandhi | Juncture | Plot structural unit |
| Vastu | Plot | Subject-matter/action |
| NÄá¹­aka | Drama | Complete dramatic form |
| Siddhi | Success | Achievement of dramatic effect |

---

*Compiled from Bharata Muni. Natyasastra: A Treatise on Hindu Dramaturgy and Histrionics. Translated by Manomohan Ghosh. Calcutta: Asiatic Society of Bengal, 1950.*
