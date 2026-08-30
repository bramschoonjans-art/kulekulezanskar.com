# -*- coding: utf-8 -*-
"""Plan your trip."""

import re
from build import Page, todo, img, wa_link, EMAIL, BRAND, SITE

CR = ("Plan", "/plan/")


def shell(inner, narrow=True):
    return ('<div class="section"><div class="wrap %s prose">\n%s\n</div></div>'
            % ("wrap--narrow" if narrow else "", inner))


def faq_block(items):
    return "\n".join(
        '<details class="faq"><summary>%s</summary><div class="faq__body">%s</div></details>' % (q, a)
        for q, a in items)


HUB = """
<div class="section">
  <div class="wrap">
    <div class="section__head">
      <h2>The practical side, in one place</h2>
      <p>Everything here applies to all of our journeys. Each page answers one question, honestly,
         including where the honest answer is uncomfortable.</p>
    </div>
    <div class="grid grid--3">
      <article class="card"><div class="card__body">
        <h3><a href="/plan/fitness-and-difficulty/">Am I fit enough?</a></h3>
        <p>Our four difficulty levels, what a walking day actually involves, and how to judge yourself
           honestly.</p><a class="arrow-link" href="/plan/fitness-and-difficulty/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/plan/altitude-and-acclimatisation/">What about the altitude?</a></h3>
        <p>Why two nights in Leh is the minimum, what the symptoms are, and what we do when someone
           gets ill.</p><a class="arrow-link" href="/plan/altitude-and-acclimatisation/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/plan/packing-list/">What do I bring?</a></h3>
        <p>The full list, with the three items people most often get wrong.</p>
        <a class="arrow-link" href="/plan/packing-list/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/plan/safety-in-remote-areas/">What if something goes wrong?</a></h3>
        <p>Rivers, weather, evacuation, insurance, and the limits of what is possible out there.</p>
        <a class="arrow-link" href="/plan/safety-in-remote-areas/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/plan/life-in-camp/">What are the nights like?</a></h3>
        <p>Tents, food, washing, toilets and the cold. No surprises on day one.</p>
        <a class="arrow-link" href="/plan/life-in-camp/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/plan/permits-and-paperwork/">Visa and permits</a></h3>
        <p>What you arrange yourself and what we arrange for you.</p>
        <a class="arrow-link" href="/plan/permits-and-paperwork/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/plan/booking-and-payment/">How do I book?</a></h3>
        <p>Deposit, balance, what happens if you cancel, and what happens if we do.</p>
        <a class="arrow-link" href="/plan/booking-and-payment/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/plan/faq/">Everything else</a></h3>
        <p>The questions we are actually asked, answered plainly.</p>
        <a class="arrow-link" href="/plan/faq/">Read</a></div></article>
    </div>
  </div>
</div>
"""

