<script>
  import Column from "../Column.svelte";
  import Logo from "../Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
  import VideoTestimonialCard from "./VideoTestimonialCard.svelte";
  import TestimonialCard from "./TestimonialCard.svelte";
  import GifTestimonialCard from "./GifTestimonialCard.svelte";

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

    <VideoTestimonialCard
      title="Order fulfillment automation for an e-commerce business"
      videoId="xkzmm07zSuo"
    >
      <figure class="flex flex-col gap-4">
        <p>
          Our company Fruchtbote is a German e-commerce business.  We specialize
          in the delivery of fresh raw fruits in Europe especially for the German
          market.
        </p>
        <p>
          We worked together with Gadget Software to automate our fulfillment
          process and improve the efficiency in our day to day business.  Before
          that we used pen and paper for employees during the fulfillment
          process, which led to errors and huge time expenditure.
        </p>
        <p>
          Since working with Gadget Software we could save 4x the time and
          valuable resources.
        </p>
        <figcaption class="text-right italic pr-16">
          Daniel Gepp<br />
          Fruchtbote
        </figcaption>
      </figure>
    </VideoTestimonialCard>

    <TestimonialCard title="Mass message sending scripts for a promoter group in Tokyo">
      <figure class="flex flex-col gap-4">
        <p>
          I decided to automate part of my workflow because I often didn't have enough time to complete it manually.
          Even when I had the time, it was tedious work that I dreaded.
        </p>
        <p>
          I chose Gadget Software because of their fast response time for the initial quote, for starting the work and
          for delivering the first release of the software.
        </p>
        <p>
          Compared to other offerings, I liked the fact that they agreed to sell the software as a product, including
          the source code, as opposed to SaaS with closed-off source code.
        </p>
        <p>
          The software freed up some of my time, enabling me to relax or focus on aspects that currently can't be
          automated.
        </p>
        <p>
          Even though the initial objective was achieved, I keep working with Gadget Software for adding new features
          and functions to the software.
        </p>
        <figcaption class="text-right italic pr-16">
          Promoter group in Tokyo
        </figcaption>
      </figure>
    </TestimonialCard>

    <GifTestimonialCard
      title="Custom topic-aware chatbot"
      gifSrc="mitama.gif"
      gifAlt="Chatbot in action being asked a couple questions in different contexts"
    >
      <figure class="flex flex-col gap-4">
        <p>
          We were in search of a chatbot for our NFT project that would
          communicate with our users when messaged on Discord. We had content,
          but not enough to "train" an AI model on, which we thought was a major
          challenge. Gadget Software offered a custom, bleeding edge solution
          that mixed a small dataset of related content with the quality of
          answers from ChatGPT to give us an AI Chatbot personality that sounded
          exactly like we wanted.
        </p>
        <figcaption class="text-right italic pr-16">
          CEO,<br />
          Mitama
        </figcaption>
      </figure>
    </GifTestimonialCard>
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
        Send us an email<br />sanath@gadget-software.tech
      </a>
    </div>
  </Column>
</div>
