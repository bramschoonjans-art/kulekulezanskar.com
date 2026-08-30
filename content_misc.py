# -*- coding: utf-8 -*-
"""About, stories, contact and the legal pages."""

from build import Page, todo, img, wa_link, EMAIL, BRAND, SITE, WHATSAPP_DISPLAY


def shell(inner, narrow=True):
    return ('<div class="section"><div class="wrap %s prose">\n%s\n</div></div>'
            % ("wrap--narrow" if narrow else "", inner))


ABOUT = """
<p class="lede">Kulé kulé Zanskar is two guides from Zangla and the people who work with them.
   It is not an agency, and it is not a brand somebody built around a valley they visit.</p>

<h2>How it started</h2>
<p>{origin}</p>

<h2>What the name means</h2>
<p><em>Kulé kulé</em> is Ladakhi for <em>slowly, slowly</em>. It is what you say to somebody hurrying a
   climb, and it is what people say to each other on a path here. We took it as a name because it is
   also our method: slow enough to acclimatise properly, slow enough to stop when a village invites you
   in, slow enough that the days have room in them.</p>

<h2>What we are</h2>
<ul>
  <li>Two guides, born in Zangla, guiding in our own region.</li>
  <li>A cook, horsemen and a driver from the same valley, working with us every season.</li>
  <li>Private groups of two to ten people, on your dates.</li>
  <li>Direct booking: the person who answers your message is the person who guides you.</li>
</ul>

<h2>What we are not</h2>
<ul>
  <li>Not a catalogue. We guide one region and we would rather do that well than list twenty.</li>
  <li>Not an international tour operator. There is no office in Europe and no 24-hour phone line.
      <a href="/guides/why-travel-with-a-local-guide/">What that means in practice</a>.</li>
  <li>Not the cheapest, and not trying to be. The price reflects a crew that is paid properly for
      a short season.</li>
</ul>

<h2>Who runs it</h2>
<p>{entity}</p>

<h2>The website</h2>
<p>The photographs and the recorded GPS tracks on this site were made on our own routes.
   Nothing here is stock imagery, and nothing describes a place we have not walked.</p>

<div class="btn-row" style="margin-top:32px">
  <a class="btn btn--primary" href="/guides/">Meet the guides</a>
  <a class="btn btn--ghost" href="/about/responsible-travel/">How we work</a>
</div>
"""

RESPONSIBLE = """
<p class="lede">Most operators have a page like this. Ours is deliberately specific, because the only
   version of it worth reading is the one with numbers in it.</p>

<h2>Where the money goes</h2>
<p>You pay us directly, so there is no international margin and no agency commission. Almost all of what
   you pay is spent within Ladakh: guides, cook, horsemen, drivers, horses, food bought in Padum and the
   villages, and camping equipment.</p>
<p>{money}</p>

<h2>Group size</h2>
<p>Two to ten people, and we do not make exceptions. Above ten, a camp stops fitting on the good ground,
   villages cannot host properly, and the valley stops being quiet — which is the thing people come for.
   A larger party gets split across two departures.</p>

<h2>Waste</h2>
<p>Everything we carry in is carried out, including what does not burn. Toilet pits are dug and filled
   in. We do not leave food waste for animals, and we do not bury packaging. If you see one of our crew
   doing otherwise, tell us — that is not what we pay them for.</p>
<p>Water is treated rather than bought in bottles. Bring a filter, tablets or a SteriPen; we do not hand
   out plastic bottles.</p>

<h2>Villages</h2>
<ul>
  <li>We camp where we have agreed to camp, not wherever is convenient.</li>
  <li>We buy locally where we can — vegetables, eggs, sometimes a night's accommodation — rather than
      carrying everything in from Leh.</li>
  <li>We do not hand things out to children. If you want to give something, we will help you give it to
      the school or the village.</li>
  <li>We ask before photographing people, and we take a no as an answer.</li>
</ul>

<h2>Fuel</h2>
<p>We cook on kerosene or gas, not on wood or dung. Wood is scarce here and dung is winter fuel for the
   households that produced it. This is not symbolic: a trekking group burning village fuel is a real
   cost to that village.</p>

<h2>The animals</h2>
<p>Load limits are respected and the horsemen have the final say on what a horse carries and where it
   crosses. If you are uncomfortable with anything you see, say so on the day.</p>

<h2>What we do not claim</h2>
<p>We do not offset your flight and we are not going to pretend that a week of low-impact walking
   cancels out a long-haul return. The flight is by far the largest environmental cost of this trip and
   it is yours to weigh. What we can say honestly is that the money you spend on the ground stays on the
   ground, and that the way we run a group is about as light as a group can be here.</p>

<h2>Read next</h2>
<ul>
  <li><a href="/zanskar/culture-and-traditions/">Being a good guest in a Zanskari village</a></li>
  <li><a href="/guides/why-travel-with-a-local-guide/">Why travel with a local guide</a></li>
</ul>
"""

