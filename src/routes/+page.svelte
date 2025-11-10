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
        I fulfill your business needs with a mix of <strong class="text-yellow-200"> incredible coaching, unique software, </strong> and <strong class="text-yellow-200"> battle tested marketing
        solutions</strong>
      </p>
      <p>
        Contact me and learn how we can optimize your business
        in ways you didn't think possible
      </p>

      <p class="flex gap-6 justify-center">
        <a href="#about-us" class="btn">
          Learn More
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
  <Column contentClass="max-w-md md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl flex flex-col gap-4 text-lg px-4">
    <h2 id="about-us">About Us</h2>
    <p class="big-text">
      After a decade of building dozens of custom software projects, I got fed up with how many 
      <span class="text-green-300 font-semibold">successful builds </span> I did that were 
      <span class="text-rose-400 font-semibold">monetary failures</span>.
    </p>
    <p>
      Driven by the pain of clients spending 5, and sometimes 6 figures USD on projects, and not getting the ROI I wanted for them, I recognized a significant gap in their project cycle, revolving around marketing, awareness, and their customer relationships.
    </p>
    <p>
      Even though I am still astounded by software's ability to automate and power to scale, the recognition that this is not enough to create great businesses has pushed me into focusing on marketing education. Even with technology, unless you are someone who is on the absolute bleeding edge of the market, the primary issues you are solving are still human, and not technical in nature.
    </p>
    <p>
      So, I spent years educating myself, and experimenting, hours a day, thousands of dollars invested, in understanding direct to consumer marketing so that a client would never have to go through an experience of investing money into a project, or their business, for no return, again.
    </p>
    <p>
       And, amazingly, with a deep understanding of the material, I have had the priviledge and luck to work with amazing clients spanning extremely varied industries.
    </p>
    <p>
      Through this, I've developed a very unique methodology - my assistance in your marketing and promotion is extremely custom - I take time to deeply understand you, your business, your strengths and weaknesses, and through that process work collaboratively on things step, by step.
    </p>
    <p>
       Developing self-awareness, and awareness of your situation is core to the process, so I keep a trusting, open space where information is held private, allowing you to speak frankly, be vulnerable with yourself, and discover where positive change and movement can actually occur. The financial results are one of many benefits to be derived.
    </p>
    <p>
       I only work with a handful of people at a time. So if you are interested, reach out to check my availability.
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
          <p class="text-sm">Manager, Marketer, Engineer, Coach</p>
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
