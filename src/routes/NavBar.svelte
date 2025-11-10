<script lang="ts">
  import Column from "./Column.svelte";
  import Logo from "./Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import {faBars, faChevronDown} from "@fortawesome/free-solid-svg-icons";


  const links: { title: string, url: string, always: boolean }[] = [
    { title: 'About', url: '/#about', always: true },
    { title: 'Testimonials', url: '/testimonials', always: true },
    { title: 'Success Roadmaps', 
      url: '/roadmaps', 
      always: true,
      sublinks: [
        { title: "Proof of Concept for Startups", url: "/roadmaps/mvp" },
        { title: "Enterprise RPA/Workflow Automation", url: "/roadmaps/automation" },
        { title: "Personal Brand for Artists/Independent Teachers", url: "/roadmaps/personal-brand" },
      ]
    },
    { title: 'Newsletter', url: '/newsletter', always: true },
    { title: 'Contact us', url: '/contact', always: true }
  ];

// Mobile menu toggle
  let mobileOpen = false;
  function toggleMobile() {
    mobileOpen = !mobileOpen;
  }
</script>

<!-- Desktop Header -->
<div class="w-full bg-white">
  <Column wider>
    <div class="h-20 px-4 flex justify-between md:justify-center items-center">
      <div class="w-full h-full flex flex-row gap-8 justify-between items-center">
        <Logo />

        <!-- Desktop Nav -->
        <nav class="hidden md:flex flex-row justify-between items-center gap-8">
          <ul class="flex gap-8">
            {#each links as link}
              <li class="relative group" class:hidden={!link.always}>
                  <a href={link.url} class="hover:text-blue-600 transition">
                    {link.title}
                  </a>
              </li>
            {/each}
          </ul>

          <!-- Uncomment when ready -->
          <!-- <a href="/#book-a-call" class="btn">Book a consultation</a> -->
        </nav>
      </div>

      <!-- Mobile menu button -->
      <button
        id="mobile-menu-button"
        class="md:hidden text-2xl"
        on:click={toggleMobile}
      >
        <Fa icon={faBars} />
      </button>
    </div>
  </Column>
</div>

<!-- Mobile Menu -->
<nav
  id="mobile-menu"
  class="text-center bg-white md:hidden"
  class:hidden={!mobileOpen}
>
  <ul class="flex flex-col w-full">
    {#each links as link}
      <li class="border-t-[1px] border-t-gray-300">
          <a href={link.url} class="block py-3 px-4">
            {link.title}
          </a>
      </li>
    {/each}
  </ul>
</nav>

<style>
  /* Tailwind already handles most, but add a tiny tweak for the chevron rotation */
  details[open] summary > svg {
    transform: rotate(180deg);
  }
  
  nav .group::before {
      content: "";
      position: absolute;
      top: 100%;
      left: 0;
      width: 100%;
      height: 8px;
      background: transparent;
  }
</style>