STORIES = """
<div class="section">
  <div class="wrap wrap--narrow prose">
    <p class="lede">Short pieces from the valley: notes from the guides during the season, and
       accounts from people who walked with us.</p>
    <div class="note note--mineral">
      <p><strong>This section is waiting for its first pieces.</strong> {first}</p>
      <p class="small" style="margin-bottom:0">Six to ten pieces a year is plenty. Two kinds work best:
         a short field note from a guide about one thing that happened — the first snow on a pass, a
         harvest day in Zangla, why the river was too high this week — and a longer account from a
         traveller, published with their name and their permission.</p>
    </div>

    <h2>What will go here</h2>
    <ul>
      <li><strong>Field notes.</strong> One event, one photograph, 200 to 400 words, written or dictated
         by Chotak or Lhamath during the season.</li>
      <li><strong>Traveller accounts.</strong> Longer pieces from people who walked a route, with their
         own photographs where they have them.</li>
      <li><strong>Seasonal updates.</strong> What the road did this year, when the passes opened, how
         the harvest went.</li>
    </ul>
    <p>If you have walked with us and want to write something, we would like to read it.
       <a href="/contact/">Send it to us</a>.</p>
  </div>
</div>
"""

CONTACT = """
<div class="section">
  <div class="wrap">
    <div class="split split--wide-media">
      <div class="split__body">
        <h2>Send us a message</h2>
        <p>Dates, group size, how much walking you want — or just a question about the region.
           You do not need to be ready to book.</p>
        <p class="small muted">We answer every message ourselves, within three working days.
           Sometimes longer, when we are out on a route or the network in Zanskar is down.</p>

        <form class="form" method="post" action="#" data-endpoint="not-configured" style="margin-top:28px">
          <div class="field">
            <label for="name">Your name</label>
            <input id="name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="email">Email</label>
            <input id="email" name="email" type="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="journey">Which journey?</label>
            <select id="journey" name="journey">
              <option value="">Not sure yet</option>
              <option value="zangla-to-phuktal">Zangla to Phuktal — 6 days</option>
              <option value="phuktal-to-tsokmichik">Phuktal to Tsokmichik — 8 days</option>
              <option value="both">Both routes, back to back</option>
              <option value="cultural">Villages and monasteries — 7 days</option>
              <option value="tailor-made">Something tailor-made</option>
            </select>
          </div>
          <div class="field field--row">
            <div>
              <label for="dates">Dates or rough window</label>
              <input id="dates" name="dates" type="text" placeholder="e.g. first half of September 2027">
            </div>
            <div>
              <label for="group">Group size</label>
              <input id="group" name="group" type="number" min="1" max="20" value="2">
            </div>
          </div>
          <div class="field">
            <label for="message">Anything we should know</label>
            <p class="hint">Previous trekking, how you have handled altitude before, or anything
               you are unsure about. Honest answers help us give you a straight one.</p>
            <textarea id="message" name="message"></textarea>
          </div>
          <label class="consent">
            <input type="checkbox" name="consent" required>
            <span>I am happy for Kulé kulé Zanskar to use these details to answer my enquiry.
              See the <a href="/privacy/">privacy statement</a>.</span>
          </label>
          <div>
            <button class="btn btn--primary" type="submit">Send enquiry</button>
          </div>
        </form>
        <div class="note note--mineral" style="margin-top:18px">
          <p>{action}</p>
          <p style="margin-bottom:0">{formnote}</p>
        </div>
      </div>

      <div class="split__media">
        <div class="card" style="padding:24px">
          <h3 style="margin-top:0">Other ways to reach us</h3>
          <p><strong>WhatsApp</strong><br>
             <a href="{wa}">{wanumber}</a><br>
             <span class="small muted">Fastest, when we are in range.</span></p>
          <p><strong>Email</strong><br>
             <a href="mailto:{email}">{email}</a></p>
          <p style="margin-bottom:0"><strong>Where we are</strong><br>
             Zangla, Zanskar<br>Ladakh, India</p>
        </div>
        <div class="note" style="margin-top:18px">
          <p style="margin-bottom:0"><strong>Before you write</strong>, it may save a round trip to read
             <a href="/plan/fitness-and-difficulty/">fitness and difficulty</a> and
             <a href="/zanskar/best-time-to-visit/">best time to visit</a>.</p>
        </div>
      </div>
    </div>
  </div>
</div>
"""

