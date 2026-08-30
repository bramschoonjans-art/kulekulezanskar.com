# -*- coding: utf-8 -*-
"""Discover Zanskar — destination cluster."""

from build import Page, todo, img, SITE, BRAND

CR = ("Zanskar", "/zanskar/")


def shell(inner, narrow=True):
    return ('<div class="section"><div class="wrap %s prose">\n%s\n</div></div>'
            % ("wrap--narrow" if narrow else "", inner))


def cta(text="Ready to see the routes?", link="/journeys/", label="All journeys"):
    return ('<div class="section section--band"><div class="wrap wrap--narrow">'
            '<h2>%s</h2><div class="btn-row">'
            '<a class="btn btn--primary" href="%s">%s</a>'
            '<a class="btn btn--ghost" href="/contact/">Ask us a question</a>'
            '</div></div></div>' % (text, link, label))


def attraction(name, desc):
    return {"@context": "https://schema.org", "@type": "TouristAttraction",
            "name": name, "description": desc,
            "address": {"@type": "PostalAddress", "addressRegion": "Ladakh",
                        "addressCountry": "IN"}}


# ==========================================================================
# hub
# ==========================================================================

HUB = """
<div class="section">
  <div class="wrap">
    <div class="section__head">
      <p class="label">Where you are going</p>
      <h2>A high valley on the far side of Ladakh</h2>
      <p>Zanskar is a district of Ladakh, in the far north of India, wedged between the Zanskar Range and
         the Great Himalaya. Almost all of it lies between 3,600 and 4,000 metres. Around fourteen thousand
         people live here, most of them farming barley on the valley floors in a growing season that lasts
         a few short months.</p>
    </div>
    <dl class="facts">
      <div><dt>Region</dt><dd>≈ 7,000 km²</dd></div>
      <div><dt>Valley floor</dt><dd>3,600 – 4,000 m</dd></div>
      <div><dt>Population</dt><dd>13,793 <span class="muted" style="font-weight:400">(2011)</span></dd></div>
      <div><dt>Main town</dt><dd>Padum</dd></div>
      <div><dt>Road access</dt><dd>Summer months</dd></div>
    </dl>
    <div class="grid grid--3" style="margin-top:44px">
      <article class="card"><div class="card__body">
        <h3><a href="/zanskar/the-region/">The region and its valleys</a></h3>
        <p>How Zanskar is put together: the Stod, the Lungnak, the rivers that join at Padum
           and the passes that close the valley in.</p>
        <a class="arrow-link" href="/zanskar/the-region/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/zanskar/villages-and-monasteries/">Villages and monasteries</a></h3>
        <p>Karsha, Stongdey, Bardan, Sani, Phuktal — and the villages between them where
           people actually live.</p>
        <a class="arrow-link" href="/zanskar/villages-and-monasteries/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/zanskar/culture-and-traditions/">Culture and traditions</a></h3>
        <p>Buddhism as daily practice, the farming year, houses built of mud brick,
           and how to be a decent guest.</p>
        <a class="arrow-link" href="/zanskar/culture-and-traditions/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/zanskar/best-time-to-visit/">Best time to visit</a></h3>
        <p>Month by month: temperature, road conditions, river levels, and what each part of
           the season is good for.</p>
        <a class="arrow-link" href="/zanskar/best-time-to-visit/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/zanskar/how-to-get-there/">Getting to Zanskar</a></h3>
        <p>Three ways in — from Leh, from Kargil and from Manali — with distances,
           driving times and season windows.</p>
        <a class="arrow-link" href="/zanskar/how-to-get-there/">Read</a></div></article>
      <article class="card"><div class="card__body">
        <h3><a href="/zanskar/festivals/">Festivals</a></h3>
        <p>The monastery festivals, when they roughly fall, and what actually happens at one.</p>
        <a class="arrow-link" href="/zanskar/festivals/">Read</a></div></article>
    </div>
  </div>
</div>

<div class="section section--band">
  <div class="wrap">
    <div class="split">
      <div class="split__media">{im}</div>
      <div class="split__body">
        <p class="label">Places</p>
        <h2>Three places to start</h2>
        <p><a href="/zanskar/phuktal-monastery/">Phuktal Monastery</a> — a Gelug monastery built around a
           cave mouth high above the Tsarap, reached on foot.</p>
        <p><a href="/zanskar/padum/">Padum</a> — the administrative centre, where almost every journey
           into Zanskar begins or ends.</p>
        <p><a href="/zanskar/zangla/">Zangla</a> — our village, 32 km north-east of Padum, with an
           eleventh-century fort on the ridge above it.</p>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <div class="wrap wrap--narrow">
    <p class="label">Who is telling you this</p>
    <h2>We live here</h2>
    <p>Everything on these pages comes from growing up in the valley and walking it every summer since.
       Where something depends on the year — the state of a river, the snow on a pass, the date of a
       festival — we say so rather than pretending it is fixed.</p>
    <p><a class="arrow-link" href="/guides/">Meet the guides</a></p>
  </div>
</div>
"""


# ==========================================================================
# the region
# ==========================================================================

