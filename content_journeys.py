# -*- coding: utf-8 -*-
"""Journeys."""

from build import Page, todo, img, wa_link, SITE, BRAND

CR = ("Journeys", "/journeys/")


def shell(inner, narrow=True):
    return ('<div class="section"><div class="wrap %s prose">\n%s\n</div></div>'
            % ("wrap--narrow" if narrow else "", inner))


def trip_schema(name, slug, days, desc):
    return {"@context": "https://schema.org", "@type": "TouristTrip",
            "name": name, "url": SITE + "/journeys/%s/" % slug, "description": desc,
            "touristType": "Trekking",
            "provider": {"@type": "TravelAgency", "name": BRAND, "url": SITE + "/"},
            "itinerary": {"@type": "ItemList", "numberOfItems": days}}


# ==========================================================================
# hub
# ==========================================================================

HUB = """
<div class="section">
  <div class="wrap">
    <div class="section__head">
      <h2>Four ways into the same valley</h2>
      <p>Every journey here is guided by the same two people and covers the same region. What changes is
         the pace, the terrain and how much of it you sleep outside. All of them run as private groups
         from two people.</p>
    </div>

    <div class="filters" data-filters>
      <fieldset>
        <legend class="label">Style</legend>
        <button type="button" class="chip is-on" data-filter="style" data-value="all">All</button>
        <button type="button" class="chip" data-filter="style" data-value="trekking">Trekking</button>
        <button type="button" class="chip" data-filter="style" data-value="cultural">Cultural</button>
        <button type="button" class="chip" data-filter="style" data-value="tailor">Tailor-made</button>
      </fieldset>
      <fieldset>
        <legend class="label">Difficulty</legend>
        <button type="button" class="chip is-on" data-filter="level" data-value="all">All</button>
        <button type="button" class="chip" data-filter="level" data-value="1">Easy</button>
        <button type="button" class="chip" data-filter="level" data-value="2">Moderate</button>
        <button type="button" class="chip" data-filter="level" data-value="3">Demanding</button>
        <button type="button" class="chip" data-filter="level" data-value="4">Serious</button>
      </fieldset>
      <fieldset>
        <legend class="label">Length</legend>
        <button type="button" class="chip is-on" data-filter="len" data-value="all">All</button>
        <button type="button" class="chip" data-filter="len" data-value="short">Up to 7 days</button>
        <button type="button" class="chip" data-filter="len" data-value="long">8 days or more</button>
      </fieldset>
    </div>
    <p class="small muted" role="status" data-count></p>

    <div class="grid grid--3" style="margin-top:24px" data-journeys>

      <article class="card" data-style="trekking" data-level="3" data-len="short">
        <div class="card__media">{im1}</div>
        <div class="card__body">
          <span class="tag">Trekking · Demanding</span>
          <h3 style="margin-top:10px"><a href="/journeys/zangla-to-phuktal-trek/">Zangla to Phuktal</a></h3>
          <ul class="meta"><li>6 days</li><li>71 km on foot</li><li>Highest 5,140 m</li><li>June–Sept</li></ul>
          <p>From our own village over the passes to a monastery built into a cliff. Camping, pack horses,
             no signal for a week.</p>
          <p class="small muted">From €1,000 per person</p>
          <a class="arrow-link" href="/journeys/zangla-to-phuktal-trek/">See the route</a>
        </div>
      </article>

      <article class="card" data-style="trekking" data-level="4" data-len="long">
        <div class="card__media">{im2}</div>
        <div class="card__body">
          <span class="tag">Trekking · Serious</span>
          <h3 style="margin-top:10px"><a href="/journeys/phuktal-to-tsokmichik-trek/">Phuktal to Tsokmichik</a></h3>
          <ul class="meta"><li>8 days</li><li>6 walking days</li><li>Two passes</li><li>June–Sept</li></ul>
          <p>Beyond the monastery into the upper Tsarap: base camp, two high passes in one day,
             and very few other people.</p>
          <p class="small muted">Price on request</p>
          <a class="arrow-link" href="/journeys/phuktal-to-tsokmichik-trek/">See the route</a>
        </div>
      </article>

      <article class="card" data-style="cultural" data-level="1" data-len="short">
        <div class="card__media">{im3}</div>
        <div class="card__body">
          <span class="tag tag--mineral">Cultural · Easy to moderate</span>
          <h3 style="margin-top:10px"><a href="/journeys/zanskar-cultural-journey/">Villages and monasteries</a></h3>
          <ul class="meta"><li>7 days</li><li>Beds at night</li><li>Short walks</li><li>June–Sept</li></ul>
          <p>Padum, Karsha, Stongdey, Zangla and the villages between them. The valley without the tent.</p>
          <p class="small muted">Price on request</p>
          <a class="arrow-link" href="/journeys/zanskar-cultural-journey/">See the journey</a>
        </div>
      </article>

      <article class="card" data-style="tailor" data-level="2" data-len="short">
        <div class="card__media">{im4}</div>
        <div class="card__body">
          <span class="tag tag--plain">Tailor-made</span>
          <h3 style="margin-top:10px"><a href="/journeys/tailor-made/">Your own route</a></h3>
          <ul class="meta"><li>Your dates</li><li>Your group</li><li>Any level</li></ul>
          <p>Most of what we organise starts as a message rather than a booking. Tell us what you want
             and we will tell you honestly whether it works.</p>
          <a class="arrow-link" href="/journeys/tailor-made/">How it works</a>
        </div>
      </article>

    </div>
  </div>
</div>

<div class="section section--band">
  <div class="wrap wrap--narrow prose">
    <h2>How our journeys work</h2>
    <h3>Private, from two people</h3>
    <p>We do not put strangers together. A journey runs for the group that books it, from two people up
       to ten. That is why the price per person falls as the group grows.</p>
    <h3>Dates are yours</h3>
    <p>Within the season we run on the dates that suit you rather than on a fixed departure calendar.
       Give us a week and a preference and we will tell you what the conditions are likely to be.</p>
    <h3>The itinerary is a plan, not a promise</h3>
    <p>Rivers, snow and weather move the details around. The shape of a route holds; individual days
       occasionally do not. We would rather say this in advance than explain it on day four.</p>
    <p><a class="arrow-link" href="/plan/">Everything practical, in one place</a></p>
  </div>
</div>
"""


