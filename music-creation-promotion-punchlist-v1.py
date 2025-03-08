import streamlit as st

# Title
st.title("Music Creation & Promotion Punchlist")

# Categories and tasks
punchlist = {
    "Writing": [
        "Brainstorm song ideas/themes",
        "Write lyrics (verse, chorus, bridge, etc.)",
        "Develop melody or beat structure",
        "Revise lyrics for flow and rhyme",
        "Finalize song structure"
    ],
    "Recording": [
        "Set up recording equipment (mic, interface, DAW)",
        "Record instrumental tracks",
        "Record vocal takes (lead and harmonies)",
        "Capture ad-libs or additional layers",
        "Review takes and select the best ones"
    ],
    "Editing": [
        "Trim and align audio clips",
        "Remove background noise",
        "Adjust timing and pitch correction",
        "Add effects (reverb, delay, etc.)",
        "Export rough edit for review"
    ],
    "Mixing": [
        "Balance levels (vocals, instruments, drums)",
        "Apply EQ to each track",
        "Add compression and dynamics processing",
        "Pan elements for stereo imaging",
        "Create a cohesive mix"
    ],
    "Mastering": [
        "Polish the final mix",
        "Adjust overall loudness (LUFS)",
        "Ensure consistency across tracks (for albums)",
        "Export in multiple formats (WAV, MP3)",
        "Test on different playback systems"
    ],
    "Copywriting": [
        "Write song descriptions for platforms",
        "Create artist bio",
        "Draft press release for release",
        "Prepare social media captions",
        "Develop marketing taglines"
    ],
    "Publishing": [
        "Register songs with PRO (ASCAP, BMI, etc.)",
        "Secure copyright for lyrics and music",
        "Assign ISRC codes for tracks",
        "Verify metadata (title, artist, genre)",
        "Submit to publishing platforms"
    ],
    "Uploading": [
        "Upload to distribution platforms (Distrokid, TuneCore, etc.)",
        "Add artwork and metadata",
        "Set release date and pre-save links",
        "Upload to SoundCloud/YouTube (if applicable)",
        "Share stems/backing tracks (optional)"
    ],
    "Sharing": [
        "Post on social media (X, Instagram, TikTok)",
        "Send to playlist curators",
        "Email to fans/subscribers",
        "Share with collaborators for promotion",
        "Submit to blogs/radio stations"
    ],
    "Calling": [
        "Contact producers for collabs",
        "Reach out to venues for gigs",
        "Call playlist curators or DJs",
        "Follow up with distributors/marketers",
        "Coordinate with team (manager, publicist)"
    ],
    "Scheduling": [
        "Plan recording sessions",
        "Set mixing/mastering deadlines",
        "Schedule release dates",
        "Book marketing campaigns",
        "Arrange tour dates and rehearsals"
    ],
    "Music Marketing": [
        "Create promotional graphics/videos",
        "Run ads (social media, Google)",
        "Engage fans on X and other platforms",
        "Launch pre-save campaigns",
        "Plan live stream or release party"
    ],
    "Music Sales": [
        "Set pricing for digital/physical copies",
        "Offer merch bundles (shirts, vinyl)",
        "Track sales analytics",
        "Adjust pricing based on demand",
        "Promote discount codes"
    ],
    "Touring": [
        "Book venues and dates",
        "Arrange travel and accommodations",
        "Rehearse setlist with band",
        "Promote tour dates online",
        "Sell tickets and VIP packages"
    ]
}

# Display checklist
for category, tasks in punchlist.items():
    st.subheader(category)
    for task in tasks:
        st.checkbox(task)

# Footer
st.write("Check off tasks as you complete them!")
