# -*- coding: utf-8 -*-
"""Our guides."""

from build import Page, todo, img, wa_link, SITE, BRAND

CR = ("Guides", "/guides/")


def shell(inner, narrow=True):
    return ('<div class="section"><div class="wrap %s prose">\n%s\n</div></div>'
            % ("wrap--narrow" if narrow else "", inner))


def person_schema(name, slug):
    return {"@context": "https://schema.org", "@type": "Person", "name": name,
            "jobTitle": "Trekking guide", "url": SITE + "/guides/%s/" % slug,
            "homeLocation": {"@type": "Place", "name": "Zangla, Zanskar, Ladakh, India"},
            "worksFor": {"@type": "Organization", "name": BRAND, "url": SITE + "/"}}


HUB = """
<div class="section">
  <div class="wrap wrap--narrow">
    <p class="label">The team</p>
    <h2>Two guides from Zangla, and the crew who make the days work</h2>
    <p class="lede" style="margin-top:20px">We are not a company that partners with local guides.
       We are the local guides. Zangla is where we were born, where our families still farm, and where
       the six-day route starts.</p>
    <p>“Local” gets used loosely in this industry, so here is what it means for us in practice: we know
       which river is safe to cross in July and which one is not, whose kitchen is open in Cha, and when
       a pass is holding snow that does not belong there in August. That knowledge is not on a map and
       it is not in a training course. It comes from having walked the same ground since we were children.</p>
  </div>
</div>

<div class="section section--band">
  <div class="wrap">
    <div class="grid grid--2">
      <article class="card">
        <div class="card__media">{ph_chotak}</div>
        <div class="card__body">
          <h3><a href="/guides/stanzin-chotak/">Stanzin Chotak</a></h3>
          <ul class="meta"><li>Born in Zangla</li><li>Ladakhi, Hindi, English</li></ul>
          <p>{chotak}</p>
          <a class="arrow-link" href="/guides/stanzin-chotak/">Read his profile</a>
        </div>
      </article>
      <article class="card">
        <div class="card__media">{ph_lhamath}</div>
        <div class="card__body">
          <h3><a href="/guides/stanzin-lhamath/">Stanzin Lhamath</a></h3>
          <ul class="meta"><li>Born in Zangla</li><li>Ladakhi, Hindi, English</li></ul>
          <p>{lhamath}</p>
          <a class="arrow-link" href="/guides/stanzin-lhamath/">Read his profile</a>
        </div>
      </article>
    </div>
  </div>
</div>

<div class="section">
  <div class="wrap wrap--narrow prose">
    <h2>The crew</h2>
    <p>A trekking group in Zanskar is never two guides and a rucksack. There is a cook, there are people
       handling the horses, and there is a driver on the road days. They are from the same valley, they
       work with us every season, and they are the reason a camp is standing and hot food is ready when
       you arrive.</p>
    <p><a class="arrow-link" href="/guides/the-crew/">Meet the crew</a></p>

    <h2>What a local guide does differently</h2>
    <h3>Reads the water</h3>
    <p>River levels rise through the day with the melt. A crossing that is straightforward at seven in
       the morning can be dangerous by four in the afternoon. Knowing which crossing on which day, in
       which month, is the single most useful thing we bring.</p>
    <h3>Knows when a pass is wrong</h3>
    <p>Snow that is still lying in August, a slope that has been shedding rock since the last rain,
       a col that is fine from one side and iced on the other. We turn people around occasionally.
       That is the job.</p>
    <h3>Can knock on a door</h3>
    <p>In a valley this small, a guide who grew up here has family or friends in most villages on the
       route. It changes what a bad day looks like — and it changes the quality of an ordinary one.</p>
    <h3>Knows how to behave</h3>
    <p>What to do in a monastery courtyard during a ceremony, when photographing is fine and when it is
       not, how to accept tea properly. We can tell you, and more usefully we can go first.</p>

    <p style="margin-top:32px"><a class="arrow-link" href="/guides/why-travel-with-a-local-guide/">More on
       why this matters</a></p>
  </div>
</div>

<div class="cta">
  <div class="wrap">
    <h2>Ask us something before you decide</h2>
    <p>You do not have to be ready to book. A question about fitness, about a date, or about whether a
       route suits you is exactly what we would rather answer first.</p>
    <div class="btn-row">
      <a class="btn btn--light" href="/contact/">Send us a message</a>
      <a class="btn btn--outline-light" href="{wa}">WhatsApp</a>
    </div>
  </div>
</div>
"""


