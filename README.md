## Semafix: Going forward, together

### What is Semafix?

Semafix is the name of a software that controls an intelligent traffic light system,
using a high-resolution camera, an algorithm available in many languages, and image
recognition libraries available on GitHub.

### What purpose does it serve?

Semafix was made by @PeterSaturniVega to help drivers save time and patience when
dealing with empty lanes on intersections, instead of having to wait decent amounts
of time when a lane is empty, or when a lane has too many vehicles.

### How does it work?

As soon as the program detects there is an empty lane, or a lane with too many
vehicles:

1. The four cameras capture each one an image of their respective lanes.
2. The images are sent to a central processor at the control box of the
intersection, where they are measured and examinated by the previously mentioned
algorithm.
3. The algorithm determines how many vehicles are in each lane, and their wait time,
and with these facts it determines which lane should be assigned a green light.

And the process repeats itself if the conditions still apply.

### Who works on the project?

Currently, only @SaturniNovaDev and @Migueldev67 are actively working on the
project, but we accept new collaborators, pull requests (that make sense), and
suggestions that could potentially make the code better.