REGION = """
<h2>Where Zanskar is</h2>
<p>Zanskar is a district of Ladakh, in the Indian union territory of the same name. It sits south of the
   Indus valley and Leh, roughly 250 km south of Kargil, closed in by the Zanskar Range to the north-east
   and by the Great Himalaya to the south-west. Those two ranges are the reason the region feels the way it
   does: they take most of the monsoon out of the air before it arrives, which is why the valley is green
   only where people irrigate it, and grey-brown everywhere else.</p>
<p>The district covers about 7,000 square kilometres and almost all of the inhabited land lies between
   3,600 and 4,000 metres. The 2011 census counted 13,793 people. That number matters more than it looks:
   it means a valley the size of a small country holds fewer people than a European market town, spread
   over villages that are often a full day's walk apart.</p>

<h2>Two rivers, one valley</h2>
<p>Zanskar is best understood as a Y. Two rivers come down from opposite directions and meet near Padum,
   and almost everything — villages, monasteries, trails, the road — follows one of the two arms.</p>
<p><strong>The Stod, or Doda.</strong> Rises near the Pensi La at about 4,400 metres, the pass that connects
   Zanskar to the Suru valley and Kargil, and runs south-east down a broad, open valley towards Padum.
   This is the gentler arm: wider fields, more villages within sight of one another, and the road in
   from Kargil.</p>
<p><strong>The Lungnak, or Tsarap.</strong> Formed where the Kargyag river — which rises near the Shinku La
   at 5,091 metres — joins the Tsarap below the village of Purney. This is the harder, narrower arm:
   a dry corridor of gorges and side valleys running north-west towards Padum. Phuktal Monastery is on
   it, and so are both of our trekking routes.</p>
<p>Below Padum the combined river becomes the Zanskar, and cuts north through a gorge to join the Indus
   near Nimmu. In winter that gorge freezes hard enough to walk on, which is the origin of the Chadar
   route — a genuinely different undertaking from anything we run in summer.</p>

<h2>The passes</h2>
<p>Because the ranges are continuous, everything that enters or leaves Zanskar crosses a pass. The three
   that shape travel here are the Pensi La (about 4,400 m, on the road from Kargil), the Shinku La —
   also spelled Shingo La — at 5,091 m on the road from Manali, and the Singge La and Hanuma La on the
   old walking route north towards Lamayuru.</p>
<p>On foot, passes are also how the days are structured. A trekking day in Zanskar is usually a long
   valley approach, a steep hour or two at the end, and then a very different landscape on the other side.
   Our own routes cross passes between roughly 4,800 and 5,150 metres.</p>

<h2>What the landscape is actually like</h2>
<p>People arrive expecting Nepal and find something closer to Tibet or the high Andes. There is very little
   forest. Colour comes from the rock — ochre, grey, rust, occasional bands of green and violet where the
   strata tilt — and from the irrigated fields, which in July and August are a startling barley green
   against all that dryness. Above about 4,200 metres there is almost nothing growing at all.</p>
<p>Water is the other constant. Most days involve a river: walking beside one, crossing one, or camping
   next to one. River levels rise through the day as the snow melts, which is why a crossing that is
   easy at eight in the morning can be a problem at four in the afternoon. That single fact governs
   more of our route planning than anything else.</p>

<div class="note">
  <p><strong>What this means for your trip.</strong> Zanskar rewards time. Distances on the map are
     misleading because everything is vertical and everything crosses water. If you have a week, take one
     valley and walk it properly. If you have two, you can cross between the arms of the Y and see how
     different they are.</p>
</div>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/best-time-to-visit/">When to come, month by month</a></li>
  <li><a href="/zanskar/how-to-get-there/">How to reach Zanskar</a></li>
  <li><a href="/zanskar/villages-and-monasteries/">The villages and monasteries of the valley</a></li>
  <li><a href="/journeys/">The journeys we guide here</a></li>
</ul>
"""


# ==========================================================================
# best time
# ==========================================================================

