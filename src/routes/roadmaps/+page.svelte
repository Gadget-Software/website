<script lang="ts">
  import Column from "../Column.svelte";
  import Footer from "../Footer.svelte";
  import Fa from "svelte-fa/src/fa.svelte";
  import {
    faLaptopCode,
    faPaintBrush,
    faBuilding
  } from "@fortawesome/free-solid-svg-icons";
  import { goto } from "$app/navigation";

  const options = [
    { label: "Tech Entrepreneur", slug: "mvp", icon: faLaptopCode },
    { label: "Artist / Teacher", slug: "personal-brand", icon: faPaintBrush },
    { label: "Enterprise Business", slug: "automation", icon: faBuilding }
  ];

  // Works **after** hydration
  function navigate(e: MouseEvent, slug: string) {
    e.preventDefault();
    goto(`/roadmaps/${slug}`);
  }
</script>

<svelte:head>
  <title>Choose Your Roadmap</title>
</svelte:head>

<section class="bg-gray-50 py-16 md:py-24">
  <Column>
    <h2 class="big-text text-center text-cyan-800 mb-12">
      Who are <em>you</em>?
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
      {#each options as opt}
        <!-- Fallback <a> + JS enhancement -->
        <a
          href="/roadmaps/{opt.slug}"
          on:click|preventDefault={(e) => navigate(e, opt.slug)}
          class="group block p-8 bg-white rounded-lg shadow-md hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center focus:outline-none focus:ring-2 focus:ring-cyan-500"
        >
          <div class="mb-4 text-5xl text-cyan-600 group-hover:text-cyan-800 transition">
            <Fa icon={opt.icon} />
          </div>

          <h3 class="text-xl font-semibold text-gray-800 mb-2">
            {opt.label}
          </h3>

          <p class="text-sm text-gray-600">
            {opt.descr}
          </p>
        </a>
      {/each}
    </div>
  </Column>
</section>

<section class="bg-cyan-600 text-white py-12 md:py-20">
  <Column contentClass="flex flex-col items-center gap-6 text-center">
    <h2 class="big-text alt">
      Not sure? <strong>Get in touch</strong>
    </h2>
    <a
      href="/contact"
      class="px-6 py-3 text-xl md:text-2xl border-2 border-cyan-400 hover:bg-cyan-500 rounded transition"
    >
      Talk to us
    </a>
  </Column>
</section>

<Footer />