PRIVACY = """
<h2>What this page is</h2>
<p>A plain statement of what happens to the information you give us. If anything here is unclear,
   write and ask.</p>

<h2>What we collect</h2>
<ul>
  <li>What you type into the enquiry form: name, email, dates, group size and your message.</li>
  <li>What you send us by WhatsApp or email, including your phone number.</li>
  <li>Before a journey: your insurance details, an emergency contact, and anything medical you choose
      to tell us that affects how we guide you.</li>
</ul>

<h2>What we do with it</h2>
<p>We use it to answer your enquiry and, if you travel with us, to organise and run your journey.
   We do not sell it, and we do not send marketing to people who have not asked for it.</p>

<h2>How long we keep it</h2>
<p>{retention}</p>

<h2>Who else sees it</h2>
<p>Nobody outside the people organising your journey, except where we have to share a name with a
   transport provider or a permit office for the trip itself.</p>

<h2>Analytics</h2>
<p>{analytics}</p>

<h2>Your rights</h2>
<p>Ask us what we hold about you, ask us to correct it, or ask us to delete it, by writing to
   <a href="mailto:{email}">{email}</a>. We will do it.</p>

<h2>Contact</h2>
<p>{controller}</p>
"""

TERMS = """
<div class="note note--mineral">
  <p>{warning}</p>
</div>

<h2>1 · Who you are contracting with</h2>
<p>{entity}</p>

<h2>2 · Booking and payment</h2>
<p>A booking is confirmed when the deposit is received. The balance is due on arrival, before the
   journey begins. Details on <a href="/plan/booking-and-payment/">booking and payment</a>.</p>

<h2>3 · Cancellation by you</h2>
<p>{cancel_you}</p>

<h2>4 · Cancellation or change by us</h2>
<p>We may change a route, camp or schedule for reasons of safety — weather, river levels, snow, illness
   or events beyond our control. Where a journey cannot take place at all for reasons on our side,
   the deposit is refunded in full.</p>

<h2>5 · Insurance</h2>
<p>Travel insurance covering trekking at the altitude of your route, including emergency evacuation and
   repatriation, is a condition of travelling with us. You must send us the policy number and emergency
   number before departure.</p>

<h2>6 · Your responsibilities</h2>
<ul>
  <li>Give us accurate information about your fitness, altitude history and health.</li>
  <li>Bring the equipment on the <a href="/plan/packing-list/">packing list</a>, in particular a
      sleeping bag rated for the conditions.</li>
  <li>Follow the guide's decisions on route, pace and safety during the journey.</li>
  <li>Hold a valid passport and visa.</li>
</ul>

<h2>7 · Risk</h2>
<p>Trekking in Zanskar takes place in remote terrain at high altitude, days from medical care, without
   communications. We manage that risk carefully but we cannot remove it, and you accept it by taking
   part. See <a href="/plan/safety-in-remote-areas/">safety in remote areas</a>.</p>

<h2>8 · Complaints</h2>
<p>Tell the guide during the journey if something is wrong; almost everything is fixable on the spot.
   Afterwards, write to <a href="mailto:{email}">{email}</a>.</p>

<h2>9 · Law</h2>
<p>{law}</p>
"""