BEST_TIME = """
<p class="lede">Short answer: come between mid-June and mid-September if you want to walk. Early September
   is our own favourite month. The road is open longer than the trekking season is comfortable, and the
   winter is a different trip altogether.</p>

<h2>The season in one table</h2>
<div class="tablewrap">
<table>
<thead><tr><th>Month</th><th>Day / night</th><th>Roads</th><th>Trekking</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>January – March</td><td class="num">Well below freezing</td><td>Closed</td><td>Winter routes only</td>
    <td>The Zanskar gorge freezes; villages are reached on foot or by air-dropped supplies.</td></tr>
<tr><td>April – May</td><td class="num">Cold, thawing</td><td>Usually still closed</td><td>No</td>
    <td>Snow on the passes, rivers rising fast and unpredictably. The hardest month to plan.</td></tr>
<tr><td>June</td><td class="num">Warm days, cold nights</td><td>Opening, variable</td><td>From mid-month</td>
    <td>Green valleys, high water. Early June crossings can be forced onto detours.</td></tr>
<tr><td>July</td><td class="num">Warmest</td><td>Open</td><td>Yes</td>
    <td>Peak melt, so the biggest rivers. Barley fields at their greenest. Most other visitors.</td></tr>
<tr><td>August</td><td class="num">Warm</td><td>Open</td><td>Yes</td>
    <td>Occasional monsoon spill over the Himalaya: short, heavy rain, and rockfall risk on some slopes.</td></tr>
<tr><td>September</td><td class="num">Cool, very clear</td><td>Open</td><td>Best</td>
    <td>Rivers drop, air is clearest, harvest in the villages. Nights get cold quickly after mid-month.</td></tr>
<tr><td>October</td><td class="num">Cold nights</td><td>Closing</td><td>Early October only</td>
    <td>Beautiful and empty, but the first snow can shut a pass with no warning.</td></tr>
<tr><td>November – December</td><td class="num">Deep cold</td><td>Closed</td><td>No</td>
    <td>The valley closes in. Not a season for visitors on foot.</td></tr>
</tbody>
</table>
</div>
<p class="small muted">Temperatures vary enormously with altitude and with sun. A July afternoon at 3,700 m
   can be shirtsleeves; the same night at 4,600 m will be at or below freezing.</p>

<h2>What actually changes through the season</h2>
<h3>June — green, wet underfoot, unpredictable</h3>
<p>The valley is at its greenest and least visited, but the rivers are running with meltwater from the
   whole winter's snow. On our routes this decides everything: some crossings that are trivial in
   September are simply not on in mid-June, and the day gets rerouted. If you come this early, come with
   a flexible itinerary and a guide who will change it.</p>

<h3>July and August — warm, busy by Zanskar standards, high water</h3>
<p>This is when most people come and when the weather is most reliably warm. It is also peak melt.
   We start early — often walking by six — because rivers are lowest in the morning and rise through the
   afternoon. In August the monsoon occasionally pushes over the Great Himalaya and gives a day or two of
   real rain, which matters less for comfort than for what it does to loose slopes.</p>

<h3>September — the month we would choose</h3>
<p>Rivers drop. The light gets very clean. Villages are harvesting barley, so the valley is at its most
   active and its most sociable. The trade-off is temperature: after about the 15th, nights at camp go
   properly cold, and you want a sleeping bag rated to around −10 °C rather than −5 °C.</p>

<h3>Winter — a different trip</h3>
<p>Winter in Zanskar is not a colder version of summer. Roads close, the valley lives on stored food and
   what comes in by air, and the frozen river becomes a route. It is possible to travel here in winter,
   but it needs different equipment, different planning and a different conversation.
   {winter}</p>

<h2>Festivals and timing</h2>
<p>Monastery festivals follow the Tibetan lunar calendar, so they move from year to year in the Western
   calendar. If a festival is the reason for your trip, tell us early and we will build the route around
   the date once it is fixed. See <a href="/zanskar/festivals/">festivals in Zanskar</a>.</p>

<div class="note">
  <p><strong>One planning rule.</strong> Whatever month you choose, add two nights in Leh at the
     beginning. Not for sightseeing — for altitude. Everything else on this page matters less than that.
     <a href="/plan/altitude-and-acclimatisation/">Why acclimatisation comes first</a>.</p>
</div>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/how-to-get-there/">How to reach Zanskar</a></li>
  <li><a href="/plan/altitude-and-acclimatisation/">Altitude and acclimatisation</a></li>
  <li><a href="/journeys/">Journeys, with their season windows</a></li>
</ul>
"""


# ==========================================================================
# how to get there
# ==========================================================================

GET_THERE = """
<p class="lede">There is no airport in Zanskar. Every route in ends with a long drive over a high pass, and
   all of them are seasonal. Plan on a full day of driving from wherever you land, and two nights of
   acclimatisation before you start it.</p>

<h2>The three ways in</h2>

<h3>1 · Fly to Leh, drive to Padum over the Nimmu–Padum–Darcha road</h3>
<p>This is the route we use for most journeys. Fly into Leh (Kushok Bakula Rimpochee Airport, IXL) from
   Delhi — a short flight, usually in the morning, and frequently cancelled for weather, which is worth
   knowing when you book onward tickets.</p>
<p>From Leh the Nimmu–Padum–Darcha road runs 298 km to Padum. It was completed as a blacktopped road in
   March 2024, which changed access to Zanskar substantially: what used to be a two-day journey is now
   possible in one long day. It is <strong>not</strong> an all-weather road. The Shinkun La tunnel that
   would make it one is still under construction, so in practice the road is usable in the summer months
   and closed by snow outside them.</p>
<div class="facts">
  <div><dt>Distance</dt><dd>298 km</dd></div>
  <div><dt>Driving time</dt><dd>10 – 12 hours</dd></div>
  <div><dt>Season</dt><dd>Roughly June – October</dd></div>
  <div><dt>Vehicle</dt><dd>Shared or private 4×4</dd></div>
</div>

<h3>2 · Via Kargil and the Pensi La</h3>
<p>The older approach, and still a good one if you are coming from Srinagar rather than Delhi. Kargil to
   Padum is about 230 km over the Pensi La (around 4,400 m), through the Suru valley — a beautiful drive
   in its own right, past Rangdum. Expect a long day, and expect the pass to be the deciding factor for
   whether it runs at all. This road generally opens later in spring than people hope.</p>

<h3>3 · From Manali over the Shinku La</h3>
<p>From Manali via Darcha and the Shinku La (5,091 m) into the south of Zanskar. It is the shortest way in
   from the Indian plains and it puts you near the southern end of the Lungnak valley, which suits some
   trekking routes well. It is also the highest and the most weather-dependent, and it gives you very
   little acclimatisation time before you are at altitude.</p>

<div class="note">
  <p><strong>Which one we would suggest.</strong> If it is your first time at this altitude: fly to Leh,
     take two nights there, then drive to Padum. The extra day costs you less than an altitude headache
     on day two of a trek.</p>
</div>

<h2>Getting around once you are here</h2>
<p>There are shared taxis and occasional buses between Padum and the larger villages, and a road now runs
   a good way up the Lungnak valley towards Phuktal. Beyond that, it is on foot. For our journeys we
   arrange all transfers ourselves — airport pick-up in Leh, the drive to Padum or to the trailhead,
   and the return at the end.</p>

<h2>Permits</h2>
<p>Indian visa requirements apply as everywhere in the country, and there are additional restrictions in
   some border areas of Ladakh. For the routes we guide, the paperwork is straightforward and we handle
   it. {permits}</p>
<p>See also <a href="/plan/permits-and-paperwork/">permits and paperwork</a>.</p>

<h2>What we can organise for you</h2>
<ul>
  <li>Pick-up at Leh airport and a hotel for the acclimatisation nights</li>
  <li>The drive to Padum or directly to the start of your route</li>
  <li>Transport back to Leh at the end, including from the far end of a point-to-point trek</li>
  <li>Route sequencing if you are combining two journeys in one trip</li>
</ul>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/best-time-to-visit/">When to come</a></li>
  <li><a href="/plan/altitude-and-acclimatisation/">Altitude and acclimatisation</a></li>
  <li><a href="/contact/">Ask us to plan the logistics</a></li>
</ul>
"""


