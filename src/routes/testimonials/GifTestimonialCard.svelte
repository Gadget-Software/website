<script lang="ts">
  export let title: string;
  export let gifSrc: string;
  export let gifAlt: string;
</script>

<div class="flex flex-col gap-8 mt-10">
  <div class="flex flex-col md:flex-row-reverse gap-8 p-8 bg-white rounded shadow">
    <div class="md:w-1/2 flex flex-col gap-4">
      <h3 class="font-bold text-cyan-800 text-lg">
        {title}
      </h3>
      <div class="font-serif">
        <slot />
      </div>
    </div>

    <div class="md:w-1/2">
      <img src={gifSrc} alt={gifAlt} />
    </div>
  </div>
</div>