PROFILE = """
<div class="person" style="margin-bottom:44px">
  <div class="person__photo person__photo--empty">{photo}</div>
  <div>
    <p class="label">Guide · Zangla</p>
    <h2 style="margin-bottom:12px">{name}</h2>
    <p class="lede">{oneline}</p>
  </div>
</div>

<dl class="facts">
  <div><dt>Home village</dt><dd>Zangla</dd></div>
  <div><dt>Languages</dt><dd>Ladakhi, Hindi, English</dd></div>
  <div><dt>Guiding since</dt><dd>{since}</dd></div>
  <div><dt>Certification</dt><dd>{cert}</dd></div>
  <div><dt>Favourite month</dt><dd>{month}</dd></div>
</dl>

<h2>In his own words</h2>
<blockquote class="quote">
  <p>{words}</p>
  <cite>{name}</cite>
</blockquote>

<h2>Ask him about</h2>
<ul>
{ask}
</ul>

<h2>One story</h2>
<p>{story}</p>

<h2>Between seasons</h2>
<p>{between}</p>

<h2>Journeys he guides</h2>
<div class="grid grid--2" style="margin-top:20px">
  <article class="card"><div class="card__body">
    <h3><a href="/journeys/zangla-to-phuktal-trek/">Zangla to Phuktal</a></h3>
    <ul class="meta"><li>6 days</li><li>Camping</li></ul>
    <a class="arrow-link" href="/journeys/zangla-to-phuktal-trek/">See the route</a></div></article>
  <article class="card"><div class="card__body">
    <h3><a href="/journeys/phuktal-to-tsokmichik-trek/">Phuktal to Tsokmichik</a></h3>
    <ul class="meta"><li>8 days</li><li>Camping</li></ul>
    <a class="arrow-link" href="/journeys/phuktal-to-tsokmichik-trek/">See the route</a></div></article>
</div>

<div class="btn-row" style="margin-top:36px">
  <a class="btn btn--primary" href="{wa}">Ask {first} a question</a>
  <a class="btn btn--ghost" href="/guides/">Back to the team</a>
</div>
"""


CREW = """
<p class="lede">Six to nine people usually move with a group of eight. Two of them are the guides.
   These are the others.</p>

<h2>Who is with you</h2>
<div class="grid grid--3" style="margin:32px 0 40px">
  <article class="card"><div class="card__body">
    <h3>Cook</h3><p>{cook}</p></div></article>
  <article class="card"><div class="card__body">
    <h3>Horsemen</h3><p>{horse}</p></div></article>
  <article class="card"><div class="card__body">
    <h3>Driver</h3><p>{driver}</p></div></article>
</div>

<h2>The horses</h2>
<p>Your main luggage travels on pack horses — up to 20 kg per person — which is what makes a six or
   eight day route possible without carrying everything yourself. You walk with a daypack: water,
   layers, camera, whatever you want during the day.</p>
<p>The horses set part of the rhythm. They leave camp after you and arrive before you, and they take
   the line the horsemen judge is safe, which is not always the line walkers take. On river days that
   difference matters, and the horsemen decide.</p>

<h2>Why we name them</h2>
<p>Plenty of operators write “our local team” and leave it there. The people carrying the load and
   cooking the food are not a category; they are specific people from specific villages, and being
   employed for a season here matters. Naming them is the least we can do, and it is also the simplest
   way for you to check that “everyone is local” is true rather than a marketing line.</p>

<div class="note note--mineral">
  <p>{consent}</p>
</div>
"""