FITNESS = """
<p class="lede">The honest test is not whether you can walk far. It is whether you can walk moderately far,
   on bad ground, at altitude, on the sixth day in a row, and still enjoy it.</p>

<h2>Our four levels</h2>
<div class="tablewrap">
<table>
<thead><tr><th>Level</th><th>What it involves</th><th>Hours a day</th><th>Highest point</th><th>Nights</th></tr></thead>
<tbody>
<tr><td><strong>1 · Easy</strong></td><td>Day walks between villages and monasteries</td>
    <td class="num">2 – 4</td><td class="num">up to 4,000 m</td><td>Guesthouse, homestay</td></tr>
<tr><td><strong>2 · Moderate</strong></td><td>Several days, short stages, one pass</td>
    <td class="num">4 – 6</td><td class="num">up to 4,600 m</td><td>Mixed</td></tr>
<tr><td><strong>3 · Demanding</strong></td><td>Multi-day trek with passes and river crossings</td>
    <td class="num">5 – 7</td><td class="num">up to 5,000 m</td><td>Tent</td></tr>
<tr><td><strong>4 · Serious</strong></td><td>Remote, several high passes, no signal, few bail-out options</td>
    <td class="num">6 – 9</td><td class="num">above 5,000 m</td><td>Tent</td></tr>
</tbody>
</table>
</div>
<p><a href="/journeys/zangla-to-phuktal-trek/">Zangla to Phuktal</a> is level 3.
   <a href="/journeys/phuktal-to-tsokmichik-trek/">Phuktal to Tsokmichik</a> is level 4.
   <a href="/journeys/zanskar-cultural-journey/">The cultural journey</a> is level 1 to 2.</p>

<h2>What a walking day is really like</h2>
<p>Up at about half past five. Tea at the tent. Breakfast, pack, and walking by seven — early, because
   rivers are lowest in the morning and because the sun is brutal by eleven. Two to three hours,
   a long stop, another two to three hours. In camp by mid-afternoon, which leaves time to rest, wash
   in a stream if there is one, and be cold by six.</p>
<p>The ground is stony, loose in places, and rarely flat even when the map says it is. There is no
   technical climbing, no rope, and nothing that requires a head for heights, but there is a lot of
   uneven walking with a river beside you.</p>

<h2>How to judge yourself honestly</h2>
<ul>
  <li>Can you walk six hours with a light pack, over rough ground, and do it again the next day?</li>
  <li>Have you done at least one multi-day walk before, anywhere?</li>
  <li>How did you feel the last time you were above 3,500 m? If you have never been, say so — it
      changes what we recommend, not whether we take you.</li>
  <li>Do knees or ankles trouble you on long descents? Day 6 to Phuktal is 23 km, mostly downhill.</li>
</ul>

<h2>Training, if you want to</h2>
<p>Walk. Two or three long walks a month for the three months before you come, on hills, in the boots
   you will bring. Add some stairs or hill repeats for the pass days. Nothing you do at sea level will
   prepare you for the altitude — that is what the acclimatisation days are for.</p>

<div class="note">
  <p><strong>The one thing we ask.</strong> Tell us the truth about your fitness and your altitude
     history when you write. Nobody is judged, and the alternative is finding out on day three at
     4,600 metres.</p>
</div>

<h2>Read next</h2>
<ul>
  <li><a href="/plan/altitude-and-acclimatisation/">Altitude and acclimatisation</a></li>
  <li><a href="/plan/packing-list/">Packing list</a></li>
  <li><a href="/journeys/">Journeys, with their levels</a></li>
</ul>
"""

ALTITUDE = """
<p class="lede">Altitude is the main risk on every route we run — more than weather, more than rivers,
   more than terrain. Almost all of it is manageable by going slowly and by not skipping the first
   two days.</p>

<h2>The numbers you are dealing with</h2>
<ul>
  <li>Leh: about 3,500 m. You land here from sea level in a few hours.</li>
  <li>Padum: about 3,600 m.</li>
  <li>Our camps: 3,800 to 4,300 m.</li>
  <li>Our passes: 4,800 to 5,150 m.</li>
</ul>
<p>Flying into Leh means arriving at an altitude most people would take days to walk up to. That is why
   the two nights there are not a sightseeing suggestion.</p>

<h2>What we ask you to do</h2>
<ol>
  <li><strong>Two nights in Leh minimum</strong> before travelling on. Three is better. Do very little
      on the first day: no hiking, no alcohol, a lot of water.</li>
  <li><strong>Tell us your history</strong> with altitude, honestly, before you book.</li>
  <li><strong>Walk kulé kulé.</strong> If you are the fittest person in the group, walk at the back for
      the first two days. The people who get ill are usually the strong ones who pushed.</li>
  <li><strong>Drink more than you want to</strong> and eat even when you are not hungry.</li>
  <li><strong>Say something early.</strong> A headache mentioned at breakfast is a small adjustment.
      The same headache mentioned at 4,800 m is a descent.</li>
</ol>

<h2>Symptoms to know</h2>
<p>Mild altitude sickness — headache, poor sleep, no appetite, mild nausea, breathlessness on effort —
   is common and usually settles with rest and a slow day. It is not a reason to be embarrassed and it
   happens to experienced walkers.</p>
<p>The serious forms are rare but they are why we take the mild ones seriously: worsening headache that
   does not respond to rest, confusion, loss of balance, breathlessness at rest, or a persistent cough.
   The treatment for all of these is the same and it is not medication — it is going down, immediately.</p>

<h2>What we do</h2>
<p>We build height gain into the route rather than fighting it: the second day of the Phuktal route
   deliberately climbs only nine kilometres but gains 500 metres, and sleeps there. We watch people at
   breakfast. We carry a first-aid kit and can arrange descent with a horse if someone cannot walk.
   {oxygen}</p>

<div class="note note--mineral">
  <p>We are guides, not doctors. Nothing on this page is medical advice. Talk to a travel clinic before
     you come, especially about acetazolamide and about any existing condition — heart, lung, pregnancy,
     or medication that affects breathing or fluid balance.</p>
</div>

<h2>Read next</h2>
<ul>
  <li><a href="/plan/safety-in-remote-areas/">Safety and evacuation</a></li>
  <li><a href="/zanskar/how-to-get-there/">Getting here, and where to acclimatise</a></li>
</ul>
"""

