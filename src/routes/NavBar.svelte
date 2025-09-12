<script lang="ts">
  import Column from "./Column.svelte";
  import Logo from "./Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import {faBars} from "@fortawesome/free-solid-svg-icons";

  const links: { title: string, url: string, always: boolean }[] = [
    { title: 'About', url: '/#about-us', always: true }
    { title: 'Testimonials', url: '/testimonials', always: true },
    { title: 'Process', url: '/#about-us', always: true },
    { title: 'Contact us', url: '/contact', always: true }
  ];
</script>

<div class="w-full bg-white">
  <Column wider>
    <div class="h-20 px-4 flex justify-between md:justify-center items-center">
      <div class="w-full h-full flex flex-row gap-8 justify-between items-center">
        <Logo />
        <nav class="hidden md:flex flex-row justify-between items-center gap-8">
          <ul class="flex gap-8">
            {#each links as link}
              <li class:hidden={!link.always} class="lg:flex">
                <a href={link.url}>{link.title}</a>
              </li>
            {/each}
          </ul>
<!--
        <a href="/#book-a-call" class="btn">
           Book a consultation
         </a>
//-->
        </nav>
      </div>
      <button id="mobile-menu-button" class="md:hidden text-2xl">
        <Fa icon={faBars} />
      </button>
    </div>
  </Column>
</div>

<nav id="mobile-menu" class="text-center bg-white hidden">
  <ul class="flex flex-col text-center w-full">
    {#each links as link}
      <li class="py-2 border-t-[1px] border-t-gray-300">
        <a href={link.url}>{link.title}</a>
      </li>
    {/each}
  </ul>
</nav>