WHY_LOCAL = """
<p class="lede">This page exists because “local guide” has become a phrase people use rather than a thing
   people check. Here is what the difference actually consists of, and what it costs you.</p>

<h2>Three ways a trek in Ladakh gets organised</h2>
<h3>Through an international operator</h3>
<p>You book in your own country, in your own language, with consumer protection behind you and a clear
   contract. The operator subcontracts to an Indian agency, which subcontracts to guides. It works, and
   for a first trip in an unfamiliar country it can be the right choice. You pay two or three margins,
   and the person walking in front of you sees a fraction of what you paid.</p>
<h3>Through an agency in Leh or Delhi</h3>
<p>Cheaper, and closer to the ground. The agency assembles a crew for your dates. Whether you get a guide
   who knows the specific valley you are walking in depends entirely on who was available that week.</p>
<h3>Directly with guides from the valley</h3>
<p>What we are. You correspond with the person who will guide you. There is no margin in between.
   The trade-off is real and worth naming: no international office, no 24-hour phone line, slower replies
   in the season, and a contract with a small Indian business rather than a European tour operator.</p>

<h2>What you gain</h2>
<ul>
  <li><strong>Judgement specific to this valley.</strong> River timing, snow on a particular col, which
      camp is sheltered when the wind comes down-valley in the afternoon.</li>
  <li><strong>Access that is not transactional.</strong> Being invited into a kitchen because the guide's
      cousin lives there is not something an agency can arrange.</li>
  <li><strong>The money stays here.</strong> Guides, cook, horsemen, driver, village purchases —
      almost the whole cost of a trek is spent within the region.</li>
  <li><strong>Continuity.</strong> The same two people, every season, on the same routes. Nobody is
      learning your route while guiding it.</li>
</ul>

<h2>What you give up</h2>
<ul>
  <li>Replies can take days when we are on a route or the network is down. We say three working days
      and we mean it as a maximum, not a target.</li>
  <li>No large office to escalate to. If something goes wrong administratively, you are dealing with us.</li>
  <li>Payment is by bank transfer and cash on arrival rather than a card checkout.
      <a href="/plan/booking-and-payment/">How booking works</a>.</li>
  <li>You need your own travel insurance, and it must cover trekking at altitude. This is not optional
      on our routes.</li>
</ul>

<div class="note">
  <p><strong>Our honest advice.</strong> If this is your first trip to a remote region, at altitude,
     without reliable communications, and that idea makes you uneasy — book with an operator in your own
     country. That is a reasonable choice and we would rather say so than have you arrive anxious.
     If you have done something like this before and what you want is the valley rather than the package,
     talk to us.</p>
</div>

<h2>Read next</h2>
<ul>
  <li><a href="/guides/">Meet the guides</a></li>
  <li><a href="/about/responsible-travel/">How we work, and what stays in the valley</a></li>
  <li><a href="/plan/booking-and-payment/">Booking and payment</a></li>
</ul>
"""


def profile(name, first, slug, month):
    return PROFILE.format(
        name=name, first=first,
        photo=todo("Portrait of %s — outdoors, on location, eye contact, landscape crop." % name),
        oneline=todo("One line: born in Zangla, guiding since which year, and what he is known for."),
        since=todo("year"),
        cert=todo("training and first aid"),
        month=month,
        words=todo("150–250 words in the first person, from a recorded interview. Lightly edited, "
                   "not rewritten — his sentence structure should survive."),
        ask="\n".join("  <li>%s</li>" % todo(x) for x in [
            "Subject one he genuinely knows well — e.g. reading river levels in July.",
            "Subject two — e.g. the old trade paths between Zanskar and Lahaul.",
            "Subject three — e.g. how a village decides when to harvest.",
        ]),
        story=todo("120–180 words about one concrete thing that happened on a route: a group that "
                   "wanted to push on, a detour forced by high water, a night with family in Cha. "
                   "A decision, not a heroic tale."),
        between=todo("What he does between October and May."),
        wa=wa_link("Juley! I would like to ask %s a question about a route in Zanskar." % first),
    )