# ==========================================================================
# villages and monasteries
# ==========================================================================

VILLAGES = """
<p class="lede">Zanskar has a handful of large monasteries, a great many small ones, and villages that
   are inseparable from both. Almost every settlement of any size has a gompa above it, and the monastery
   year and the farming year run on the same calendar.</p>

<h2>The main monasteries</h2>

<h3>Karsha</h3>
<p>The largest monastery in Zanskar, on the slope above the Stod valley across from Padum — a stack of
   whitewashed buildings that is visible from a long way down the valley. Gelug order. It is the easiest
   of the great monasteries to reach, which makes it the usual first stop for anyone arriving in Padum,
   and its summer festival is the biggest gathering in the valley.</p>

<h3>Phuktal</h3>
<p>Built around the mouth of a natural cave high above the Tsarap, in the Lungnak valley about 52 km
   south-east of Padum. Founded in the early fifteenth century by Jangsem Sherap Zangpo, a disciple of
   Tsongkhapa, and home to around seventy monks. Until recently it could only be reached on foot; a road
   now comes far enough up the valley that the final approach is a two to three hour walk from Purney.
   <a href="/zanskar/phuktal-monastery/">More about Phuktal</a>.</p>

<h3>Stongdey</h3>
<p>On the road between Padum and Zangla, high on a spur with a long view down the valley. Gelug order, and
   generally counted as the second largest monastic community in Zanskar. It is a good half-day from
   Padum and much quieter than Karsha.</p>

<h3>Bardan</h3>
<p>Drukpa order, on a rock outcrop above the Lungnak river a short drive south of Padum. Small, dramatic,
   and usually on the way to somewhere else — most people passing towards Phuktal stop here.</p>

<h3>Sani</h3>
<p>West of Padum in the Stod valley, unusual for being on flat ground rather than a crag, and for its
   ancient stupa. Drukpa order. Its summer festival includes masked dances and draws people from the
   whole western end of the valley.</p>

<h2>Villages</h2>
<p>The villages are where the valley actually happens. Most are small — a cluster of flat-roofed mud-brick
   houses, poplar and willow planted for timber, irrigation channels cut along the contour, and barley
   fields stepping down to the river. Roofs are stacked with brushwood and dung through the summer:
   that is next winter's fuel, and how full the roof is tells you how the year has gone.</p>
<ul>
  <li><strong><a href="/zanskar/padum/">Padum</a></strong> — the administrative centre, about seven hundred
      people, where almost everyone arrives.</li>
  <li><strong><a href="/zanskar/zangla/">Zangla</a></strong> — 32 km north-east of Padum, at 3,931 m,
      with a ruined fort on the ridge. Our village.</li>
  <li><strong>Purney</strong> — the junction below which the Kargyag and the Tsarap become the Lungnak,
      and the road-head for Phuktal.</li>
  <li><strong>Shadey</strong> — an isolated settlement in the upper Tsarap, reached on both of our
      trekking routes from opposite directions.</li>
  <li><strong>Cha, Testa, Purney, Anmu</strong> — the string of small villages along the Lungnak that
      keep the walking route through the valley possible.</li>
</ul>

<div class="note">
  <p><strong>Visiting a monastery.</strong> Walk clockwise around chortens and mani walls. Ask before
     photographing inside a temple or during a ceremony, and accept a no. Take your shoes off where
     others do. A small donation in the box is normal and welcome. If you are not sure, watch what the
     Zanskari people around you do and copy it — that is what we do too.</p>
</div>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/culture-and-traditions/">Culture and traditions</a></li>
  <li><a href="/zanskar/festivals/">Festivals</a></li>
  <li><a href="/journeys/zanskar-cultural-journey/">The journey built around villages and monasteries</a></li>
</ul>
"""


