# Spin of Light - Development Log

## 🎮 Project Overview
A physics-based puzzle-platformer where you play as a magical dreidel brought to life by the last spark of Hanukkah's final candle. Complete 9 nights to rekindle the light across the world.

---

## 📋 Development Roadmap

### Phase 1: Core Foundation (Week 1-2)

#### Step 1: Physics System
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Create `physics_system.py` with gravity, velocity, acceleration
- [ ] Implement momentum-based movement (inertia)
- [ ] Add collision detection (AABB or pixel-perfect)
- [ ] Test with simple rectangles

**Notes:**
- 

---

#### Step 2: Dreidel Entity
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Create `dreidel.py` with basic sprite
- [ ] Implement left/right movement with momentum
- [ ] Add jump mechanic (bounce height tied to speed)
- [ ] Add spin animation (rotation based on velocity)
- [ ] Implement particle trail system

**Notes:**
- 

---

#### Step 3: Platform System
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Create base `platform.py` class
- [ ] Implement collision with dreidel
- [ ] Add platform types: solid, one-way (jump through)

**Notes:**
- 

---

#### Step 4: Camera System
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Create `camera_system.py`
- [ ] Implement smooth follow (lerp)
- [ ] Add bounds to keep camera in level

**Notes:**
- 

---

### Phase 2: Level Infrastructure (Week 2-3)

#### Step 5: Level Loading
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Create `level_loader.py`
- [ ] Design JSON format for levels (platforms, candle position, spawn point)
- [ ] Implement level parsing and entity spawning

**Notes:**
- 

---

#### Step 6: Candle Goal
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Create `candle.py` entity
- [ ] Add collision detection with dreidel
- [ ] Implement "lighting" animation and effect

**Notes:**
- 

---

#### Step 7: Night Base Class
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Create `night_base.py` inheriting from `BaseState`
- [ ] Add level loading in `startup()`
- [ ] Implement win condition (reach candle → transition)
- [ ] Add restart functionality

**Notes:**
- 

---

#### Step 8: Build Night 1
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Create simple test level in `night_1.json`
- [ ] Implement basic platforming challenge
- [ ] Test full loop: spawn → move → light candle → next state

**Notes:**
- 

---

### Phase 3: Visual Polish (Week 3-4)

#### Step 9: Particle System
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Create `particle_system.py`
- [ ] Implement spark particles trailing dreidel
- [ ] Add candle glow effect
- [ ] Create candle bloom effect (color burst when lit)

**Notes:**
- 

---

#### Step 10: Parallax Backgrounds
**Status:** ⬜ Not Started  
**Priority:** 🟢 Medium

- [ ] Create `parallax_system.py`
- [ ] Load layered backgrounds for each night
- [ ] Implement scroll speed based on camera

**Notes:**
- 

---

#### Step 11: Transitions
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Create `transition.py` UI component
- [ ] Fade to black between nights
- [ ] Add "Night X" title card

**Notes:**
- 

---

#### Step 12: Visual Assets
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Create/find dreidel sprite
- [ ] Create candle sprites (lit/unlit)
- [ ] Design platform sprites
- [ ] Design backgrounds for each night (different palettes)

**Notes:**
- 

---

### Phase 4: Audio System (Week 4)

#### Step 13: Audio Manager
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Create `audio_system.py`
- [ ] Implement layered music system (start with base, add layers)
- [ ] Add SFX manager (spin, jump, bounce, land, candle light)

**Notes:**
- 

---

#### Step 14: Sound Assets
**Status:** ⬜ Not Started  
**Priority:** 🟢 Medium

- [ ] Create/find ambient base track
- [ ] Create 9 instrument layers (one per candle)
- [ ] Create sound effects

**Notes:**
- 

---

### Phase 5: Mechanics & Nights (Week 5-7)

#### Step 15: Special Platform Types
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] `ice_platform.py` - Reduced friction
- [ ] `bouncy_platform.py` - High bounce multiplier
- [ ] `moving_platform.py` - Moves on path
- [ ] `rotating_platform.py` - Rotates around center

**Notes:**
- 

---

#### Step 16: Wind System
**Status:** ⬜ Not Started  
**Priority:** 🟢 Medium

- [ ] Create `wind_zone.py` - Invisible area applying force
- [ ] Test with dreidel physics

**Notes:**
- 

---

#### Step 17: Build Remaining Nights
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Night 2 - Ice platforms (slippery)
- [ ] Night 3 - Moving platforms (timing)
- [ ] Night 4 - Rotating platforms (precision)
- [ ] Night 5 - Switch/multi-dreidel puzzle (unity theme)
- [ ] Night 6 - Bouncy platforms (high jumps)
- [ ] Night 7 - Wind zones (air control)
- [ ] Night 8 - Light puzzles (darkness + glow)
- [ ] Night 9 - Final challenge (all mechanics)