# ==========================================================================
# Zangla → Phuktal
# ==========================================================================

PHUKTAL_DAYS = [
    ("Zangla → Sumdo",
     ["10.0 km", "+400 m", "Camp at 3,800 m"],
     "The route leaves the village on the old path rather than the road, past fields and irrigation "
     "channels, and climbs steadily into a landscape that empties out within an hour. There are river "
     "crossings on this first day — shallow at this time of year, but a useful introduction to how we "
     "handle them. Camp is in the side valley at Sumdo.",
     "day-1.jpg", "The valley below Zangla in evening light, fields braided along the river"),
    ("Sumdo → Kong Lumche",
     ["8.9 km", "+480 m", "Camp at 4,300 m"],
     "A short day by distance and a real one by altitude: the camp is 500 metres higher than the last. "
     "That is deliberate. The valley opens as you climb, the vegetation thins to cushion plants, and "
     "with luck there are blue sheep on the slopes above. This is the day the acclimatisation is "
     "actually being done.",
     "day-2.jpg", "Two loaded pack horses on a stony trail among willows"),
    ("Kong Lumche → Yarumchun",
     ["7.5 km", "+740 m", "High point about 5,140 m"],
     "The pass day. A long climb on scree and old snow to the highest point of the route, at around "
     "5,140 metres by our own GPS track, then a descent to a glacial stream and a camp on the far side. "
     "Short in kilometres, long in hours. We start early and we walk kulé kulé.",
     "day-3.jpg", "Prayer flags and a cairn on an open ridge under a heavy sky"),
    ("Yarumchun → Lar La",
     ["11.1 km", "−270 m", "Camp at 4,280 m"],
     "An easier day after the pass, following a wide river valley north-east between rock walls that "
     "change colour through the morning. Almost no climbing. This is the day people start noticing the "
     "silence rather than their legs.",
     "day-4.jpg", "A cairn beside a braided river in a wide, dry valley with steep golden slopes"),
    ("Lar La → Shadey",
     ["10.4 km", "+900 m / −930 m", "Two passes, high point 4,860 m"],
     "Two crossings in one day, with a steep flank in between and a stupa marking the arrival at Shadey — "
     "an isolated settlement in the upper Tsarap that sees very few visitors. The hardest day after "
     "the pass, and for most people the most memorable.",
     "day-5.jpg", "A dark, stormy valley with a lone chorten on the trail"),
    ("Shadey → Phuktal Monastery",
     ["23.4 km", "−530 m", "Finish at 3,880 m"],
     "The long last day, following the Tsarap down through a gorge, over hanging bridges, until the "
     "monastery appears above you on the cliff without any warning at all. Twenty-three kilometres, "
     "but almost all of it downhill and beside water. We sleep near the monastery.",
     "day-6.jpg", "Phuktal Monastery in warm light, its white buildings stacked below the cave mouth"),
]

