<script lang="ts">
  import Column from "./Column.svelte";
  import ServiceCard from "./ServiceCard.svelte";
  import Logo from "./Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import {faChartLine, faEnvelope, faHandshake, faUser} from "@fortawesome/free-solid-svg-icons";
  import sanath from '../../static/sanath-pic-min.jpg';

  const year = new Date().getFullYear();
</script>

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
        <button class="btn alt">
          Services
        </button>
        <button class="btn">
          Book a consultation
        </button>
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

    <section class="flex flex-col gap-4 mt-12 items-center">
      <h2 id="our-services">Our Services</h2>
      <div
        class="flex flex-col md:flex-row md:justify-between items-center md:items-end gap-4 md:gap-16 text-center md:text-left max-w-sm md:max-w-full">
        <p class="big-text md:w-2/3">Custom software to expand your business</p>
        <button class="btn min-w-fit">Book a consultation</button>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-sm md:max-w-full">
        <ServiceCard
          icon={faUser}
          title="Custom solutions"
          text="Off-the-shelf solutions often do not consider the specific nuances of your own business in the slightest, our solutions are completely unique to your context"/>
        <ServiceCard
          icon={faChartLine}
          title="Optimize your resources"
          text="Free up your employees', or your own time, by developing custom solutions to automate work"/>
        <ServiceCard
          icon={faHandshake}
          title="A to Z service"
          text="We'll guide you through the process from A to Z, you can trust in our years of expertise in providing custom business solutions"/>
      </div>
    </section>
  </Column>
</div>

<section class="bg-cyan-600 text-white py-10 md:py-20">
  <Column>
    <div class="max-w-screen-sm flex flex-col gap-4">
      <h2 id="about-us">About Us</h2>
      <p class="big-text">
        Domain experts coming together to deliver unique solutions.
      </p>
      <p>
        Our team is composed of a close group of friends passionate for
        software solution.
      </p>
      <p>
        Our combined knowledge of software through each of our own journeys
        in the industry allow us to identify problems in your business and
        develop unique solutions for them.
      </p>
      <div class="flex flex-row justify-start items-center gap-5">
        <div>
          <img
            class="rounded-full w-20 border-2 border-white"
            alt="Nice picture of Sanath Sambamoorthi"
            src="/sanath-pic-min.jpg" />
        </div>
        <div>
          <p>Sanath Sambamoorthi</p>
          <p>Project Manager at Gadget Software</p>
        </div>
      </div>
    </div>
  </Column>

  <Column contentClass="flex flex-col gap-8 mt-20">
    <p class="big-text alt text-center">
      Get in touch <strong>today</strong>
    </p>
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
        <Logo/>
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
