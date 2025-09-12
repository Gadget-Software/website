<script lang="ts">
  import Footer from './Footer.svelte';
  import Column from "./Column.svelte";
</script>

<svelte:head>
  <title>Gadget Software</title>
</svelte:head>

<div class="bg-cyan-900 text-white">
  <Column class="text-center">
    <div class="mt-8 md:mt-20 mb-8 md:mb-20 flex flex-col gap-3 max-w-screen-sm mx-auto">
      <p>
        Welcome to Gadget Software
      </p>
      <p class="big-text">
        We fulfill your business needs with <strong>completely unique software
        solutions</strong>
      </p>
      <p>
        Book a free consultation with our custom software experts and learn how
        we can optimize your business in ways you didn't think possible
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
      src="https://www.youtube-nocookie.com/embed/0AnExD_mi7M?controls=0"
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
      Domain experts coming together to deliver unique solutions.
    </p>
    <p>
      My team, and I are absolutely excellent at not only delivering production ready software,
      but also ensuring that as a business owner, you get a real return on your invested resources.
    </p>
    <p>
      With experiences working in, for and with tiny 5 person companies, and
      30,000 monolith companies - industries spanning paint e-commerce to
      entrepreneur training platforms, projects in Europe, America, Japan and
      more - we have the decades of experience required to say we are absolute
      experts in the field of custom software.
    </p>
    <div class="flex gap-2 justify-between">
      <div class="flex flex-row justify-start items-center gap-5">
        <div>
          <img
            class="rounded-full w-20 border-2 border-white"
            alt="Picture of Sanath Sambamoorthi, Co-founder and Project Manager at Gadget Software"
            src="/sanath-pic-min.jpg" />
        </div>
        <div>
          <p><strong>Sanath Sambamoorthi</strong></p>
          <p class="text-sm">Manager</p>
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
