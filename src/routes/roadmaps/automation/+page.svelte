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
      Workflow Automation Roadmap
    </h2>

    <TestimonialCard title="Step 1: Understand the Current Workflow">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            The initial step is deeply mapping your existing workflow — through interviews, shadowing, and tracing how information flows between people, departments, and systems.
            <br /><br />
            With software costs dropping, this discovery phase now constitutes 80% of the project’s success. Understanding the lifecycle of data is critical.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Sitting with your team, observe daily operations, and document every handoff, delay, and data entry point will pay dividends downstream.
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
            With full visibility, this gives an opportunity to pinpoint duplicate data entry, manual reporting, and bottlenecks.
            <br /><br />
            Loow-hanging fruit is easily uncovered at this point: automated dashboards, real-time alerts, and admin reporting that were previously impossible.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            This is where ROI becomes crystal clear. A single eliminated spreadsheet can save a scary number of man hours and result in immediate cost savings per year.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 3: Define Requirements & Proposal">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            With this clarity, understanding what is best - an off-the-shelf tool, custom build, or hybrid setup becomes much simpler to understand.
            <br /><br />
            At this point, a proposal with a clear scope, timeline, cost, risk mitigation, and success metrics is many fold more likely to be correct.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            High-risk components and complexity can be flagged early here. Since the majority of the ambiguity is removed, a clear decision on moving forward (or not!) can be met with confidence.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 4: Plan for Organizational Impact">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Automation changes jobs. To turn potential crisis into opportunity, forecasting is extremely important:
            <br />
            • Reduced man-hours<br />
            • Role shifts<br />
            • Training needs
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Building a change management plan your team is excited about, rather than resists, will be pivotal for getting the return on the project.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 5: Build & Deploy Gradually">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Automate piece by piece when possible — reducing risk and enabling early wins.
            <br /><br />
            Sometimes a full build is required — but never without fallback.
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Each module is tested in real use. Feedback loops are built in from day one. Course correction is easier and smoother, if it happens with higher testing and cadence.
          </p>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Step 6: Training & Observation">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            Users are trained hands-on. Watch how they actually use it — not just what they say. There is endless surprise in these steps, and sometimes there are massive opportunities that reveal themselves at this step.
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
            Most value comes after launch. Implementing observed improvements results in greater momentum:
            <br />
            • Faster workflows<br />
            • Better UX<br />
            • Higher adoption
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            It's sometimes possible to see even higher returns on the project than originally expected from post-launch improvements.
          </p>
        </figure>
      </div>
    </TestimonialCard>
  </Column>
</section>

<section class="bg-cyan-600 text-white py-10 md:py-20">
  <Column contentClass="flex flex-col items-center gap-6 text-center">
    <h2 class="big-text alt">
      Understand the process, but still want my direct guidance? <strong>Let’s talk</strong>
    </h2>
    <a
      href="/contact"
      class="px-6 py-4 text-2xl md:text-3xl border-2 border-cyan-500 hover:bg-cyan-500 rounded transition"
    >
      Get in Contact and Let's Get Started
    </a>
  </Column>
</section>

<Footer />
