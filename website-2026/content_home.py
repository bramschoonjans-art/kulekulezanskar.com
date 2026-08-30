# -*- coding: utf-8 -*-
"""Home page."""

from build import Page, todo, wa_link, img, SITE, BRAND, EMAIL, WHATSAPP_DISPLAY

HERO = dict(
    image="/assets/images/itinerary/day-1.jpg",
    alt="The Zanskar valley in evening light, the river braiding through fields far below the trail",
    eyebrow="Zanskar · Ladakh · India",
    h1="Zanskar, from the inside",
    intro="Walk quiet valleys, sleep under the passes and meet the people who live here — "
          "guided by two friends who grew up in the middle of it.",
    buttons=('<a class="btn btn--light" href="/zanskar/">Explore Zanskar</a>'
             '<a class="btn btn--outline-light" href="/journeys/">See our journeys</a>'),
    **{"class": "hero--tall"}
)

BODY = """
<!-- 02 · positioning -->
<div class="section">
  <div class="wrap wrap--narrow">
    <p class="label">Kulé kulé Zanskar</p>
    <h2>One region, walked slowly, with the people who know it</h2>
    <p class="lede" style="margin-top:20px">We are Stanzin Chotak and Stanzin Lhamath, childhood friends from Zangla,
      a village in the north of the Zanskar valley. We guide trekking routes, cultural journeys and trips built
      around your own dates — all of them here, in the region we come from.</p>
    <p><em>Kulé kulé</em> means slowly, slowly. It is how we walk, how we let you acclimatise, and how we think
      this place is best understood. <a href="/about/">More about how we work</a>.</p>
    <dl class="facts" style="margin-top:32px">
      <div><dt>Based in</dt><dd>Zangla, Zanskar</dd></div>
      <div><dt>Group size</dt><dd>2 to 10 people</dd></div>
      <div><dt>Booked</dt><dd>Directly with the guides</dd></div>
      <div><dt>Season</dt><dd>June – September</dd></div>
    </dl>
  </div>
</div>

<!-- 03 · the guides -->
<div class="section section--band">
  <div class="wrap">
    <div class="section__head">
      <p class="label">The guides</p>
      <h2>You will be walking with Chotak and Lhamath</h2>
      <p>We were born in Zangla and started guiding on paths our families have used for generations.
         Most of what a guide does here is not showing people things. It is deciding when to stop.</p>
    </div>
    <div class="grid grid--2">
      <article class="card">
        <div class="card__body">
          <h3><a href="/guides/stanzin-chotak/">Stanzin Chotak</a></h3>
          <ul class="meta"><li>Born in Zangla</li><li>Ladakhi, Hindi, English</li></ul>
          <p>{chotak}</p>
          <a class="arrow-link" href="/guides/stanzin-chotak/">Read his profile</a>
        </div>
      </article>
      <article class="card">
        <div class="card__body">
          <h3><a href="/guides/stanzin-lhamath/">Stanzin Lhamath</a></h3>
          <ul class="meta"><li>Born in Zangla</li><li>Ladakhi, Hindi, English</li></ul>
          <p>{lhamath}</p>
          <a class="arrow-link" href="/guides/stanzin-lhamath/">Read his profile</a>
        </div>
      </article>
    </div>
    <p style="margin-top:28px"><a class="arrow-link" href="/guides/">Meet the whole team, including the crew</a></p>
  </div>
</div>

<!-- 04 · ways to travel -->
<div class="section">
  <div class="wrap">
    <div class="section__head">
      <p class="label">Journeys</p>
      <h2>Different ways to spend time here</h2>
      <p>All of our journeys cover the same region and are led by the same people. What changes is the pace,
         the terrain, and how much of it you sleep outside.</p>
    </div>
    <div class="grid grid--3">
      <article class="card">
        <div class="card__media">{img_phuktal}</div>
        <div class="card__body">
          <span class="tag">Trekking</span>
          <h3 style="margin-top:10px"><a href="/journeys/zangla-to-phuktal-trek/">Zangla to Phuktal</a></h3>
          <ul class="meta"><li>6 days</li><li>Camping</li><li>Demanding</li></ul>
          <p>Wide valleys, high passes and camp life, ending at a monastery built into a cliff above the Tsarap.</p>
          <a class="arrow-link" href="/journeys/zangla-to-phuktal-trek/">See the route</a>
        </div>
      </article>
      <article class="card">
        <div class="card__media">{img_tsok}</div>
        <div class="card__body">
          <span class="tag">Trekking</span>
          <h3 style="margin-top:10px"><a href="/journeys/phuktal-to-tsokmichik-trek/">Phuktal to Tsokmichik</a></h3>
          <ul class="meta"><li>8 days</li><li>Camping</li><li>Serious</li></ul>
          <p>Most people reach the monastery and turn around. This route starts there and keeps going east.</p>
          <a class="arrow-link" href="/journeys/phuktal-to-tsokmichik-trek/">See the route</a>
        </div>
      </article>
      <article class="card">
        <div class="card__media">{img_cult}</div>
        <div class="card__body">
          <span class="tag tag--mineral">Cultural</span>
          <h3 style="margin-top:10px"><a href="/journeys/zanskar-cultural-journey/">Villages and monasteries</a></h3>
          <ul class="meta"><li>7 days</li><li>Beds at night</li><li>Easy to moderate</li></ul>
          <p>The valley without the tent: Padum, the great monasteries, village days and short walks.</p>
          <a class="arrow-link" href="/journeys/zanskar-cultural-journey/">See the journey</a>
        </div>
      </article>
    </div>
    <p style="margin-top:28px">Nothing here fits your dates or your group?
       <a href="/journeys/tailor-made/">We build journeys to order</a> — that is how most of our trips start.</p>
  </div>
</div>

<!-- 05 · places -->
<div class="section section--band">
  <div class="wrap">
    <div class="section__head">
      <p class="label">The region</p>
      <h2>Places worth knowing before you come</h2>
      <p>Zanskar is not one valley but several, joined by rivers and separated by passes.
         These are good places to start reading.</p>
    </div>
    <div class="mosaic">
      <figure>{img_m1}<figcaption><a href="/zanskar/phuktal-monastery/">Phuktal Monastery</a>
        <span>A cave monastery above the Tsarap, reached on foot</span></figcaption></figure>
      <figure>{img_m2}<figcaption><a href="/zanskar/the-region/">The Lungnak valley</a>
        <span>The dry corridor that carries the Tsarap towards Padum</span></figcaption></figure>
      <figure>{img_m3}<figcaption><a href="/zanskar/zangla/">Zangla</a>
        <span>Our village, its ruined fort and its barley fields</span></figcaption></figure>
    </div>
    <p style="margin-top:28px"><a class="arrow-link" href="/zanskar/">Discover the region</a></p>
  </div>
</div>

<!-- 06 · why us -->
<div class="section">
  <div class="wrap">
    <div class="section__head">
      <h2>Why travel with us</h2>
    </div>
    <div class="grid grid--2">
      <div>
        <h3>You book with the guides, not with an agency</h3>
        <p>The person answering your message is the person walking in front of you. There is no office
           in Delhi in between, and no commission on top.</p>
      </div>
      <div>
        <h3>We are from here</h3>
        <p>Not partnered with a local operator — from the valley itself, with family in villages
           you will walk through.</p>
      </div>
      <div>
        <h3>The pace is the safety plan</h3>
        <p>Altitude is the main risk on every route we run. Walking slowly is not a philosophy we sell;
           it is how we keep people well above 4,500 metres.</p>
      </div>
      <div>
        <h3>Small groups, and we mean it</h3>
        <p>Two to ten people. Beyond that the valley stops being quiet and the villages stop being able
           to host us properly.</p>
      </div>
    </div>
  </div>
</div>

<!-- 07 · travellers  (kept out until there are real quotes) -->
{testimonials}

<!-- 08 · first practical answers -->
<div class="section section--band">
  <div class="wrap">
    <div class="section__head">
      <p class="label">Practical</p>
      <h2>Three things people ask first</h2>
    </div>
    <div class="grid grid--3">
      <div>
        <h3>When to come</h3>
        <p>The trekking season runs from June to September. July and August are the warmest and the busiest;
           early September is our own favourite.</p>
        <a class="arrow-link" href="/zanskar/best-time-to-visit/">Best time to visit</a>
      </div>
      <div>
        <h3>How to get here</h3>
        <p>Fly to Leh, acclimatise for two nights, then drive to Padum over the Nimmu–Padum–Darcha road.
           That road is open in summer only.</p>
        <a class="arrow-link" href="/zanskar/how-to-get-there/">Getting to Zanskar</a>
      </div>
      <div>
        <h3>How fit you need to be</h3>
        <p>If you can walk six hours a day on rough ground for a week, you can do our trekking routes.
           Altitude matters more than speed.</p>
        <a class="arrow-link" href="/plan/fitness-and-difficulty/">Fitness and difficulty</a>
      </div>
    </div>
  </div>
</div>

<!-- 09 · invitation -->
<div class="cta">
  <div class="wrap">
    <h2>Tell us what you have in mind</h2>
    <p>Dates, group size, how much walking you want, or just a question about the region.
       We answer every message ourselves, within three working days — sometimes longer, when we are out
       on a route or the network in Zanskar is down.</p>
    <div class="btn-row">
      <a class="btn btn--light" href="/contact/">Plan your trip</a>
      <a class="btn btn--outline-light" href="{wa}">Message us on WhatsApp</a>
    </div>
    <p class="small">A person answers, not a booking system.</p>
  </div>
</div>
"""

