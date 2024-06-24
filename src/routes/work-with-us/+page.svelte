<script>
  import Column from '../Column.svelte';
  import Footer from '../Footer.svelte';
  import ServiceCard from './ServiceCard.svelte';
  import {
    faClock,
    faUsers,
    faHandshake,
  } from '@fortawesome/free-solid-svg-icons';
  export let data;
</script>

<svelte:head>
  <title>Work With Us - Gadget Software</title>
</svelte:head>

<div class="bg-cyan-900 text-white">
  <Column class="">
    <div class="mt-8 md:mt-20 mb-8 md:mb-20 flex flex-col gap-6 max-w-screen-lg mx-auto text-lg">
      {@html data.copyHtml}

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
  <Column contentClass="flex flex-col items-center gap-6">
    <h2 id="book-a-call" class="big-text alt text-center">
      Get in touch <strong>today</strong>
    </h2>
    <a
        class="px-4 py-2 text-2xl md:px-6 md:py-4 md:text-3xl border-2 border-cyan-500 hover:bg-cyan-500 rounded"
        href="https://form.typeform.com/to/RVOS4h03"
    >
      Apply Here to Work With Us!
    </a>
  </Column>
</section>

<Footer />
