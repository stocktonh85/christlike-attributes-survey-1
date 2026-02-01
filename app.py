import streamlit as st
from statistics import mean

st.set_page_config(
    page_title="Christlike Attributes Strengths Survey",
    page_icon="✨",
    layout="centered",
)

SCALE_HELP = "1 = Never • 2 = Sometimes • 3 = Often • 4 = Almost Always • 5 = Always"

ATTRIBUTES = {
    "Faith": [
        "I believe in Christ and accept Him as my Savior.",
        "I feel confident that God loves me.",
        "I trust the Savior enough to accept His will and do what He asks.",
        "I believe that through the Atonement of Jesus Christ and the power of the Holy Ghost, I can be forgiven of my sins and sanctified as I repent.",
        "I have faith that God hears and answers my prayers.",
        "I think about the Savior during the day and remember what He has done for me.",
        "I have faith that God will bring about good things in my life and the lives of others as we devote ourselves to Him and His Son.",
        "I know by the power of the Holy Ghost that the Book of Mormon is true.",
        "I have faith to accomplish what Christ wants me to do.",
    ],
    "Hope": [
        "One of my greatest desires is to inherit eternal life in the celestial kingdom.",
        "I am confident that I will have a happy and successful mission.",
        "I feel peaceful and optimistic about the future.",
        "I believe that someday I will dwell with God and become like Him.",
    ],
    "Charity and Love": [
        "I feel a sincere desire for the eternal welfare and happiness of others.",
        "When I pray, I ask for charity—the pure love of Christ.",
        "I try to understand others’ feelings and see their point of view.",
        "I forgive others who have offended or wronged me.",
        "I reach out in love to help those who are lonely, struggling, or discouraged.",
        "When appropriate, I express my love and care for others through word and deed.",
        "I look for opportunities to serve others.",
        "I say positive things about others.",
        "I am kind and patient with others, even when they are hard to get along with.",
        "I find joy in others’ achievements.",
    ],
    "Virtue": [
        "I am clean and pure in heart.",
        "I desire to do good.",
        "I focus on righteous, uplifting thoughts and put unwholesome thoughts out of my mind.",
        "I repent of my sins and strive to overcome my weaknesses.",
        "I feel the influence of the Holy Ghost in my life.",
    ],
    "Integrity": [
        "I am true to God at all times.",
        "I do not lower my standards or behavior so I can impress or be accepted by others.",
        "I am honest with God, myself, my leaders, and others.",
        "I am dependable.",
    ],
    "Knowledge": [
        "I feel confident in my understanding of gospel doctrine and principles.",
        "I study the scriptures daily.",
        "I seek to understand the truth and find answers to my questions.",
        "I seek knowledge and guidance through the Spirit.",
        "I cherish the doctrine and principles of the gospel.",
    ],
    "Patience": [
        "I wait patiently for the blessings and promises of the Lord to be fulfilled.",
        "I am able to wait for things without getting upset or frustrated.",
        "I am patient with the challenges of being a missionary.",
        "I am patient with others.",
        "I am patient with myself and rely on the Lord as I work to overcome my weaknesses.",
        "I face adversity with patience and faith.",
    ],
    "Humility": [
        "I am meek and lowly in heart.",
        "I rely on God for help.",
        "I am grateful for the blessings I have received from God.",
        "My prayers are earnest and sincere.",
        "I appreciate direction from my leaders or teachers.",
        "I strive to be submissive to God’s will.",
    ],
    "Diligence": [
        "I work effectively, even when I’m not under close supervision.",
        "I focus my efforts on the most important things.",
        "I have a personal prayer at least twice a day.",
        "I focus my thoughts on my calling as a missionary.",
        "I set goals and plan regularly.",
        "I work hard until the job is completed.",
        "I find joy and satisfaction in my work.",
    ],
    "Obedience": [
        "When I pray, I ask for strength to resist temptation and to do what is right.",
        "I am worthy to have a temple recommend.",
        "I willingly obey mission rules and follow the counsel of my leaders.",
        "I strive to live in accordance with the laws and principles of the gospel.",
    ],
}

DESCRIPTIONS = {
    "Faith": "You trust in Jesus Christ and act with confidence in His promises.",
    "Hope": "You look forward with peace and optimism, trusting God’s eternal promises.",
    "Charity and Love": "You sincerely care about others and seek to lift, understand, and serve.",
    "Virtue": "You seek purity in heart and mind and strive to live in a way that invites the Spirit.",
    "Integrity": "You aim to be honest and consistent with God, yourself, and others.",
    "Knowledge": "You value gospel learning and seek truth through study and the Spirit.",
    "Patience": "You trust God’s timing and endure challenges with steady faith.",
    "Humility": "You rely on God, stay teachable, and respond with gratitude.",
    "Diligence": "You work steadily and purposefully and find meaning in effort and responsibility.",
    "Obedience": "You willingly align your life with God’s commandments and inspired counsel.",
}

st.title("Christlike Attributes Strengths Survey")
st.caption("Anonymous • For personal reflection • Immediate results")
st.write(
    "There are no right or wrong answers. This is not a test. "
    "Answer based on what feels true *right now*."
)
st.info(SCALE_HELP)
st.divider()

# Collect responses
all_answered = True
responses = {}

for attr, items in ATTRIBUTES.items():
    st.subheader(attr)
    responses[attr] = []
    for i, text in enumerate(items, start=1):
        key = f"{attr}-{i}"
        val = st.radio(
            label=text,
            options=[1, 2, 3, 4, 5],
            horizontal=True,
            index=None,
            key=key,
            help=SCALE_HELP,
        )
        if val is None:
            all_answered = False
        else:
            responses[attr].append(int(val))
    st.divider()

if not all_answered:
    st.warning("Please answer every statement to see your results.")
    st.stop()

scores = {attr: mean(vals) for attr, vals in responses.items()}

# Rank: higher is better; stable tie-break by name
ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
top2 = ranked[:2]

# Focus: lowest; stable tie-break by name
focus = sorted(scores.items(), key=lambda x: (x[1], x[0]))[0]

st.header("Your Results")
st.write(
    "This is meant to help you reflect, not judge yourself. "
    "No one scores “always” in every area. Christlike growth is lifelong."
)

st.subheader("Christlike Strengths (Top 2)")
for name, _ in top2:
    st.markdown(f"**{name}** — {DESCRIPTIONS.get(name, '')}")

st.subheader("Prayerful Focus Attribute")
st.markdown(
    f"**{focus[0]}** — This is not a weakness. It may be an area the Lord invites you to strengthen next.\n\n"
    f"{DESCRIPTIONS.get(focus[0], '')}"
)

st.subheader("Reflection")
st.markdown(
    "- How can I use one of my strengths to bless others?\n"
    "- What is one small action I could take this week to strengthen my focus attribute?"
)
