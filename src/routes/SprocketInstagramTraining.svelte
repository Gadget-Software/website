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

  let submitting = false;
  let submitted = false;
  let error = "";

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

    const message = buildMessage();

    try {
      const res = await fetch("https://formspree.io/f/mwpndjey", {
        method: "POST",
        headers: { Accept: "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({
          subject: "New Sprocket Instagram Training Application",
          igProfile,
          postDaily,
          openToFeedback,
          offer,
          targetMonthlyRevenue,
          contentBudget,
          valuesCommunication,
          whatsappNumber,
          message,
        }),
      });
      if (!res.ok) throw new Error("Submission failed");

      submitted = true;
    } catch (err) {
      error = "Something went wrong submitting the form. Please try again.";
    } finally {
      submitting = false;
    }
  }
</script>

<!-- hero section -->
<section class="bg-cyan-900 text-white">
  <div class="max-w-screen-lg mx-auto px-4">
    <div class="text-center py-14 md:py-24 flex flex-col gap-4 md:gap-6">
      <h1 class="text-3xl md:text-5xl font-semibold leading-tight">
        Apply for <span class="text-cyan-300">Sprocket Instagram Training</span>
      </h1>
      <p class="text-lg md:text-2xl text-cyan-100">
        A small, hands-on group for people who are serious about posting consistently, refining their
        message, and turning Instagram into a real driver of their business.
      </p>
      <p class="text-lg md:text-2xl text-cyan-100">
        Fill out the application below. If it's a good fit, I'll message you on WhatsApp to bring you into the
        Sprocket group.
      </p>
    </div>
  </div>
</section>

<!-- intake form -->
<section class="bg-white text-cyan-900">
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
</style>

<Footer />