# ==========================================================================
# culture
# ==========================================================================

CULTURE = """
<p class="lede">Zanskar is a Tibetan Buddhist culture that has been continuously inhabited for a very long
   time and largely left to organise itself. What that produces is a place where religion, farming and
   family are not separate subjects.</p>

<h2>Buddhism as daily practice</h2>
<p>Most Zanskari families are Buddhist, following the Gelug or Drukpa schools depending on which monastery
   their village belongs to. In practice this is less visible in doctrine than in landscape: chortens at
   the edge of every village, mani walls of carved stones along the paths, prayer flags on ridges and
   bridges, and a rhythm of small daily observances. Many families have a son in a monastery. Monks come
   home for the harvest.</p>

<h2>The farming year</h2>
<p>The growing season is short and the whole valley runs on it. Fields are irrigated by channels that carry
   meltwater along the contour, sometimes for kilometres, and the water is shared on a schedule that
   villages have worked out among themselves for generations. Barley is the main crop — for flour,
   for <em>tsampa</em>, and for <em>chang</em>. Peas, potatoes and some vegetables grow where the
   valley is low and sheltered enough.</p>
<p>Harvest falls in late August and September, which is one reason we like guiding then: you walk through
   villages that are entirely occupied, and you are far more likely to be pulled in for tea.</p>

<h2>Houses, food and hospitality</h2>
<p>Houses are mud brick on stone foundations, with small windows and thick walls, built to hold heat.
   The kitchen is usually the warmest room and the social centre. If you are invited in, you will be given
   butter tea (salty, and an acquired taste) or sweet tea, and it is polite to accept at least a little.</p>
<p>Food on our journeys is cooked fresh by our own crew: rice and dal, vegetables, chapati, soup, eggs,
   and as much tea as anyone can drink. It is simple, it is a lot, and at altitude it is what keeps
   people walking.</p>

<h2>Language</h2>
<p>Zanskari is a Tibetic language, closely related to Ladakhi. Hindi is widely spoken and English is common
   among younger people and anyone working with visitors. Two words carry you a long way:</p>
<ul>
  <li><strong>Juley</strong> (also written <em>jullay</em>) — hello, goodbye, thank you, please. Use it
      constantly; everybody does.</li>
  <li><strong>Kulé kulé</strong> — slowly, slowly. What you say to someone rushing a climb, and what
      we named ourselves after.</li>
</ul>

<h2>Being a good guest</h2>
<ul>
  <li>Ask before photographing people, and accept a refusal without negotiating. Ask especially with
      children, and ask their parents.</li>
  <li>Walk clockwise around chortens and mani walls, and keep them on your right.</li>
  <li>Dress covered: shoulders and knees, in villages and monasteries.</li>
  <li>Do not hand out sweets or pens to children. If you want to give something, give it to the school
      or the village, and ask us how.</li>
  <li>Carry your waste out. Everything you bring in has to leave again, including what burns badly.</li>
</ul>
<p>More on how we handle this as an organisation: <a href="/about/responsible-travel/">responsible travel</a>.</p>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/villages-and-monasteries/">Villages and monasteries</a></li>
  <li><a href="/zanskar/festivals/">Festivals</a></li>
  <li><a href="/plan/life-in-camp/">What camp life is like</a></li>
</ul>
"""


# ==========================================================================
# festivals
# ==========================================================================

FESTIVALS = """
<p class="lede">Monastery festivals in Zanskar follow the Tibetan lunar calendar, so their dates move every
   year against the Western one. If a festival is the reason for your trip, tell us early: we can confirm
   the date once it is set and build the route around it.</p>

<h2>The festivals worth planning around</h2>

<h3>Karsha Gustor</h3>
<p>The biggest gathering in the valley, at Karsha Monastery above the Stod valley. Two days of masked
   <em>cham</em> dances performed by the monks, ending with the destruction of a ritual effigy. Held in
   summer. People come in from the whole western half of Zanskar, so it is as much a social event as a
   religious one.</p>

<h3>Stongdey Gustor</h3>
<p>The same form of festival at Stongdey, on the road towards Zangla. Smaller than Karsha and, for that
   reason, easier to experience up close.</p>

<h3>Sani Naro Nasjal</h3>
<p>At Sani, west of Padum, around the ancient stupa. Masked dances and a procession; one of the few
   festivals here associated with a site rather than only with a monastic community.</p>

<h3>Losar</h3>
<p>The new year, celebrated in winter. Ladakh and Zanskar traditionally observe it earlier than the
   Tibetan calendar would suggest, which surprises people. It is a family and village occasion rather
   than a spectacle for visitors, and the valley is closed by road when it happens.</p>

<div class="note note--mineral">
  <p><strong>Dates for the coming season</strong><br>{dates}</p>
</div>

<h2>What a festival is actually like</h2>
<p>Long. The dances run for hours, with pauses, and the crowd treats it as a day out: families arrive
   early, sit along the walls, share food, and talk through the quieter passages. There is no ticket and
   no seating plan. Arrive early if you want to see anything, expect to stand, and expect it to be cold
   in the morning and hot by midday.</p>
<p>Photography is generally accepted in the courtyard during the dances and generally not accepted inside
   the temple buildings. Ask, watch what others do, and keep out of the dancers' path.</p>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/best-time-to-visit/">Best time to visit Zanskar</a></li>
  <li><a href="/journeys/zanskar-cultural-journey/">Our cultural journey</a></li>
  <li><a href="/journeys/tailor-made/">Build a trip around a festival date</a></li>
</ul>
"""


