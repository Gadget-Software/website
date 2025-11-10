<script lang="ts">
  import Column from "./Column.svelte";
  import Logo from "./Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import {faBars, faChevronDown} from "@fortawesome/free-solid-svg-icons";

  const links: { title: string, url: string, always: boolean }[] = [
    { title: 'About', url: '/#about', always: true },
    { title: 'Testimonials', url: '/testimonials', always: true },
    { title: 'Process', 
      url: '/process', 
      always: true 
      sublinks: [
        { title: "Proof of Concept for Startups", url: "/process/mvp" },
        { title: "Enterprise RPA/Workflow Automation", url: "/process/automation" },
        { title: "Personal Brand for Artists/Independent Teachers", url: "/process/personal-brand" },
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
                {#if link.sublinks}
                  <!-- Dropdown trigger -->
                  <button class="flex items-center gap-1 hover:text-blue-600 transition">
                    {link.title}
                    <Fa icon={faChevronDown} class="text-xs" />
                  </button>

                  <!-- Dropdown menu -->
                  <ul class="absolute left-0 top-full mt-2 w-48 bg-white shadow-lg rounded-md opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-opacity duration-200 z-50">
                    {#each link.sublinks as sub}
                      <li>
                        <a
                          href={sub.url}
                          class="block px-4 py-2 text-sm hover:bg-gray-100"
                        >
                          {sub.title}
                        </a>
                      </li>
                    {/each}
                  </ul>
                {:else}
                  <a href={link.url} class="hover:text-blue-600 transition">
                    {link.title}
                  </a>
                {/if}
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
        {#if link.sublinks}
          <!-- Expandable section in mobile -->
          <details class="w-full">
            <summary class="py-3 px-4 flex justify-between items-center cursor-pointer">
              {link.title}
              <Fa icon={faChevronDown} class="text-xs transition-transform" />
            </summary>
            <ul class="bg-gray-50">
              {#each link.sublinks as sub}
                <li class="border-t border-t-gray-200">
                  <a href={sub.url} class="block py-2 px-6 text-sm">
                    {sub.title}
                  </a>
                </li>
              {/each}
            </ul>
          </details>
        {:else}
          <a href={link.url} class="block py-3 px-4">
            {link.title}
          </a>
        {/if}
      </li>
    {/each}
  </ul>
</nav>

<style>
  /* Tailwind already handles most, but add a tiny tweak for the chevron rotation */
  details[open] summary > svg {
    transform: rotate(180deg);
  }
</style>
