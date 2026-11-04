<script lang="ts">
  import Footer from "./Footer.svelte";

  let igProfile = "";
  let postDaily = "";
  let openToFeedback = "";
  let offer = "";
  let targetMonthlyRevenue = "";
  let contentBudget = "";
  let valuesCommunication = "";
  let whatsappNumber = "";
  
  const FORMSPREE = "https://formspree.io/f/mwpndjey";
  const VSL_ID = "k08gEChaUqs";

  let submitting = false;
  let submitted = false;
  let error = "";

  const whoFor = [
    "You want to work on your communication, messaging, and understanding your ideal customer - and you're excited to explore, test, and try things out.",
    "You don't want to just be told what to do. You want to notice for yourself what's working and what's not, and you're willing to spend time reviewing your own profile.",
    "You're happy to put in volume and reps - you just need direction and a community to support your action.",
    "You're capable of taking feedback and insight, implementing it, and running with it.",
    "You want to use Instagram as a real marketing channel for your business, and you're willing to stay focused on it until it works.",
    "You have an offer - or you're happy to use posting regularly as a chance to figure out what your offer could be.",
  ];

  const whoNotFor = [
    "Posting with regularity on Instagram feels more like a hassle than something useful.",
    "When someone gives you feedback, or encourages you to post or think, you'd rather ignore it and do your own thing.",
    "Being called out on making excuses instead of taking action is annoying to you.",
    "You're not interested in learning the business side of content creation on Instagram.",
  ];

  const features = [
    {
      title: "Active Accountability",
      body: "A real human will directly message you to prod you into action if you start to fall off or lose motivation - free for those who qualify.",
    },
    {
      title: "Expert Feedback",
      body: "Regular feedback on your profile from a diverse set of people who've grown real businesses through Instagram, ranging from 10K to 500K+ followers, across a variety of backgrounds and industries.",
    },
    {
      title: "A Real Community",
      body: "A group of motivated, active, engaged people of different account sizes and styles, all posting regularly - raising your standards, inspiring you with their wins, and cheering you on through what can otherwise be a lonely process.",
    },
    {
      title: "Discover Your Own Gifts",
      body: "An ethos of discovering your own strengths and unique gifts, and learning to package them so they help others - and you - come alive through a real process of growth that's tested by, and yields, real results.",
    },
  ];

  function buildMessage() {
    return [
      "New Sprocket Instagram Training application",
      "",
      `Instagram profile: ${igProfile}`,
      `Willing to post daily (multiple times/day)?: ${postDaily}`,
      `Open to feedback via message/calls?: ${openToFeedback}`,
      `Offer / industry: ${offer}`,
      `Target monthly revenue from IG traffic: ${targetMonthlyRevenue}`,
      `Monthly budget for content creation/improvement: ${contentBudget}`,
      `Values improving communication skills?: ${valuesCommunication}`,
      `Applicant WhatsApp: ${whatsappNumber}`,
    ].join("\n");
  }

  async function onSubmit(e: SubmitEvent) {
    e.preventDefault();
    if (submitting) return;
    submitting = true;
    error = "";

    const body = new FormData();
    body.set("_subject", "New Sprocket Instagram Training Application");
    body.set("igProfile", igProfile);
    body.set("postDaily", postDaily);
    body.set("openToFeedback", openToFeedback);
    body.set("offer", offer);
    body.set("targetMonthlyRevenue", targetMonthlyRevenue);
    body.set("contentBudget", contentBudget);
    body.set("valuesCommunication", valuesCommunication);
    body.set("whatsappNumber", whatsappNumber);
    body.set("message", buildMessage());

    try {
      const res = await fetch(FORMSPREE, {
        method: "POST",
        headers: { Accept: "application/json" },
        body
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok || data?.ok === false) {
        const detail =
          data?.errors?.map((err: { message?: string }) => err.message).filter(Boolean).join(" ") ||
          data?.error ||
      `Submission failed (${res.status})`;
      throw new Error(detail);
      }

      submitted = true;
    } catch (err) {
      error = err instanceof Error ? err.message : "Something went wrong submitting the form. Please try again.";
    } finally {
      submitting = false;
    }
  }
</script>

<svelte:head>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  <link
    href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap"
    rel="stylesheet"
  />
</svelte:head>

<!-- hero section -->
<section class="hero bg-cyan-900 text-white">
  <div class="max-w-screen-lg mx-auto px-4">
    <div class="text-center py-14 md:py-24 flex flex-col items-center gap-6 md:gap-8">
      <div class="wordmark">
        <svg class="gear" viewBox="0 0 100 100" width="56" height="56" aria-hidden="true">
          <g fill="#ffd23f" stroke="#7a4b00" stroke-width="3" stroke-linejoin="round">
            <rect x="44" y="0" width="12" height="20" transform="rotate(0 50 50)" />
            <rect x="44" y="0" width="12" height="20" transform="rotate(45 50 50)" />
            <rect x="44" y="0" width="12" height="20" transform="rotate(90 50 50)" />
            <rect x="44" y="0" width="12" height="20" transform="rotate(135 50 50)" />
            <rect x="44" y="0" width="12" height="20" transform="rotate(180 50 50)" />
            <rect x="44" y="0" width="12" height="20" transform="rotate(225 50 50)" />
            <rect x="44" y="0" width="12" height="20" transform="rotate(270 50 50)" />
            <rect x="44" y="0" width="12" height="20" transform="rotate(315 50 50)" />
            <circle cx="50" cy="50" r="28" />
          </g>
          <circle cx="50" cy="50" r="13" fill="#0b1730" stroke="#7a4b00" stroke-width="3" />
        </svg>
        <h1 class="mega-title">SPROCKET</h1>
      </div>
      <p class="mega-subtitle">INSTAGRAM TRAINING</p>
      <p class="text-lg md:text-2xl text-cyan-100 max-w-2xl">
        You sell transformation. You built an audience. But it is not financially stable enough to go deeper with the work.
      </p>
      <div class="vsl">
        <iframe
           src="https://www.youtube-nocookie.com/embed/{VSL_ID}?rel=0&modestbranding=1&playsinline=1"
           title="Sprocket Instagram Training"
           allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
           allowfullscreen
           loading="lazy"
        ></iframe>
      </div>
      <a href="#apply" class="cta-button">Apply Now</a>
    </div>
  </div>
</section>

<!-- who it's for / not for -->
<section class="bg-gray-50 text-cyan-900">
  <div class="max-w-screen-lg mx-auto px-4 py-12 md:py-20">
    <div class="grid gap-8 md:grid-cols-2">
      <div class="fit-card fit-yes">
        <h2>This is for you if...</h2>
        <ul>
          {#each whoFor as item}
            <li><span class="mark yes">✓</span>{item}</li>
          {/each}
        </ul>
      </div>
      <div class="fit-card fit-no">
        <h2>This is not for you if...</h2>
        <ul>
          {#each whoNotFor as item}
            <li><span class="mark no">✗</span>{item}</li>
          {/each}
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- features + benefits -->
<section class="bg-white text-cyan-900">
  <div class="max-w-screen-lg mx-auto px-4 py-12 md:py-20">
    <h2 class="section-title text-center">What&apos;s in it for you?</h2>
    <div class="grid gap-6 md:grid-cols-2 mt-8">
      {#each features as feature}
        <div class="feature-card">
          <h3>{feature.title}</h3>
          <p>{feature.body}</p>
        </div>
      {/each}
    </div>
  </div>
</section>

<!-- testimonial -->
<section class="bg-gray-50 text-cyan-900">
  <div class="max-w-screen-lg mx-auto px-4 py-12 md:py-20">
    <h2 class="section-title text-center">What members say</h2>
    <blockquote class="testimonial mt-8">
      <p>
        "Your proactive approach is effective. Thank you for inviting me - it was quite helpful for my process.
        I'm not sure I would've gotten two reels past 80,000 views in the past few days if you didn't push back
        on my excuses when you talked about posting dailies. I'd never even heard that term before. Thank you
        for being tough on me - besides myself, I've never had anyone tough with me when it comes to getting
        things done. Because my results are usually good, I think I underestimate that part of the process
        sometimes."
      </p>
      <p>
        "Thank you for being real with your thoughts when communicating with me. I took it as objectively
        constructive."
      </p>
      <footer>- Sprocket member, two reels past 80K views in one week after joining</footer>
    </blockquote>
  </div>
</section>

<section class="bg-white text-cyan-900">
  <div class="max-w-screen-lg mx-auto px-4 py-12 md:py-20">
    <article class="letter">
      <p class="pull">
        I'll get you there, by teaching you the secrets of what would have sold, even when you had just 100 followers.
      </p>
      <p>In order to be successful selling a product on Instagram, most people think you need:</p>
      <ul>
        <li>A massive following</li>
        <li>A cheap product to sell on Instagram</li>
        <li>A competitive offer against the market</li>
      </ul>
      <p>
        This is all a mega trap. Unless you are going to meme-ify yourself, it is unlikely you will have the million-plus followers necessary to convert a low-ticket offer easily.
      </p>
      <p>
        Plus, as someone who deeply cares about transformation, you yourself probably don't really care about those things. You likely care a lot more about going deeper with your clients, offering unique value related to your strengths, and being valued in a non-commodified way for the uniqueness of your perspective.
      </p>
      <p>
        But you're blocked. It's highly likely you are in some weird halfway liminal space, where you have an offer, maybe even made a little money here and there. There's a door open to completely doing your own thing, and perhaps you have your foot partially through it, but there's something that's keeping you from getting all the way through.
      </p>
      <p>This is a tragedy.</p>
      <p>
        Transformational products are needed. Now, more than ever. In the uncertainty of AI, cyberattacks, pandemics, we need more people to realize they are more than what they've been told to think about themselves. And that requires the people who steward these products to put them out there at their highest capacity.
      </p>
      <p>
        Working another job, not being priced high enough, or letting fear and anxiety stop you from doubling down on the signals that this is actually working, is a disaster. No one is going to pick up the slack on our behalf. We need to step up for our own sake, and for the sake of the people around us.
      </p>
      <p>
        But the good news is that it is actually working. In fact, that's the best news. The hardest part is out of the way.
      </p>
      <p>
        Financial abundance, the freedom to choose how you use your time, designing a life for yourself through living your highest contribution. All those things are possible. And it's not just possible for me or someone else. It's possible for you.
      </p>
      <p>So now you know that it's possible. How do you get there?</p>
      <p class="pull">How it works</p>
      <p>
        A lot of building a business with predictable revenue is more like going to the gym than most people think. You carve out the time, put in reps, monitor how things are going, and adjust.
      </p>
      <p>
        For your business you will need to take action, track, and receive and implement feedback.
      </p>
      <p>
        Taking action simply boils down to consistently posting content, sending outreach, doing follow-ups, and having sales calls.
      </p>
      <p>Tracking means paying attention to how much of every activity is happening.</p>
      <p>
        Getting and implementing feedback means problem-solving bottlenecks, noticing trends, experimenting, and doubling down on what's working while cutting the unnecessary away.
      </p>
      <p>The issues with a business always boil down to the following:</p>
      <ul>
        <li>A lack of enough action</li>
        <li>Not tracking or paying attention to the numbers related to the funnel</li>
        <li>Not actively considering the problem, or ways to improve the funnel</li>
      </ul>
      <p>
        If any of these three are missing, you're likely not going to progress at all, other than by sheer luck. Transformation businesses, like the product they sell, require tons of intentionality.
      </p>
      <p>My product tackles all three of these.</p>
      <p>Accountability for posting, and tracking for outreach, follow-ups, and sales interactions.</p>
      <p>
        Coaching to help you reflect on your funnel and your ideal customer, and to diagnose and fix any issues you are noticing in the process.
      </p>
      <p>Simple? Yes. Ruthlessly effective? Yes.</p>
      <p>
        My product is the result of being nearly a year in the lab, trying to figure out how businesses on Instagram actually work, from starting at scratch all the way to being semi-famous.
      </p>
      <p>
        Observing clients as they make their way, and countless conversations with creators, showed me the pathway to consistent profitability. The same fear of posting consistently shows up again later, when people need to engage with their audience more deeply.
      </p>
      <p>
        That's what made me realize that accountability to doing volume, while it seems like the least important part, is actually the most important. The rest follows very naturally, especially as more success is found.
      </p>
      <p>
        Now, even though it is simple, it is not easy. I have brought people into the fold who simply gave up because of how challenging it actually is to be consistent. They get distracted, believe there is another way out that doesn't require as much effort, and disappear.
      </p>
      <p>
        But if you've read this far, you probably recognize you don't have another way out. You have to make this work, whether it's this person or the next person who helps you. Work is no obstacle. You just need direction.
      </p>
      <p>I get it. I've been there too. Let's not waste any more time.</p>
      <p><a href="#apply" class="cta-button">Fill out the form, and let's get to work.</a></p>
    </article>
  </div>
</section>


<!-- intake form -->
<section id="apply" class="bg-white text-cyan-900">
  <div class="max-w-screen-lg mx-auto px-4">
    <div class="py-10 md:py-16">
      {#if submitted}
        <div class="wrap">
          <div class="contact-form" style="max-width:560px;">
            <h2>Application received.</h2>
            <p class="lede">
              Thanks for applying to Sprocket. I review every application personally - if it's a fit, I'll message
              you on WhatsApp using the number you shared to bring you into the group.
            </p>
          </div>
        </div>
      {:else}
        <form class="wrap" on:submit={onSubmit}>
          <div class="contact-form" style="max-width:640px;">
            <h2>Sprocket Instagram Training Application</h2>

            <label>
              What is your Instagram profile?
              <input type="text" bind:value={igProfile} required placeholder="@yourhandle or profile link" />
            </label>

            <label>
              Are you willing to post to Instagram every day - potentially multiple times a day - to dial in your
              messaging, ICP, and business?
              <select bind:value={postDaily} required>
                <option value="">Select…</option>
                <option>Yes</option>
                <option>No</option>
              </select>
            </label>

            <label>
              Are you open to receiving feedback on your profile over message, or on calls?
              <select bind:value={openToFeedback} required>
                <option value="">Select…</option>
                <option>Yes</option>
                <option>No</option>
              </select>
            </label>

            <label>
              What is your offer? If you haven't figured it out yet, that's ok, you can refine it as you post - but
              what is your industry, if that's the case?
              <textarea bind:value={offer} required placeholder="Describe your offer, or your industry if it's still unclear"></textarea>
            </label>

            <label>
              How much money would you like to make from Instagram-driven traffic per month?
              <input type="text" bind:value={targetMonthlyRevenue} required placeholder="e.g. $5,000/mo" />
            </label>

            <label>
              How much are you willing to spend to create and/or improve content on a monthly basis?
              <input type="text" bind:value={contentBudget} required placeholder="e.g. $500/mo" />
            </label>

            <label>
              Do you value upping your communication skills as part of this process?
              <select bind:value={valuesCommunication} required>
                <option value="">Select…</option>
                <option>Yes</option>
                <option>No</option>
              </select>
            </label>

            <label>
              What is your WhatsApp number?
              <input type="tel" bind:value={whatsappNumber} required placeholder="+1 555 123 4567" />
            </label>

            <button type="submit" disabled={submitting}>
              {submitting ? "Submitting..." : "Submit Application"}
            </button>
            {#if error}
              <p class="form-status" style="color:#c0392b;">{error}</p>
            {/if}
          </div>
        </form>
      {/if}
    </div>
  </div>
</section>

<style>
  /* hero / wordmark */
  .hero {
    background: linear-gradient(180deg, #0b1730 0%, #16406b 100%);
  }

  .wordmark {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .gear {
    animation: spin 9s linear infinite;
    flex-shrink: 0;
  }

  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }

  .mega-title {
    font-family: "Press Start 2P", monospace;
    font-size: clamp(1.8rem, 7vw, 3.5rem);
    line-height: 1;
    margin: 0;
    color: #ffd23f;
    letter-spacing: 2px;
    text-shadow:
      3px 3px 0 #0b1730,
      5px 5px 0 rgba(0, 0, 0, 0.35);
  }

  .mega-subtitle {
    font-family: "Press Start 2P", monospace;
    font-size: clamp(0.7rem, 2.2vw, 1.1rem);
    letter-spacing: 3px;
    color: #7dd3fc;
    margin: -0.5rem 0 0 0;
  }
  .vsl {
    width: min(340px, 86vw);
    aspect-ratio: 9 / 16;
    max-height: 72vh;
    border-radius: 16px;
    overflow: hidden;
    background: #000;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35);
    border: 3px solid #ffd23f;
  }
  .vsl iframe {
    width: 100%;
    height: 100%;
    border: 0;
    display: block;
  }

  .cta-button {
    display: inline-block;
    background: #ffd23f;
    color: #1b2a4a;
    font-weight: 700;
    padding: 0.9em 2em;
    border-radius: 8px;
    text-decoration: none;
    transition: transform .15s, background .15s;
  }

  .cta-button:hover {
    background: #ffdc6b;
    transform: translateY(-2px);
  }

  /* who's for / not for */
  .fit-card {
    background: #fff;
    border-radius: 12px;
    padding: 2em;
    box-shadow: 0 2px 16px 0 rgba(0, 0, 0, 0.06);
  }

  .fit-card h2 {
    font-size: 1.3em;
    font-weight: 700;
    margin-bottom: 0.8em;
  }

  .fit-yes h2 {
    color: #1a7f4b;
  }

  .fit-no h2 {
    color: #b3261e;
  }

  .fit-card ul {
    display: flex;
    flex-direction: column;
    gap: 0.9em;
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .fit-card li {
    display: flex;
    gap: 0.6em;
    align-items: flex-start;
    line-height: 1.5;
    color: #303642;
  }

  .mark {
    flex-shrink: 0;
    font-weight: 700;
  }

  .mark.yes {
    color: #1a7f4b;
  }

  .mark.no {
    color: #b3261e;
  }

  /* features */
  .section-title {
    font-size: 1.8em;
    font-weight: 700;
    color: #164e63;
  }

  .feature-card {
    background: #f8fafc;
    border: 1px solid #e6e9ef;
    border-radius: 12px;
    padding: 1.6em 1.8em;
  }

  .feature-card h3 {
    font-size: 1.15em;
    font-weight: 700;
    color: #0e7490;
    margin-bottom: 0.4em;
  }

  .feature-card p {
    color: #444;
    line-height: 1.5;
    margin: 0;
  }

  /* testimonial */
  .testimonial {
    max-width: 760px;
    margin: 0 auto;
    background: #fff;
    border-radius: 12px;
    padding: 2em 2.4em;
    box-shadow: 0 2px 16px 0 rgba(0, 0, 0, 0.06);
    border-left: 4px solid #6a8cff;
  }

  .testimonial p {
    font-family: serif;
    font-size: 1.1em;
    line-height: 1.6;
    color: #303642;
    margin: 0 0 1em 0;
  }

  .testimonial footer {
    margin-top: 1em;
    font-weight: 600;
    color: #164e63;
  }

  /* form */
  .wrap {
    padding: 0;
  }

  .contact-form {
    margin: 0 auto;
    padding: 2em 2.5em 2.5em 2.5em;
    border-radius: 12px;
    box-shadow: 0 2px 16px 0 rgba(0,0,0,0.08);
    background: #fff;
    display: flex;
    flex-direction: column;
    gap: 1.2em;
    text-align: left;
  }

  .contact-form h2 {
    margin-bottom: .2em;
    color: #2a2e34;
    font-size: 1.3em;
    font-weight: 600;
  }

  .contact-form label {
    display: flex;
    flex-direction: column;
    font-weight: 500;
    gap: 0.4em;
    color: #23272f;
  }

  .hp {
    position: absolute;
    left: -9999px;
    height: 0;
    overflow: hidden;
  }

  .contact-form input[type="text"],
  .contact-form input[type="tel"],
  .contact-form textarea,
  .contact-form select {
    padding: 0.7em;
    border: 1px solid #d0d4da;
    border-radius: 6px;
    font-size: 1em;
    transition: border-color .2s;
    background: #fafbfc;
  }

  .contact-form input:focus,
  .contact-form textarea:focus,
  .contact-form select:focus {
    outline: none;
    border-color: #6a8cff;
    background: #f0f6ff;
  }

  .contact-form button {
    margin-top: 0.4em;
    background: #6a8cff;
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 0.9em 1.2em;
    font-size: 1em;
    font-weight: 600;
    cursor: pointer;
    transition: background .17s;
  }

  .contact-form button:hover:not(:disabled) {
    background: #5273e0;
  }

  .contact-form button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  .form-status {
    text-align: left;
    font-size: .95em;
    margin-top: .2em;
  }

  .lede {
    color: #444;
    line-height: 1.5;
  }
.letter {
  max-width: 42rem;
  margin: 0 auto;
}

.letter p,
.letter li {
  font-size: 1.125rem;
  line-height: 1.7;
  color: #1f2933;
}

.letter p {
  margin: 0 0 1.15em 0;
}

.letter ul {
  margin: 0 0 1.15em 1.2em;
  list-style: disc;
}

.letter li + li {
  margin-top: 0.35em;
}

.letter .pull {
  font-size: 1.45rem;
  line-height: 1.4;
  font-weight: 700;
  color: #0b1730;
}

.letter .cta-button {
  margin-top: 0.5em;
}

</style>

<Footer />