def pages():
    out = []

    out.append(Page(
        "guides",
        "Our Guides — Local Trekking Guides from Zangla, Zanskar | " + BRAND,
        "Meet Stanzin Chotak and Stanzin Lhamath, trekking guides born in Zangla, and the crew who "
        "work with them every season in the Zanskar valley.",
        HUB.format(
            ph_chotak=('<div class="person__photo--empty" style="height:100%%;border:0">%s</div>'
                       % todo("Photograph of Stanzin Chotak")),
            ph_lhamath=('<div class="person__photo--empty" style="height:100%%;border:0">%s</div>'
                        % todo("Photograph of Stanzin Lhamath")),
            chotak=todo("One characterising sentence about Stanzin Chotak."),
            lhamath=todo("One characterising sentence about Stanzin Lhamath."),
            wa=wa_link("Juley! I have a question about travelling in Zanskar."),
        ),
        crumbs=[CR], section="guides",
        og_image="/assets/images/tsokmichik/day-2.jpg",
        hero=dict(image="/assets/images/tsokmichik/day-2.jpg",
                  alt="A walker and a loaded pack horse on a green trail beside the river",
                  eyebrow="The people", h1="The guides",
                  intro="Two childhood friends from Zangla, and the crew who move with them "
                        "every season.")))

    out.append(Page(
        "guides/stanzin-chotak",
        "Stanzin Chotak — Trekking Guide from Zangla, Zanskar | " + BRAND,
        "Stanzin Chotak, trekking guide born in Zangla in the Zanskar valley: his routes, his "
        "languages, and what he knows about this region.",
        shell(profile("Stanzin Chotak", "Chotak", "stanzin-chotak", "September")),
        crumbs=[CR, ("Stanzin Chotak", "/guides/stanzin-chotak/")], section="guides",
        schema=[person_schema("Stanzin Chotak", "stanzin-chotak")]))

    out.append(Page(
        "guides/stanzin-lhamath",
        "Stanzin Lhamath — Trekking Guide from Zangla, Zanskar | " + BRAND,
        "Stanzin Lhamath, trekking guide born in Zangla in the Zanskar valley: his routes, his "
        "languages, and what he knows about this region.",
        shell(profile("Stanzin Lhamath", "Lhamath", "stanzin-lhamath", "September")),
        crumbs=[CR, ("Stanzin Lhamath", "/guides/stanzin-lhamath/")], section="guides",
        schema=[person_schema("Stanzin Lhamath", "stanzin-lhamath")]))

    out.append(Page(
        "guides/the-crew",
        "The Crew — Cooks, Horsemen and Drivers in Zanskar | " + BRAND,
        "The cook, the horsemen and the driver who work with us every season in Zanskar, and how "
        "pack horses shape the rhythm of a trekking day.",
        shell(CREW.format(
            cook=todo("Name, village and one line about the cook."),
            horse=todo("Names, villages and one line about the horsemen."),
            driver=todo("Name, village and one line about the driver."),
            consent=todo("Before publishing: written permission from each crew member for their name "
                         "and photograph to appear on the site."))),
        crumbs=[CR, ("The crew", "/guides/the-crew/")], section="guides",
        og_image="/assets/images/itinerary/day-2.jpg",
        hero=dict(image="/assets/images/itinerary/day-2.jpg",
                  alt="Two loaded pack horses on a stony trail among willows",
                  eyebrow="The people", h1="The crew",
                  intro="The cook, the horsemen and the driver — from the same valley, "
                        "every season.")))

    out.append(Page(
        "guides/why-travel-with-a-local-guide",
        "Why Travel with a Local Guide in Zanskar | " + BRAND,
        "The honest difference between booking through an international operator, an agency in Leh, "
        "and directly with guides who live in the valley — including what you give up.",
        shell(WHY_LOCAL),
        crumbs=[CR, ("Why a local guide", "/guides/why-travel-with-a-local-guide/")],
        section="guides"))

    return out