PACKING = """
<p class="lede">Main luggage travels on horses, up to 20 kg per person, in a soft duffel rather than a
   hard case. You walk with a daypack. Bring less than you think, except in the three categories below.</p>

<div class="note">
  <p><strong>The three things people get wrong:</strong> a sleeping bag that is not warm enough,
     boots that are not broken in, and no sun protection for the lips and the back of the neck.
     Everything else can be improvised. These cannot.</p>
</div>

<h2>Footwear</h2>
<ul class="checklist">
  <li>Trekking boots with ankle support, properly broken in</li>
  <li>Camp shoes or sandals — also useful for river crossings</li>
  <li>Three or four pairs of warm walking socks</li>
  <li>Blister kit you know how to use</li>
  <li>Trekking poles, strongly recommended, especially for the long descent on the last day</li>
</ul>

<h2>Clothing, in layers</h2>
<ul class="checklist">
  <li>Two sets of base layers, merino or synthetic — not cotton</li>
  <li>Fleece or light down mid layer</li>
  <li>Insulated jacket for camp</li>
  <li>Waterproof and windproof shell, jacket and trousers</li>
  <li>Walking trousers, and something to change into in camp</li>
  <li>Warm hat, sun hat, gloves, buff or scarf</li>
</ul>

<h2>Sleeping and warmth</h2>
<ul class="checklist">
  <li>Sleeping bag with a comfort rating around −10 °C. In September this is the difference between
      sleeping and not sleeping.</li>
  <li>Silk or fleece liner, optional but worth it</li>
  <li>Head torch and spare batteries</li>
  <li>Something warm to sleep in that you have not walked in</li>
</ul>

<h2>Daypack</h2>
<ul class="checklist">
  <li>20 to 30 litre pack with a rain cover</li>
  <li>1.5 to 2 litres of water capacity</li>
  <li>Water purification — tablets, filter or SteriPen</li>
  <li>Sunscreen (high factor), SPF lip balm, sunglasses that actually block UV at altitude</li>
  <li>Dry bag for camera, phone and documents</li>
</ul>

<h2>Health and personal</h2>
<ul class="checklist">
  <li>Your own small first-aid kit: painkillers, blister care, anything you take regularly</li>
  <li>Rehydration salts</li>
  <li>Toilet paper and a lighter, plus sealable bags to carry out what does not burn</li>
  <li>Wet wipes and a small quick-dry towel</li>
  <li>Earplugs — rivers are loud and so are tents in wind</li>
</ul>

<h2>Documents and money</h2>
<ul class="checklist">
  <li>Passport and visa, plus a photocopy kept separately</li>
  <li>Travel insurance certificate with the emergency number, and a copy for us</li>
  <li>Cash in rupees from Leh — ATMs in Padum are not dependable</li>
</ul>

<h2>What not to bring</h2>
<p>A hard suitcase. A drone, unless you have discussed it with us first — they are a problem near
   monasteries and in villages. More clothes than the list. A hairdryer, which we have genuinely seen.</p>

<h2>Read next</h2>
<ul>
  <li><a href="/plan/life-in-camp/">What camp is like</a></li>
  <li><a href="/plan/fitness-and-difficulty/">Fitness and difficulty</a></li>
</ul>
"""

