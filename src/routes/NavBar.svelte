<script lang="ts">
  import Column from "./Column.svelte";
  import Logo from "./Logo.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import {faBars} from "@fortawesome/free-solid-svg-icons";

  const links: { title: string, url: string }[] = [
    { title: 'Our Services', url: '/#our-services' },
    { title: 'About Us', url: '/#about-us' },
  ];
</script>

<div class="w-full h-20 bg-white">
  <Column class="h-full">
    <div class="flex flex-row justify-between items-center h-full">
      <div >
        <Logo />
      </div>
      <div class="hidden md:flex flex-row justify-between items-center gap-8">
        <ul class="flex gap-8">
          {#each links as link}
            <li>
              <a href={link.url}>{link.title}</a>
            </li>
          {/each}
        </ul>
        <a href="/#book-a-call" class="btn">
          Book a consultation
        </a>
      </div>
      <button id="mobile-menu-button" role="button" class="md:hidden text-2xl">
        <Fa icon={faBars} />
      </button>
    </div>
  </Column>
</div>

<div id="mobile-menu" class="text-center bg-white hidden">
  <ul class="flex flex-col text-center w-full">
    {#each links as link}
      <li class="py-2 border-t-[1px] border-t-gray-300">
        <a href={link.url}>{link.title}</a>
      </li>
    {/each}
  </ul>
</div>
