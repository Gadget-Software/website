<script>
  import Column from "../../Column.svelte";
  import Footer from "../../Footer.svelte";
  import TestimonialCard from "../../testimonials/TestimonialCard.svelte";
</script>

<svelte:head>
  <title>Personal Brand for Artists & Teachers – Gadget Software</title>
</svelte:head>

<section class="bg-gray-50 py-10">
  <Column>
    <h2 class="big-text text-center text-cyan-800">
      Personal Brand Process for Artists & Teachers
    </h2>

    <TestimonialCard title="Step 1: Define Your Foundation">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            We map your **strengths**, **goals**, and viable **business models**.
            <br /><br />
            You get a custom action plan and your **off-platform hub**: personal website + email list.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            No more relying on algorithms. You own your audience.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 2: Study Proven Models">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            We analyze what **still works** in your niche:
            <br />
            • Patreon? Courses? Live events?<br />
            • YouTube → Email → Paid product?
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Touring rarely works unless you’re already famous. We focus on **scalable, sustainable paths**.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 3: Get Visible">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Time to **publish consistently** on YouTube, Instagram, TikTok — wherever your people are.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            We help you batch, schedule, and optimize for **algorithm + human engagement**.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 4: Remove Blockers (Optional but Critical)">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Can’t post consistently? We audit:
            <br />
            • Time<br />
            • Energy<br />
            • Motivation<br />
            • Skill gaps
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Sometimes **therapy or coaching** is the fix. We’ll point you there if needed.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 5: Analyze & Iterate">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            We track:
            <br />
            • Views → Email signups<br />
            • Engagement trends<br />
            • Content performance
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Every post is data. We refine hooks, thumbnails, CTAs — and **grow your list**.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 6: Build Your Offer Ladder">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Free → $9 → $97 → $997
            <br /><br />
            Digital courses, coaching, templates, memberships — tailored to **your** audience.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            We help you package what you already know how to do.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 7: Launch Cycle">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Launch offer → Free content → Launch again
            <br /><br />
            We build automated funnels: email, waitlists, scarcity.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Track conversions. Fix weak points. Scale what works.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 8: Diagnose & Scale">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Post-launch: what broke?
            <br />
            • Cart abandonment?<br />
            • No-shows?<br />
            • Support overload?
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            We fix it. Then **rinse and repeat** — bigger audience, better offers, higher income.
          </p>
        </figure>
      </div>
    </TestimonialCard>
  </Column>
</section>

<section class="bg-cyan-600 text-white py-10 md:py-20">
  <Column contentClass="flex flex-col items-center gap-6 text-center">
    <h2 class="big-text alt">
      Ready to build your brand? <strong>Let’s build it</strong>
    </h2>
    <a
      href="/contact"
      class="px-6 py-4 text-2xl md:text-3xl border-2 border-cyan-500 hover:bg-cyan-500 rounded transition"
    >
      Start My Brand
    </a>
  </Column>
</section>

<Footer />