SAFETY = """
<p class="lede">On our routes you are between one and three days' walk from a road, with no phone signal
   and no helicopter you can count on. That is the whole appeal, and it is also the thing to understand
   before you book.</p>

<h2>The real risks, in order</h2>
<h3>1 · Altitude</h3>
<p>The most likely thing to spoil a trip, and the most preventable. See
   <a href="/plan/altitude-and-acclimatisation/">altitude and acclimatisation</a>.</p>
<h3>2 · Rivers</h3>
<p>Levels rise through the day with the melt. We cross early. If a crossing is not right, we do not do
   it — we wait, take a different line, or change the day. The horsemen have the final word on where the
   animals cross, and often that is the safest line for people too.</p>
<h3>3 · Ordinary injury on rough ground</h3>
<p>Ankles and knees, mostly, on descents. Poles help more than people expect.</p>
<h3>4 · Weather</h3>
<p>Sun and dehydration more often than storms. In August a monsoon spill can loosen slopes; we avoid
   the sections that matter when that happens.</p>

<h2>What we carry and what we can do</h2>
<ul>
  <li>A comprehensive first-aid kit and first-aid training. {training}</li>
  <li>Horses, which can carry someone who cannot walk.</li>
  <li>Route knowledge to shorten a day, change a camp or exit a valley early.</li>
  <li>{comms}</li>
</ul>

<h2>What we cannot do</h2>
<p>We cannot guarantee a fast evacuation. From the middle of either trekking route, getting an injured
   person to a road is a matter of hours to more than a day, on foot and by horse. From Padum, serious
   cases go to Leh, which is a long drive or, weather permitting, a flight. Helicopter rescue exists in
   Ladakh but it is not a service you can rely on being available, and it is expensive.</p>
<p>This is not a reason to avoid the region. It is the reason we walk slowly, turn back when we should,
   and insist on the next point.</p>

<h2>Insurance — not optional</h2>
<p>You must have travel insurance that explicitly covers trekking at the altitude of your route,
   including emergency evacuation and repatriation. Many standard policies exclude anything above
   4,000 or 5,000 metres. Read the exclusions, not the summary. Send us the policy number and the
   emergency number before you travel.</p>

<h2>Decisions on the trail</h2>
<p>Route decisions during a journey are made by the guide. If we say a crossing is not happening, or a
   pass is off, or a day is being cut short, that is the decision. We will always explain why, and it is
   never about convenience.</p>

<h2>Read next</h2>
<ul>
  <li><a href="/plan/altitude-and-acclimatisation/">Altitude and acclimatisation</a></li>
  <li><a href="/plan/booking-and-payment/">Booking, cancellation and what happens if we cancel</a></li>
</ul>
"""

CAMP = """
<p class="lede">Five or seven nights outside, between 3,800 and 4,300 metres, with a crew of five or six
   people making it work. Here is exactly what that looks like, so that nothing on day one is a surprise.</p>

<h2>The camp</h2>
<p>Two-person tents, a mess tent where everyone eats, a kitchen tent, and a toilet tent. Camps are chosen
   for water, shelter from the afternoon wind, and flat ground — usually beside a river, which means it
   is never completely quiet.</p>
<p>The crew go ahead with the horses and the camp is standing when you arrive. That is the single biggest
   practical difference between this and carrying your own gear.</p>

<h2>The food</h2>
<p>Cooked fresh, three meals a day plus tea whenever anyone stops. Rice, dal, vegetables, chapati, soup,
   pasta, eggs, porridge in the morning. Mostly vegetarian, which is normal here and easiest at altitude.
   Portions are large because appetite drops with height and you need the calories anyway.</p>
<p>Tell us in advance about allergies, coeliac disease, or anything you cannot eat. At 4,300 metres there
   is no shop.</p>

<h2>Washing and toilets</h2>
<p>A toilet tent over a dug pit, moved and filled in when we leave. Bring your own paper and a lighter;
   anything that does not burn goes out with us in sealed bags. For washing: a bowl of hot water in the
   morning, and a river if you are brave. There is no shower for the whole route.</p>

<h2>The cold</h2>
<p>Temperature drops fast the moment the sun leaves the valley, usually in the late afternoon. People
   underestimate this. Change into dry clothes as soon as you stop walking, put the insulated jacket on
   before you feel cold, and get into the sleeping bag warm rather than trying to warm up in it.</p>

<h2>Evenings</h2>
<p>Tea, dinner, and usually in bed by half past eight. There is no light pollution for a hundred
   kilometres in any direction, so on a clear night it is worth standing outside for ten minutes in the
   cold. Most people do it once and then every night.</p>

<h2>Electricity and signal</h2>
<p>Neither. Bring a power bank for a phone or camera and expect it to be your whole supply. There is no
   signal on the route.</p>

<h2>Read next</h2>
<ul>
  <li><a href="/plan/packing-list/">Packing list</a></li>
  <li><a href="/zanskar/culture-and-traditions/">Food, tea and hospitality in the villages</a></li>
</ul>
"""

