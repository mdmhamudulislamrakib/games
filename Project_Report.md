# Project Report

## Table of Contents

Declaration\ti  
Course & Program Outcome\tii  
Introduction\t1  
Introduction\t1  
Motivation\t1  
Objectives\t1  
Feasibility Study\t1  
Gap Analysis\t1  
Project Outcome\t1  
System Architecture / Scene Description & Architecture\t2  
Requirement Analysis & Design Specification\t2  
Requirements\t2  
Sketch of project\t2  
Use of Modern Tools\t2  
Algorithm Used\t2  
2D Transformations Applied\t2  
Animation Logic\t2  
Implementation and Results\t3  
Implementation\t3  
Output\t3  
Discussion\t3  
Engineering Standards and Mapping\t4  
Impact on Society, Environment and Sustainability\t4  
Impact on Life\t4  
Impact on Society & Environment\t4  
Ethical Aspects\t4  
Sustainability Plan\t4  
Complex Engineering Problem\t4  
Mapping of Program Outcome\t4  
Complex Problem Solving\t4  
Engineering Activities\t5  
Conclusion\t6  
Summary\t6  
Limitation\t6  
Future Work\t6  
References\t6

---

## Declaration

I hereby declare that this mini project report titled **"Space Shooter Game Using Python OpenGL"** is an original work carried out by the project team as part of the academic curriculum under the guidance of the faculty mentor. The work submitted in this document has been developed through design, coding, testing, and analysis activities performed during the current semester.

I also declare that:

1. This report has not been submitted earlier for any degree, diploma, or certificate in this or any other institution.
2. All external ideas, APIs, and learning resources used in the development process are acknowledged in the references section.
3. The implementation and observations documented here represent actual project behavior observed during execution in the Python OpenGL environment.

Team members are fully responsible for the correctness of the presented material and for any future updates or maintenance of this project.

---

## Course & Program Outcome

This project was developed as part of a Computer Graphics related course with the purpose of translating classroom concepts into a working interactive software system. The project directly applies topics such as coordinate systems, 2D transformations, clipping assumptions, event-driven rendering, and geometric intersection logic.

The work also reinforces software engineering fundamentals including modular decomposition, interface handling, debugging, and report-driven documentation.

### Course Learning Alignment

1. Understand and implement OpenGL rendering primitives and pipeline setup.
2. Apply transformation operations to build composite objects.
3. Build event-driven graphical programs using callback mechanisms.
4. Integrate algorithmic logic with visual rendering in real-time.
5. Evaluate design trade-offs between accuracy, speed, and simplicity.

Program outcomes addressed:

1. Apply engineering knowledge to model and solve game logic and rendering problems.
2. Design and implement software components for interactive systems.
3. Use modern tools and programming libraries for simulation and visualization.
4. Analyze technical and social impact of software systems.
5. Work toward sustainable and ethical engineering practices.

### Outcome Contribution Summary

1. The project demonstrates measurable application of mathematics through line-circle intersection testing for hit detection.
2. It demonstrates software design through clear separation of scenes, input handlers, and draw routines.
3. It demonstrates professional practice through virtual environment usage and dependency management.
4. It demonstrates reflective engineering through impact and ethics analysis.

---

## Introduction

Computer graphics is a core engineering domain that connects mathematics, algorithms, and real-time systems to produce visual interaction. In modern applications, graphics is used in games, simulations, design tools, AR/VR systems, and educational interfaces. To understand these systems effectively, students must go beyond static examples and build complete interactive software.

This mini project presents a two-player 2D **Space Shooter** game implemented in Python using PyOpenGL and GLUT. The game includes complete scene flow, keyboard and mouse interaction, animation, collision logic, and winning conditions.

The game includes multiple views (intro, menu, instructions, gameplay, and game over), animated player spaceships, laser firing mechanics, collision detection, and health-based win conditions.

## Introduction

The central objective of this project is to demonstrate how graphics theory is transformed into a running software artifact. Instead of limiting implementation to a single static shape or basic animation, this project integrates:

