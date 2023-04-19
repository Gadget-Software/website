<script lang="ts">
  export let title: string;
</script>

<div class="flex flex-col gap-8 mt-10">
  <div class="flex flex-col p-8 bg-white rounded shadow">
    <div class="flex flex-col gap-4">
      <h3 class="font-bold text-cyan-800 text-lg">
        {title}
      </h3>
      <div class="font-serif text-lg">
        <slot />
      </div>
    </div>
  </div>
</div>
