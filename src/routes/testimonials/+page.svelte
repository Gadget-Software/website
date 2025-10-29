<script>
  import Column from "../Column.svelte";
  import Footer from "../Footer.svelte";
  import VideoTestimonialCard from "./VideoTestimonialCard.svelte";
  import TestimonialCard from "./TestimonialCard.svelte";
  import GifTestimonialCard from "./GifTestimonialCard.svelte";
  import Mp4TestimonialCard from "./Mp4TestimonialCard.svelte";
</script>

<svelte:head>
  <title>Testimonials Gadget Software</title>
</svelte:head>

<section class="bg-cyan-900 text-white">
  <div class="max-w-screen-lg mx-auto px-4">
    <div class="text-center py-14 md:py-24 flex flex-col gap-4 md:gap-6">
      <h1 class="text-3xl md:text-5xl font-semibold leading-tight">
        <span class="text-cyan-300">We are passionate about the value created through software and automation. Not just in building it.</span>
      </h1>
      <p class="text-lg md:text-2xl text-cyan-100">
        Just see what our clients have had to say about us.
      </p>
    </div>
  </div>
</section>

<section class="bg-gray-50 py-10">
  <Column>
    <h2 id="case-studies" class="big-text text-center text-cyan-800">
      Case studies
    </h2>

    <TestimonialCard title="AI-powered Shopping Assistant Startup">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2">
          <img src="/aisle-min.png" alt="Chat box with user prompting 'I want a new Macbook' and chatbot responding with shopping guidance and clarifying questions in the style of the tech YouTuber it's representing" />
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            The team at Gadget Software over-delivers. At Aisle, we set out to build the first e-comm platform native to
            the creator economy– specifically rooted in conversational commerce capabilities enabled by LLMs. After
            developing the idea/plan, I was referred to Gadget by a network connection and happy customer. Sanath and
            Eduardo’s experience, intelligence, and professionalism were immediately apparent. They had relevant projects
            to extrapolate insights from, they were able to efficiently translate high-level thoughts into a technical
            roadmap, and most of all they championed flexibility and generosity. Unlike many other dev shops, this team
            prioritizes value for their partners and not for themselves. It was common for them to offer extra time to
            walk through something I didn’t fully understand (extremely helpful when you’re early-phase and playing
            telephone with customers, developers, and investors), and they were always honest about what they thought
            would move the needle even if it meant less hours/work for them. I would easily recommend the level of
            partnership that Gadget follows through with.
          </p>

          <figcaption class="text-right italic pr-16">
            Jacob Laufer,<br />
            Aisle
          </figcaption>
        </figure>
      </div>
    </TestimonialCard>

    <TestimonialCard title="Automatic mass translation checker">
      <div class="flex flex-col md:flex-row justify-between items-start gap-8">
        <div class="w-full md:w-1/2 grid grid-cols-2 md:grid-cols-2 gap-2">
          <img class="border rounded shadow-sm cursor-pointer" data-action="zoom" src="/mugen/Upload.png" />
          <img class="border rounded shadow-sm cursor-pointer" data-action="zoom" src="/mugen/Prompts.png" />
          <img class="border rounded shadow-sm cursor-pointer" data-action="zoom" src="/mugen/Status.png" />
          <img class="border rounded shadow-sm cursor-pointer" data-action="zoom" src="/mugen/Glossary.png" />
          <img class="border rounded shadow-sm cursor-pointer" data-action="zoom" src="/mugen/Analysis.png" />
        </div>
        <figure class="w-full md:w-1/2 flex flex-col gap-4">
          <p>
            Gadget Software made it extremely easy to get started and finish
            the project with minimal time invested from my part. Just a few
            meetings to handle handoff, some back and forth messaging on when
            features were released, and a bit of feedback, and now I have a
            fully working, cutting edge LLM leveraging translation application
            that has turned a 105 hour man hour job into just two easy hours.
            The ROI is absolutely insane. Can't recommend working with them
            enough.
          </p>

          <figcaption class="text-right italic pr-16">
            Taylor Matthews,<br />
            CEO, Mugen Creations
          </figcaption>
        </figure>
      </div>
    </TestimonialCard>

    <Mp4TestimonialCard
      title="AI Vehicle Coach (Web3/API Integrated)"
      mp4Src="vehiclegenius.mp4"
      gifSrc="vehiclegenius.gif"
      gifAlt="A walkthrough of the Vehicle Genius application integrated with DIMO."
      reverse={true}
    >
      <figure class="flex flex-col gap-4">
        <p>
          Gadget Software came on high recommendation through a relationship
          with one of the DIMO founders. Their expertise in how to leverage
          current AI products for what we wanted to build, and how thoughtful
          and involved they wanted to be in the project and bigger picture of
          Vehicle Genius at the beginning of the relationship made them a an
          easy decision to work with.
        </p>

        <p>
          We needed to integrate existing API data for specific vehicles, to
          make a chat assistant to answer questions related to a user's
          vehicle. We ended up using it as a tool to speed up customer support
          - and found that we had a 15% gain in productivity on that side of
          the business.
        </p>

        <p>
          Additionally, they integrated a Web3 Oauth process involving Metamask
          and transfer of vehicle data through the blockchain. Even in a
          situation where they were provided little guidance or documentation -
          they figured out how to complete the project requirements
          satisfactorily.
        </p>

        <figcaption class="text-right italic pr-16">
          Colin Knudsen,<br />
          Vehicle Genius
        </figcaption>
      </figure>
    </Mp4TestimonialCard>

    <GifTestimonialCard
      title="Character NFT AI Chatbot"
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
          Mitama Mint Team
        </figcaption>
      </figure>
    </GifTestimonialCard>

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

    <VideoTestimonialCard
      title="Order fulfillment automation for an e-commerce business"
      videoId="xkzmm07zSuo"
    >
      <figure class="flex flex-col gap-4">
        <p>
          Our company Fruchtbote is a German e-commerce business. We specialize
          in the delivery of fresh raw fruits in Europe especially for the German
          market.
        </p>
        <p>
          We worked together with Gadget Software to automate our fulfillment
          process and improve the efficiency in our day to day business. Before
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