TSOK_DAYS = [
    ("Padum → Phuktal", ["Transfer day", "≈ 53 km by road", "Final approach on foot"],
     "The drive south from Padum along the Lungnak, with the Bardan monastery on its rock on the way, "
     "as far as the road goes. The last section to Phuktal is on foot along the Tsarap. Arriving at the "
     "monastery on the first day sets the tone for everything that follows.",
     "day-1.jpg", "A row of whitewashed chortens against a bare mountainside"),
    ("Phuktal → Thanthak", ["22 km", "7–8 hours", "Camp"],
     "The long day that opens the route. The trail follows the Tsarap east through a remote valley "
     "section, with the river as a constant on your right. Raw, open country, and no settlements for "
     "most of it. Camp near Thanthak.",
     "day-2.jpg", "A walker and a loaded pack horse on a green trail beside the river"),
    ("Thanthak → Shadey → Thanthak", ["14 km", "Out and back", "Same camp"],
     "A quieter day, walking out to the isolated village of Shadey and back to the same camp. Less "
     "altitude, more people: this is the cultural day of the route, and it also gives the body a "
     "measured step before the climb to base camp.",
     "day-3.jpg", "Low stone houses and enclosures of an old settlement on a dry slope"),
    ("Thanthak → Nyalokuntse base camp", ["10 km", "To 4,260 m", "Camp"],
     "A modest distance and a real gain. The route climbs out of the river valley into open alpine "
     "terrain and settles at a base camp below the passes. From here on, the route is committed.",
     "day-4.jpg", "Walkers moving up a broad hillside with cloud coming over the ridge"),
    ("Base camp → Hormochey", ["15 km", "Two passes", "4,827 m and 5,143 m"],
     "The defining day. Nyalokuntse pass at around 4,827 metres, then Gothungtukla at around 5,143 "
     "metres, then a long descent towards Hormochey and the Tsarap. High, dry and silent, and the "
     "reason people choose this route over the other one.",
     "day-5.jpg", "A high ridge line under deep blue sky with a single walker on the skyline"),
    ("Hormochey → Tsatsak", ["14 km", "Zara river crossing", "Camp"],
     "Down out of the high ground into broader valley terrain, with the crossing of the Zara river as "
     "the main event of the day. Camp near the old village of Tsatsak, among abandoned fields.",
     "day-6.jpg", "A whitewashed chorten hung with prayer flags above a green meadow"),
    ("Tsatsak → Tsokmichik", ["15 km", "Greener valley", "Forest camp"],
     "The last walking day, and the softest. The valley greens as you descend, with sections of real "
     "trees — something you will not have seen for a week. Camp in the forest near Tsokmichik.",
     "day-7.jpg", "A stone village house with a wooden window frame and brushwood on the roof"),
    ("Tsokmichik → Leh", ["2.5 hours on foot", "≈ 4 hours by road", "Two passes by car"],
     "A short walk out to meet the vehicle, then the drive to Leh across two passes and through Tibetan "
     "nomad country. After a week without a road, the return is gradual rather than abrupt.",
     "day-8.jpg", "A brown mountainside dropping to a river with the line of a track along it"),
]


def days_html(days, folder):
    out = ['<ol class="days">']
    for i, (title, meta, text, image, alt) in enumerate(days, 1):
        out.append(
            '<li><div class="day">'
            '<div class="day__media">%s</div>'
            '<div><span class="day__no">Day %d</span><h3>%s</h3>'
            '<ul class="meta">%s</ul><p>%s</p></div>'
            '</div></li>' % (
                img("/assets/images/%s/%s" % (folder, image), alt),
                i, title,
                "".join("<li>%s</li>" % m for m in meta),
                text))
    out.append("</ol>")
    return "\n".join(out)