# ==========================================================================
# phuktal
# ==========================================================================

PHUKTAL = """
<p class="lede">A monastery built around the mouth of a cave, on a cliff high above the Tsarap river in the
   Lungnak valley. It is the single most recognisable place in Zanskar, and it is still reached on foot.</p>

<h2>What it is</h2>
<p>Phuktal — also written Phugtal, and pronounced closer to <em>Phuk-tal</em> — is a Gelug monastery
   roughly 52 km south-east of Padum. The buildings are stacked in tiers below and around a natural cave
   in the cliff face, held on to the rock rather than built out from it. Around seventy monks live there.
   A spring runs from inside the cave, which is part of why the site was settled in the first place.</p>
<p>It was founded in the early fifteenth century by Jangsem Sherap Zangpo, a disciple of Tsongkhapa,
   the founder of the Gelug school. The cave itself is much older than the monastery: it was in use by
   hermits and scholars long before there were buildings on the cliff.</p>

<div class="facts">
  <div><dt>Order</dt><dd>Gelug</dd></div>
  <div><dt>Founded</dt><dd>Early 15th century</dd></div>
  <div><dt>Monks</dt><dd>≈ 70</dd></div>
  <div><dt>From Padum</dt><dd>≈ 52 km south-east</dd></div>
  <div><dt>Access</dt><dd>On foot</dd></div>
</div>

<h2>How you reach it</h2>
<p>Until 2023 the only way to Phuktal was to walk, for a day or more. A road now runs up the Lungnak
   valley as far as Purney, and from there it is a two to three hour walk along the Tsarap — moderate,
   with some exposure, on a good path. That is the short way, and it is what most visitors do.</p>
<p>The other way is to arrive at Phuktal at the end of a trek, which is what we would suggest if you
   have the time. Coming over the passes and down the last gorge, the monastery appears without warning
   above you. It is a different experience from being dropped at the road-head, and it is the reason our
   six-day route from Zangla finishes here rather than starting here.</p>

<h2>Visiting</h2>
<ul>
  <li>The monastery is a working religious community, not a museum. Ceremonies are not performances.</li>
  <li>Ask before photographing inside any building, and accept a no.</li>
  <li>Shoulders and knees covered. Shoes off where others take theirs off.</li>
  <li>There is simple guest accommodation near the monastery; it is basic and it fills up in high season.</li>
  <li>Carry out everything you carry in. There is no waste collection here.</li>
</ul>

<h2>Journeys that go there</h2>
<div class="grid grid--2" style="margin-top:24px">
  <article class="card"><div class="card__body">
    <h3><a href="/journeys/zangla-to-phuktal-trek/">Zangla to Phuktal</a></h3>
    <p>Six days on foot from our own village, over the passes, arriving at the monastery on the last day.</p>
    <a class="arrow-link" href="/journeys/zangla-to-phuktal-trek/">See the route</a></div></article>
  <article class="card"><div class="card__body">
    <h3><a href="/journeys/phuktal-to-tsokmichik-trek/">Phuktal to Tsokmichik</a></h3>
    <p>Eight days starting at the monastery and heading east, deeper into the upper Tsarap.</p>
    <a class="arrow-link" href="/journeys/phuktal-to-tsokmichik-trek/">See the route</a></div></article>
</div>
"""


# ==========================================================================
# zangla / padum
# ==========================================================================

ZANGLA = """
<p class="lede">Our village. Thirty-two kilometres north-east of Padum, at 3,931 metres, with a ruined fort
   on the ridge above it and barley fields on the flat ground below.</p>

<h2>The village</h2>
<p>Zangla sits near the northern end of the inhabited Zanskar valley, where the fields give out and the
   gorge begins. It is a working farming village: irrigation channels, poplars planted along them, flat
   roofs stacked with brushwood for winter fuel, and a road that arrives and then stops being a road.</p>
<p>Both of us were born here. It is where our families are, and it is the start of the trekking route we
   know better than any other — which is why our six-day journey begins at the edge of the village rather
   than at a car park somewhere convenient.</p>

<h2>Zangla Khar, the fort</h2>
<p>About a kilometre outside the village, on a hilltop, stands the ruin of Zangla Khar — the old fort or
   castle, believed to date from around the eleventh century. It is a short, steep walk up and worth doing
   in the late afternoon, when the light comes down the valley and you can see the whole run of fields
   below. Zangla was historically a small principality with its own ruling family, and the fort is what
   is left of that.</p>

<div class="facts">
  <div><dt>Altitude</dt><dd>3,931 m</dd></div>
  <div><dt>From Padum</dt><dd>32 km north-east</dd></div>
  <div><dt>Fort</dt><dd>Believed 11th century</dd></div>
  <div><dt>Road</dt><dd>Yes, seasonal</dd></div>
</div>

<h2>What there is to do</h2>
<ul>
  <li>Walk up to the fort in the evening.</li>
  <li>Follow an irrigation channel out along the contour and see how the water is distributed.</li>
  <li>Sit in the fields at harvest time, if you are here in September.</li>
  <li>Start walking south-east, which is what our route does.</li>
</ul>

<h2>Read next</h2>
<ul>
  <li><a href="/guides/">The guides from Zangla</a></li>
  <li><a href="/journeys/zangla-to-phuktal-trek/">The trek that starts here</a></li>
  <li><a href="/zanskar/villages-and-monasteries/">Other villages and monasteries</a></li>
</ul>
"""

