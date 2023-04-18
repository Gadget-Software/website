<script>
  import Column from "../Column.svelte";
  import ServiceCard from "../ServiceCard.svelte";
  import Logo from "../Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import {faChartLine, faEnvelope, faHandshake, faUser} from "@fortawesome/free-solid-svg-icons";

  const year = new Date().getFullYear();
</script>

<svelte:head>
  <title>Testimonials Gadget Software</title>
</svelte:head>

<div class="bg-cyan-900 text-white">
  <Column class="text-center">
    <div class="mt-8 md:mt-20 mb-8 md:mb-20 flex flex-col gap-3 max-w-screen-sm mx-auto">
      <p>
        What our customers say about Gadget Software
      </p>
      <p class="big-text">
        Our customers strongly recommend us and <strong>actively want to work
        with us again</strong>
      </p>
      <p>
        Book a free consultation with our custom software experts and learn how
        we can optimize your business in ways you didn't think possible
      </p>

      <p class="flex gap-6 justify-center">
        <a href="/#book-a-call" class="btn">
          Book a consultation
        </a>
      </p>
    </div>
  </Column>
</div>

<section class="bg-gray-50 py-10">
  <Column>
    <h2 id="case-studies" class="big-text text-center text-cyan-800">
      Case studies
    </h2>

    <div class="flex flex-col gap-8 mt-10">
      <div class="flex flex-col md:flex-row-reverse gap-8 p-8 bg-white rounded shadow">
        <div class="w-1/2 flex flex-col gap-4">
          <h3 class="font-bold text-cyan-800 text-lg">
            Fruchtbote, fruit shipping business
          </h3>
          <figure class="flex flex-col gap-4">
            <p>
              Fruchtbote is a startup that delivers fresh fruits and vegetables
              to customers in Berlin. They needed a custom software solution to
              automate their business processes and increase their efficiency.
            </p>
            <p>
              Gadget Software helped us to grow our business by 30% in the first
              year of our partnership. We are now able to focus on our core
              business instead of worrying about our software.
            </p>
            <figcaption class="text-right italic pr-16">
              Daniel Gepp<br />
              Fruchtbote
            </figcaption>
          </figure>
        </div>

        <div class="w-1/2">
          <iframe
            class="w-full aspect-video rounded "
            src="https://www.youtube-nocookie.com/embed/cwL3FKupkWs?controls=0"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          >
          </iframe>
        </div>
      </div>
    </div>
  </Column>
</section>

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

<div class="bg-white">
  <Column class="pt-10 pb-10">
    <div class="flex flex-col-reverse justify-between gap-4 items-center md:flex-row md:items-start">
      <div>
        <Logo />
        <p class="mt-4">Not just any software, your software</p>
        <p>&copy; {year} Gadget Software</p>
      </div>
      <a
        href="mailto:sanath@gadget-software.tech"
        class="shadow border-[1px] border-gray-200 hover:border-cyan-500 rounded-lg flex justify-between items-center gap-4 p-4">
        <span class="text-2xl">
          <Fa icon={faEnvelope} />
        </span>
        Send us an email<br/>sanath@gadget-software.tech
      </a>
    </div>
  </Column>
</div>