PERMITS = """
<p class="lede">For the routes we guide, the paperwork is simple. You arrange the visa; we arrange
   everything local.</p>

<h2>What you arrange</h2>
<ul>
  <li><strong>An Indian visa.</strong> Most nationalities can use the e-visa; check the current rules for
      your passport well before you travel, because processing times move.</li>
  <li><strong>Travel insurance</strong> covering trekking at the altitude of your route, with evacuation
      and repatriation. See <a href="/plan/safety-in-remote-areas/">safety</a>.</li>
  <li><strong>Domestic flights</strong> to Leh, if you are not driving in.</li>
</ul>

<h2>What we arrange</h2>
<ul>
  <li>Local permits and registrations required for the route</li>
  <li>Transport, drivers and vehicle paperwork</li>
  <li>Camping arrangements and village agreements along the way</li>
</ul>
<p>{detail}</p>

<h2>What to bring with you</h2>
<ul>
  <li>Passport, plus a photocopy carried separately</li>
  <li>Two or three passport photographs — occasionally still asked for</li>
  <li>Your insurance certificate and emergency number</li>
</ul>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/how-to-get-there/">Getting to Zanskar</a></li>
  <li><a href="/plan/booking-and-payment/">Booking and payment</a></li>
</ul>
"""

BOOKING = """
<p class="lede">You are booking directly with the guides, not through an agency. That keeps the price
   honest and the communication direct, and it also means the process is simple rather than automated.</p>

<h2>How it works</h2>
<ol>
  <li><strong>Write to us</strong> with your dates, group size and any questions.
      We reply within three working days.</li>
  <li><strong>We agree the plan</strong> — route, dates, transfers, price — usually over two or three
      messages.</li>
  <li><strong>You confirm with a deposit</strong> of 50% of the trek price.</li>
  <li><strong>You pay the balance on arrival</strong>, in cash, before the journey starts.</li>
  <li><strong>We start arranging</strong> permits, crew, horses and transport as soon as the deposit
      is received.</li>
</ol>

<h2>Payment</h2>
<p>{payment}</p>

<h2>Cancellation</h2>
<p>{cancellation}</p>

<h2>If we cancel or change the route</h2>
<p>We will not cancel a confirmed journey for a small group size — if you have booked, it runs.
   We will change a route, a camp or a day for weather, river levels, snow or illness, and we will
   explain why. If a journey becomes impossible before it starts for reasons on our side, you get your
   deposit back in full.</p>
<p>If a journey is cut short once it has started, we will get you out safely and discuss what is fair
   afterwards. We will not pretend a formula covers every case.</p>

<h2>Insurance</h2>
<p>Required, and it must cover trekking at the altitude of your route. We ask for the policy number and
   the emergency contact before departure. See <a href="/plan/safety-in-remote-areas/">safety in remote
   areas</a>.</p>

<h2>Who you are contracting with</h2>
<p>{entity}</p>

<h2>Read next</h2>
<ul>
  <li><a href="/terms/">Terms and conditions</a></li>
  <li><a href="/contact/">Send us your dates</a></li>
</ul>
"""