ZP_BODY = """
<dl class="facts">
  <div><dt>Duration</dt><dd>6 days</dd></div>
  <div><dt>Difficulty</dt><dd>3 of 4 — Demanding</dd></div>
  <div><dt>On foot</dt><dd>71 km</dd></div>
  <div><dt>Total ascent</dt><dd>≈ 2,750 m</dd></div>
  <div><dt>Highest point</dt><dd>≈ 5,140 m</dd></div>
  <div><dt>Season</dt><dd>June – September</dd></div>
  <div><dt>Group</dt><dd>2 – 10 people</dd></div>
  <div><dt>Nights</dt><dd>Camping</dd></div>
</dl>
<p class="small muted">Distances and ascent measured from our own GPS tracks, which you can download
   day by day below.</p>

<h2>In one paragraph</h2>
<p>Six days on foot from Zangla, our village at the northern end of the inhabited valley, south-east
   over a 5,140-metre pass and down the upper Tsarap to Phuktal Monastery. Wide gravel valleys, two long
   pass days, camps beside glacial water, and a last day through a gorge that ends with a monastery
   appearing in the cliff above you. Luggage travels on horses. There is no phone signal after the first
   morning.</p>

<h2>Is this route for you?</h2>
<div class="split-lists">
  <div>
    <h3>It suits you if</h3>
    <ul class="checklist">
      <li>You can walk five to seven hours a day on rough ground, for six days in a row.</li>
      <li>You are comfortable sleeping in a tent for five nights, with no shower.</li>
      <li>You have been above 4,000 m before, or you are willing to take the acclimatisation days
          seriously.</li>
      <li>You want a region rather than a summit.</li>
    </ul>
  </div>
  <div>
    <h3>It does not suit you if</h3>
    <ul class="checklist">
      <li>This would be your first multi-day walk of any kind.</li>
      <li>You need to be reachable during the week.</li>
      <li>You want a guaranteed fixed itinerary — rivers and snow decide part of it.</li>
      <li>You are travelling with children under about twelve.</li>
    </ul>
  </div>
</div>
<p><a class="arrow-link" href="/plan/fitness-and-difficulty/">How our difficulty levels work</a></p>

<h2>Day by day</h2>
<p>{gpxnote}</p>
{days}

<h2>What it is like</h2>
<h3>The walking</h3>
<p>Long valley approaches on gravel and old moraine, a couple of steep climbs to passes, river crossings
   most days. Nothing technical — no rope, no exposure that requires a head for heights — but the ground
   is rough and the altitude does the work. We start early, walk slowly, and stop often.</p>
<h3>The nights</h3>
<p>Five nights in tents, at between 3,800 and 4,300 metres. Two-person tents, a mess tent for eating,
   and a toilet tent. It gets cold after sunset, quickly. The last night is in simple accommodation
   near the monastery.</p>
<h3>The food</h3>
<p>Cooked fresh by our own cook: rice, dal, vegetables, chapati, soup, eggs, plenty of tea. Vegetarian
   by default and easy to keep that way. Tell us about allergies and preferences when you book —
   at 4,300 metres improvisation is limited.</p>

<h2>Who guides it</h2>
<p>Both of us, on every departure — this is the route we grew up walking.
   <a href="/guides/">Meet the guides</a>.</p>

<h2>What is included</h2>
<div class="split-lists">
  <div>
    <h3>Included</h3>
    <ul class="checklist">
      <li>Local guiding by both guides, plus cook and horsemen</li>
      <li>All camping equipment: tents, mess tent, toilet tent, mats</li>
      <li>All meals and hot drinks during the trek</li>
      <li>Luggage transport by pack horse, up to 20 kg per person</li>
      <li>Accommodation near Phuktal on the last night</li>
      <li>Permits and local route arrangements</li>
      <li>First-aid support and route decisions on the ground</li>
    </ul>
  </div>
  <div>
    <h3>Not included</h3>
    <ul class="checklist">
      <li>Flights, and the flight to Leh</li>
      <li>Hotel and meals in Leh before and after</li>
      <li>Transport between Leh and the start and end of the trek (we arrange it; it is quoted separately)</li>
      <li>Travel insurance, which must cover trekking above 5,000 m</li>
      <li>Sleeping bag — bring your own, rated to about −10 °C</li>
      <li>Personal equipment, tips and drinks outside the trek</li>
    </ul>
  </div>
</div>

<h2>Price</h2>
<div class="tablewrap">
<table>
<thead><tr><th>Group size</th><th>Per person</th></tr></thead>
<tbody>
<tr><td>2 – 3 people</td><td class="num">€1,500</td></tr>
<tr><td>4 – 6 people</td><td class="num">€1,250</td></tr>
<tr><td>7 – 10 people</td><td class="num">€1,000</td></tr>
</tbody>
</table>
</div>
<p>The price falls with group size because the fixed costs — guides, cook, camp — are shared.
   Payment is 50% at confirmation and 50% on arrival.
   <a href="/plan/booking-and-payment/">How booking and payment work</a>.</p>

<h2>Dates</h2>
<p>We run this route on your dates within the season, from June to September. Tell us the week you have
   in mind and we will tell you what the rivers and passes are likely to be doing.</p>

<h2>Before you come</h2>
<ul>
  <li><a href="/plan/altitude-and-acclimatisation/">Altitude and acclimatisation</a> — two nights in Leh,
      minimum.</li>
  <li><a href="/plan/packing-list/">Packing list</a> — the sleeping bag is the item people get wrong.</li>
  <li><a href="/plan/safety-in-remote-areas/">Safety in remote areas</a> — what happens if something
      goes wrong out there.</li>
</ul>

<h2>Questions about this route</h2>
{faq}

<h2>Related</h2>
<ul>
  <li><a href="/journeys/phuktal-to-tsokmichik-trek/">Phuktal to Tsokmichik</a> — the natural
      continuation, and it can be walked straight on from here.</li>
  <li><a href="/zanskar/phuktal-monastery/">About Phuktal Monastery</a></li>
  <li><a href="/zanskar/zangla/">About Zangla, where the route starts</a></li>
</ul>
"""


