<script lang="ts">
  import Footer from './Footer.svelte';
  import Column from "./Column.svelte";
</script>

<svelte:head>
  <title>Sanath Sambamoorthi</title>
</svelte:head>

<div class="bg-cyan-900 text-white">
  <Column class="text-center">
    <div class="mt-8 md:mt-20 mb-8 md:mb-20 flex flex-col gap-3 max-w-screen-sm mx-auto">
      <p>
        Yo! Sanath here.
      </p>
      <p class="big-text">
        I fulfill your business needs with a mix of <strong> incredible coaching, unique software, and battle tested marketing
        solutions</strong>
      </p>
      <p>
        Contact me and learn how we can optimize your business
        in ways you didn't think possible
      </p>

      <p class="flex gap-6 justify-center">
        <a href="/contact" class="btn">
          Contact Us
        </a>
      </p>
    </div>
    <div class="h-56"></div>
  </Column>
</div>

<div class="bg-gray-50 pb-10 md:pb-20">
  <Column class="flex flex-col gap-8">
    <iframe
      class="w-full aspect-video -mt-56 z-10 rounded-2xl"
      src="https://www.youtube-nocookie.com/embed/8gc1bqrfnH4?si=r506ffVPCOULe2Xy"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    >
    </iframe>
  </Column>
</div>

<section class="bg-cyan-600 text-white py-10 md:py-20">
  <Column contentClass="max-w-screen-sm flex flex-col gap-4 text-lg">
    <h2 id="about-us">About Us</h2>
    <p class="big-text">
      After building dozens and dozens of custom software projects for more than a decade, I got fed up with how many successful builds I did that were monetary failures.
    </p>
    <p>
      Driven by the pain of clients spending 5, and sometimes 6 figures USD on projects, and not getting the ROI they thought, I recognized a significant gap in their project cycle, in marketing, awareness, and their customer relationships.
    </p>
    <p>
      Even though software is still absolutely incredible in terms of it's ability to automate, and understand it's power to scale, I primarily now focus on marketing education, because even with technology, unless you are someone who is on the absolute bleeding edge of the market, the primary issues you are solving are still human, and not technical in nature.
    </p>
    <p>
      So, I spent years educating myself, hours a day, on direct to consumer marketing so that a client would never have to go through that experience again.
    </p>
    <p>
      My methodology is unique - my assistance in your marketing and promotion is custom tailored - I take time to deeply understand you, your business, your strengths and weaknesses, and through that process work collaboratively on next steps, and getting you to actually do those steps.
    </p>
    <p>
      With a deep understanding of the material, I have had the priviledge and luck to work with amazing clients spanning extremely varied industries. In order to facilitate change, developing self-awareness, and awareness of your situation is paramount, so I keep a trusting, open space where information is held private, allowing you to speak frankly, be vulnerable with yourself, and discover where positive change and movement can actually occur. This will ultimately get the financial results that you are looking for.
    </p>
    <div class="flex gap-2 justify-between">
      <div class="flex flex-row justify-start items-center gap-5">
        <div>
          <img
            class="rounded-full w-20 border-2 border-white"
            alt="Picture of Sanath Sambamoorthi, Founder at Gadget Software"
            src="/sanath-pic-min.jpg" />
        </div>
        <div>
          <p><strong>Sanath Sambamoorthi</strong></p>
          <p class="text-sm">Manager, Engineer, Coach</p>
        </div>
      </div>
    </div>
  </Column>

  <section class="bg-cyan-600 text-white py-10 md:py-20">
    <Column contentClass="flex flex-col items-center gap-6">
      <h2 id="book-a-call" class="big-text alt text-center">
        Get in touch <strong>today</strong>
      </h2>
      <a class="px-4 py-2 text-2xl md:px-6 md:py-4 md:text-3xl border-2 border-cyan-500 hover:bg-cyan-500 rounded" href="/contact">
        Work with us
      </a>
    </Column>
  </section>
</section>

<Footer />
