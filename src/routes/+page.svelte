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
        I help e-commerce businesses add more value, and make more money through the <strong class="text-yellow-200">power of email automations and scripts.</strong> (Oh, and through incredible coaching, unique software, and battle tested marketing
        solutions) :)
      </p>
      <p class="flex gap-6 justify-center">
        <a href="#about" class="btn">
          Learn More
        </a>
      </p>
      <p class="flex gap-6 justify-center">
        on how we can improve your business
        in ways you didn't think possible
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

<section id="about" class="bg-cyan-600 text-white py-10 md:py-20">
  <Column contentClass="max-w-md md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl flex flex-col gap-4 text-lg px-4">
    <p class="big-text">
      After a decade of building dozens of custom software projects, I got fed up with how many 
      <span class="text-green-300 font-semibold">successful builds </span> I did that were 
      <span class="text-rose-400 font-semibold">monetary failures.</span>
    </p>
    <p>
      Driven by the pain of clients spending 5, and sometimes 6 figures USD on projects, and not getting the ROI I wanted for them, I started noticing gaps around marketing knowledge, awareness of their business-related strengths and weaknesses, and lack of depth in their customer relationships.
    </p>
    <p>
      And with the advent of AI, new platforms and SaaS businesses now having the ability to be created at the snap of a finger - software, by itself is no longer a competitive advantage, at a all.
    </p>
    <p>
      It's enough to feel backed into corner. So what did I do?
    </p>
    <p>
      I saw the iceberg coming, and instead of panicking, I spent a few <bold>years</bold> educating myself, and experimenting, hours a day, tens of thousands of dollars invested, in understanding direct to consumer marketing and psychology. 
    </p>
    <p>
       And, amazingly I found that all this u-turn in my education did, was make me an unstoppable force in your business. From being able to identify low hanging fruit to make your marketing more successful, to automating away menial error prone tasks - I can walk into any marketing department, observe what they are doing, and make them either more efficient, increase topline revenue, and most likely, do both.
    </p>
    <p>
       Developing awareness of your situation is core to the process, so I keep a trusting, open space where information is held private, allowing us to have a frank dialogue, and discover where positive change and movement can actually occur. The financial results are one of many benefits to be derived.
    </p>
    <p>
       I only work with a handful of people at a time. So if you are interested, reach out to check my availability.
    </p>
    <div class="flex gap-2 justify-between">
      <div class="flex flex-row justify-start items-center gap-5">
        <div>
          <img
            class="rounded-full w-20 border-2 border-white"
            alt="Picture of Sanath Sambamoorthi"
            src="/sanath-pic-min.jpg" />
        </div>
        <div>
          <p><strong>Sanath Sambamoorthi</strong></p>
          <p class="text-sm">Marketer, Software Engineer, Coach</p>
        </div>
      </div>
    </div>
  </Column>

<Footer />