TS_BODY = """
<dl class="facts">
  <div><dt>Duration</dt><dd>8 days</dd></div>
  <div><dt>Walking days</dt><dd>6 + 2 transfer</dd></div>
  <div><dt>Difficulty</dt><dd>4 of 4 — Serious</dd></div>
  <div><dt>On foot</dt><dd>≈ 90 km</dd></div>
  <div><dt>Highest point</dt><dd>≈ 5,143 m</dd></div>
  <div><dt>Season</dt><dd>June – September</dd></div>
  <div><dt>Group</dt><dd>2 – 10 people</dd></div>
  <div><dt>Nights</dt><dd>Camping, one village day</dd></div>
</dl>
<p class="small muted">{measured}</p>

<h2>In one paragraph</h2>
<p>Most people reach Phuktal Monastery and turn around. This route starts there. It follows the Tsarap
   east into a valley with a handful of settlements, climbs to a base camp at 4,260 metres, crosses two
   passes in a single day — the higher of them at about 5,143 metres — and comes down through old fields
   and forest to Tsokmichik. Six walking days, two transfer days, and very few other walkers.</p>

<h2>Is this route for you?</h2>
<div class="split-lists">
  <div>
    <h3>It suits you if</h3>
    <ul class="checklist">
      <li>You have trekked at altitude before and know how your body reacts above 4,500 m.</li>
      <li>You can walk seven to eight hours on a long day.</li>
      <li>You are comfortable with a week in a tent and no phone signal.</li>
      <li>You want terrain rather than sights.</li>
    </ul>
  </div>
  <div>
    <h3>It does not suit you if</h3>
    <ul class="checklist">
      <li>It would be your first multi-day trek.</li>
      <li>You need a shower or a bed.</li>
      <li>You want a guarantee that the itinerary will not change.</li>
      <li>You are travelling with children under about fourteen.</li>
    </ul>
  </div>
</div>
<p>Many people walk this straight on from <a href="/journeys/zangla-to-phuktal-trek/">Zangla to
   Phuktal</a>, which makes a two-week journey and solves the acclimatisation question completely.
   It also works as a standalone route starting at the monastery.</p>

<h2>Day by day</h2>
{days}

<h2>What it is like</h2>
<h3>The walking</h3>
<p>Longer days than the Phuktal route and more exposure. The base camp day and the double-pass day are
   the two that decide whether this route suits you. River crossings, including the Zara, are a real
   part of the route rather than an incident.</p>
<h3>The nights</h3>
<p>Camping throughout, with one night in or beside a village. The base camp night at 4,260 m is the
   cold one; a sleeping bag rated to −10 °C is not optional here.</p>
<h3>The food</h3>
<p>The same as on our other routes: cooked fresh by our own crew, mostly vegetarian, and a lot of it.</p>

<h2>Who guides it</h2>
<p><a href="/guides/">Chotak and Lhamath</a>, with a cook and horsemen from the valley.</p>

<h2>What is included</h2>
<div class="split-lists">
  <div>
    <h3>Included</h3>
    <ul class="checklist">
      <li>Guiding, cook and crew for the whole route</li>
      <li>Camping equipment and camp logistics</li>
      <li>All meals during the trek</li>
      <li>Luggage transport by pack horse</li>
      <li>Permits and route arrangements</li>
      <li>First-aid support</li>
    </ul>
  </div>
  <div>
    <h3>Not included</h3>
    <ul class="checklist">
      <li>Flights and transport to Leh</li>
      <li>Hotel and meals in Leh</li>
      <li>Transfers Padum / Phuktal and Tsokmichik / Leh (arranged by us, quoted separately)</li>
      <li>Travel insurance covering trekking above 5,000 m</li>
      <li>Sleeping bag and personal equipment</li>
    </ul>
  </div>
</div>

<h2>Price</h2>
<p>{price}</p>

<h2>Before you come</h2>
<ul>
  <li><a href="/plan/fitness-and-difficulty/">Fitness and difficulty</a></li>
  <li><a href="/plan/altitude-and-acclimatisation/">Altitude and acclimatisation</a></li>
  <li><a href="/plan/safety-in-remote-areas/">Safety in remote areas</a></li>
</ul>

<h2>Related</h2>
<ul>
  <li><a href="/journeys/zangla-to-phuktal-trek/">Zangla to Phuktal</a> — walk them back to back.</li>
  <li><a href="/zanskar/phuktal-monastery/">Phuktal Monastery</a></li>
  <li><a href="/zanskar/the-region/">The Lungnak and the Tsarap</a></li>
</ul>
"""


