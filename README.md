# Algopedia

This is a two-fold exercise for me. 

The principle tagline is  **"Code by Ed, Tests by AI"**

## First Goal: Fun with Code
I'm writing all of the algorithms and data structures (mostly so I can stay relevant.) As I get older and spend more time in meetings, I want to keep my hands on the keyboard as much as time allows. 

My code probably sucks, but that's ok. Feel free to send me recommendations for what to do with the rest of my career at me@emangini.com.


## Second Goal: AIAIO
The second aspect is to use AI more in my daily work.... as a result the tests are fully AI generated. 

### What does this mean? 
- AI tool(s) (Claude, Junie, Copilot, Jetbrains AI Assistant, Cursor, etc.) get "first whack" for tests.
- YES.. I do swap out tool(s) haphazardly to play around with the results.
- YES.. I do iterate on the prompts to increase the tests.
- YES.. I try VERY VERY hard to keep the tests unchanged by the AI. My primary metrics are "readability and functional accuracy". As long as the tests work and they are reasonble "understandable", I won't touch them.

- YES.. I have and will intervene and write the damn tests when AI fails.

### Tools

Most of the tools being used are Junie / AI Assistant (Jetbrains), leveraging Claude Sonnet 4. 

I've compared results by using Claude directly. (Most of the results are close enough to assume that either system could generate the tests). 

### Challenges. 

When some tests fail, the AI applications want to change the algorithm / data structure code. I've updated my prompts to request human validation w/ mixed results. (Junie flat out ignores this most of the time). 