FAQ = [
    ("How far in advance should I book?",
     "<p>For July and August, two to four months is comfortable. For September, a little less. We can "
     "sometimes take a group at three weeks' notice, but horses and crew are easier to arrange with "
     "time.</p>"),
    ("Can I come alone?",
     "<p>Yes. The minimum group is two, so a solo traveller pays the two-person rate unless we can pair "
     "you with another booking — tell us if you are open to that and we will try.</p>"),
    ("How old do I have to be? Is there an upper limit?",
     "<p>No fixed limits. For the trekking routes we would say about twelve as a lower age, and for the "
     "harder route about fourteen. At the other end, what matters is how you handle several days at "
     "altitude, not the number.</p>"),
    ("Is there phone signal or wifi?",
     "<p>Not on any trekking route. In Padum there is patchy mobile coverage, and connectivity across "
     "Ladakh can be interrupted for days at a time. Assume you are unreachable for the duration.</p>"),
    ("What happens if I get ill during the trek?",
     "<p>We assess, and usually the answer is rest or descend. A horse can carry someone who cannot "
     "walk. See <a href='/plan/safety-in-remote-areas/'>safety in remote areas</a> for what is and is "
     "not possible out there.</p>"),
    ("I am vegetarian / vegan / coeliac. Is that a problem?",
     "<p>Vegetarian is easy — most of what we cook already is. Vegan is workable with notice. Coeliac "
     "is harder because chapati is a staple, but it can be planned around if you tell us early.</p>"),
    ("Can you organise the rest of my time in Ladakh?",
     "<p>Yes — airport pick-up, hotels in Leh, acclimatisation days and the drives. Ask when you "
     "write.</p>"),
    ("Do you take large groups?",
     "<p>Up to ten. Beyond that the valley stops being quiet and villages cannot host us properly. "
     "For a bigger party we would split it across two departures.</p>"),
    ("What is the best month?",
     "<p>Early September, if you want our own answer. July and August are warmer and busier. "
     "See <a href='/zanskar/best-time-to-visit/'>best time to visit</a>.</p>"),
    ("Why is your reply taking so long?",
     "<p>Because we are probably on a route without signal, or the network in Ladakh is down. "
     "We answer everything within three working days once we are back in range.</p>"),
]