CULTURAL = """
<dl class="facts">
  <div><dt>Duration</dt><dd>7 days</dd></div>
  <div><dt>Difficulty</dt><dd>1–2 of 4 — Easy to moderate</dd></div>
  <div><dt>Walking</dt><dd>2 – 4 hours a day</dd></div>
  <div><dt>Highest point</dt><dd>Around 4,000 m</dd></div>
  <div><dt>Nights</dt><dd>Guesthouse and homestay</dd></div>
  <div><dt>Season</dt><dd>June – September</dd></div>
</dl>

<h2>In one paragraph</h2>
<p>The valley without the tent. Seven days based in Padum and Zangla, with day walks between villages,
   time at the great monasteries — Karsha, Stongdey, Sani, Bardan — and evenings in houses rather than
   at 4,300 metres. It is for travellers who want the culture and the landscape but not six days of
   camping, and for groups where not everybody wants to walk the same distance.</p>

<h2>Is this journey for you?</h2>
<div class="split-lists">
  <div>
    <h3>It suits you if</h3>
    <ul class="checklist">
      <li>You want monasteries, villages and conversation more than passes.</li>
      <li>You would rather sleep in a bed.</li>
      <li>You are travelling as a couple or a family with mixed walking appetites.</li>
      <li>You have a festival date in mind.</li>
    </ul>
  </div>
  <div>
    <h3>It does not suit you if</h3>
    <ul class="checklist">
      <li>You came for a physical challenge — take a trekking route instead.</li>
      <li>You expect hotel comfort. Guesthouses here are simple and honest about it.</li>
      <li>You are not willing to spend two nights acclimatising in Leh first. Padum is at 3,600 m.</li>
    </ul>
  </div>
</div>

<h2>The shape of the week</h2>
<div class="note">
  <p>{outline}</p>
</div>

<h2>What is included</h2>
<p>Guiding, accommodation, all transport within Zanskar, breakfast and dinner, monastery entrance where
   it applies, and the arrangements with the families who host us. Flights, insurance and lunch on
   travel days are not included.</p>

<h2>Price</h2>
<p>{price}</p>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/villages-and-monasteries/">The monasteries this journey visits</a></li>
  <li><a href="/zanskar/festivals/">Building the week around a festival</a></li>
  <li><a href="/journeys/tailor-made/">Change the balance of walking and resting</a></li>
</ul>
"""


TAILOR = """
<p class="lede">Most of what we organise starts as a message rather than a booking. If you have dates,
   a group and an idea, we can usually build something around it — or tell you honestly that it does
   not work.</p>

<h2>What we can put together</h2>
<ul>
  <li><strong>The two trekking routes back to back</strong> — Zangla to Phuktal, then on to Tsokmichik.
      Around two weeks, and the best solution to acclimatisation there is.</li>
  <li><strong>A shorter version of either route</strong>, for groups with less time or mixed fitness.</li>
  <li><strong>Trekking with a soft landing</strong> — a few village and monastery days before or after
      the walking.</li>
  <li><strong>A week built around a festival date</strong>, once the lunar calendar fixes it.</li>
  <li><strong>Family journeys</strong>, with realistic days and a plan for whoever does not want to
      walk that morning.</li>
  <li><strong>Photography or writing trips</strong>, where the pace is set by light rather than distance.</li>
  <li><strong>The Ladakh side of the plan</strong> — Leh accommodation, acclimatisation, transfers,
      and the drive over the Nimmu–Padum–Darcha road.</li>
</ul>

<h2>What we will say no to</h2>
<p>An itinerary that skips acclimatisation. A group larger than ten. A schedule so tight that a single
   bad river day breaks it. Anything that puts a village in the position of hosting more people than it
   can. We would rather lose the booking.</p>

<h2>How it works</h2>
<ol>
  <li><strong>You write.</strong> Dates or a rough window, group size, what kind of walking you want,
      and anything we should know about fitness or altitude experience.</li>
  <li><strong>We reply within three working days</strong> with a proposal, an honest assessment and a
      price. Sometimes with a question or two first.</li>
  <li><strong>We adjust.</strong> Usually two or three rounds. This is the useful part.</li>
  <li><strong>You confirm</strong> with a deposit, and we start arranging permits, transport and crew.
      <a href="/plan/booking-and-payment/">Booking and payment</a>.</li>
</ol>

<div class="btn-row" style="margin-top:32px">
  <a class="btn btn--primary" href="/contact/?journey=tailor-made">Start a tailor-made trip</a>
  <a class="btn btn--ghost" href="{wa}">Ask on WhatsApp first</a>
</div>
"""