1. Scene-level state management.
2. Composite object drawing using multiple primitives.
3. Real-time interaction and physics-like event checks.
4. Repetitive frame redraw using callback scheduling.

By doing so, the project becomes a compact but complete model of an interactive graphics application and an effective demonstration of practical engineering workflow.

## Motivation

Most introductory graphics exercises focus on drawing isolated objects without interaction, resulting in weak understanding of real application flow. This project is motivated by the need to build a coherent system where rendering, logic, and user controls are tightly integrated.

Primary motivation points:

1. Create an engaging academic demonstration instead of a static lab submission.
2. Learn how to organize medium-sized graphics code into reusable functions.
3. Explore practical collision detection methods suitable for real-time systems.
4. Demonstrate multiplayer interaction and fairness through deterministic rules.
5. Build a base project that can be extended into a full-featured game in future semesters.

## Objectives

1. Build a two-player game using Python and OpenGL.
2. Implement scene management for multiple interface screens.
3. Apply geometric transformations for object composition and movement.
4. Implement laser-based collision and health reduction.
5. Provide smooth user interaction through keyboard and mouse controls.

### Measurable Objectives

1. Maintain continuous display updates using idle redisplay callbacks.
2. Support at least five UI states: intro, menu, instructions, game, and game-over.
3. Ensure life values update in fixed decrements with lower bound protection.
4. Keep controls responsive under normal execution on student hardware.
5. Keep code modular enough for future additions like sound, scoring, and AI.

## Feasibility Study

Technical feasibility:

1. Python offers quick development and readability.
2. OpenGL via PyOpenGL supports low-level graphics drawing and transforms.
3. GLUT provides window creation and input callback handling.

Operational feasibility:

1. Runs on standard systems with Python and OpenGL dependencies installed.
2. Simple controls make the game usable without training.

Economic feasibility:

1. Open-source tools reduce cost to nearly zero.
2. Requires no specialized hardware.

Schedule feasibility:

1. The project scope is suitable for a mini-project timeline.
2. Development can be split into phases: drawing, controls, gameplay logic, testing, and documentation.

Risk feasibility:

1. Dependency risk is low because Python, OpenGL bindings, and GLUT are mature libraries.
2. Performance risk is manageable due to limited 2D complexity and primitive-based rendering.
3. Correctness risk in collision logic is handled through repeated gameplay testing.

## Gap Analysis

Existing simple demo projects often include only static shapes, no gameplay loop, and no multi-screen architecture. This project bridges that gap by integrating:

1. Complete game-state transitions.
2. Real-time user input handling.
3. Animated gameplay with health and winner logic.
4. Structured visual UI for intro/menu/instructions/game over.

### Comparative View

1. Conventional demos: isolated drawing without progression.
2. Proposed system: progression-based gameplay with deterministic outcomes.
3. Conventional demos: no game-state memory.
4. Proposed system: persistent states and transitions based on input/events.
5. Conventional demos: minimal user engagement.
6. Proposed system: two-player competition and replay capability.

## Project Outcome

The outcome is a functioning two-player Space Shooter game with:

1. Start screen and instruction interface.
2. Distinct spaceship/player visuals.
3. Directional laser firing.
4. Collision-driven health reduction.
5. Automatic winner declaration and replay support.

Additional outcomes achieved:

1. Practical understanding of transformation composition in a real object model.
2. Experience in balancing code readability with real-time loop constraints.
3. End-to-end documentation capability from requirements to impact analysis.
4. Foundation for integrating advanced modules in future work.

---

## System Architecture / Scene Description & Architecture

The system follows an event-driven architecture:

1. **Initialization Layer**: Sets projection (`gluOrtho2D`), screen dimensions, and OpenGL states.
2. **Input Layer**: Captures keyboard press/release and mouse events through GLUT callbacks.
3. **State Manager**: Controls view transitions using an enumerated `View` state.
4. **Render Layer**: Draws specific scenes and game entities each frame.
5. **Logic Layer**: Updates movement, firing direction, laser collision, and life values.