def pages():
    out = []

    out.append(Page("plan", "Plan Your Trip to Zanskar | " + BRAND,
                    "Everything practical about travelling in Zanskar: fitness and difficulty, altitude, "
                    "packing, safety, camp life, permits, booking and answers to common questions.",
                    HUB, crumbs=[CR], section="plan",
                    og_image="/assets/images/itinerary/day-2.jpg",
                    hero=dict(image="/assets/images/itinerary/day-2.jpg",
                              alt="Two loaded pack horses on a stony trail among willows",
                              eyebrow="Plan your trip", h1="The practical side",
                              intro="Fitness, altitude, kit, safety and booking — the answers "
                                    "you need before you decide.")))

    def mk(path, title, desc, h1, lede, body, crumb):
        p = Page(path, title, desc, shell(body), crumbs=[CR, (crumb, "/%s/" % path)], section="plan")
        p.h1 = h1
        p.lede = lede
        return p

    out.append(mk("plan/fitness-and-difficulty",
                  "How Hard Is Trekking in Zanskar? Fitness and Difficulty | " + BRAND,
                  "Our four difficulty levels, what a walking day in Zanskar actually involves, and an "
                  "honest way to judge whether a route suits you.",
                  "Fitness and difficulty",
                  "Four levels, one honest test, and what a walking day really looks like.",
                  FITNESS, "Fitness and difficulty"))

    out.append(mk("plan/altitude-and-acclimatisation",
                  "Altitude and Acclimatisation in Ladakh and Zanskar | " + BRAND,
                  "Why two nights in Leh is the minimum, the altitudes you will actually sleep and walk "
                  "at in Zanskar, symptoms to watch for, and what we do when someone is unwell.",
                  "Altitude and acclimatisation",
                  "The main risk on every route we run, and the one that responds best to going slowly.",
                  ALTITUDE.format(oxygen=todo(
                      "Confirm what we actually carry: oxygen cylinder, pulse oximeter, satellite "
                      "phone or messenger? Only list what is genuinely on the route.")),
                  "Altitude"))

    out.append(mk("plan/packing-list",
                  "Zanskar Trekking Packing List | " + BRAND,
                  "What to bring for a trek in Zanskar: footwear, layers, a sleeping bag warm enough "
                  "for the camps, daypack essentials and the three things people most often get wrong.",
                  "Packing list",
                  "Twenty kilos on a horse, a daypack on your back, and three items that cannot "
                  "be improvised.",
                  PACKING, "Packing list"))

    out.append(mk("plan/safety-in-remote-areas",
                  "Safety, Evacuation and Insurance in Remote Zanskar | " + BRAND,
                  "The real risks on a Zanskar trek, what we carry, what evacuation actually involves "
                  "days from a road, and the insurance cover you must have.",
                  "Safety in remote areas",
                  "What can go wrong, what we can do about it, and — just as important — what "
                  "we cannot.",
                  SAFETY.format(
                      training=todo("Which first-aid or wilderness first-aid training the guides hold, "
                                    "and when it was last renewed."),
                      comms=todo("Do we carry a satellite phone or messenger on the routes? "
                                 "If yes, say which. If no, say so plainly.")),
                  "Safety"))

    out.append(mk("plan/life-in-camp",
                  "Camp Life on a Zanskar Trek | " + BRAND,
                  "Tents, food, washing, toilets, the cold and the evenings — exactly what a night on "
                  "a Zanskar trekking camp is like, with no surprises on day one.",
                  "Life in camp",
                  "Five nights outside at around 4,000 metres. Here is precisely what that involves.",
                  CAMP, "Life in camp"))

    out.append(mk("plan/permits-and-paperwork",
                  "Permits, Visa and Paperwork for Zanskar | " + BRAND,
                  "What you arrange yourself — visa, insurance, flights — and what we arrange locally "
                  "for a trekking or cultural journey in Zanskar.",
                  "Permits and paperwork",
                  "You do the visa and the insurance. We do everything local.",
                  PERMITS.format(detail=todo(
                      "Confirm exactly which permits or registrations apply to each route for the "
                      "coming season, and whether anything changed.")),
                  "Permits"))

    out.append(mk("plan/booking-and-payment",
                  "Booking and Payment | " + BRAND,
                  "How booking works when you deal directly with the guides: deposit, balance on "
                  "arrival, cancellation, insurance and who you are contracting with.",
                  "Booking and payment",
                  "Direct, simple, and slower than a checkout button — which is the trade-off "
                  "of booking with people rather than a platform.",
                  BOOKING.format(
                      payment=todo("Bank details and accepted payment methods for the deposit, the "
                                   "currency, who bears the transfer fees, and the currency for the "
                                   "cash balance on arrival."),
                      cancellation=todo("The cancellation policy: what is refunded and up to which "
                                        "point before departure. This must be written down before "
                                        "the site goes live."),
                      entity=todo("The legal entity that contracts with the traveller: name, "
                                  "registration, address, and what the traveller's rights are.")),
                  "Booking"))

    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage",
                  "mainEntity": [{"@type": "Question", "name": re.sub("<[^>]+>", "", q),
                                  "acceptedAnswer": {"@type": "Answer",
                                                     "text": re.sub("<[^>]+>", "", a).strip()}}
                                 for q, a in FAQ]}

    out.append(mk("plan/faq",
                  "Questions and Answers | " + BRAND,
                  "The questions travellers actually ask us about trekking and travelling in Zanskar, "
                  "answered plainly.",
                  "Questions and answers",
                  "The things people write to ask, answered here so you do not have to.",
                  faq_block(FAQ) +
                  '<h2 style="margin-top:44px">Still not answered?</h2>'
                  '<p>Write to us. A question is not a commitment, and we would rather answer it '
                  'now than have you guess.</p>'
                  '<div class="btn-row"><a class="btn btn--primary" href="/contact/">Ask us</a>'
                  '<a class="btn btn--ghost" href="%s">WhatsApp</a></div>'
                  % wa_link("Juley! I have a question about your journeys."),
                  "Questions"))
    out[-1].schema = [faq_schema]

    return out