TESTIMONIALS_PLACEHOLDER = """
<div class="section">
  <div class="wrap wrap--narrow">
    <p class="label">From people who walked with us</p>
    <div class="note note--mineral">
      <p><strong>This section is deliberately empty.</strong> {t}</p>
      <p class="small" style="margin-bottom:0">Ask every traveller two weeks after they get home:
         what did you expect, what surprised you, and who is this trip not for? Ask for permission to use
         their first name, country and a photo in the same message.</p>
    </div>
  </div>
</div>
"""


def pages():
    schema = [{
        "@context": "https://schema.org",
        "@type": "TravelAgency",
        "name": BRAND,
        "url": SITE + "/",
        "description": "Guided trekking and cultural journeys in the Zanskar valley, Ladakh, "
                       "led by local guides from Zangla.",
        "email": EMAIL,
        "telephone": WHATSAPP_DISPLAY,
        "areaServed": {"@type": "Place", "name": "Zanskar, Ladakh, India"},
        "address": {"@type": "PostalAddress", "addressLocality": "Zangla",
                    "addressRegion": "Ladakh", "addressCountry": "IN"},
        "image": SITE + "/assets/images/itinerary/day-1.jpg",
    }]

    body = BODY.format(
        chotak=todo("One characterising sentence about Stanzin Chotak — what he is known for on the trail."),
        lhamath=todo("One characterising sentence about Stanzin Lhamath — what he is known for on the trail."),
        img_phuktal=img("/assets/images/hero.jpg",
                        "Phuktal Monastery built into the cliff face above the Tsarap river"),
        img_tsok=img("/assets/images/tsokmichik/journey-monastery.jpg",
                     "The Tsarap river running wide between autumn-coloured banks east of Phuktal"),
        img_cult=img("/assets/images/tsokmichik/day-6.jpg",
                     "A whitewashed chorten with prayer flags above a green meadow, with pack horses resting"),
        img_m1=img("/assets/images/itinerary/day-6.jpg",
                   "Phuktal Monastery in warm light, its white buildings stacked below the cave mouth"),
        img_m2=img("/assets/images/journey-settlement.jpg",
                   "Turquoise meltwater running between red rock walls in a narrow section of the valley"),
        img_m3=img("/assets/images/itinerary/day-1.jpg",
                   "Cultivated fields on the valley floor below Zangla, seen from the trail above"),
        testimonials=TESTIMONIALS_PLACEHOLDER.format(
            t=todo("Two or three real traveller quotes, each with first name, country, "
                   "which journey and which year.")),
        wa=wa_link("Juley! I am interested in a journey in Zanskar."),
    )

    return [Page(
        path="",
        title="Zanskar Travel & Trekking with Local Guides | Kulé kulé Zanskar",
        description="Guided journeys through the Zanskar valley, led by two guides born in Zangla. "
                    "Trekking, cultural travel and tailor-made trips in one Himalayan region.",
        body=body, hero=HERO, section=None, schema=schema,
    )]
