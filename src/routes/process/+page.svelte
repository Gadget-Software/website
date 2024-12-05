<script>
  import Column from "../Column.svelte";
  import Footer from "../Footer.svelte";
  import TestimonialCard from "./../testimonials/TestimonialCard.svelte";
</script>

<svelte:head>
  <title>Our Process Gadget Software</title>
</svelte:head>

<section class="bg-gray-50 py-10">
  <Column>
    <h2 id="case-studies" class="big-text text-center text-cyan-800">
      Case studies
    </h2>

    <TestimonialCard title="Step 1: Niching">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <p>
            In general, as an entrepreneur with limited financial and network resources, we might not be able to dominate the global market immediately. 

            But we can dominate a small, local market.

            As Sam Walton famously mentioned in his book on the legendary Walmart, Walmart was never able to compete with local businesses who knew their customers on a deeper level than Walmart was capable of allocating resources to. 

            This is what makes the process of niching a necessary tool. The tighter we can narrow our customer profile, the easier we can identify common threads between customers, and the faster we can communicate with them in a compelling way, and the easier it is to deliver a solution that actually adds value to their lives in someway.

            Secretly, there are other benefits as well, since a tight niche allows higher performing marketing, non-competitive pricing (meaning you can charge much higher prices), and easier targeting and access. 
          </p>
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            We work with the entrepreneur specifically to determine a niche that will easily accessible to them. Everyone who has worked for more than a few years has access to an existing set of potential customers they know really well. We hone in on where they the entrepreneur has a natural competitive advantage and determine the specifics of what this niche actually looks like using the existing information that's in their head.
          </p>
        </figure>
      </div>
    </TestimonialCard>
  </Column>
</section>

<section class="bg-cyan-600 text-white py-10 md:py-20">
  <Column contentClass="flex flex-col items-center gap-6">
    <h2 id="book-a-call" class="big-text alt text-center">
      Get in touch <strong>today</strong>
    </h2>
    <a class="px-4 py-2 text-2xl md:px-6 md:py-4 md:text-3xl border-2 border-cyan-500 hover:bg-cyan-500 rounded"
       href="https://www.skool.com/custom-software-build-fix/about">
      Work with us
    </a>
  </Column>
</section>

<Footer />
