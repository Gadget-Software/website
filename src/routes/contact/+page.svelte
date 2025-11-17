<script>
  import Footer from "../Footer.svelte";
  let formStatus = "";
  let submitting = false;

  async function onSubmit(e) {
    if (submitting) return;
    submitting = true;
    formStatus = "Submitting...";
    // let the native POST happen; this is just UX sugar
    // if you stay on the same page (no redirect), you could intercept here and fetch instead
  }
</script>

<section class="wrap">
  <header class="page-header">
    <h1>I work with artists, teachers, and business builders</h1>
    <p class="sub">Premium, selective, and tailored to longer-term outcomes.</p>
  </header>

  <div class="grid">
    <!-- Pricing / Positioning -->
    <aside class="pricing-card">
      <h2>How I Work</h2>
      <ul>
        <li><strong>Consulting & Coaching</strong><br />
          Sessions start at <b>¥25,000/hr</b>. Discounted packages available for longer engagements.
        </li>
        <li><strong>Teaching Immersions</strong><br />
          In-person 5+ day immersions, <b>¥600,000 base</b>, where I take you by the hand, giving you access to my entire knowledge-base, and get you implementing marketing and other business strategies custom tailored to you and your goals. 
        </li>
        <li><strong>Done for You Marketing & Software</strong><br />
          Marketing & Software Projects from <b>¥3,000,000 base</b>, with implementation scoped collaboratively.
        </li>
      </ul>
      <p class="note">I prioritize coaching-led, longer relationships.</p>
    </aside>

    <!-- Contact Form (Formspree) -->
    <form 
      class="contact-form"
      action="https://formspree.io/f/mwpndjey" 
      method="POST" 
      on:submit={onSubmit}
    >
      <!-- subject for Formspree -->
      <input type="hidden" name="subject" value="New Contact Message from Website" />
      <!-- honeypot (spam trap) -->
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="hp" />

      <h2>Start a Conversation</h2>

      <label>
        Name:
        <input type="text" name="name" required />
      </label>

      <label>
        Email:
        <input type="email" name="email" required />
      </label>

      <label>
        Message:
        <textarea name="message" required placeholder="What are you trying to achieve? Timeline, constraints, context…"></textarea>
      </label>

      <!-- Optional: quick intent fields (helpful for triage, Formspree will include them) -->
      <label>
        Engagement interest:
        <select name="engagement">
          <option value="">Select…</option>
          <option>Hourly Session</option>
          <option>10-Session Pack</option>
          <option>Marketing Project</option>
          <option>Software Project</option>
        </select>
      </label>

      <label>
        Indicative budget:
        <select name="budget">
          <option value="">Select…</option>
          <option>¥150,000–¥600,000</option>
          <option>¥600,000–¥1,200,000</option>
          <option>¥1,200,0000+</option>
        </select>
      </label>

      <button type="submit">Send</button>
      <p class="form-status">{formStatus}</p>
    </form>
  </div>
</section>

<style>
/* layout shell */
.wrap {
  padding: 2.5em 1.2em;
}

.page-header {
  max-width: 900px;
  margin: 0 auto 1.4em auto;
  text-align: center;
}
.page-header h1 {
  margin: 0 0 .25em 0;
  font-size: clamp(1.2rem, 3.6vw, 2rem);
  color: #2a2e34;
  letter-spacing: .2px;
}
.page-header .sub {
  color: #5a6270;
  margin: 0;
}

/* responsive grid for pricing + form */
.grid {
  display: grid;
  gap: 1.2em;
  grid-template-columns: 1fr;
  max-width: 1100px;
  margin: 0 auto;
}
@media (min-width: 900px) {
  .grid {
    grid-template-columns: 1fr 1fr;
    align-items: start;
  }
}

/* pricing card */
.pricing-card {
  max-width: 520px;
  margin: 0 auto;
  padding: 2em 2.2em;
  border-radius: 12px;
  box-shadow: 0 2px 16px 0 rgba(0,0,0,0.08);
  background: #f8fafc;
  border: 1px solid #e6e9ef;
}
.pricing-card h2 {
  margin: 0 0 .6em 0;
  color: #2a2e34;
  font-size: 1.3em;
  font-weight: 600;
}
.pricing-card ul {
  margin: 0 0 .8em 1.2em;
  padding: 0;
  color: #303642;
  display: grid;
  gap: .8em;
}
.pricing-card .note {
  color: #596276;
  font-size: .95em;
  border-left: 3px solid #6a8cff;
  padding-left: .6em;
}

/* your original form styles */
.contact-form {
  max-width: 520px;
  margin: 0 auto;
  padding: 2em 2.5em 2.5em 2.5em;
  border-radius: 12px;
  box-shadow: 0 2px 16px 0 rgba(0,0,0,0.08);
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 1.2em;
}

.contact-form h2 {
  text-align: left;
  margin-bottom: .2em;
  color: #2a2e34;
  font-size: 1.2em;
  font-weight: 600;
}

.contact-form label {
  display: flex;
  flex-direction: column;
  font-weight: 500;
  gap: 0.4em;
  color: #23272f;
}

.contact-form input[type="text"],
.contact-form input[type="email"],
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

.contact-form button:hover {
  background: #5273e0;
}

.form-status {
  text-align: left;
  color: #6a8cff;
  font-size: .95em;
  margin-top: .2em;
}

/* honeypot field (hidden) */
.hp {
  position: absolute !important;
  left: -9999px !important;
  width: 1px; height: 1px; opacity: 0;
}

/* Optional: center Cloudflare Turnstile if you add it later */
.cf-turnstile {
  margin: 0.5em 0 0.5em 0;
  align-self: center;
}
</style>

<Footer />
