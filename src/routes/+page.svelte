<script lang="ts">
  import Column from "./Column.svelte";
  import ServiceCard from "./ServiceCard.svelte";
  import Logo from "./Logo.svelte";
</script>

<div class="bg-black text-white">
  <Column class="text-center">
    <div class="mt-8 md:mt-20  mb-8 md:mb-20">
      <p>
        Welcome, to T14 Marketing
      </p>
      <p>
        We get you more leads & more sales utilising unparalleled knowledge of paid advertising algorithms
      </p>
      <p>
        Book your free consultation with our marketing strategy experts and learn how you can utilize paid ads to
        acquire high-value customers at lower cost, in greater volume, and profit more from each one.
      </p>

      <p>
        <button>
          Book a consultation
        </button>
        <button>
          Services
        </button>
      </p>
    </div>
    <div class="h-56"></div>
  </Column>
</div>

<div class="bg-gray-50 pb-20">
  <Column>
    <iframe
      class="w-full aspect-video -mt-56 z-10 rounded-2xl"
      src="https://www.youtube-nocookie.com/embed/0AnExD_mi7M?controls=0"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    >
    </iframe>

    <section>
      <h2>Our Services</h2>
      <div class="flex flex-col md:flex-row justify-between items-start md:items-end">
        <p>Custom software to expand your business</p>
        <p>
          <button>Book a consultation</button>
        </p>
      </div>
      <div class="flex flex-col md:flex-row justify-between gap-6">
        <ServiceCard title="Cookies" text="We make the best cookies" color="amber-600"/>
        <ServiceCard title="Cookies" text="We make the best cookies" color="amber-600"/>
        <ServiceCard title="Cookies" text="We make the best cookies" color="amber-600"/>
      </div>
    </section>
  </Column>
</div>

<section class="bg-cyan-600 text-white">
  <Column>
    <div class="max-w-screen-sm">
      <h2>About Us</h2>
      <p>
        Domain experts coming together to deliver total business transformation.
      </p>
      <p>Our team includes several former Meta, Google & Deloitte employees, experienced entrepreneurs, and decades of
        internet marketing experience. </p>
      <p> Our unparalleled insider knowledge of paid advertising algorithms allows us to build campaigns that are
        unbeaten within the industry.</p>
      <div class="border-b-[1px] mx-10"></div>
      <div class="flex flex-row justify-start">
        <div>
          <img
            class="rounded-full"
            src="https://media.licdn.com/dms/image/C4E03AQGOUL0D3_76ug/profile-displayphoto-shrink_800_800/0/1563301482920?e=1677715200&v=beta&t=nxknty6CFJOBKLhHhw-PQmWBskg3v9GU921gjzS7x9o"/>
        </div>
        <div>
          <p>Sanath Sambamoorthi</p>
          <p>CEO, Project Manager at Gadget Software</p>
        </div>
      </div>
    </div>
  </Column>

  <Column>
    <p>Get in touch <strong>today</strong></p>
    <div>
      <!-- Calendly inline widget begin -->
      <div class="calendly-inline-widget"
           data-url="https://calendly.com/sanaths/gadget-software-custom-software-discussion?hide_gdpr_banner=1"
           style="min-width:320px;height:630px;"></div>
      <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
      <!-- Calendly inline widget end -->
    </div>
  </Column>
</section>

<div class="bg-white">
  <Column class="pt-20 pb-16">
    <div class="flex flex-row justify-between items-start">
      <div>
        <Logo />
        <p>More than just paid advertising</p>
      </div>
      <a href="mailto:sanath@gadget-software.tech" class="shadow border-[1px] border-gray-200 rounded-lg">
        Shoot us an email sanath@gadget-software.tech
      </a>
    </div>
  </Column>
</div>
