<script>
  import Column from '../Column.svelte';
  import Footer from '../Footer.svelte';
  import ServiceCard from './ServiceCard.svelte';
  import {
    faClock,
    faUsers,
    faHandshake,
  } from '@fortawesome/free-solid-svg-icons';
</script>

<svelte:head>
  <title>Consulting Gadget Software</title>
</svelte:head>

<div class="bg-cyan-900 text-white">
  <Column class="">
    <div class="mt-8 md:mt-20 mb-8 md:mb-20 flex flex-col gap-6 max-w-screen-lg mx-auto text-lg">
      <p>So, will your business eat, or be eaten by AI?</p>

      <p>
        With AI having taken off like a rocket ship, it's no surprise that all
        of us are worried about whether this thing is gonna take our damn jobs
        or not.
      </p>
      <p>
        The bad news, is that, well yes, it is going to change things. The good
        news is, it's likely going to be so in a very, very good way.
      </p>
      <p>
        You see, having worked in the custom software and automation space for a
        decade, through catastrophic failures, and through incredible successes,
        placing entrepreneurs in a place to raise capital, help teachers get
        greater engagement from their students, and getting accounting staff off
        of data entry tasks - I've noticed ONE consistent thing amongst them
        all.
      </p>
      <p>
        Effectively used, automations releases people to work more creatively.
        To find larger patterns, to identify greater bottlenecks, and ultimately
        to be of even GREATER value to their organizations.
      </p>
      <p>
        Yeah, there's always a little friction, as those people are given free
        time, and are not quite sure what to do with it.
      </p>
      <p>
        But inevitably, every time, work is found - and it's not an accident.
        People who get to choose the work they tackle - are going to frickin'
        love it! It's basic psychology - the kind that Ikea uses to make you
        love their furniture (I built it - so I love it).
      </p>
      <p>
        So it's extremely lucky that we have not only the experience of dozens of
        projects, organizations spanning every application from shrimp
        processing to home insurance, and user counts spanning from just 1 to
        1,000,000s, but also extensive experience building LLM applications
        since day 1 of OpenAI's ChatGPT releasing their APIs for developers to
        work with.
      </p>
      <p>
        And even since then, while the rules of successful custom software
        projects still apply - there's TONS of nuance that goes into both using
        Generative AI, and also creating applications with it.
      </p>
      <p>
        So let us, as an expert, handle these types of applications for you.
      </p>
      <p>
        It is only logical, and intelligent, to avoid the burning wreckage of
        $10,000s wasted, headaches of not understanding what to do, how to do
        it, where to go, and all that time, never to be found again, by working
        with someone like us to get what you need. The result.
      </p>
      <p>
        A functional, safe, software application, that does what it needs to in
        order to accrue value for you, your stakeholders, and most importantly,
        your users.
      </p>
      <p>
        And a process where we can take you by the hand, and make it super silky
        smooth to get to the end result. No banging your head against the wall.
        No sleepless nights wondering what's going to happen. No irritating
        mornings feeling like you need to take control. Just a peaceful flow.
      </p>
      <p>Here's the kinds of thing that you can expect from working with us:</p>
      <div class="mt-4 md:mt-8" />

      <h2 class="text-left text-2xl md:text-3xl font-bold">Fixed pricing!</h2>
      <p>
        How many times have you shouldered the risk of hourly contractors,
        quoting you one price, and then chronically adding unexpected things to
        the final price, even in some cases not even delivering <i>anything</i>?
        What was the value add to you? NOTHING. Just wasted time, money, and the
        feeling of being betrayed. At Gadget, we charge one fixed, total price,
        and we don't stop until we reach the agreed upon endpoint - which is
        always to get you to the next value capturing milestone of your project.
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">Regular checkins</h2>
      <p>
        Let's avoid all the nonsense of over-planning - most roadmaps are at
        best a guess, and at worst wrong. Project specifications change as you
        get feedback from the users of your system (even if YOU are a user). Our
        team keeps in touch with you at regular intervals to make sure we are
        aligned with your needs, even as they are changing.
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">
        Decades of experience
      </h2>
      <p>
        Experience tested, solid advice and project leadership from a small team
        that has nearly 20 years of combined experience. We know where projects
        snag, where momentum is lost, and all the potential points of failure
        that can happen. Running into new territory? Stuck and not sure where to
        go? Instead of losing life and morale by watching your project go up in
        flames before it's even had a chance, let our experience and guidance do
        the work, and we'll make the process from confusion to victory so easy
        that project success will seem like it "just happened".
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">
        FREE consultation
      </h2>
      <p>
        Have an idea that seems a bit crazy, but you <b><i>know</i></b> will work?
        Take advantage of our absolutely FREE consultation and specification session
        - where we will either poke all the necessary holes in your plan, and leave
        you feeling clear of mind that the project doesn't make sense, OR we will
        refine your plan to make it robust and crystal clear as to how to go from
        just a rough idea to an executable list of items. Easily $1247 of value,
        done with you service, no strings attached. It's like you're' stealing,
        legally!
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">Total control</h2>
      <p>
        Total, full control over all assets and items created by our company. We
        don't own any of the intellectual property after we are done - and have
        no interest in it, so you can sell it and make a quick ROI on your
        investment, build it without fear of creating competitors by
        outsourcing, and feel good that you have full flexibility to hire
        in-house or otherwise after your project is complete (you won't want to,
        but we thought we'd mention it).
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">
        LLM (Chatbot) AI experts
      </h2>
      <p>
        Experience with cutting edge LLM (Chatbot) AI technology and more. We've
        been working with LLMs since public developer API access has been
        available for OpenAIs ChatGPT. Take advantage of this before the cats
        out of the bag and everyone and their mother realize the revenue
        exploding capabilities of the technology!
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">
        ZERO privacy or legal concerns with the AIs that we work with
      </h2>
      <p>
        We can use micro-LLMs thar are self-hosted, so you are full control of the
        data of your customers. As a result the model will not produce content
        that counts as plagiarism, and you can rest in peace knowing that you
        will not have privacy leaks, or heart attack inducing legal notices
        like copyright infringment lawsuits randomly showing up at your door.
      </p>
      <p>
        Without any reduction in quality of the output from the LLM thanks to
        advanced RAG integration which has been proven to be the key factor in
        LLM performance, NOT model size.
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">Limited capacity</h2>
      <p>
        We aspire to excellence and meeting your needs.
      </p>
      <p>
        As a result, we only take on 3 clients at a time. If you want to be part
        of that exclusive triad, reach out ASAP, as recently we've been capped
        more often.
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">
        RUTHLESS HEATSEEKING MISSILE VALUE DRIVEN APPROACH
      </h2>

      <p>
        Most custom software companies bloat your projects with unnecessary
        time-consuming processes, or nonsense features ("architecture" anyone?)
        to fill billable hours and keep their personal quotas full.
      </p>
      <p>
        We get bored easily - so in order to have fun, get value to you fast,
        we've stripped down everything to the bare essentials. The benefit? Your
        time and money get stretched out to their limits, simply by us having
        learned to say NO to anything that doesn't get you to your first
        customers quickly.
      </p>
      <p>
        For certain customers this can be annoying, but for the ones that really
        want to have their project succeed, this is a crucial piece that
        distinguishes Gadget from the average, soulless, software factory - and
        not only makes things more fun for Gadget, but it also takes a process
        has a lot of stressful, potential gut-wrenching uncertainty into a more
        easeful, zippy, interesting, fun, and simple way of working that nets
        RESULTS for you, the customer.
      </p>

      <h2 class="text-left text-2xl md:text-3xl font-bold">
        "OFF TO THE RACES" SYSTEM TO MAKE YOUR PROJECT REAL AND SUCCESSFUL
      </h2>

      <p>
        Every project fails because of lack of continuous directional momentum.
        There are two things that fuel that in a software project - users, or
        money. We won't even start building for you until we have either an
        investor demo milestone, which is one source of initial money, or for
        user acquisition and acquiring feedback in place, which is really just
        another proxy for cash coming in.
      </p>
      <p>
        Why? Because otherwise the business envisioned is a complete fantasy.
        If those things aren't in place at the very beginning of the project,
        it doesn't matter how awesome a product we make, there will be no ROI.
        We love to build things because it's fun, impactful, and potentially
        life changing, but if the math doesn't make sense, there's sadly not
        much that can happen from there.
      </p>
      <p>
        If this is enough to scare you off, good. We've seen enough failures to
        know what's pivotal for software projects to be successful, and if
        someone isn't willing to do either one of those two basic things, well,
        to say we have no faith in that project would be a nice way of putting
        it.
      </p>

      <section class="flex flex-col gap-8 mt-12">
        <p class="text-2xl max-w-[90%]">
          With almost two decades of experience, dozens of software projects,
          failures, successes, and everything in-between - including experience
          at working in Software at companies of several sizes (from just 5
          people, to 1000, to 30,000), and multiple successful LLM/AI projects
          under our belt at Gadget (just check out
          <a class="text-cyan-500 underline" href="/testimonials">our testimonials page</a>),
          let us take you by the hand and help you run, not walk past the
          burning wreckage of failures of peers that didn't get expert help, and
          that are carefully hidden from public eye.
        </p>
        <div
          class="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-sm md:max-w-full"
        >
          <ServiceCard
            icon={faClock}
            title="Hourly Consulting"
            text="Let us give you all the expertise you need to skill up and make the attempts at integrating LLMs in house"
          />
          <ServiceCard
            icon={faUsers}
            title="Fixed - Done With You"
            text="We'll embed a programmer on your team at FIXED COST and handle LLM integrations alongside YOUR process. We don't stop working until the agreement is complete"
          />
          <ServiceCard
            icon={faHandshake}
            title="Fixed - Done For You"
            text="Let us handle your project from start to finish. You pay a fixed price, and we take you from 0 - 1 and get you capturing value from what we've done"
          />
        </div>
      </section>
    </div>
  </Column>
</div>

<section class="bg-cyan-600 text-white py-10 md:py-20">
  <Column contentClass="flex flex-col gap-8">
    <h2 id="book-a-call" class="big-text alt text-center">
      Get in touch <strong>today</strong>
    </h2>
    <!-- Calendly inline widget begin -->
    <div
      class="calendly-inline-widget h-[700px] min-w-[320px] relative rounded-2xl"
      data-url="https://calendly.com/sanaths/gadget-software-custom-software-discussion?hide_gdpr_banner=1&hide_landing_page_details=1"
    />
    <script
      type="text/javascript"
      src="https://assets.calendly.com/assets/external/widget.js"
      async
    ></script>
    <!-- Calendly inline widget end -->
  </Column>
</section>

<Footer />