def pages():
    out = []

    out.append(Page(
        "about", "About Kulé kulé Zanskar | " + BRAND,
        "Who we are: two guides born in Zangla, the crew who work with them, what the name means "
        "and how we organise journeys in the Zanskar valley.",
        shell(ABOUT.format(
            origin=todo("How Kulé kulé Zanskar started, in the guides' own words: whose idea it was, "
                        "when, and what they were doing before. Two or three short paragraphs."),
            entity=todo("The operating company, its registration, and how Kulé kulé Zanskar relates "
                        "to Ladakh Mountain Tour & Travel. State plainly who organises the journey, "
                        "who receives payment and who is responsible."))),
        crumbs=[("About", "/about/")], section="about",
        og_image="/assets/images/itinerary/day-1.jpg",
        hero=dict(image="/assets/images/itinerary/day-1.jpg",
                  alt="Cultivated fields on the valley floor below Zangla, seen from the trail above",
                  eyebrow="About", h1="Kulé kulé Zanskar",
                  intro="Two guides from Zangla, a crew from the same valley, and one region "
                        "we would rather know well than list.")))

    out.append(Page(
        "about/responsible-travel", "Responsible Travel in Zanskar | " + BRAND,
        "How we run journeys in Zanskar: where the money goes, why groups stay small, how waste and "
        "fuel are handled, and what we deliberately do not claim.",
        shell(RESPONSIBLE.format(
            money=todo("A concrete figure: roughly what share of the trek price is spent in Ladakh, "
                       "and how many people are employed per group. A number here is worth more than "
                       "a paragraph of intent."))),
        crumbs=[("About", "/about/"), ("Responsible travel", "/about/responsible-travel/")],
        section="about"))

    stories = Page(
        "stories", "Stories from Zanskar | " + BRAND,
        "Field notes from the guides and accounts from travellers who walked our routes in the "
        "Zanskar valley.",
        STORIES.format(first=todo(
            "The first three or four pieces: one field note from each guide and one traveller "
            "account. Until they exist this section should not be linked from the main navigation.")),
        crumbs=[("Stories", "/stories/")], section="stories",
        og_image="/assets/images/itinerary/day-3.jpg",
        hero=dict(image="/assets/images/itinerary/day-3.jpg",
                  alt="Prayer flags and a cairn on an open ridge under a heavy sky",
                  eyebrow="Journal", h1="Stories from the valley",
                  intro="Notes from the guides during the season, and accounts from people "
                        "who walked with us."))
    out.append(stories)

    out.append(Page(
        "contact", "Contact — Plan Your Journey in Zanskar | " + BRAND,
        "Tell us your dates, your group size and what kind of walking you want. We answer every "
        "message ourselves, within three working days.",
        CONTACT.format(
            action=todo("Form endpoint — a service such as Formspree or Netlify Forms, set to deliver "
                        "to two addresses so nothing is lost when one of us is offline."),
            formnote=todo("Confirm the form is delivering before launch: send a test enquiry and "
                          "check that both recipients receive it."),
            wa=wa_link("Juley! I would like to ask about a journey in Zanskar."),
            wanumber=WHATSAPP_DISPLAY,
            email=EMAIL),
        crumbs=[("Contact", "/contact/")], section=None,
        og_image="/assets/images/tsokmichik/day-2.jpg",
        hero=dict(image="/assets/images/tsokmichik/day-2.jpg",
                  alt="A walker and a loaded pack horse on a green trail beside the river",
                  eyebrow="Contact", h1="Plan your trip",
                  intro="A person answers, not a booking system.")))

    p = Page("privacy", "Privacy | " + BRAND,
             "What happens to the information you give us when you enquire about or book a journey.",
             shell(PRIVACY.format(
                 retention=todo("How long enquiry data and traveller data are kept, and when they "
                                "are deleted."),
                 analytics=todo("Which analytics tool is used, whether it sets cookies, and whether "
                                "a consent banner is therefore required. A privacy-friendly tool "
                                "avoids the banner entirely."),
                 controller=todo("Name and address of the entity responsible for this data."),
                 email=EMAIL)),
             crumbs=[("Privacy", "/privacy/")], section=None)
    p.h1 = "Privacy"
    out.append(p)

    t = Page("terms", "Terms and Conditions | " + BRAND,
             "The terms on which we organise and guide journeys in Zanskar: booking, cancellation, "
             "insurance, responsibilities and risk.",
             shell(TERMS.format(
                 warning=todo("These terms are a working draft written alongside the site. They must "
                              "be reviewed against Indian law and the law of the traveller's country "
                              "before the site goes live."),
                 entity=todo("Legal name, registration number and registered address of the "
                             "contracting entity."),
                 cancel_you=todo("The cancellation terms: what is refunded and up to which point "
                                 "before departure."),
                 law=todo("Governing law and where disputes are settled."),
                 email=EMAIL)),
             crumbs=[("Terms", "/terms/")], section=None)
    t.h1 = "Terms and conditions"
    out.append(t)

    return out