def faq_block(items):
    out = []
    for q, a in items:
        out.append('<details class="faq"><summary>%s</summary><div class="faq__body">%s</div></details>'
                   % (q, a))
    return "\n".join(out)


ZP_FAQ = [
    ("How fit do I need to be?",
     "<p>If you can walk five to seven hours on rough ground several days in a row at home, you have "
     "the fitness. The altitude is the harder part and there is no way to train for it at sea level — "
     "which is why the acclimatisation days matter more than the gym. "
     "<a href='/plan/fitness-and-difficulty/'>More on difficulty</a>.</p>"),
    ("Do I need previous high-altitude experience?",
     "<p>It helps, but it is not required. What is required is that you take the two nights in Leh "
     "seriously and tell us honestly how you have reacted to altitude before.</p>"),
    ("How much do I carry?",
     "<p>A daypack of 20 to 30 litres: water, layers, sun protection, camera. Everything else goes on "
     "the horses, up to 20 kg per person.</p>"),
    ("Is there phone signal?",
     "<p>No. There is none after the first morning, and there is no wifi. Tell people at home before you "
     "leave. Connectivity in Ladakh generally can also go down for extended periods, so build slack into "
     "any plan that depends on being reachable.</p>"),
    ("What if the weather turns?",
     "<p>We change the plan. That may mean a shorter day, a different camp, a different pass, or — very "
     "occasionally — turning back. The decision is the guide's and it is not negotiable on the day.</p>"),
    ("Can I download the route?",
     "<p>Yes. The GPX track for each day is linked in the itinerary above. It is our own recorded track, "
     "not a plotted line.</p>"),
]


