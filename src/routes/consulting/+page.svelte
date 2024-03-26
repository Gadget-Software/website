<script>
  import Column from "../Column.svelte";
  import Footer from "../Footer.svelte";
</script>

<svelte:head>
  <title>Consulting Gadget Software</title>
</svelte:head>

<div class="bg-cyan-900 text-white">
  <Column class="">
    <div class="mt-8 md:mt-20 mb-8 md:mb-20 flex flex-col gap-6 max-w-screen-lg mx-auto">
      <h1 class="big-text">
        Find out why our customers strongly recommend us and <strong>actively want to work
        with us again</strong>
      </h1>

      <h2 class="text-center md:text-left text-2xl md:text-3xl font-bold">Fixed pricing!</h2>
      <p class="text-lg md:text-xl">
        How many times have you shouldered the risk of hourly contractors,
        quoting you one price, and then chronically adding unexpected things to
        the final price, even in some cases not even delivering <i>anything</i>?
        What was the value add to you?  NOTHING.  Just wasted time, money, and
        the feeling of being betrayed.  At Gadget, we charge one fixed, total
        price, and we don't stop until we reach the agreed upon endpoint - which
        is always to get you to the next value capturing milestone of your
        project.
      </p>

      <h2 class="text-center md:text-left text-2xl md:text-3xl font-bold">Regular checkins</h2>
      <p class="text-lg md:text-xl">
        Let's avoid all the nonsense of over-planning - most roadmaps are at
        best a guess, and at worst wrong.  Project specifications change as you
        get feedback from the users of your system (even if YOU are a user).
        Our team keeps in touch with you at regular intervals to make sure we
        are aligned with your needs, even as they are changing.
      </p>

      <h2 class="text-center md:text-left text-2xl md:text-3xl font-bold">Decades of experience</h2>
      <p class="text-lg md:text-xl">
        Experience tested, solid advice and project leadership from a small team
        that has nearly 20 years of combined experience.  We know where projects
        snag, where momentum is lost, and all the potential points of failure
        that can happen. Running into new territory?  Stuck and not sure where
        to go?  Instead of losing life and morale by watching your project go up
        in flames before it's even had a chance, let our experience and guidance
        do the work, and we'll make the process from confusion to victory so
        easy that project success will seem like it "just happened".
      </p>

      <h2 class="text-center md:text-left text-2xl md:text-3xl font-bold">FREE consultation</h2>
      <p class="text-lg md:text-xl">
        Have an idea that seems a bit crazy, but you <b><i>know</i></b> will
        work? Take advantage of our absolutely FREE consultation and
        specification session - where we will either poke all the necessary
        holes in your plan, and leave you feeling clear of mind that the project
        doesn't make sense, OR we will refine your plan to make it robust and
        crystal clear as to how to go from just a rough idea to an executable
        list of items.  Easily $1247 of value, done with you service, no strings
        attached.  It's like your stealing, legally!
      </p>

      <h2 class="text-center md:text-left text-2xl md:text-3xl font-bold">Total control</h2>
      <p class="text-lg md:text-xl">
        Total, full control over all assets and items created by our company We
        don't own any of the intellectual property after we are done - and have
        no interest in it, so you can sell it and make a quick ROI on your
        investment, build it without fear of creating competitors by
        outsourcing, and feel good that you have full flexibility to hire
        in-house or otherwise after your project is complete (you won't want
        to, but we thought we'd mention it).
      </p>
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
    >
    </div>
    <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
    <!-- Calendly inline widget end -->
  </Column>
</section>

<Footer />