**Notes:**
- 

---

### Phase 6: Story & Flow (Week 7-8)

#### Step 18: Menu Screens
**Status:** ⬜ Not Started  
**Priority:** 🟢 Medium

- [ ] Polish `menu.py` with visual design
- [ ] Add `splash_screen.py` (opening scene)
- [ ] Create `pause_menu.py` (restart, quit, resume)

**Notes:**
- 

---

#### Step 19: Ending Sequence
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Create `ending.py` state
- [ ] Show all 9 candles lit
- [ ] Dreidel fades into light
- [ ] Play full music with all layers

**Notes:**
- 

---

#### Step 20: Credits
**Status:** ⬜ Not Started  
**Priority:** 🔵 Low

- [ ] Create `credits.py` state
- [ ] List contributors, tools, music

**Notes:**
- 

---

### Phase 7: Polish & Testing (Week 8-9)

#### Step 21: Playtesting
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Test each night for difficulty balance
- [ ] Adjust physics parameters in `physics_config.json`
- [ ] Ensure smooth progression

**Notes:**
- 

---

#### Step 22: Juice & Feel
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Add screen shake on landing
- [ ] Enhance particle effects
- [ ] Fine-tune camera smoothing
- [ ] Add subtle background animations

**Notes:**
- 

---

#### Step 23: Bug Fixing
**Status:** ⬜ Not Started  
**Priority:** 🔴 Critical

- [ ] Fix collision edge cases
- [ ] Test platform interactions
- [ ] Ensure audio doesn't overlap weirdly

**Notes:**
- 

---

#### Step 24: Performance
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Optimize particle count
- [ ] Test on target hardware
- [ ] Ensure 60fps stability

**Notes:**
- 

---

### Phase 8: Release Preparation (Week 9-10)

#### Step 25: Documentation
**Status:** ⬜ Not Started  
**Priority:** 🟢 Medium

- [ ] Write `README.md` with story, controls, credits
- [ ] Add installation instructions

**Notes:**
- 

---

#### Step 26: Packaging
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Test standalone build (PyInstaller or similar)
- [ ] Create game icon
- [ ] Prepare itch.io page

**Notes:**
- 

---

#### Step 27: Final Polish
**Status:** ⬜ Not Started  
**Priority:** 🟡 High

- [ ] Add options menu (volume, fullscreen toggle works)
- [ ] Ensure all states transition smoothly
- [ ] Final playthrough

**Notes:**
- 

---

## 🎯 Implementation Guidelines

### Physics Considerations
- Spin speed affects jump height
- Momentum carries through air
- Landing reduces spin slightly (friction)
- Each platform type modifies physics differently

### Level Design Philosophy
- **Night 1:** Tutorial (just movement)
- **Nights 2-8:** One new mechanic each
- **Night 9:** Combination of everything

### Visual Identity
- Each night has unique color palette
- Warm candlelight hues (orange, yellow, blue)
- Minimal UI (only night number, subtle)

### Audio Design
- Start with drone/ambient base
- Each candle adds an instrument
- By Night 9, full orchestra plays

---

## 📊 Progress Tracker

| Phase | Status | Completion |
|-------|--------|------------|
| Phase 1: Core Foundation | ⬜ Not Started | 0% |
| Phase 2: Level Infrastructure | ⬜ Not Started | 0% |
| Phase 3: Visual Polish | ⬜ Not Started | 0% |
| Phase 4: Audio System | ⬜ Not Started | 0% |
| Phase 5: Mechanics & Nights | ⬜ Not Started | 0% |
| Phase 6: Story & Flow | ⬜ Not Started | 0% |
| Phase 7: Polish & Testing | ⬜ Not Started | 0% |
| Phase 8: Release Preparation | ⬜ Not Started | 0% |

**Overall Progress:** 0%

---

## 📝 Development Journal

### [Date] - Entry Title
*Write your daily development notes, challenges, breakthroughs, and decisions here.*

---

## 🐛 Known Issues
- *Track bugs and issues here*

---

## 💡 Ideas & Future Features
- *Track potential features, improvements, and creative ideas here*

---

## 🙏 Credits & Resources
- **Engine:** luneth_engine (custom)
- **Framework:** Pygame
- **Art:** [To be determined]
- **Music:** [To be determined]
- **Sound Effects:** [To be determined]

---

**Last Updated:** [Date]



Status Icons:

⬜ Not Started
🟦 In Progress
✅ Complete

Priority Levels:

🔴 Critical
🟡 High
🟢 Medium
🔵 Low