def pages():
    out = []

    out.append(Page(
        "journeys",
        "Trekking and Cultural Journeys in Zanskar | " + BRAND,
        "Guided journeys in the Zanskar valley: two trekking routes, a cultural journey through the "
        "villages and monasteries, and tailor-made trips. Private groups from two people.",
        HUB.format(
            im1=img("/assets/images/hero.jpg",
                    "Phuktal Monastery built into the cliff face above the Tsarap river"),
            im2=img("/assets/images/tsokmichik/journey-monastery.jpg",
                    "The Tsarap river running wide between autumn-coloured banks east of Phuktal"),
            im3=img("/assets/images/tsokmichik/day-6.jpg",
                    "A whitewashed chorten with prayer flags above a green meadow, pack horses resting"),
            im4=img("/assets/images/journey-valley.jpg",
                    "A small group walking across a wide gravel plain towards snow-covered peaks")),
        crumbs=[CR], section="journeys",
        og_image="/assets/images/journey-valley.jpg",
        hero=dict(image="/assets/images/journey-valley.jpg",
                  alt="A small group walking across a wide gravel plain towards snow-covered peaks",
                  eyebrow="Journeys", h1="Ways to travel in Zanskar",
                  intro="Two trekking routes, a cultural journey and trips built to order — "
                        "all guided by the same two people.")))

    out.append(Page(
        "journeys/zangla-to-phuktal-trek",
        "Zangla to Phuktal Trek — 6 Days in Zanskar | " + BRAND,
        "A six-day guided trek from Zangla to Phuktal Monastery: 71 km on foot, a 5,140 m pass, "
        "camping, pack horses and local guides. Day-by-day itinerary, price and GPX tracks.",
        shell(ZP_BODY.format(
            days=days_html(PHUKTAL_DAYS, "itinerary"),
            gpxnote='Each day links to the GPX track we recorded ourselves. '
                    '<a href="/assets/routes/day-1.gpx">Day 1</a> · '
                    '<a href="/assets/routes/day-2.gpx">Day 2</a> · '
                    '<a href="/assets/routes/day-3.gpx">Day 3</a> · '
                    '<a href="/assets/routes/day-4.gpx">Day 4</a> · '
                    '<a href="/assets/routes/day-5.gpx">Day 5</a> · '
                    '<a href="/assets/routes/day-6.gpx">Day 6</a>',
            faq=faq_block(ZP_FAQ))),
        crumbs=[CR, ("Zangla to Phuktal", "/journeys/zangla-to-phuktal-trek/")],
        section="journeys", og_image="/assets/images/itinerary/day-6.jpg",
        hero=dict(image="/assets/images/itinerary/day-6.jpg",
                  alt="Phuktal Monastery in warm light, its white buildings stacked below the cave mouth",
                  eyebrow="Trekking · 6 days",
                  h1="Zangla to Phuktal",
                  intro="From our own village, over a 5,140-metre pass, down the Tsarap to a monastery "
                        "built into a cliff.",
                  buttons='<a class="btn btn--light" href="/contact/?journey=zangla-to-phuktal">'
                          'Check availability</a>'),
        schema=[trip_schema("Zangla to Phuktal Trek", "zangla-to-phuktal-trek", 6,
                            "Six-day guided trekking route from Zangla to Phuktal Monastery in the "
                            "Zanskar valley, Ladakh.")]))

    out.append(Page(
        "journeys/phuktal-to-tsokmichik-trek",
        "Phuktal to Tsokmichik Trek — 8 Days in Remote Zanskar | " + BRAND,
        "An eight-day guided trek beyond Phuktal Monastery into the upper Tsarap: base camp at 4,260 m, "
        "two passes in one day and very few other walkers. Day-by-day itinerary.",
        shell(TS_BODY.format(
            days=days_html(TSOK_DAYS, "tsokmichik"),
            measured=todo("Distances and altitudes on this route come from the guides' own route "
                          "description and have not yet been checked against a GPS track. Record the "
                          "route once and replace these figures."),
            price=todo("Price per person by group size for this route, plus the transfer costs "
                       "from Padum and back from Tsokmichik."))),
        crumbs=[CR, ("Phuktal to Tsokmichik", "/journeys/phuktal-to-tsokmichik-trek/")],
        section="journeys", og_image="/assets/images/tsokmichik/journey-monastery.jpg",
        hero=dict(image="/assets/images/tsokmichik/journey-monastery.jpg",
                  alt="The Tsarap river running wide between autumn-coloured banks east of Phuktal",
                  eyebrow="Trekking · 8 days",
                  h1="Phuktal to Tsokmichik",
                  intro="Where most journeys end, this one begins — east into the upper Tsarap, "
                        "over two passes, to the forest at Tsokmichik.",
                  buttons='<a class="btn btn--light" href="/contact/?journey=phuktal-to-tsokmichik">'
                          'Check availability</a>'),
        schema=[trip_schema("Phuktal to Tsokmichik Trek", "phuktal-to-tsokmichik-trek", 8,
                            "Eight-day guided trekking route from Phuktal Monastery east through the "
                            "upper Tsarap valley to Tsokmichik, Zanskar, Ladakh.")]))

    out.append(Page(
        "journeys/zanskar-cultural-journey",
        "Zanskar Cultural Journey — Villages and Monasteries, 7 Days | " + BRAND,
        "A seven-day guided journey through the villages and monasteries of Zanskar, with beds at night "
        "and short daily walks. Karsha, Stongdey, Sani, Bardan and Zangla.",
        shell(CULTURAL.format(
            outline=todo("The day-by-day outline for the cultural journey: which nights in Padum, "
                         "which in Zangla, which monasteries on which day, and which families host. "
                         "Once this exists it replaces this box with a proper day-by-day list."),
            price=todo("Price per person by group size for the cultural journey."))),
        crumbs=[CR, ("Cultural journey", "/journeys/zanskar-cultural-journey/")],
        section="journeys", og_image="/assets/images/tsokmichik/day-6.jpg",
        hero=dict(image="/assets/images/tsokmichik/day-6.jpg",
                  alt="A whitewashed chorten hung with prayer flags above a green meadow",
                  eyebrow="Cultural · 7 days",
                  h1="Villages and monasteries",
                  intro="The valley without the tent: Padum, the great gompas, village days "
                        "and short walks.",
                  buttons='<a class="btn btn--light" href="/contact/?journey=cultural">'
                          'Ask about this journey</a>'),
        schema=[trip_schema("Zanskar Cultural Journey", "zanskar-cultural-journey", 7,
                            "Seven-day cultural journey through the villages and monasteries of the "
                            "Zanskar valley, Ladakh.")]))

    out.append(Page(
        "journeys/tailor-made",
        "Tailor-made Journeys in Zanskar | " + BRAND,
        "Trips built around your dates, your group and your pace in the Zanskar valley — including "
        "combining both trekking routes, family journeys and festival timing.",
        shell(TAILOR.format(wa=wa_link("Juley! I would like to put together my own journey in Zanskar."))),
        crumbs=[CR, ("Tailor-made", "/journeys/tailor-made/")], section="journeys",
        og_image="/assets/images/tsokmichik/day-5.jpg",
        hero=dict(image="/assets/images/tsokmichik/day-5.jpg",
                  alt="A high ridge line under deep blue sky with a single walker on the skyline",
                  eyebrow="Tailor-made", h1="Your own route",
                  intro="Your dates, your group, your pace. This is how most of our journeys "
                        "actually start.")))

    return out