### Architectural Components in Detail

1. **Core Configuration**:
   - Defines viewport dimensions and movement speed constants.
   - Stores common geometric arrays for spaceship and alien components.
2. **Input Controller**:
   - Maintains `keyStates` for continuous movement and firing.
   - Maps mouse movement and click events for menu interaction.
3. **Scene Renderer**:
   - Renders each view independently to keep concerns separate.
   - Uses raster text for labels, life values, and instructions.
4. **Entity Renderer**:
   - Builds spaceship/alien models using polygon and line primitives.
   - Applies transformation stacking with push/pop matrix operations.
5. **Gameplay Engine**:
   - Updates position vectors.
   - Triggers laser rendering.
   - Runs contact checks and life updates.

Scene flow:

`Intro -> Menu -> Instructions or Game -> Game Over -> Menu/Game`

### Scene Description

1. **Intro Scene**:
   - Displays institutional details and project title.
   - Waits for ENTER key to proceed.
2. **Menu Scene**:
   - Presents Start, Instructions, and Quit options.
   - Uses cursor-based highlight and click selection.
3. **Instruction Scene**:
   - Displays key mappings for both players.
   - Includes back navigation.
4. **Gameplay Scene**:
   - Draws both players, life display, and active lasers.
   - Updates based on keyboard states each frame.
5. **Game Over Scene**:
   - Announces winner.
   - Returns user to menu for replay.

---

## Requirement Analysis & Design Specification

The design adopts a function-oriented modular structure where each concern is implemented in a separate callable unit. This improves readability, debugging ease, and extension capability.

### Design Principles Used

1. **Single Responsibility**: Each function has one clear rendering or logic task.
2. **State Isolation**: View transitions are controlled through enumerated values.
3. **Incremental Rendering**: Scene is redrawn each cycle using current state variables.
4. **Data Simplicity**: Primitive lists and scalar values are used for performance and clarity.

## Requirements

Functional requirements:

1. Display intro, menu, instructions, gameplay, and game-over views.
2. Support two-player movement and shooting controls.
3. Detect laser contact and reduce opponent life.
4. Show life bars and announce winner.

Non-functional requirements:

1. Real-time response to user input.
2. Readable and modular source code.
3. Compatibility with standard Python runtime.

Interface requirements:

1. Keyboard support for both players with non-overlapping key sets.
2. Mouse hover and click support for menu buttons.
3. Stable window rendering at specified dimensions.

Performance requirements:

1. Scene updates should feel continuous during gameplay.
2. Input lag should remain low enough for two-player competition.

Reliability requirements:

1. Life value should never become negative.
2. Invalid state transitions should not crash the game loop.

## Sketch of project

Conceptual sketch:

1. Left and right spaceship entities facing each other.
2. Heads-up display at top showing life values.
3. Laser line emitted in chosen direction.
4. Boundary-framed menu with selectable options.

Layout description for report readers:

1. Coordinate system is centered around a symmetric orthographic projection.
2. Player entities are positioned opposite to each other with mirrored rendering.
3. HUD area is reserved at upper corners for life indicators.
4. Interaction zones in the menu are rectangular regions with text overlays.

## Use of Modern Tools

1. **Python 3** for application logic.
2. **PyOpenGL** for rendering primitives and transformations.
3. **GLUT** for window lifecycle and event callbacks.
4. **Virtual environment** for dependency isolation.

Additional tool usage context:

1. Source code is organized into modular files for experimentation and testing.
2. Environment setup through virtual environment improves reproducibility.
3. Standard package management allows easy deployment across machines.
4. Open-source ecosystem enables low-cost academic development.

## Algorithm Used

Core algorithms:

1. **Game State Switching** using finite state transitions.
2. **Input Polling + Key State Array** for continuous movement/shoot actions.
3. **Collision Approximation**:
   - Laser represented by line equation.
   - Target approximated by bounding sphere.
   - Discriminant-based intersection check.
4. **Health Update Rule**:
   - On hit: `life = max(0, life - 5)`.