PADUM = """
<p class="lede">The administrative centre of Zanskar and, for practical purposes, its front door.
   Around seven hundred people live here. Almost every journey into the region begins or ends in Padum.</p>

<h2>What Padum is for</h2>
<p>Padum sits where the Stod and the Lungnak meet, which is why it is where it is. It has the district
   offices, the hospital, the bank, the shops that stock anything, the bus stand and the guesthouses.
   It is not the reason anyone comes to Zanskar, and nobody pretends otherwise — but it is where you
   arrive, resupply, sleep before a trek and wash after one.</p>

<h2>Around Padum in a day</h2>
<ul>
  <li><strong>Karsha Monastery</strong> — across the valley, the largest in Zanskar and an easy half day.</li>
  <li><strong>Sani</strong> — west along the Stod, with its ancient stupa, roughly 6 km.</li>
  <li><strong>Stongdey</strong> — on the road towards Zangla, high on its spur.</li>
  <li><strong>Bardan</strong> — south along the Lungnak, on a rock above the river.</li>
  <li><strong>Pibiting</strong> — the hill and gompa right on the edge of town, good for a first
      afternoon when you are still getting used to the altitude.</li>
</ul>

<h2>Practical</h2>
<p>Accommodation is guesthouses and small hotels, simple but adequate. Mobile coverage exists but is
   unreliable, and connectivity in Ladakh can go down for extended periods; do not plan on being reachable.
   Cash matters — ATMs exist but are not dependable, so bring rupees from Leh. Shops carry basics rather
   than trekking equipment; bring anything technical with you.</p>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/how-to-get-there/">How to reach Padum</a></li>
  <li><a href="/zanskar/villages-and-monasteries/">Villages and monasteries</a></li>
  <li><a href="/plan/packing-list/">What to bring</a></li>
</ul>
"""


# ==========================================================================
# registry
# ==========================================================================

