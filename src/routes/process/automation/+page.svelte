<script>
  import Column from "../../Column.svelte";
  import Footer from "../../Footer.svelte";
  import TestimonialCard from "../../testimonials/TestimonialCard.svelte";
</script>

<svelte:head>
  <title>Workflow Automation Process – Gadget Software</title>
</svelte:head>

<section class="bg-gray-50 py-10">
  <Column>
    <h2 class="big-text text-center text-cyan-800">
      Workflow Automation Process
    </h2>

    <TestimonialCard title="Step 1: Understand the Current Workflow">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            We begin by deeply mapping your existing workflow — through interviews, shadowing, and tracing how information flows between people, departments, and systems.
            <br /><br />
            With software costs dropping, this discovery phase now constitutes 80% of the project’s success. Understanding the lifecycle of data is critical.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            We sit with your team, observe daily operations, and document every handoff, delay, and data entry point.
            <br /><br />
            This isn’t just about “what” — it’s about why, who, and how often.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 2: Identify Redundancies & Opportunities">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            With full visibility, we pinpoint duplicate data entry, manual reporting, and bottlenecks.
            <br /><br />
            We also uncover low-hanging fruit: automated dashboards, real-time alerts, and admin reporting that were previously impossible.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            This is where ROI becomes crystal clear. A single eliminated spreadsheet can save thousands of hours per year.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 3: Define Requirements & Proposal">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Now we know: off-the-shelf tool, custom build, or hybrid?
            <br /><br />
            We draft a bulletproof proposal with clear scope, timeline, risk mitigation, and success metrics.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            High-risk components are flagged early. You sign off knowing exactly what you’re getting.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 4: Plan for Organizational Impact">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Automation changes jobs. We forecast:
            <br />
            • Reduced man-hours<br />
            • Role shifts<br />
            • Training needs
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            We build a change management plan so your team adopts, not resists.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 5: Build & Deploy Gradually">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            We automate piece by piece when possible — reducing risk and enabling early wins.
            <br /><br />
            Sometimes a full build is required — but never without fallback.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Each module is tested in real use. Feedback loops are built in from day one.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 6: Training & Observation">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Users are trained hands-on. We watch how they actually use it — not just what they say.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Notes become the roadmap for v2 improvements.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 7: Iterate & Optimize (Recommended)">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Most value comes after launch. We implement observed improvements:
            <br />
            • Faster workflows<br />
            • Better UX<br />
            • Higher adoption
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Clients often see 2–3x the original ROI after this phase.
          </p>
        </figure>
      </div>
    </TestimonialCard>
  </Column>
</section>

<section class="bg-cyan-600 text-white py-10 md:py-20">
  <Column contentClass="flex flex-col items-center gap-6 text-center">
    <h2 class="big-text alt">
      Ready to automate? <strong>Let’s talk</strong>
    </h2>
    <a
      href="/contact"
      class="px-6 py-4 text-2xl md:text-3xl border-2 border-cyan-500 hover:bg-cyan-500 rounded transition"
    >
      Start Your Automation
    </a>
  </Column>
</section>

<Footer />