### Algorithmic Flow (High Level)

1. Initialize display, projection, input callbacks, and state variables.
2. Enter continuous render loop.
3. Process current key states and mouse action.
4. Render scene based on active state.
5. In gameplay state, compute movement and laser behavior.
6. Evaluate hit logic and update life.
7. If any life value reaches zero, move to game-over state.

### Collision Logic Details

1. Laser trajectory is represented using start point and directional end point.
2. Line equation is computed as `y = mx + k`.
3. Opponent body is approximated by a circle with fixed radius.
4. Substituting the line equation into circle equation yields quadratic form.
5. If discriminant is non-negative, an intersection is assumed and life is reduced.

This method offers acceptable speed and simplicity for a student-level real-time game.

## 2D Transformations Applied

The project uses key transformations:

1. **Translation (`glTranslated`)** for positioning spaceships and components.
2. **Scaling (`glScalef`)** for resizing body parts and scene-level effects.
3. **Rotation (`glRotated`)** for eye and component orientation.
4. **Mirroring (`glScalef(-1, 1, 1)`)** to render the second player symmetrically.

### Mathematical Basis

1. Translation matrix:

$$
T =
\begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
$$

2. Scaling matrix:

$$
S =
\begin{bmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

3. Rotation matrix:

$$
R =
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Composite modeling is implemented through matrix stack operations (`glPushMatrix` and `glPopMatrix`) to avoid transformation side effects across objects.

## Animation Logic

Animation is achieved by continuous redraw in the idle loop and frame-wise updates:

1. Keyboard state is checked each frame.
2. Position variables update by constant speed increments.
3. Laser visibility toggles based on firing keys.
4. Dynamic color cycling and transformed components give motion feel.

### Frame Update Sequence

1. `glutIdleFunc(glutPostRedisplay)` requests continuous repaint.
2. Display callback clears frame buffer.
3. Input operation function updates movement/fire states.
4. Active scene is rendered using updated state values.
5. Buffers are flushed/swapped to present next frame.

### Animation Quality Considerations

1. Constant speed produces predictable motion suitable for two-player control.
2. Direct key-state polling avoids missed movement during key hold.
3. Lightweight primitives keep frame generation efficient.

---

## Implementation and Results

## Implementation

Implementation highlights:

1. Global constants define world dimensions and speed.
2. Separate drawing functions build complex characters from primitives.
3. Screen rendering is modularized by state.
4. Input callbacks maintain key and mouse states.
5. Winner logic is triggered when any life value reaches zero.

### Module-Wise Implementation Description

1. **Initialization Module**:
   - Sets orthographic projection and initial OpenGL state.
2. **Text and UI Module**:
   - Renders menu labels, instructions, life values, and status messages.
3. **Entity Rendering Module**:
   - Draws alien body parts and spaceship structure via reusable functions.
4. **Control Module**:
   - Handles keyboard press/release and mouse activity through GLUT callbacks.
5. **Game Logic Module**:
   - Updates positions, firing, collision detection, and state transition to game-over.

### Implementation Decisions and Justification

1. A key-state array is used instead of one-shot key events to support smooth movement while holding keys.
2. Primitive-based modeling is used to clearly demonstrate graphics fundamentals.
3. Collision approximation is selected to keep computation inexpensive and implementation understandable.
4. Fixed decrement health model provides transparent and fair gameplay behavior.

## Output

Observed output behavior:

1. Intro screen with project and institutional text.
2. Interactive menu with Start, Instructions, and Quit.
3. Gameplay with two controllable spaceships and directional shooting.
4. Life values decrease upon successful hit.
5. Game-over screen displays winner and allows replay via menu.

### Sample Gameplay Observation

1. User launches program and sees intro screen.
2. Pressing ENTER transitions to menu.
3. Mouse hover highlights selected button; click starts game.
4. Both players move independently and attempt to target opponent.
5. Every successful hit reduces opponent life by 5.
6. On reaching zero life, winner message appears.
7. User can restart from menu without restarting the program process.

### Test Scenarios Executed

1. Scene transition correctness for all valid paths.
2. Key-mapping correctness for both players.
3. Laser direction toggling with vertical key modifiers.
4. Life update accuracy and non-negative bound check.
5. Replay behavior after game-over state.

## Discussion

The project successfully integrates core graphics topics with interactive logic in a single executable program. It demonstrates that even a moderate codebase can provide clear evidence of transformation usage, event handling, and scene-state control when organized modularly.

### Strengths

1. Strong educational value due to visible relation between code and rendered behavior.
2. Effective decomposition into rendering and logic functions.
3. Stable scene architecture with deterministic transitions.
4. Replayable gameplay loop suitable for demonstration and evaluation.

### Improvement Areas

1. Collision can be made more geometrically accurate.
2. Frame rate instrumentation can be added for performance study.
3. Code can be further refactored into object-oriented architecture.
4. Gameplay can be enhanced with boundary checks, scoring, and effects.

---

## Engineering Standards and Mapping

The implementation aligns with software engineering and graphics programming practices:

1. Functional decomposition for maintainability.
2. Reusable drawing routines.
3. Deterministic state transitions.
4. Input-validation through bounded control logic.

### Standards Followed in Practice

1. **Modularity Standard**: Functions grouped by concern.
2. **Traceability Standard**: Requirements mapped to implemented behavior and observed results.
3. **Testability Standard**: Scenarios created for controls, transitions, and life updates.
4. **Maintainability Standard**: Constants and reusable shape definitions reduce duplication.

### Quality Attributes Achieved

1. Usability through simple keyboard/mouse interaction.
2. Reliability through constrained state and value updates.
3. Performance through lightweight primitive rendering.
4. Extensibility via clear scene and function boundaries.

## Impact on Society, Environment and Sustainability

This section evaluates wider implications beyond technical execution. Even small educational software projects influence learning quality, software practice, and resource usage.

## Impact on Life

1. Encourages creative learning in programming and graphics.
2. Improves problem-solving and logical thinking skills.
3. Promotes collaborative team development experience.
4. Builds confidence in converting abstract formulas into working software.
5. Encourages disciplined debugging and documentation habits.

## Impact on Society & Environment

1. Educational games can improve engagement in technical subjects.
2. Digital simulations reduce need for physical resources used in conventional prototypes.
3. Open-source tooling reduces financial barriers for learners.
4. Reusable academic codebases reduce repeated development effort and associated energy consumption.

## Ethical Aspects

1. Promotes fair-play logic in competitive interaction.
2. Uses open-source libraries responsibly.
3. Avoids collection of personal user data.
4. Maintains transparent game rules and deterministic outcomes.
5. Encourages proper attribution of external resources and references.

## Sustainability Plan

1. Reuse the codebase for future academic batches.
2. Maintain dependency versions through virtual environments.
3. Extend as an educational template rather than building from scratch repeatedly.
4. Add lightweight code profiling before adding heavy graphical effects.
5. Maintain versioned documentation for long-term knowledge transfer.

## Complex Engineering Problem

The problem combines geometry, interaction, and rendering under real-time constraints, requiring integration of:

1. Mathematical modeling of collision.
2. User-input driven control flow.
3. Dynamic scene updates with consistent frame output.

### Why It Qualifies as a Complex Engineering Problem

1. Multi-domain integration is required: mathematics, graphics APIs, and software architecture.
2. Runtime correctness depends on synchronized behavior across multiple callback-based modules.
3. Trade-offs must be made between collision accuracy and execution simplicity.
4. System must remain stable under unpredictable user input patterns.

### Constraints Considered

1. Limited development time and student-level resources.
2. Need for understandable implementation for academic evaluation.
3. Cross-platform dependency constraints of graphics libraries.

## Mapping of Program Outcome

1. **PO1 (Engineering Knowledge)**: Applied graphics and mathematics in game rendering.
2. **PO2 (Problem Analysis)**: Analyzed collision and state-transition challenges.
3. **PO3 (Design/Development)**: Built complete user-interactive software.
4. **PO5 (Modern Tool Usage)**: Used Python, OpenGL, GLUT toolchain.
5. **PO6/PO7 (Society/Environment)**: Reflected impacts of digital educational tools.

### Detailed PO Mapping Matrix

1. **PO1**: Orthographic projection, geometric modeling, and transformation composition.
2. **PO2**: Collision method selection and game-state consistency checks.
3. **PO3**: End-to-end implementation of scenes, controls, and game outcomes.
4. **PO4**: Functional testing through repeated scenario-based validation.
5. **PO5**: Effective use of PyOpenGL, GLUT callbacks, and Python virtual environment.
6. **PO9/PO10**: Team coordination and report communication practices.
7. **PO12**: Self-learning and iterative improvement through debugging and extension planning.

## Complex Problem Solving

Problem-solving steps followed:

1. Break project into screen, object, and logic modules.
2. Build and test each component independently.
3. Integrate and verify transitions and gameplay outcomes.
4. Refine controls and collision accuracy through repeated testing.

### Engineering Method Adopted

1. Requirement analysis and feature boundary definition.
2. Prototype rendering and coordinate verification.
3. Integration of control logic and frame update loop.
4. Introduction of hit detection and life model.
5. Validation against expected behavior and defect correction.
6. Documentation of results, limitations, and future roadmap.

## Engineering Activities

1. Requirement gathering and scope finalization.
2. Design of game scenes and object structure.
3. Development and integration of rendering plus logic.
4. Testing and debugging of controls, transitions, and hit detection.
5. Documentation and report preparation.

### Suggested Activity Timeline (Indicative)

1. Week 1: Problem selection, requirement drafting, environment setup.
2. Week 2: Intro/menu/instructions screen implementation.
3. Week 3: Spaceship modeling and transformation tuning.
4. Week 4: Input controls and continuous movement logic.
5. Week 5: Laser mechanics, collision checks, life management.
6. Week 6: Testing, bug fixing, and final documentation.

---

## Conclusion

The project achieved its primary goal of building a playable two-player 2D Space Shooter that demonstrates important graphics and engineering concepts in one integrated system. The implementation confirms practical understanding of rendering pipeline setup, transformation composition, callback-driven interaction, and algorithmic event handling.

The completed project is academically valuable because it maps directly to course outcomes while remaining extendable for advanced features.

## Summary

1. Multi-scene architecture was successfully implemented.
2. Two-player interaction and firing mechanics were completed.
3. 2D transformations and real-time animation were demonstrated.
4. Collision-based health and winner logic worked as expected.
5. Structured evaluation and impact analysis were documented.
6. Extension pathways were identified for future development cycles.

## Limitation

1. Collision model is approximate and may register edge-case hits.
2. No textures, audio, or advanced visual effects.
3. No single-player AI mode.
4. Limited balancing and gameplay depth.
5. Runtime metrics such as FPS and latency are not yet instrumented.
6. Boundary and obstacle mechanics are currently minimal.

## Future Work

1. Add sprite textures and background effects.
2. Include sound effects and background music.
3. Implement AI opponent and difficulty levels.
4. Add scoring system and power-ups.
5. Improve collision with pixel-perfect or polygon methods.
6. Add pause/resume and settings screen for usability.
7. Introduce frame-timed movement for consistent speed across systems.
8. Store match history and performance analytics.
9. Refactor into class-based architecture for larger feature growth.
10. Explore OpenGL shader-based visual enhancements for advanced coursework.

## References

1. PyOpenGL Documentation, official project resources.
2. OpenGL Programming Guide (introductory concepts).
3. GLUT API references for callback and window handling.
4. Python 3 official documentation.
5. Classroom notes on Computer Graphics and 2D transformations.
6. Foley, van Dam et al., *Computer Graphics: Principles and Practice*.
7. Interactive Computer Graphics lecture materials (institutional handouts).
8. Python virtual environment and packaging best-practice guides.