def pages():
    out = []

    hub = Page("zanskar",
               "Zanskar Travel Guide — The Region, Seasons and Access | " + BRAND,
               "A guide to the Zanskar valley in Ladakh, written by guides who live there: the region "
               "and its valleys, villages and monasteries, culture, the best time to visit and how to get there.",
               HUB.format(im=img("/assets/images/journey-valley.jpg",
                                 "A small group walking across a wide gravel plain towards snow-covered peaks")),
               crumbs=[("Zanskar", "/zanskar/")], section="zanskar",
               hero=dict(image="/assets/images/itinerary/day-3.jpg",
                         alt="Prayer flags and a cairn on an open ridge in Zanskar under a heavy sky",
                         eyebrow="Discover", h1="Zanskar",
                         intro="A high valley in Ladakh, closed in by two mountain ranges, "
                               "with around fourteen thousand people living in it."))
    out.append(hub)

    def mk(path, title, desc, h1, lede, body, crumb, imgpath, alt, schema=None):
        p = Page(path, title, desc, shell(body),
                 crumbs=[CR, (crumb, "/%s/" % path)], section="zanskar",
                 schema=schema or [], og_image=imgpath,
                 hero=dict(image=imgpath, alt=alt, eyebrow="Zanskar", h1=h1, intro=lede))
        return p

    out.append(mk("zanskar/the-region",
                  "The Zanskar Valley: Geography, Rivers and Passes | " + BRAND,
                  "Where Zanskar is, how the Stod and Lungnak valleys fit together, the passes that close "
                  "the region in, and what the landscape is actually like on foot.",
                  "The region and its valleys",
                  "Two rivers, a handful of passes, and about fourteen thousand people in an area the "
                  "size of a small country.",
                  REGION, "The region",
                  "/assets/images/journey-settlement.jpg",
                  "Turquoise meltwater running between red rock walls in a narrow section of the valley"))

    out.append(mk("zanskar/best-time-to-visit",
                  "Best Time to Visit Zanskar — Month by Month | " + BRAND,
                  "When to travel to Zanskar: a month-by-month guide to weather, road openings, river "
                  "levels and trekking conditions, from the guides who walk here every season.",
                  "Best time to visit Zanskar",
                  "Mid-June to mid-September for walking. Early September if you want our honest "
                  "preference. Here is what changes, and why.",
                  BEST_TIME.format(winter=todo(
                      "Do we offer a winter programme, and if so which one? Until that is decided this "
                      "paragraph should not promise anything.")),
                  "Best time to visit",
                  "/assets/images/itinerary/day-5.jpg",
                  "A dark, stormy valley with a lone chorten on the trail and cloud closing over the ridge"))

    out.append(mk("zanskar/how-to-get-there",
                  "How to Get to Zanskar — Leh, Kargil and Manali Routes | " + BRAND,
                  "Three ways into Zanskar, with distances, driving times and season windows: the "
                  "Nimmu–Padum–Darcha road from Leh, the Pensi La from Kargil, and the Shinku La from Manali.",
                  "Getting to Zanskar",
                  "No airport, three roads, and all of them seasonal. What each one involves and which "
                  "we would choose.",
                  GET_THERE.format(permits=todo(
                      "Confirm the current permit situation for the specific routes we run, and whether "
                      "anything changed for the 2027 season.")),
                  "Getting there",
                  "/assets/images/tsokmichik/day-8.jpg",
                  "A brown mountainside dropping to a river, with the line of a track visible along it"))

    out.append(mk("zanskar/villages-and-monasteries",
                  "Monasteries and Villages of Zanskar | " + BRAND,
                  "Karsha, Phuktal, Stongdey, Bardan and Sani, and the farming villages between them — "
                  "what each one is, and how to visit respectfully.",
                  "Villages and monasteries",
                  "The great gompas of the valley, the villages that support them, and how to be "
                  "a decent guest in both.",
                  VILLAGES, "Villages and monasteries",
                  "/assets/images/tsokmichik/day-7.jpg",
                  "A stone village house with a wooden window frame and brushwood stacked on the flat roof"))

    out.append(mk("zanskar/culture-and-traditions",
                  "Culture and Daily Life in Zanskar | " + BRAND,
                  "Tibetan Buddhism as daily practice, the barley year, houses and hospitality, the "
                  "language, and how to be a good guest in a Zanskari village.",
                  "Culture and traditions",
                  "Religion, farming and family are not separate subjects here. A short guide to how "
                  "the valley actually works.",
                  CULTURE, "Culture and traditions",
                  "/assets/images/tsokmichik/day-3.jpg",
                  "Low stone houses and enclosures of an old settlement on a dry slope in the upper valley"))

    out.append(mk("zanskar/festivals",
                  "Zanskar Festivals: Karsha Gustor, Stongdey and Sani | " + BRAND,
                  "The monastery festivals of Zanskar, when they roughly fall, what happens at one, and "
                  "how to plan a trip around a date that moves every year.",
                  "Festivals",
                  "Masked dances, a moving lunar calendar, and a day out for the whole valley.",
                  FESTIVALS.format(dates=todo(
                      "Confirmed festival dates for the coming season — Karsha Gustor, Stongdey Gustor, "
                      "Sani Naro Nasjal. Update this block every year.")),
                  "Festivals",
                  "/assets/images/tsokmichik/day-6.jpg",
                  "A whitewashed chorten hung with prayer flags above a green meadow, with pack horses resting"))

    out.append(mk("zanskar/phuktal-monastery",
                  "Phuktal Monastery, Zanskar — The Cave Gompa | " + BRAND,
                  "Phuktal (Phugtal) Monastery: a Gelug monastery built around a cave above the Tsarap "
                  "river, founded in the early 15th century and still reached on foot.",
                  "Phuktal Monastery",
                  "Built around the mouth of a cave, on a cliff above the Tsarap. Around seventy monks "
                  "live there. You arrive on foot.",
                  PHUKTAL, "Phuktal Monastery",
                  "/assets/images/itinerary/day-6.jpg",
                  "Phuktal Monastery in warm light, its white buildings stacked below the cave mouth in the cliff",
                  schema=[attraction("Phuktal Monastery",
                                     "Gelug monastery built around a cave above the Tsarap river in the "
                                     "Lungnak valley, Zanskar, Ladakh.")]))

    out.append(mk("zanskar/zangla",
                  "Zangla, Zanskar — The Village and its Fort | " + BRAND,
                  "Zangla at 3,931 m, 32 km north-east of Padum: the village, the eleventh-century fort "
                  "on the ridge above it, and the start of our six-day trek.",
                  "Zangla",
                  "Our village: barley fields, a ruined fort on the ridge, and the point where the road "
                  "stops being a road.",
                  ZANGLA, "Zangla",
                  "/assets/images/itinerary/day-1.jpg",
                  "Cultivated fields on the valley floor below Zangla, seen from the trail above in evening light",
                  schema=[attraction("Zangla", "Village in the Zanskar valley, Ladakh, with an "
                                               "eleventh-century hilltop fort.")]))

    out.append(mk("zanskar/padum",
                  "Padum, Zanskar — Arriving, Staying and What to See | " + BRAND,
                  "Padum, the administrative centre of Zanskar: what it is for, what you can see in a day "
                  "around it, and the practical things to sort out before heading into the valley.",
                  "Padum",
                  "Not the reason you come to Zanskar, but where you arrive, resupply and sleep before "
                  "the walking starts.",
                  PADUM, "Padum",
                  "/assets/images/itinerary/day-4.jpg",
                  "A cairn beside a braided river in a wide, dry valley with steep golden slopes above"))

    return out
